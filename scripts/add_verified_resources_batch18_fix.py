#!/usr/bin/env python3
"""
Batch 18 Fix: Add resources to correct category names
"""

import json

# Resources for correct category names
NEW_RESOURCES = {
    # ===== 面试排期工具 =====
    "面试排期工具": [
        {
            "name": "GoodTime（智能面试安排）",
            "name_en": "GoodTime (Intelligent Interview Scheduling)",
            "type": "url",
            "url": "https://www.goodtime.io/",
            "tags": ["Scheduling", "AI", "Automation"]
        },
        {
            "name": "Paradox（AI对话式安排）",
            "name_en": "Paradox (AI Conversational Scheduling)",
            "type": "url",
            "url": "https://www.paradox.ai/",
            "tags": ["Scheduling", "AI", "Conversational"]
        },
    ],

    # ===== 校园招聘与实习 =====
    "校园招聘与实习": [
        {
            "name": "RippleMatch（校园匹配平台）",
            "name_en": "RippleMatch (Campus Matching Platform)",
            "type": "url",
            "url": "https://ripplematch.com/",
            "tags": ["Campus", "AI", "Matching"]
        },
        {
            "name": "Parker Dewey（微实习平台）",
            "name_en": "Parker Dewey (Micro-Internship Platform)",
            "type": "url",
            "url": "https://www.parkerdewey.com/",
            "tags": ["Campus", "Internship", "Project-Based"]
        },
    ],

    # ===== 校园招聘平台（国际） =====
    "校园招聘平台（国际）": [
        {
            "name": "GradConnection（澳洲校园招聘）",
            "name_en": "GradConnection (Australia Campus Recruiting)",
            "type": "url",
            "url": "https://au.gradconnection.com/",
            "tags": ["Campus", "Australia", "Graduate"]
        },
        {
            "name": "Prospects.ac.uk（英国毕业生就业）",
            "name_en": "Prospects UK (Graduate Careers)",
            "type": "url",
            "url": "https://www.prospects.ac.uk/",
            "tags": ["Campus", "UK", "Graduate"]
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
