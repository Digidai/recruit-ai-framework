#!/usr/bin/env python3
"""
Batch 20 Fix: Add resources to specific nested weak categories
"""

import json

def find_node_by_path(node, path_parts):
    """Find a node by navigating a specific path"""
    if not path_parts:
        return node
    target = path_parts[0]
    for child in node.get('children', []):
        if child.get('name') == target:
            return find_node_by_path(child, path_parts[1:])
    return None


def get_all_urls(node):
    """Get all existing URLs in the tree"""
    urls = set()
    if node.get('type') == 'url' and node.get('url'):
        urls.add(node.get('url'))
    for child in node.get('children', []):
        urls.update(get_all_urls(child))
    return urls


def main():
    print("Loading tarf.json...")
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_urls = get_all_urls(data)
    added = 0
    skipped = 0

    # Resources for G/远程面试与虚拟招聘/视频面试平台
    video_path = ['G 雇主品牌与候选人体验', '远程面试与虚拟招聘', '视频面试平台']
    video_resources = [
        {
            "name": "Whereby（简易视频会议）",
            "name_en": "Whereby (Simple Video Meetings)",
            "type": "url",
            "url": "https://whereby.com/",
            "tags": ["Video", "Meeting", "No Download"]
        },
        {
            "name": "Webex Meetings（企业视频）",
            "name_en": "Webex Meetings (Enterprise Video)",
            "type": "url",
            "url": "https://www.webex.com/video-conferencing",
            "tags": ["Video", "Enterprise", "Cisco"]
        },
        {
            "name": "Around（AI视频协作）",
            "name_en": "Around (AI Video Collaboration)",
            "type": "url",
            "url": "https://www.around.co/",
            "tags": ["Video", "AI", "Collaboration"]
        },
    ]

    video_node = find_node_by_path(data, video_path)
    if video_node:
        if 'children' not in video_node:
            video_node['children'] = []
        for resource in video_resources:
            if resource['url'] in existing_urls:
                print(f"⏭️  Skipped (URL exists): {resource['name_en']}")
                skipped += 1
                continue
            video_node['children'].append(resource)
            existing_urls.add(resource['url'])
            print(f"✅ Added: {resource['name_en']} -> G/.../视频面试平台")
            added += 1

    # Resources for G/招聘营销与内容创作/招聘营销平台
    marketing_path = ['G 雇主品牌与候选人体验', '招聘营销与内容创作', '招聘营销平台']
    marketing_resources = [
        {
            "name": "Phenom（人才体验平台）",
            "name_en": "Phenom (Talent Experience Platform)",
            "type": "url",
            "url": "https://www.phenom.com/",
            "tags": ["Marketing", "TXM", "AI"]
        },
        {
            "name": "Stories Incorporated（员工故事）",
            "name_en": "Stories Incorporated (Employee Stories)",
            "type": "url",
            "url": "https://storiesincorporated.com/",
            "tags": ["Marketing", "Stories", "Video"]
        },
        {
            "name": "Seenit（员工生成内容）",
            "name_en": "Seenit (Employee-Generated Content)",
            "type": "url",
            "url": "https://seenit.io/",
            "tags": ["Marketing", "UGC", "Video"]
        },
    ]

    marketing_node = find_node_by_path(data, marketing_path)
    if marketing_node:
        if 'children' not in marketing_node:
            marketing_node['children'] = []
        for resource in marketing_resources:
            if resource['url'] in existing_urls:
                print(f"⏭️  Skipped (URL exists): {resource['name_en']}")
                skipped += 1
                continue
            marketing_node['children'].append(resource)
            existing_urls.add(resource['url'])
            print(f"✅ Added: {resource['name_en']} -> G/.../招聘营销平台")
            added += 1

    print("\nSaving tarf.json...")
    with open('docs/tarf.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"""
{'='*60}
Summary:
  ✅ Added: {added}
  ⏭️  Skipped: {skipped}
{'='*60}""")


if __name__ == '__main__':
    main()
