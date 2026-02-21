#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查 app.js 中 i18n 对象的键是否同步（稳健版）"""

import re


def extract_balanced_block(text, open_brace_idx):
    """从给定 '{' 位置提取平衡花括号块，忽略字符串内容。"""
    if open_brace_idx < 0 or open_brace_idx >= len(text) or text[open_brace_idx] != '{':
        return None

    depth = 0
    in_single = False
    in_double = False
    in_backtick = False
    escaped = False

    for i in range(open_brace_idx, len(text)):
        ch = text[i]

        if escaped:
            escaped = False
            continue

        if ch == '\\':
            escaped = True
            continue

        if in_single:
            if ch == "'":
                in_single = False
            continue

        if in_double:
            if ch == '"':
                in_double = False
            continue

        if in_backtick:
            if ch == '`':
                in_backtick = False
            continue

        if ch == "'":
            in_single = True
            continue

        if ch == '"':
            in_double = True
            continue

        if ch == '`':
            in_backtick = True
            continue

        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return text[open_brace_idx:i + 1]

    return None


def extract_named_object(parent_block, name):
    m = re.search(rf'\b{name}\s*:\s*\{{', parent_block)
    if not m:
        return None
    open_idx = parent_block.find('{', m.start())
    return extract_balanced_block(parent_block, open_idx)


def extract_keys(obj_block):
    # 仅抓顶层键名（格式：key: ...）
    return set(re.findall(r'^\s*([A-Za-z0-9_]+)\s*:', obj_block, re.MULTILINE))


def extract_i18n_keys(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    m = re.search(r'\bconst\s+i18n\s*=\s*\{', content)
    if not m:
        print("❌ 无法在 app.js 中找到 i18n 对象定义")
        return None, None

    i18n_open = content.find('{', m.start())
    i18n_block = extract_balanced_block(content, i18n_open)
    if not i18n_block:
        print("❌ 无法提取完整 i18n 对象（括号不平衡）")
        return None, None

    zh_block = extract_named_object(i18n_block, 'zh')
    en_block = extract_named_object(i18n_block, 'en')
    if not zh_block or not en_block:
        print("❌ 未找到 zh/en 语言块")
        return None, None

    return extract_keys(zh_block), extract_keys(en_block)


def check_sync(zh_keys, en_keys):
    if zh_keys is None or en_keys is None:
        return

    missing_in_en = sorted(zh_keys - en_keys)
    missing_in_zh = sorted(en_keys - zh_keys)

    print("=" * 60)
    print("🌍 i18n 键同步检查报告")
    print("=" * 60)
    print(f"中文键数量: {len(zh_keys)}")
    print(f"英文键数量: {len(en_keys)}")
    print("-" * 60)

    if not missing_in_en and not missing_in_zh:
        print("✅ 所有键都已同步！")
        return

    if missing_in_en:
        print(f"❌ 英文翻译缺失 ({len(missing_in_en)} 个):")
        for k in missing_in_en:
            print(f"  - {k}")

    if missing_in_zh:
        print(f"❌ 中文翻译缺失 ({len(missing_in_zh)} 个):")
        for k in missing_in_zh:
            print(f"  - {k}")


if __name__ == '__main__':
    print("正在分析 docs/app.js...")
    zh, en = extract_i18n_keys('docs/app.js')
    check_sync(zh, en)
