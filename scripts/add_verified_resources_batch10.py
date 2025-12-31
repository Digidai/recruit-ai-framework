#!/usr/bin/env python3
"""
Batch 10: Add verified resources to tarf.json
Cross-validated resources covering weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== ATS 与招聘协作 =====
    "ATS 与招聘协作": [
        {
            "name": "Homerun（小企业ATS）",
            "name_en": "Homerun (SMB Hiring Platform)",
            "type": "url",
            "url": "https://www.homerun.co/",
            "tags": ["ATS", "SMB", "Design"]
        },
        {
            "name": "Manatal（AI招聘软件）",
            "name_en": "Manatal (AI Recruiting Software)",
            "type": "url",
            "url": "https://www.manatal.com/",
            "tags": ["ATS", "AI", "Affordable"]
        },
        {
            "name": "Zoho Recruit（招聘ATS）",
            "name_en": "Zoho Recruit (ATS & CRM)",
            "type": "url",
            "url": "https://www.zoho.com/recruit/",
            "tags": ["ATS", "CRM", "Free"]
        },
    ],

    # ===== 校园招聘与实习 =====
    "校园招聘与实习": [
        {
            "name": "Rakuna（校园招聘软件）",
            "name_en": "Rakuna (Campus Recruiting Software)",
            "type": "url",
            "url": "https://www.rakuna.co/",
            "tags": ["Campus", "Events", "CRM"]
        },
        {
            "name": "Untapped（多元化早期人才）",
            "name_en": "Untapped (Diverse Early Talent)",
            "type": "url",
            "url": "https://www.untapped.io/",
            "tags": ["Campus", "DEI", "Early Career"]
        },
    ],

    # ===== AI 面试助手 =====
    "AI 面试助手": [
        {
            "name": "Kira AI（AI招聘助手）",
            "name_en": "Kira AI (AI Recruiting Assistant)",
            "type": "url",
            "url": "https://getkira.com/",
            "tags": ["AI", "Interview", "Screening"]
        },
        {
            "name": "Final Round AI（面试准备）",
            "name_en": "Final Round AI (Interview Prep)",
            "type": "url",
            "url": "https://www.finalroundai.com/",
            "tags": ["AI", "Interview", "Prep"]
        },
    ],

    # ===== 游戏化与 VR/AR 招聘 =====
    "游戏化与 VR/AR 招聘": [
        {
            "name": "Criteria Cognify（游戏化认知测试）",
            "name_en": "Criteria Cognify (Gamified Cognitive Test)",
            "type": "url",
            "url": "https://www.criteriacorp.com/assess/game-based",
            "tags": ["Gamification", "Cognitive", "Assessment"]
        },
        {
            "name": "MindmetriQ（游戏化评估）",
            "name_en": "MindmetriQ (Gamified Assessment)",
            "type": "url",
            "url": "https://www.testpartnership.com/assessments/mindmetriq.html",
            "tags": ["Gamification", "Psychometric"]
        },
    ],

    # ===== 职位/技能字典 =====
    "职位/技能字典": [
        {
            "name": "ESCO（欧洲技能分类）",
            "name_en": "ESCO (European Skills Classification)",
            "type": "url",
            "url": "https://esco.ec.europa.eu/",
            "tags": ["Taxonomy", "Skills", "EU"]
        },
        {
            "name": "WEF全球技能分类（世界经济论坛）",
            "name_en": "WEF Global Skills Taxonomy",
            "type": "url",
            "url": "https://www.weforum.org/publications/building-a-common-language-for-skills-at-work-a-global-taxonomy/",
            "tags": ["Taxonomy", "Skills", "Global"]
        },
    ],

    # ===== 薪酬与职位数据 =====
    "薪酬与职位数据": [
        {
            "name": "Glassdoor Salaries（薪酬数据）",
            "name_en": "Glassdoor Salaries",
            "type": "url",
            "url": "https://www.glassdoor.com/Salaries/",
            "tags": ["Compensation", "Free", "Reviews"]
        },
        {
            "name": "Comparably（薪酬对比）",
            "name_en": "Comparably (Compensation Comparison)",
            "type": "url",
            "url": "https://www.comparably.com/",
            "tags": ["Compensation", "Culture", "Reviews"]
        },
        {
            "name": "Ravio（欧洲薪酬基准）",
            "name_en": "Ravio (European Compensation Benchmarking)",
            "type": "url",
            "url": "https://ravio.com/",
            "tags": ["Compensation", "Europe", "Real-time"]
        },
    ],

    # ===== 人才流动追踪 =====
    "人才流动追踪": [
        {
            "name": "Gloat（内部人才市场）",
            "name_en": "Gloat (Internal Talent Marketplace)",
            "type": "url",
            "url": "https://www.gloat.com/",
            "tags": ["Mobility", "AI", "Marketplace"]
        },
        {
            "name": "Fuel50（职业发展平台）",
            "name_en": "Fuel50 (Career Development Platform)",
            "type": "url",
            "url": "https://fuel50.com/",
            "tags": ["Mobility", "Career", "Skills"]
        },
    ],

    # ===== 招聘营销平台 =====
    "招聘营销平台": [
        {
            "name": "Rally Awards（招聘营销奖项）",
            "name_en": "Rally Awards (Recruitment Marketing Awards)",
            "type": "url",
            "url": "https://rallyawards.com/",
            "tags": ["Marketing", "Awards", "EB"]
        },
        {
            "name": "Sense Playbook（招聘营销指南）",
            "name_en": "Sense EB Playbook 2025",
            "type": "url",
            "url": "https://www.sensehq.com/books-reports/the-2025-employer-branding-recruitment-marketing-playbook",
            "tags": ["Marketing", "Guide", "EB"]
        },
    ],

    # ===== 视频面试平台 =====
    "视频面试平台": [
        {
            "name": "Pipplet（语言技能视频）",
            "name_en": "Pipplet (Language Skills Video)",
            "type": "url",
            "url": "https://www.pipplet.com/",
            "tags": ["Video", "Language", "Assessment"]
        },
        {
            "name": "VantageSpark（视频面试）",
            "name_en": "VantageSpark (Video Interview)",
            "type": "url",
            "url": "https://www.vantagecircle.com/solutions/video-interview/",
            "tags": ["Video", "Interview"]
        },
    ],

    # ===== 专业招聘机构 =====
    "专业招聘机构": [
        {
            "name": "Egon Zehnder（高管搜索）",
            "name_en": "Egon Zehnder (Executive Search)",
            "type": "url",
            "url": "https://www.egonzehnder.com/",
            "tags": ["Executive", "Leadership"]
        },
        {
            "name": "Russell Reynolds（高管猎头）",
            "name_en": "Russell Reynolds Associates",
            "type": "url",
            "url": "https://www.russellreynolds.com/",
            "tags": ["Executive", "Board"]
        },
    ],

    # ===== 招聘数据隐私与合规 =====
    "招聘数据隐私与合规": [
        {
            "name": "IAPP（隐私专业人士协会）",
            "name_en": "IAPP (Privacy Professionals Association)",
            "type": "url",
            "url": "https://iapp.org/",
            "tags": ["Privacy", "Certification", "GDPR"]
        },
        {
            "name": "DLA Piper数据保护法（全球指南）",
            "name_en": "DLA Piper Data Protection Laws",
            "type": "url",
            "url": "https://www.dlapiperdataprotection.com/",
            "tags": ["Privacy", "Global", "Legal"]
        },
    ],

    # ===== 招聘反欺诈与验证 =====
    "招聘反欺诈与验证": [
        {
            "name": "Accurate（背景调查）",
            "name_en": "Accurate Background (Background Check)",
            "type": "url",
            "url": "https://www.accurate.com/",
            "tags": ["Background Check", "Compliance"]
        },
    ],

    # ===== 技术招聘专项 =====
    "技术招聘专项": [
        {
            "name": "Triplebyte（技术人才评估）",
            "name_en": "Triplebyte (Technical Talent Assessment)",
            "type": "url",
            "url": "https://triplebyte.com/",
            "tags": ["Technical", "Assessment", "Matching"]
        },
        {
            "name": "Turing（远程开发者）",
            "name_en": "Turing (Remote Developers)",
            "type": "url",
            "url": "https://www.turing.com/",
            "tags": ["Technical", "Remote", "Global"]
        },
    ],

    # ===== 批量招聘工具 =====
    "批量招聘工具": [
        {
            "name": "CEIPAL（高流量ATS）",
            "name_en": "CEIPAL (High-Volume ATS)",
            "type": "url",
            "url": "https://www.ceipal.com/",
            "tags": ["High-Volume", "Staffing", "AI"]
        },
    ],

    # ===== 竞争对手分析 =====
    "竞争对手分析": [
        {
            "name": "Draup（人才智能）",
            "name_en": "Draup (Talent Intelligence)",
            "type": "url",
            "url": "https://draup.com/",
            "tags": ["Intelligence", "Skills", "Enterprise"]
        },
    ],

    # ===== 心理测评 AI =====
    "心理测评 AI": [
        {
            "name": "Emotify（情商评估）",
            "name_en": "Emotify (Emotional Intelligence Assessment)",
            "type": "url",
            "url": "https://www.criteriacorp.com/assess/emotify",
            "tags": ["Psychometric", "EQ", "Gamification"]
        },
    ],

    # ===== 招聘运营 (RecOps) =====
    "招聘运营 (RecOps)": [
        {
            "name": "RecOps Con（招聘运营大会）",
            "name_en": "RecOps Con (Recruiting Operations Conference)",
            "type": "url",
            "url": "https://www.recopscon.com/",
            "tags": ["RecOps", "Conference", "Community"]
        },
    ],

    # ===== AI 视频面试 =====
    "AI 视频面试": [
        {
            "name": "Wedge HR（AI视频筛选）",
            "name_en": "Wedge HR (AI Video Screening)",
            "type": "url",
            "url": "https://www.wedge.hr/",
            "tags": ["AI", "Video", "Screening"]
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
