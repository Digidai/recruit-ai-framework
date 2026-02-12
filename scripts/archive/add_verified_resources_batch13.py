#!/usr/bin/env python3
"""
Batch 13: Add verified resources to tarf.json
Cross-validated resources covering weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== ATS 与招聘协作 =====
    "ATS 与招聘协作": [
        {
            "name": "Eightfold AI（企业人才管理）",
            "name_en": "Eightfold AI (Enterprise Talent Management)",
            "type": "url",
            "url": "https://eightfold.ai/",
            "tags": ["ATS", "AI", "Enterprise"]
        },
        {
            "name": "Workable（一站式招聘平台）",
            "name_en": "Workable (All-in-One Recruiting)",
            "type": "url",
            "url": "https://www.workable.com/",
            "tags": ["ATS", "SMB", "AI"]
        },
        {
            "name": "Recruit CRM（ATS+CRM平台）",
            "name_en": "Recruit CRM (ATS + CRM Platform)",
            "type": "url",
            "url": "https://recruitcrm.io/",
            "tags": ["ATS", "CRM", "Agency"]
        },
    ],

    # ===== 人才市场情报与竞争分析 =====
    "人才市场情报与竞争分析": [
        {
            "name": "TalentNeuron（劳动力市场智能）",
            "name_en": "TalentNeuron (Labor Market Intelligence)",
            "type": "url",
            "url": "https://www.talentneuron.com/",
            "tags": ["Intelligence", "Market Data", "Analytics"]
        },
        {
            "name": "Findem（人才市场数据）",
            "name_en": "Findem (Talent Market Intelligence)",
            "type": "url",
            "url": "https://www.findem.ai/",
            "tags": ["Intelligence", "AI", "Analytics"]
        },
        {
            "name": "Skima AI（人才智能工具）",
            "name_en": "Skima AI (Talent Intelligence Tool)",
            "type": "url",
            "url": "https://skima.ai/",
            "tags": ["Intelligence", "AI", "Sourcing"]
        },
    ],

    # ===== AI 视频面试 =====
    "AI 视频面试": [
        {
            "name": "VidCruiter（企业视频面试）",
            "name_en": "VidCruiter (Enterprise Video Interview)",
            "type": "url",
            "url": "https://vidcruiter.com/",
            "tags": ["Video", "Enterprise", "Compliance"]
        },
        {
            "name": "Spark Hire（视频面试平台）",
            "name_en": "Spark Hire (Video Interview Platform)",
            "type": "url",
            "url": "https://www.sparkhire.com/",
            "tags": ["Video", "SMB", "Affordable"]
        },
        {
            "name": "Interviewer.AI（AI视频筛选）",
            "name_en": "Interviewer.AI (AI Video Screening)",
            "type": "url",
            "url": "https://interviewer.ai/",
            "tags": ["Video", "AI", "Automation"]
        },
        {
            "name": "Jobma（多格式面试平台）",
            "name_en": "Jobma (Multi-Format Interview)",
            "type": "url",
            "url": "https://www.jobma.com/",
            "tags": ["Video", "Assessment", "Enterprise"]
        },
    ],

    # ===== 心理测评 AI =====
    "心理测评 AI": [
        {
            "name": "Pymetrics（游戏化神经科学评估）",
            "name_en": "Pymetrics (Gamified Neuroscience Assessment)",
            "type": "url",
            "url": "https://www.pymetrics.ai/",
            "tags": ["Psychometric", "Gamification", "AI"]
        },
        {
            "name": "Arctic Shores（行为评估游戏）",
            "name_en": "Arctic Shores (Behavioral Assessment Games)",
            "type": "url",
            "url": "https://www.arcticshores.com/",
            "tags": ["Psychometric", "Games", "Potential"]
        },
        {
            "name": "Vervoe（技能沉浸式评估）",
            "name_en": "Vervoe (Skills-Based Immersive Assessment)",
            "type": "url",
            "url": "https://vervoe.com/",
            "tags": ["Assessment", "Skills", "AI"]
        },
    ],

    # ===== 开发者工具/SDK =====
    "开发者工具/SDK": [
        {
            "name": "Pearch AI（候选人搜索API）",
            "name_en": "Pearch AI (Candidate Sourcing API)",
            "type": "url",
            "url": "https://pearch.ai/",
            "tags": ["API", "Sourcing", "AI"]
        },
        {
            "name": "SmartRecruiters开发者平台（招聘API）",
            "name_en": "SmartRecruiters Developer Platform",
            "type": "url",
            "url": "https://developers.smartrecruiters.com/",
            "tags": ["API", "SDK", "Enterprise"]
        },
        {
            "name": "Talentobe API（软技能API）",
            "name_en": "Talentobe API (Soft Skills API)",
            "type": "url",
            "url": "https://talentobe.com/",
            "tags": ["API", "Assessment", "Soft Skills"]
        },
    ],

    # ===== 日程协调 =====
    "日程协调": [
        {
            "name": "Sense面试排程（AI排程）",
            "name_en": "Sense Interview Scheduling",
            "type": "url",
            "url": "https://www.sensehq.com/platform/interview-scheduling",
            "tags": ["Scheduling", "AI", "Automation"]
        },
        {
            "name": "VidCruiter排程工具（面试协调）",
            "name_en": "VidCruiter Scheduling Tool",
            "type": "url",
            "url": "https://vidcruiter.com/video-interviewing/scheduling/",
            "tags": ["Scheduling", "Video", "Automation"]
        },
    ],

    # ===== 视频面试平台 =====
    "视频面试平台": [
        {
            "name": "Hirevire（异步视频面试）",
            "name_en": "Hirevire (Async Video Interview)",
            "type": "url",
            "url": "https://hirevire.com/",
            "tags": ["Video", "Async", "SMB"]
        },
        {
            "name": "Veloxhire AI（AI视频平台）",
            "name_en": "Veloxhire AI (AI Video Platform)",
            "type": "url",
            "url": "https://veloxhire.ai/",
            "tags": ["Video", "AI", "Speed"]
        },
    ],

    # ===== 专业招聘机构 =====
    "专业招聘机构": [
        {
            "name": "Hays（全球专业招聘）",
            "name_en": "Hays (Global Professional Recruiting)",
            "type": "url",
            "url": "https://www.hays.com/",
            "tags": ["Staffing", "Professional", "Global"]
        },
        {
            "name": "Randstad（人力资源服务）",
            "name_en": "Randstad (HR Services)",
            "type": "url",
            "url": "https://www.randstad.com/",
            "tags": ["Staffing", "Temp", "Global"]
        },
    ],

    # ===== 招聘营销平台 =====
    "招聘营销平台": [
        {
            "name": "Harver（高流量招聘自动化）",
            "name_en": "Harver (High-Volume Hiring Automation)",
            "type": "url",
            "url": "https://harver.com/",
            "tags": ["Marketing", "High-Volume", "Assessment"]
        },
        {
            "name": "Elevatus（AI招聘平台）",
            "name_en": "Elevatus (AI Recruitment Platform)",
            "type": "url",
            "url": "https://www.elevatus.io/",
            "tags": ["Marketing", "AI", "Video"]
        },
    ],

    # ===== 候选人体验平台 =====
    "候选人体验平台": [
        {
            "name": "Beamery（人才生命周期）",
            "name_en": "Beamery (Talent Lifecycle)",
            "type": "url",
            "url": "https://beamery.com/",
            "tags": ["CX", "CRM", "Enterprise"]
        },
        {
            "name": "Reejig（劳动力智能）",
            "name_en": "Reejig (Workforce Intelligence)",
            "type": "url",
            "url": "https://reejig.com/",
            "tags": ["CX", "AI", "Mobility"]
        },
    ],

    # ===== 人才流动追踪 =====
    "人才流动追踪": [
        {
            "name": "TurboHire（招聘自动化）",
            "name_en": "TurboHire (Recruiting Automation)",
            "type": "url",
            "url": "https://turbohire.co/",
            "tags": ["Mobility", "AI", "Automation"]
        },
    ],

    # ===== 年度报告 =====
    "年度报告": [
        {
            "name": "McKinsey人才趋势报告（咨询研究）",
            "name_en": "McKinsey Talent Trends Report",
            "type": "url",
            "url": "https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights",
            "tags": ["Report", "Trends", "Consulting"]
        },
        {
            "name": "Mercer全球人才趋势（年度调研）",
            "name_en": "Mercer Global Talent Trends",
            "type": "url",
            "url": "https://www.mercer.com/insights/people-strategy/future-of-work/global-talent-trends/",
            "tags": ["Report", "Global", "HR"]
        },
    ],

    # ===== 行业分析 =====
    "行业分析": [
        {
            "name": "Bersin研究（HR技术分析）",
            "name_en": "Bersin Research (HR Tech Analysis)",
            "type": "url",
            "url": "https://joshbersin.com/",
            "tags": ["Research", "HR Tech", "Analysis"]
        },
        {
            "name": "Fosway Group（欧洲HR分析）",
            "name_en": "Fosway Group (European HR Analysis)",
            "type": "url",
            "url": "https://www.fosway.com/",
            "tags": ["Research", "Europe", "HCM"]
        },
    ],

    # ===== 招聘职业发展 =====
    "招聘职业发展": [
        {
            "name": "ERE Recruiting（招聘策略社区）",
            "name_en": "ERE Recruiting (Recruiting Strategy Community)",
            "type": "url",
            "url": "https://www.ere.net/",
            "tags": ["Career", "Community", "Strategy"]
        },
        {
            "name": "Recruiting Brainfood（行业通讯）",
            "name_en": "Recruiting Brainfood Newsletter",
            "type": "url",
            "url": "https://www.recruitingbrainfood.com/",
            "tags": ["Career", "Newsletter", "Trends"]
        },
    ],

    # ===== 术语表/词典 =====
    "术语表/词典": [
        {
            "name": "AIHR HR术语表（人力资源词汇）",
            "name_en": "AIHR HR Glossary",
            "type": "url",
            "url": "https://www.aihr.com/resources/hr-glossary/",
            "tags": ["Glossary", "HR", "Learning"]
        },
        {
            "name": "Indeed招聘词典（求职术语）",
            "name_en": "Indeed Hiring Glossary",
            "type": "url",
            "url": "https://www.indeed.com/career-advice/career-development/hiring-terminology",
            "tags": ["Glossary", "Hiring", "Reference"]
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
