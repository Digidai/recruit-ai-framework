#!/usr/bin/env python3
"""
Batch 7 Fix: Add resources to correct category names
"""

import json

# Resources for correct category names
NEW_RESOURCES = {
    # ===== 招聘分析 (People Analytics) =====
    "招聘分析 (People Analytics)": [
        {
            "name": "Visier People Analytics（人员分析平台）",
            "name_en": "Visier People Analytics Platform",
            "type": "url",
            "url": "https://www.visier.com/solutions/people-analytics/",
            "tags": ["Analytics", "AI", "Enterprise"]
        },
        {
            "name": "Tableau HR分析（人力资源分析）",
            "name_en": "Tableau HR Analytics",
            "type": "url",
            "url": "https://www.tableau.com/solutions/human-resources-analytics",
            "tags": ["Analytics", "BI", "Visualization"]
        },
        {
            "name": "Zoho HR分析（HR分析）",
            "name_en": "Zoho HR Analytics",
            "type": "url",
            "url": "https://www.zoho.com/analytics/hr-analytics.html",
            "tags": ["Analytics", "SMB"]
        },
    ],

    # ===== 招聘自动化工具 =====
    "招聘自动化工具": [
        {
            "name": "GoodTime面试协调（AI排程）",
            "name_en": "GoodTime Interview Coordination",
            "type": "url",
            "url": "https://www.goodtime.io/",
            "tags": ["Scheduling", "AI", "Enterprise"]
        },
        {
            "name": "Cronofy日历API（排程集成）",
            "name_en": "Cronofy Calendar API",
            "type": "url",
            "url": "https://www.cronofy.com/",
            "tags": ["Scheduling", "API", "Integration"]
        },
        {
            "name": "Calendly招聘（面试排程）",
            "name_en": "Calendly for Recruiting",
            "type": "url",
            "url": "https://calendly.com/solutions/recruiting",
            "tags": ["Scheduling", "Free"]
        },
    ],

    # ===== AI 候选人沟通/Chatbot =====
    "AI 候选人沟通/Chatbot": [
        {
            "name": "Paradox/Olivia（对话式招聘AI）",
            "name_en": "Paradox/Olivia (Conversational Recruiting AI)",
            "type": "url",
            "url": "https://www.paradox.ai/",
            "tags": ["Chatbot", "AI", "Enterprise"]
        },
        {
            "name": "XOR招聘AI（多渠道对话）",
            "name_en": "XOR Recruiting AI (Multi-channel)",
            "type": "url",
            "url": "https://www.xor.ai/",
            "tags": ["Chatbot", "AI", "High-Volume"]
        },
        {
            "name": "Sense人才参与（候选人沟通）",
            "name_en": "Sense Talent Engagement",
            "type": "url",
            "url": "https://www.sensehq.com/",
            "tags": ["Chatbot", "Engagement"]
        },
    ],

    # ===== 心理测评 AI =====
    "心理测评 AI": [
        {
            "name": "Hogan霍根评估（性格测评）",
            "name_en": "Hogan Assessments (Personality)",
            "type": "url",
            "url": "https://www.hoganassessments.com/",
            "tags": ["Psychometric", "Personality"]
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
