#!/usr/bin/env python3
"""
AI 面试与评估技术 资源补充脚本
Cross-validated resources for AI interview and assessment technologies
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== AI 视频面试 =====
    "AI 视频面试": [
        {
            "name": "Spark Hire（AI视频面试）",
            "name_en": "Spark Hire (AI Video Interview)",
            "type": "url",
            "url": "https://www.sparkhire.com/",
            "tags": ["AI", "Video", "One-Way"]
        },
        {
            "name": "Willo（异步视频筛选）",
            "name_en": "Willo (Async Video Screening)",
            "type": "url",
            "url": "https://www.willo.video/",
            "tags": ["AI", "Async", "Global"]
        },
        {
            "name": "Hirevire（AI视频筛选）",
            "name_en": "Hirevire (AI Video Screening)",
            "type": "url",
            "url": "https://hirevire.com/",
            "tags": ["AI", "Video", "Affordable"]
        },
        {
            "name": "Sapia.ai（对话式AI面试）",
            "name_en": "Sapia.ai (Conversational AI Interview)",
            "type": "url",
            "url": "https://sapia.ai/",
            "tags": ["AI", "Conversational", "Chat"]
        },
        {
            "name": "Jobma AI（多语言视频面试）",
            "name_en": "Jobma AI (Multilingual Video)",
            "type": "url",
            "url": "https://www.jobma.com/",
            "tags": ["AI", "Video", "Multilingual"]
        },
        {
            "name": "Elevatus AI（中东视频面试）",
            "name_en": "Elevatus AI (Middle East Video)",
            "type": "url",
            "url": "https://www.elevatus.io/",
            "tags": ["AI", "Video", "Middle East"]
        },
    ],

    # ===== AI 面试助手 =====
    "AI 面试助手": [
        {
            "name": "Metaview（AI面试记录员）",
            "name_en": "Metaview (AI Interview Scribe)",
            "type": "url",
            "url": "https://www.metaview.ai/",
            "tags": ["AI", "Notes", "Transcription"]
        },
        {
            "name": "BarRaiser AI Copilot（面试协作）",
            "name_en": "BarRaiser AI Copilot (Interview Collaboration)",
            "type": "url",
            "url": "https://www.barraiser.com/",
            "tags": ["AI", "Copilot", "Technical"]
        },
        {
            "name": "BrightHire（面试智能平台）",
            "name_en": "BrightHire (Interview Intelligence)",
            "type": "url",
            "url": "https://brighthire.com/",
            "tags": ["AI", "Recording", "Insights"]
        },
        {
            "name": "Pillar AI（面试分析）",
            "name_en": "Pillar AI (Interview Analytics)",
            "type": "url",
            "url": "https://www.pillar.hr/",
            "tags": ["AI", "Analytics", "Feedback"]
        },
        {
            "name": "Promap AI（面试Copilot）",
            "name_en": "Promap AI (Interview Copilot)",
            "type": "url",
            "url": "https://www.promap.ai/",
            "tags": ["AI", "Copilot", "Follow-up"]
        },
    ],

    # ===== 心理测评 AI =====
    "心理测评 AI": [
        {
            "name": "Pymetrics（神经科学游戏评估）",
            "name_en": "Pymetrics (Neuroscience-Based Games)",
            "type": "url",
            "url": "https://www.pymetrics.ai/",
            "tags": ["Psychometric", "Games", "Neuroscience"]
        },
        {
            "name": "TestGorilla（技能与心理测评）",
            "name_en": "TestGorilla (Skills & Psychometric Tests)",
            "type": "url",
            "url": "https://www.testgorilla.com/",
            "tags": ["Psychometric", "Skills", "Assessment"]
        },
        {
            "name": "Arctic Shores（游戏化心理测评）",
            "name_en": "Arctic Shores (Gamified Psychometric)",
            "type": "url",
            "url": "https://www.arcticshores.com/",
            "tags": ["Psychometric", "Games", "Behavioral"]
        },
        {
            "name": "Harver（AI预聘评估）",
            "name_en": "Harver (AI Pre-Employment Assessment)",
            "type": "url",
            "url": "https://harver.com/",
            "tags": ["Psychometric", "AI", "Volume"]
        },
        {
            "name": "INVIEWS（AI心理测评）",
            "name_en": "INVIEWS (AI Psychometric Assessment)",
            "type": "url",
            "url": "https://inviews.io/",
            "tags": ["Psychometric", "AI", "Analytics"]
        },
        {
            "name": "Plum（人才适配评估）",
            "name_en": "Plum (Talent Fit Assessment)",
            "type": "url",
            "url": "https://www.plum.io/",
            "tags": ["Psychometric", "Fit", "Predictive"]
        },
    ],

    # ===== AI 编程面试 =====
    "AI 编程面试": [
        {
            "name": "HackerEarth（AI技术评估）",
            "name_en": "HackerEarth (AI Tech Assessment)",
            "type": "url",
            "url": "https://www.hackerearth.com/",
            "tags": ["Coding", "AI", "Enterprise"]
        },
        {
            "name": "Coderbyte（编程评估平台）",
            "name_en": "Coderbyte (Coding Assessment Platform)",
            "type": "url",
            "url": "https://coderbyte.com/",
            "tags": ["Coding", "Assessment", "Affordable"]
        },
        {
            "name": "Vervoe（AI技能模拟）",
            "name_en": "Vervoe (AI Skills Simulation)",
            "type": "url",
            "url": "https://vervoe.com/",
            "tags": ["Coding", "Simulation", "AI"]
        },
        {
            "name": "Testlify（AI技能评估）",
            "name_en": "Testlify (AI Skills Assessment)",
            "type": "url",
            "url": "https://testlify.com/",
            "tags": ["Coding", "Skills", "AI"]
        },
        {
            "name": "InCruiter（AI编程评估）",
            "name_en": "InCruiter (AI Coding Assessment)",
            "type": "url",
            "url": "https://incruiter.com/",
            "tags": ["Coding", "AI", "Virtual"]
        },
        {
            "name": "Interview Coder（技术面试AI）",
            "name_en": "Interview Coder (Technical Interview AI)",
            "type": "url",
            "url": "https://www.interviewcoder.co/",
            "tags": ["Coding", "AI", "Assistant"]
        },
    ],

    # ===== AI 面试研究 =====
    "AI 面试研究": [
        {
            "name": "HBR AI招聘公平性研究",
            "name_en": "HBR AI and Fairness in Hiring Research",
            "type": "url",
            "url": "https://hbr.org/topic/subject/artificial-intelligence",
            "tags": ["Research", "HBR", "Fairness"]
        },
        {
            "name": "arXiv AI招聘公平性综述",
            "name_en": "arXiv Fairness in AI-Driven Recruitment",
            "type": "url",
            "url": "https://arxiv.org/list/cs.CY/recent",
            "tags": ["Research", "Academic", "Fairness"]
        },
        {
            "name": "LinkedIn Future of Recruiting报告",
            "name_en": "LinkedIn Future of Recruiting Report",
            "type": "url",
            "url": "https://business.linkedin.com/talent-solutions/resources/future-of-recruiting",
            "tags": ["Research", "LinkedIn", "Trends"]
        },
        {
            "name": "Deloitte AI HR研究",
            "name_en": "Deloitte AI in HR Research",
            "type": "url",
            "url": "https://www2.deloitte.com/us/en/insights/focus/human-capital-trends.html",
            "tags": ["Research", "Deloitte", "Trends"]
        },
        {
            "name": "Gartner HR Technology研究",
            "name_en": "Gartner HR Technology Research",
            "type": "url",
            "url": "https://www.gartner.com/en/human-resources",
            "tags": ["Research", "Gartner", "Technology"]
        },
    ],

    # ===== AI 面试与评估技术 (直接子节点) =====
    "AI 面试与评估技术": [
        {
            "name": "XOR AI（对话式招聘）",
            "name_en": "XOR AI (Conversational Recruiting)",
            "type": "url",
            "url": "https://xor.ai/",
            "tags": ["AI", "Chatbot", "Screening"]
        },
        {
            "name": "Paradox Olivia（AI招聘助手）",
            "name_en": "Paradox Olivia (AI Recruiting Assistant)",
            "type": "url",
            "url": "https://www.paradox.ai/",
            "tags": ["AI", "Chatbot", "Scheduling"]
        },
        {
            "name": "Interviewing.io（技术面试练习）",
            "name_en": "Interviewing.io (Technical Interview Practice)",
            "type": "url",
            "url": "https://interviewing.io/",
            "tags": ["Interview", "Practice", "Anonymous"]
        },
        {
            "name": "Karat（外包技术面试）",
            "name_en": "Karat (Outsourced Technical Interviews)",
            "type": "url",
            "url": "https://www.karat.com/",
            "tags": ["Interview", "Technical", "Outsource"]
        },
        {
            "name": "HiringBranch（软技能AI评估）",
            "name_en": "HiringBranch (Soft Skills AI Assessment)",
            "type": "url",
            "url": "https://www.hiringbranch.com/",
            "tags": ["AI", "Soft Skills", "Assessment"]
        },
        {
            "name": "Criteria Corp（认知能力测评）",
            "name_en": "Criteria Corp (Cognitive Ability Testing)",
            "type": "url",
            "url": "https://www.criteriacorp.com/",
            "tags": ["Assessment", "Cognitive", "Personality"]
        },
        {
            "name": "Eightfold AI（人才智能平台）",
            "name_en": "Eightfold AI (Talent Intelligence Platform)",
            "type": "url",
            "url": "https://eightfold.ai/",
            "tags": ["AI", "Talent", "Matching"]
        },
        {
            "name": "Phenom AI（人才体验平台）",
            "name_en": "Phenom AI (Talent Experience Platform)",
            "type": "url",
            "url": "https://www.phenom.com/",
            "tags": ["AI", "TXM", "Enterprise"]
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
