#!/usr/bin/env python3
"""
AI 面试与评估技术 资源补充脚本 (Batch 2)
Additional cross-validated resources for AI interview and assessment technologies
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== AI 视频面试 =====
    "AI 视频面试": [
        {
            "name": "Talview（AI面试与监考）",
            "name_en": "Talview (AI Interview & Proctoring)",
            "type": "url",
            "url": "https://www.talview.com/",
            "tags": ["AI", "Video", "Proctoring"]
        },
        {
            "name": "Knockri（无偏见AI面试）",
            "name_en": "Knockri (Bias-Free AI Interview)",
            "type": "url",
            "url": "https://knockri.com/",
            "tags": ["AI", "Video", "Bias-Free"]
        },
        {
            "name": "Mya Systems（对话AI招聘）",
            "name_en": "Mya Systems (Conversational AI Recruiting)",
            "type": "url",
            "url": "https://www.mya.com/",
            "tags": ["AI", "Conversational", "Chatbot"]
        },
    ],

    # ===== AI 面试助手 =====
    "AI 面试助手": [
        {
            "name": "Interview Sidekick（AI面试辅助）",
            "name_en": "Interview Sidekick (AI Interview Helper)",
            "type": "url",
            "url": "https://interviewsidekick.com/",
            "tags": ["AI", "Assistant", "Practice"]
        },
        {
            "name": "Final Round AI（面试准备助手）",
            "name_en": "Final Round AI (Interview Prep Assistant)",
            "type": "url",
            "url": "https://www.finalroundai.com/",
            "tags": ["AI", "Prep", "Copilot"]
        },
        {
            "name": "Verve AI Copilot（实时面试支持）",
            "name_en": "Verve AI Copilot (Real-Time Interview Support)",
            "type": "url",
            "url": "https://www.vervecopilot.com/",
            "tags": ["AI", "Copilot", "Real-Time"]
        },
        {
            "name": "Beyz AI（面试问答库）",
            "name_en": "Beyz AI (Interview Q&A Database)",
            "type": "url",
            "url": "https://beyz.ai/",
            "tags": ["AI", "Q&A", "Practice"]
        },
    ],

    # ===== 心理测评 AI =====
    "心理测评 AI": [
        {
            "name": "Mercer Mettl（综合评估平台）",
            "name_en": "Mercer Mettl (Comprehensive Assessment)",
            "type": "url",
            "url": "https://mettl.com/",
            "tags": ["Psychometric", "Enterprise", "Proctoring"]
        },
        {
            "name": "iMocha（技能智能平台）",
            "name_en": "iMocha (Skills Intelligence Platform)",
            "type": "url",
            "url": "https://www.imocha.io/",
            "tags": ["Skills", "AI", "Assessment"]
        },
        {
            "name": "Equalture（游戏化无偏见评估）",
            "name_en": "Equalture (Gamified Bias-Free Assessment)",
            "type": "url",
            "url": "https://www.equalture.com/",
            "tags": ["Psychometric", "Games", "Bias-Free"]
        },
        {
            "name": "Sova Assessment（心理评估）",
            "name_en": "Sova Assessment (Psychometric Testing)",
            "type": "url",
            "url": "https://www.sovaassessment.com/",
            "tags": ["Psychometric", "Assessment", "UK"]
        },
        {
            "name": "AON Cut-e（人才评估）",
            "name_en": "AON Cut-e (Talent Assessment)",
            "type": "url",
            "url": "https://assessment.aon.com/cut-e/",
            "tags": ["Psychometric", "Enterprise", "Global"]
        },
    ],

    # ===== AI 编程面试 =====
    "AI 编程面试": [
        {
            "name": "HireHunch（技术面试平台）",
            "name_en": "HireHunch (Technical Interview Platform)",
            "type": "url",
            "url": "https://hirehunch.com/",
            "tags": ["Coding", "Interview", "AI"]
        },
        {
            "name": "Utkrusht AI（技术面试AI）",
            "name_en": "Utkrusht AI (Technical Interview AI)",
            "type": "url",
            "url": "https://utkrusht.ai/",
            "tags": ["Coding", "AI", "CTO"]
        },
        {
            "name": "Intervue.io（技术评估平台）",
            "name_en": "Intervue.io (Technical Assessment Platform)",
            "type": "url",
            "url": "https://www.intervue.io/",
            "tags": ["Coding", "Assessment", "AI"]
        },
    ],

    # ===== AI 面试研究 =====
    "AI 面试研究": [
        {
            "name": "Nature AI招聘伦理研究",
            "name_en": "Nature AI Recruitment Ethics Research",
            "type": "url",
            "url": "https://www.nature.com/subjects/artificial-intelligence",
            "tags": ["Research", "Academic", "Ethics"]
        },
        {
            "name": "Frontiers心理学AI招聘研究",
            "name_en": "Frontiers Psychology AI Hiring Research",
            "type": "url",
            "url": "https://www.frontiersin.org/journals/psychology",
            "tags": ["Research", "Psychology", "Academic"]
        },
        {
            "name": "TestGorilla技能招聘报告",
            "name_en": "TestGorilla State of Skills-Based Hiring Report",
            "type": "url",
            "url": "https://www.testgorilla.com/skills-based-hiring/",
            "tags": ["Research", "Report", "Skills"]
        },
    ],

    # ===== AI 面试与评估技术 (直接子节点) =====
    "AI 面试与评估技术": [
        {
            "name": "Peoplebox AI（AI评估工具）",
            "name_en": "Peoplebox AI (AI Assessment Tools)",
            "type": "url",
            "url": "https://www.peoplebox.ai/",
            "tags": ["AI", "Assessment", "OKR"]
        },
        {
            "name": "WeCReateProblems（AI评估指南）",
            "name_en": "WeCreateProblems (AI Assessment Guide)",
            "type": "url",
            "url": "https://www.wecreateproblems.com/",
            "tags": ["AI", "Guide", "Assessment"]
        },
        {
            "name": "Vettio（AI心理评估）",
            "name_en": "Vettio (AI Psychometric Assessment)",
            "type": "url",
            "url": "https://vettio.com/",
            "tags": ["AI", "Psychometric", "Unbiased"]
        },
        {
            "name": "LockedIn AI（AI面试助手）",
            "name_en": "LockedIn AI (AI Interview Assistant)",
            "type": "url",
            "url": "https://www.lockedinai.com/",
            "tags": ["AI", "Assistant", "Multilingual"]
        },
        {
            "name": "JobTwine（AI面试Copilot）",
            "name_en": "JobTwine (AI Interview Copilot)",
            "type": "url",
            "url": "https://www.jobtwine.com/",
            "tags": ["AI", "Copilot", "Hiring"]
        },
        {
            "name": "Pesto Tech（AI面试平台）",
            "name_en": "Pesto Tech (AI Interview Platform)",
            "type": "url",
            "url": "https://pesto.tech/",
            "tags": ["AI", "Interview", "Tech"]
        },
        {
            "name": "Qureos（AI招聘指南）",
            "name_en": "Qureos (AI Hiring Guide)",
            "type": "url",
            "url": "https://www.qureos.com/",
            "tags": ["AI", "Guide", "Career"]
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
