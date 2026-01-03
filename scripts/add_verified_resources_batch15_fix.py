#!/usr/bin/env python3
"""
Batch 15 Fix: Add resources to correct category names
"""

import json

# Resources for correct category names
NEW_RESOURCES = {
    # ===== 招聘 Newsletter =====
    "招聘 Newsletter": [
        {
            "name": "Recruiting Headlines（招聘新闻）",
            "name_en": "Recruiting Headlines Newsletter",
            "type": "url",
            "url": "https://recruitingheadlines.com/",
            "tags": ["Newsletter", "News", "Daily"]
        },
        {
            "name": "HRExaminer（HR数字分析）",
            "name_en": "HRExaminer (HR Digital Analysis)",
            "type": "url",
            "url": "https://www.hrexaminer.com/",
            "tags": ["Media", "Analysis", "Research"]
        },
    ],

    # ===== 招聘社区 =====
    "招聘社区": [
        {
            "name": "People Managing People社区（HR社区）",
            "name_en": "People Managing People Community",
            "type": "url",
            "url": "https://peoplemanagingpeople.com/community/",
            "tags": ["Community", "HR", "Leadership"]
        },
        {
            "name": "HR Uprising（HR热点讨论）",
            "name_en": "HR Uprising Forum",
            "type": "url",
            "url": "https://hruprising.com/",
            "tags": ["Community", "Forum", "UK"]
        },
    ],

    # ===== 招聘行业媒体 =====
    "招聘行业媒体": [
        {
            "name": "Talent Acquisition Excellence（TA卓越）",
            "name_en": "Talent Acquisition Excellence Magazine",
            "type": "url",
            "url": "https://hr.com/en/magazines/talent_acquisition_excellence_essentials/",
            "tags": ["Media", "Magazine", "TA"]
        },
        {
            "name": "Talent Management Magazine（人才管理杂志）",
            "name_en": "Talent Management Magazine",
            "type": "url",
            "url": "https://talentmgt.com/",
            "tags": ["Media", "Magazine", "TM"]
        },
    ],
}


def find_node_by_name(node, target_name):
    """Recursively find a node by name"""
    if node.get('name') == target_name:
        return node
    for child in node.get('children', []):
        result = find_node_by_name(child, target_name)
        if result:
            return result
    return None


def get_all_urls(node):
    """Get all existing URLs in the tree"""
    urls = set()
    if node.get('type') == 'url' and node.get('url'):
        urls.add(node.get('url'))
    for child in node.get('children', []):
        urls.update(get_all_urls(child))
    return urls


def get_all_names(node):
    """Get all existing names in the tree"""
    names = set()
    name = node.get('name', '')
    if name:
        names.add(name)
    for child in node.get('children', []):
        names.update(get_all_names(child))
    return names


def add_resources(data):
    """Add new resources to the appropriate categories"""
    existing_urls = get_all_urls(data)
    existing_names = get_all_names(data)

    added = 0
    skipped = 0
    errors = 0

    for category_name, resources in NEW_RESOURCES.items():
        parent = find_node_by_name(data, category_name)
        if not parent:
            print(f"⚠️  Category not found: {category_name}")
            errors += len(resources)
            continue

        if 'children' not in parent:
            parent['children'] = []

        for resource in resources:
            url = resource.get('url', '')
            name = resource.get('name', '')

            # Check for duplicates
            if url in existing_urls:
                print(f"⏭️  Skipped (URL exists): {resource['name_en']}")
                skipped += 1
                continue

            if name in existing_names:
                print(f"⏭️  Skipped (name exists): {resource['name_en']}")
                skipped += 1
                continue

            parent['children'].append(resource)
            existing_urls.add(url)
            existing_names.add(name)
            print(f"✅ Added: {resource['name_en']} -> {category_name}")
            added += 1

    return added, skipped, errors


def main():
    print("Loading tarf.json...")
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    added, skipped, errors = add_resources(data)

    print("\nSaving tarf.json...")
    with open('docs/tarf.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"""
{'='*60}
Summary:
  ✅ Added: {added}
  ⏭️  Skipped: {skipped}
  ❌ Errors: {errors}
{'='*60}""")


if __name__ == '__main__':
    main()
