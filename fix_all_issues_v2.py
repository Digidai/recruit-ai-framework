#!/usr/bin/env python3
"""
修复所有检查出的问题：
1. 修复7个分类节点的英文翻译
2. 去除重复URL
3. 规范化低频标签
"""

import json
import re
from collections import defaultdict


# 1. 分类节点英文翻译
FOLDER_TRANSLATIONS = {
    "自动化工具": "Automation Tools",
    "AI 编程面试": "AI Coding Interviews",
    "简历欺诈检测": "Resume Fraud Detection",
    "招聘团队协作": "Recruiting Team Collaboration",
    "沟通工具": "Communication Tools",
    "技术面试平台": "Technical Interview Platforms",
    "技术技能评估": "Technical Skills Assessment",
}


def fix_folder_translations(node):
    """修复分类节点的英文翻译"""
    fixed = 0
    name = node.get('name', '')

    if name in FOLDER_TRANSLATIONS:
        node['name_en'] = FOLDER_TRANSLATIONS[name]
        fixed += 1

    for child in node.get('children', []):
        fixed += fix_folder_translations(child)

    return fixed


def remove_duplicate_urls(node, seen_urls=None, path=""):
    """移除重复的URL节点"""
    if seen_urls is None:
        seen_urls = set()

    removed = 0
    name = node.get('name', '')
    current_path = f"{path} > {name}" if path else name

    if 'children' in node:
        new_children = []
        for child in node['children']:
            url = child.get('url', '')
            if url:
                if url in seen_urls:
                    # 跳过重复的URL
                    removed += 1
                else:
                    seen_urls.add(url)
                    new_children.append(child)
            else:
                # 递归处理文件夹节点
                child_removed = remove_duplicate_urls(child, seen_urls, current_path)
                removed += child_removed
                new_children.append(child)

        node['children'] = new_children

    return removed


# 标签规范化映射
TAG_NORMALIZATION = {
    # 统一大小写
    'guide': 'Guide',
    'tool': 'Tool',
    'tools': 'Tool',
    'review': 'Review',
    'reviews': 'Review',
    'assessment': 'Assessment',
    'assessments': 'Assessment',
    'interview': 'Interview',
    'interviews': 'Interview',
    'template': 'Template',
    'templates': 'Template',
    'report': 'Report',
    'reports': 'Report',
    'research': 'Research',
    'community': 'Community',
    'framework': 'Framework',
    'law': 'Law',
    'privacy': 'Privacy',
    'analytics': 'Analytics',
    'automation': 'Automation',
    'sourcing': 'Sourcing',
    'startup': 'Startup',
    'startups': 'Startup',
    'best practice': 'Best Practice',
    'best practices': 'Best Practice',

    # 合并相似标签
    '面试': 'Interview',
    '课程': 'Course',
    '最佳实践': 'Best Practice',
    '流程优化': 'Optimization',
    '招聘效率': 'Efficiency',
    '技能测试': 'Assessment',
    '招聘工具': 'Tool',
    '退伍军人': 'Veteran',
    '招聘板': 'Job Board',
    '职位': 'Job',

    # 区域标签统一
    'apac': 'APAC',
    'mena': 'MENA',
    'latam': 'LATAM',
    'africa': 'Africa',

    # 行业标签统一
    'healthcare': 'Healthcare',
    'finance': 'Finance',
    'retail': 'Retail',
    'manufacturing': 'Manufacturing',
    'logistics': 'Logistics',
    'education': 'Education',
    'hospitality': 'Hospitality',

    # 其他
    'gig': 'Gig',
    'referral': 'Referral',
    'onboarding': 'Onboarding',
    'branding': 'Branding',
    'marketing': 'Marketing',
    'scheduling': 'Scheduling',
    'communication': 'Communication',
    'collaboration': 'Collaboration',
    'verification': 'Verification',
    'crm': 'CRM',
    'ats': 'ATS',
    'hrm': 'HRM',
    'hris': 'HRIS',
    'roi': 'ROI',
    'seo': 'SEO',
    'dei': 'DEI',
    'pdf': 'PDF',
}


def normalize_tags(node):
    """规范化标签"""
    normalized = 0

    if 'tags' in node:
        new_tags = []
        for tag in node['tags']:
            lower = tag.lower()
            if lower in TAG_NORMALIZATION:
                new_tag = TAG_NORMALIZATION[lower]
                if new_tag != tag:
                    normalized += 1
                new_tags.append(new_tag)
            else:
                new_tags.append(tag)

        # 去重
        unique_tags = list(dict.fromkeys(new_tags))
        if len(unique_tags) != len(node['tags']):
            normalized += len(node['tags']) - len(unique_tags)
        node['tags'] = unique_tags

    for child in node.get('children', []):
        normalized += normalize_tags(child)

    return normalized


def count_stats(node, stats):
    """统计数据"""
    stats['total'] += 1
    if 'url' in node:
        stats['url'] += 1
    else:
        stats['folder'] += 1

    for child in node.get('children', []):
        count_stats(child, stats)


def main():
    print("读取 tarf.json...")
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 修复前统计
    stats_before = {'total': 0, 'url': 0, 'folder': 0}
    count_stats(data, stats_before)

    print(f"\n修复前: {stats_before['url']} URL资源")

    # 1. 修复分类翻译
    print("\n[1] 修复分类节点翻译...")
    trans_fixed = fix_folder_translations(data)
    print(f"    修复了 {trans_fixed} 个翻译")

    # 2. 移除重复URL
    print("\n[2] 移除重复URL...")
    dup_removed = remove_duplicate_urls(data)
    print(f"    移除了 {dup_removed} 个重复URL")

    # 3. 规范化标签
    print("\n[3] 规范化标签...")
    tags_normalized = normalize_tags(data)
    print(f"    规范化了 {tags_normalized} 个标签")

    # 修复后统计
    stats_after = {'total': 0, 'url': 0, 'folder': 0}
    count_stats(data, stats_after)

    print(f"\n修复后: {stats_after['url']} URL资源")

    # 保存
    print("\n保存数据...")
    with open('docs/tarf.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n{'=' * 50}")
    print("修复完成!")
    print(f"{'=' * 50}")
    print(f"  翻译修复: {trans_fixed}")
    print(f"  重复移除: {dup_removed}")
    print(f"  标签规范: {tags_normalized}")
    print(f"  URL变化: {stats_before['url']} → {stats_after['url']} ({stats_after['url'] - stats_before['url']})")


if __name__ == '__main__':
    main()
