#!/usr/bin/env python3
"""
Batch 14 Fix: Add resources to correct category names
"""

import json

# Resources for correct category names
NEW_RESOURCES = {
    # ===== 医疗/生命科学 =====
    "医疗/生命科学": [
        {
            "name": "iCIMS医疗招聘（医疗ATS）",
            "name_en": "iCIMS Healthcare Recruiting",
            "type": "url",
            "url": "https://www.icims.com/products/industry/hospital-healthcare-recruiting-software/",
            "tags": ["Healthcare", "ATS", "Hospital"]
        },
        {
            "name": "Cejka Search（医疗高管猎头）",
            "name_en": "Cejka Search (Healthcare Executive Search)",
            "type": "url",
            "url": "https://www.cejkasearch.com/",
            "tags": ["Healthcare", "Executive", "Search"]
        },
        {
            "name": "HCRI（医疗招聘国际）",
            "name_en": "HealthCare Recruiters International",
            "type": "url",
            "url": "https://www.hcrnetwork.com/",
            "tags": ["Healthcare", "Global", "Recruiting"]
        },
        {
            "name": "Health eCareers（医疗人才市场）",
            "name_en": "Health eCareers (Healthcare Job Board)",
            "type": "url",
            "url": "https://www.healthecareers.com/",
            "tags": ["Healthcare", "Job Board", "Clinical"]
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
