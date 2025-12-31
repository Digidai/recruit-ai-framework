#!/usr/bin/env python3
"""
Batch 9: Add verified resources to tarf.json
Cross-validated resources covering weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== ATS 与招聘协作 =====
    "ATS 与招聘协作": [
        {
            "name": "JazzHR（小企业ATS）",
            "name_en": "JazzHR (SMB ATS)",
            "type": "url",
            "url": "https://www.jazzhr.com/",
            "tags": ["ATS", "SMB", "Affordable"]
        },
        {
            "name": "Breezy HR（协作招聘）",
            "name_en": "Breezy HR (Collaborative Hiring)",
            "type": "url",
            "url": "https://breezy.hr/",
            "tags": ["ATS", "Collaboration", "SMB"]
        },
        {
            "name": "Pinpoint（敏捷ATS）",
            "name_en": "Pinpoint (Agile ATS)",
            "type": "url",
            "url": "https://www.pinpointhq.com/",
            "tags": ["ATS", "Enterprise", "Customizable"]
        },
    ],

    # ===== 招聘运营 (RecOps) =====
    "招聘运营 (RecOps)": [
        {
            "name": "Fetcher（AI外展自动化）",
            "name_en": "Fetcher (AI Outreach Automation)",
            "type": "url",
            "url": "https://fetcher.ai/",
            "tags": ["RecOps", "AI", "Outreach"]
        },
        {
            "name": "Recruiterflow（招聘流程）",
            "name_en": "Recruiterflow (Recruiting Workflow)",
            "type": "url",
            "url": "https://recruiterflow.com/",
            "tags": ["RecOps", "Automation", "Agency"]
        },
    ],

    # ===== 人才库管理 =====
    "人才库管理": [
        {
            "name": "Loxo（人才智能平台）",
            "name_en": "Loxo (Talent Intelligence Platform)",
            "type": "url",
            "url": "https://www.loxo.co/",
            "tags": ["CRM", "Sourcing", "AI"]
        },
        {
            "name": "Crelate（招聘CRM）",
            "name_en": "Crelate (Recruiting CRM)",
            "type": "url",
            "url": "https://www.crelate.com/",
            "tags": ["CRM", "Search", "Staffing"]
        },
    ],

    # ===== 技术面试平台 =====
    "技术面试平台": [
        {
            "name": "HackerEarth（技术评估）",
            "name_en": "HackerEarth (Technical Assessment)",
            "type": "url",
            "url": "https://www.hackerearth.com/",
            "tags": ["Coding", "Assessment", "Hackathon"]
        },
        {
            "name": "TestGorilla（综合测评）",
            "name_en": "TestGorilla (Comprehensive Testing)",
            "type": "url",
            "url": "https://www.testgorilla.com/",
            "tags": ["Assessment", "Personality", "Skills"]
        },
        {
            "name": "Coderbyte（编程筛选）",
            "name_en": "Coderbyte (Code Screening)",
            "type": "url",
            "url": "https://coderbyte.com/",
            "tags": ["Coding", "Interview", "Assessment"]
        },
    ],

    # ===== 中国数据安全法规 =====
    "中国数据安全法规": [
        {
            "name": "China Briefing PIPL指南（PIPL合规）",
            "name_en": "China Briefing PIPL Guide",
            "type": "url",
            "url": "https://www.china-briefing.com/doing-business-guide/china/company-establishment/pipl-personal-information-protection-law",
            "tags": ["China", "PIPL", "Compliance"]
        },
        {
            "name": "Chambers China数据保护指南（数据保护）",
            "name_en": "Chambers China Data Protection Guide",
            "type": "url",
            "url": "https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2025/china",
            "tags": ["China", "Data Privacy", "Legal"]
        },
    ],

    # ===== 视频面试平台 =====
    "视频面试平台": [
        {
            "name": "myInterview（AI视频面试）",
            "name_en": "myInterview (AI Video Interview)",
            "type": "url",
            "url": "https://www.myinterview.com/",
            "tags": ["Video", "AI", "SMB"]
        },
        {
            "name": "Recright（单向视频）",
            "name_en": "Recright (One-way Video)",
            "type": "url",
            "url": "https://www.recright.com/",
            "tags": ["Video", "Async", "Europe"]
        },
    ],

    # ===== GitHub 搜索 =====
    "GitHub 搜索": [
        {
            "name": "OctoHR（GitHub招聘扩展）",
            "name_en": "OctoHR (GitHub Recruiting Extension)",
            "type": "url",
            "url": "https://octohr.info/",
            "tags": ["Sourcing", "GitHub", "Chrome"]
        },
        {
            "name": "DevSkiller GitHub Sourcing（开发者搜索）",
            "name_en": "DevSkiller GitHub Sourcing Guide",
            "type": "url",
            "url": "https://devskiller.com/blog/source-developers-from-github/",
            "tags": ["Sourcing", "GitHub", "Guide"]
        },
    ],

    # ===== 招聘分析 (People Analytics) =====
    "招聘分析 (People Analytics)": [
        {
            "name": "Ashby Analytics（招聘分析）",
            "name_en": "Ashby Analytics (Recruiting Analytics)",
            "type": "url",
            "url": "https://www.ashbyhq.com/analytics",
            "tags": ["Analytics", "Dashboard", "Reporting"]
        },
    ],

    # ===== 候选人关系管理 =====
    "候选人关系管理": [
        {
            "name": "Yello CRM（校园招聘CRM）",
            "name_en": "Yello CRM (Campus Recruiting CRM)",
            "type": "url",
            "url": "https://yello.co/campus-recruitment/",
            "tags": ["CRM", "Campus", "Events"]
        },
        {
            "name": "iCIMS Talent Cloud CRM（人才云）",
            "name_en": "iCIMS Talent Cloud CRM",
            "type": "url",
            "url": "https://www.icims.com/products/talent-cloud-crm/",
            "tags": ["CRM", "Enterprise", "Marketing"]
        },
    ],

    # ===== 招聘反欺诈与验证 =====
    "招聘反欺诈与验证": [
        {
            "name": "Certn（全球背调）",
            "name_en": "Certn (Global Background Check)",
            "type": "url",
            "url": "https://certn.co/",
            "tags": ["Background Check", "Global", "AI"]
        },
        {
            "name": "Springverify（印度背调）",
            "name_en": "Springverify (India Background Check)",
            "type": "url",
            "url": "https://www.springverify.com/",
            "tags": ["Background Check", "India"]
        },
    ],

    # ===== 批量招聘工具 =====
    "批量招聘工具": [
        {
            "name": "Grayscale（候选人沟通）",
            "name_en": "Grayscale (Candidate Communication)",
            "type": "url",
            "url": "https://www.grayscaleapp.com/",
            "tags": ["High-Volume", "SMS", "Communication"]
        },
    ],

    # ===== AI 视频面试 =====
    "AI 视频面试": [
        {
            "name": "Sapia.ai（对话式AI面试）",
            "name_en": "Sapia.ai (Conversational AI Interview)",
            "type": "url",
            "url": "https://sapia.ai/",
            "tags": ["AI", "Chat", "Fair"]
        },
    ],

    # ===== 心理测评 AI =====
    "心理测评 AI": [
        {
            "name": "Plum.io（人才评估）",
            "name_en": "Plum.io (Talent Assessment)",
            "type": "url",
            "url": "https://www.plum.io/",
            "tags": ["Psychometric", "AI", "Potential"]
        },
        {
            "name": "Traitify（视觉评估）",
            "name_en": "Traitify (Visual Assessment)",
            "type": "url",
            "url": "https://www.traitify.com/",
            "tags": ["Psychometric", "Visual", "Fast"]
        },
    ],

    # ===== 游戏化与 VR/AR 招聘 =====
    "游戏化与 VR/AR 招聘": [
        {
            "name": "Scoutible（游戏化评估）",
            "name_en": "Scoutible (Gamified Assessment)",
            "type": "url",
            "url": "https://www.scoutible.com/",
            "tags": ["Gamification", "AI", "Potential"]
        },
    ],

    # ===== 招聘数据隐私与合规 =====
    "招聘数据隐私与合规": [
        {
            "name": "OneTrust（隐私管理）",
            "name_en": "OneTrust (Privacy Management)",
            "type": "url",
            "url": "https://www.onetrust.com/",
            "tags": ["Privacy", "Compliance", "GDPR"]
        },
        {
            "name": "TrustArc（隐私合规）",
            "name_en": "TrustArc (Privacy Compliance)",
            "type": "url",
            "url": "https://trustarc.com/",
            "tags": ["Privacy", "Compliance"]
        },
    ],

    # ===== 技术技能评估 =====
    "技术技能评估": [
        {
            "name": "Adaface（自适应测试）",
            "name_en": "Adaface (Adaptive Testing)",
            "type": "url",
            "url": "https://www.adaface.com/",
            "tags": ["Coding", "Adaptive", "Anti-Cheating"]
        },
    ],

    # ===== 招聘社交媒体 =====
    "招聘社交媒体": [
        {
            "name": "Sprout Social（社交媒体管理）",
            "name_en": "Sprout Social (Social Media Management)",
            "type": "url",
            "url": "https://sproutsocial.com/",
            "tags": ["Social Media", "Analytics"]
        },
    ],

    # ===== AI 面试助手 =====
    "AI 面试助手": [
        {
            "name": "BarRaiser（AI面试协作）",
            "name_en": "BarRaiser (AI Interview Collaboration)",
            "type": "url",
            "url": "https://www.barraiser.com/",
            "tags": ["AI", "Interview", "Quality"]
        },
    ],

    # ===== 候选人体验平台 =====
    "候选人体验平台": [
        {
            "name": "Phenom CX（候选人体验）",
            "name_en": "Phenom Candidate Experience",
            "type": "url",
            "url": "https://www.phenom.com/candidate-experience",
            "tags": ["CX", "AI", "Personalization"]
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
