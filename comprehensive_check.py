#!/usr/bin/env python3
"""
全面项目问题检查：
1. 翻译问题（name = name_en）
2. 标签规范性
3. URL 格式问题
4. 重复资源
5. 空分类
6. 结构问题
7. 缺失字段
8. 标签使用分析
"""

import json
import os
import re
from collections import defaultdict
from urllib.parse import urlparse


def check_all(node, issues, stats, path="", seen_urls=None, seen_names=None):
    """递归检查所有问题"""
    if seen_urls is None:
        seen_urls = {}
    if seen_names is None:
        seen_names = {}

    name = node.get('name', '')
    name_en = node.get('name_en', '')
    url = node.get('url', '')
    tags = node.get('tags', [])
    children = node.get('children', [])

    current_path = f"{path} > {name}" if path else name
    stats['total'] += 1

    # 1. 检查翻译问题
    if name and name_en:
        name_norm = name.replace('｜', '|').replace('：', ':').strip()
        name_en_norm = name_en.replace('｜', '|').replace('：', ':').strip()
        if name_norm == name_en_norm:
            issues['translation_same'].append({
                'name': name,
                'path': current_path
            })

    # 2. 检查 name_en 中包含中文
    if name_en and re.search(r'[\u4e00-\u9fff]', name_en):
        issues['chinese_in_name_en'].append({
            'name': name,
            'name_en': name_en,
            'path': current_path
        })

    # 3. 检查缺失 name_en
    if name and not name_en and (url or children):
        issues['missing_name_en'].append({
            'name': name,
            'path': current_path
        })

    # URL 节点检查
    if url:
        stats['url'] += 1

        # 4. 检查 URL 格式
        if not url.startswith('http://') and not url.startswith('https://'):
            issues['invalid_url_format'].append({
                'name': name,
                'url': url,
                'path': current_path
            })

        # 5. 检查重复 URL
        if url in seen_urls:
            issues['duplicate_url'].append({
                'name': name,
                'url': url,
                'original': seen_urls[url],
                'path': current_path
            })
        else:
            seen_urls[url] = current_path

        # 6. 检查 URL 编码问题
        if '%' in url and re.search(r'%[^0-9A-Fa-f]|%[0-9A-Fa-f][^0-9A-Fa-f]', url):
            issues['url_encoding'].append({
                'name': name,
                'url': url,
                'path': current_path
            })

        # 7. 检查缺失标签
        if not tags:
            issues['missing_tags'].append({
                'name': name,
                'path': current_path
            })

        # 8. 统计标签
        for tag in tags:
            stats['tags'][tag] += 1

        # 9. 检查标签大小写不一致
        for tag in tags:
            lower = tag.lower()
            if lower != tag and tag != tag.upper() and tag != tag.title():
                issues['tag_case_inconsistent'].append({
                    'name': name,
                    'tag': tag,
                    'path': current_path
                })

    # 文件夹节点检查
    else:
        stats['folder'] += 1

        # 10. 检查空文件夹
        if not children:
            issues['empty_folder'].append({
                'name': name,
                'path': current_path
            })

        # 11. 检查只有1个子节点的文件夹
        elif len(children) == 1:
            child = children[0]
            if 'url' not in child and child.get('type') != 'template':
                issues['single_child_folder'].append({
                    'name': name,
                    'child': child.get('name', ''),
                    'path': current_path
                })

        # 12. 检查资源过少的叶子分类（<3个）
        url_children = [c for c in children if c.get('url') or c.get('type') == 'template']
        folder_children = [c for c in children if not c.get('url') and c.get('type') != 'template']
        if len(folder_children) == 0 and 0 < len(url_children) < 3:
            issues['few_resources'].append({
                'name': name,
                'count': len(url_children),
                'path': current_path
            })

    # 13. 检查重复名称
    if name:
        if name in seen_names and url:  # 只检查 URL 节点
            issues['duplicate_name'].append({
                'name': name,
                'original': seen_names[name],
                'path': current_path
            })
        elif url:
            seen_names[name] = current_path

    # 递归检查子节点
    for child in children:
        check_all(child, issues, stats, current_path, seen_urls, seen_names)


def analyze_tags(stats):
    """分析标签使用情况"""
    tag_issues = []

    # 检查低频标签
    for tag, count in stats['tags'].items():
        if count == 1:
            tag_issues.append(f"仅使用1次: {tag}")

    # 检查可能的大小写重复
    lower_tags = defaultdict(list)
    for tag in stats['tags']:
        lower_tags[tag.lower()].append(tag)

    for lower, variants in lower_tags.items():
        if len(variants) > 1:
            tag_issues.append(f"大小写重复: {variants}")

    return tag_issues


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tarf_path = os.path.join(script_dir, 'docs', 'tarf.json')
    with open(tarf_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    issues = {
        'translation_same': [],
        'chinese_in_name_en': [],
        'missing_name_en': [],
        'invalid_url_format': [],
        'duplicate_url': [],
        'url_encoding': [],
        'missing_tags': [],
        'tag_case_inconsistent': [],
        'empty_folder': [],
        'single_child_folder': [],
        'few_resources': [],
        'duplicate_name': [],
    }

    stats = {
        'total': 0,
        'url': 0,
        'folder': 0,
        'tags': defaultdict(int),
    }

    check_all(data, issues, stats)
    tag_issues = analyze_tags(stats)

    # 输出报告
    print("=" * 70)
    print("项目问题检查报告")
    print("=" * 70)

    print(f"\n【基础统计】")
    print(f"  总节点数:    {stats['total']}")
    print(f"  URL 资源:    {stats['url']}")
    print(f"  分类文件夹:  {stats['folder']}")
    print(f"  标签种类:    {len(stats['tags'])}")

    # 问题汇总
    print(f"\n【问题汇总】")
    total_issues = 0
    issue_summary = [
        ('翻译相同 (name=name_en)', 'translation_same', '高'),
        ('name_en 含中文', 'chinese_in_name_en', '高'),
        ('缺失 name_en', 'missing_name_en', '中'),
        ('URL 格式错误', 'invalid_url_format', '高'),
        ('重复 URL', 'duplicate_url', '高'),
        ('URL 编码问题', 'url_encoding', '低'),
        ('缺失标签', 'missing_tags', '中'),
        ('标签大小写不一致', 'tag_case_inconsistent', '低'),
        ('空分类', 'empty_folder', '高'),
        ('单子节点分类', 'single_child_folder', '低'),
        ('资源过少(<3)', 'few_resources', '中'),
        ('重复名称', 'duplicate_name', '低'),
    ]

    for desc, key, severity in issue_summary:
        count = len(issues[key])
        total_issues += count
        if count > 0:
            icon = "🔴" if severity == '高' else "🟡" if severity == '中' else "🟢"
            print(f"  {icon} {desc}: {count} 个")
        else:
            print(f"  ✅ {desc}: 0 个")

    # 详细问题列表
    print(f"\n{'=' * 70}")
    print("详细问题列表")
    print("=" * 70)

    # 高优先级问题
    if issues['translation_same']:
        print(f"\n【翻译相同】共 {len(issues['translation_same'])} 个")
        for item in issues['translation_same'][:10]:
            print(f"  - {item['name']}")
        if len(issues['translation_same']) > 10:
            print(f"  ... 还有 {len(issues['translation_same']) - 10} 个")

    if issues['chinese_in_name_en']:
        print(f"\n【name_en 含中文】共 {len(issues['chinese_in_name_en'])} 个")
        for item in issues['chinese_in_name_en'][:10]:
            print(f"  - {item['name']}")
            print(f"    name_en: {item['name_en']}")
        if len(issues['chinese_in_name_en']) > 10:
            print(f"  ... 还有 {len(issues['chinese_in_name_en']) - 10} 个")

    if issues['duplicate_url']:
        print(f"\n【重复 URL】共 {len(issues['duplicate_url'])} 个")
        for item in issues['duplicate_url'][:10]:
            print(f"  - {item['name']}")
            print(f"    URL: {item['url']}")
            print(f"    原始: {item['original'].split(' > ')[-1]}")
        if len(issues['duplicate_url']) > 10:
            print(f"  ... 还有 {len(issues['duplicate_url']) - 10} 个")

    if issues['missing_tags']:
        print(f"\n【缺失标签】共 {len(issues['missing_tags'])} 个")
        for item in issues['missing_tags'][:10]:
            print(f"  - {item['name']}")
        if len(issues['missing_tags']) > 10:
            print(f"  ... 还有 {len(issues['missing_tags']) - 10} 个")

    if issues['few_resources']:
        print(f"\n【资源过少】共 {len(issues['few_resources'])} 个")
        for item in issues['few_resources']:
            print(f"  - [{item['count']}] {item['name']}")

    if issues['empty_folder']:
        print(f"\n【空分类】共 {len(issues['empty_folder'])} 个")
        for item in issues['empty_folder']:
            print(f"  - {item['name']}")

    # 标签分析
    if tag_issues:
        print(f"\n【标签问题】共 {len(tag_issues)} 个")
        for issue in tag_issues[:20]:
            print(f"  - {issue}")
        if len(tag_issues) > 20:
            print(f"  ... 还有 {len(tag_issues) - 20} 个")

    # 总结
    print(f"\n{'=' * 70}")
    print("问题总结")
    print("=" * 70)

    high_priority = (
        len(issues['translation_same']) +
        len(issues['chinese_in_name_en']) +
        len(issues['invalid_url_format']) +
        len(issues['duplicate_url']) +
        len(issues['empty_folder'])
    )

    medium_priority = (
        len(issues['missing_name_en']) +
        len(issues['missing_tags']) +
        len(issues['few_resources'])
    )

    low_priority = (
        len(issues['url_encoding']) +
        len(issues['tag_case_inconsistent']) +
        len(issues['single_child_folder']) +
        len(issues['duplicate_name'])
    )

    print(f"  🔴 高优先级: {high_priority} 个")
    print(f"  🟡 中优先级: {medium_priority} 个")
    print(f"  🟢 低优先级: {low_priority} 个")
    print(f"  📊 总计: {total_issues} 个问题")

    if total_issues == 0:
        print(f"\n  ✅ 恭喜！未发现任何问题。")
    elif high_priority == 0:
        print(f"\n  ✅ 无高优先级问题，项目状态良好。")
    else:
        print(f"\n  ⚠️ 建议优先处理高优先级问题。")


if __name__ == '__main__':
    main()
