#!/usr/bin/env python3
"""
Batch 11: Add verified resources to tarf.json
Cross-validated resources covering weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== 视频面试平台 =====
    "视频面试平台": [
        {
            "name": "Interviewstream（视频面试套件）",
            "name_en": "Interviewstream (Video Interview Suite)",
            "type": "url",
            "url": "https://www.interviewstream.com/",
            "tags": ["Video", "Interview", "Scheduling"]
        },
        {
            "name": "Talview（AI监考与面试）",
            "name_en": "Talview (AI Proctoring & Interviewing)",
            "type": "url",
            "url": "https://www.talview.com/",
            "tags": ["Video", "AI", "Proctoring"]
        },
        {
            "name": "HarQen（数字面试平台）",
            "name_en": "HarQen (Digital Interview Platform)",
            "type": "url",
            "url": "https://www.harqen.com/",
            "tags": ["Video", "Audio", "High-Volume"]
        },
    ],

    # ===== 领英 X-Ray =====
    "领英 X-Ray": [
        {
            "name": "SourcingLab（布尔搜索扩展）",
            "name_en": "SourcingLab (Boolean Search Extension)",
            "type": "url",
            "url": "https://www.sourcinglab.io/",
            "tags": ["Sourcing", "Boolean", "Chrome"]
        },
        {
            "name": "recruitRyte AI Boolean（AI布尔生成器）",
            "name_en": "recruitRyte AI Boolean Generator",
            "type": "url",
            "url": "https://recruitryte.com/",
            "tags": ["Sourcing", "AI", "Boolean"]
        },
    ],

    # ===== 候选人体验平台 =====
    "候选人体验平台": [
        {
            "name": "Talent Board CandE（候选人体验奖）",
            "name_en": "Talent Board CandE Awards",
            "type": "url",
            "url": "https://www.thetalentboard.org/",
            "tags": ["CX", "Awards", "Research"]
        },
    ],

    # ===== 技术面试平台 =====
    "技术面试平台": [
        {
            "name": "Karat（技术面试外包）",
            "name_en": "Karat (Technical Interview Outsourcing)",
            "type": "url",
            "url": "https://karat.com/",
            "tags": ["Technical", "Interview", "Enterprise"]
        },
        {
            "name": "Interviewing.io（模拟技术面试）",
            "name_en": "Interviewing.io (Mock Technical Interviews)",
            "type": "url",
            "url": "https://interviewing.io/",
            "tags": ["Technical", "Mock", "FAANG"]
        },
        {
            "name": "Pramp/Exponent（点对点面试练习）",
            "name_en": "Pramp/Exponent (Peer-to-Peer Practice)",
            "type": "url",
            "url": "https://www.tryexponent.com/",
            "tags": ["Technical", "Practice", "Free"]
        },
    ],

    # ===== 年度报告 =====
    "年度报告": [
        {
            "name": "Deloitte人力资本趋势报告（年度）",
            "name_en": "Deloitte Global Human Capital Trends",
            "type": "url",
            "url": "https://www2.deloitte.com/us/en/insights/focus/human-capital-trends.html",
            "tags": ["Report", "Trends", "Annual"]
        },
        {
            "name": "Josh Bersin HR技术市场报告（年度）",
            "name_en": "Josh Bersin HR Tech Market Report",
            "type": "url",
            "url": "https://joshbersin.com/research/",
            "tags": ["Report", "HR Tech", "Annual"]
        },
    ],

    # ===== 校园招聘平台（中国） =====
    "校园招聘平台（中国）": [
        {
            "name": "实习僧（实习招聘平台）",
            "name_en": "Shixiseng (Internship Platform)",
            "type": "url",
            "url": "https://www.shixiseng.com/",
            "tags": ["Campus", "China", "Internship"]
        },
        {
            "name": "BOSS直聘校园版（校招）",
            "name_en": "BOSS Zhipin Campus (Campus Recruiting)",
            "type": "url",
            "url": "https://www.zhipin.com/school/",
            "tags": ["Campus", "China", "Job Board"]
        },
    ],

    # ===== 面试官培训平台 =====
    "面试官培训平台": [
        {
            "name": "SocialTalent（面试智能平台）",
            "name_en": "SocialTalent (Interview Intelligence Platform)",
            "type": "url",
            "url": "https://www.socialtalent.com/",
            "tags": ["Training", "Interview", "Enterprise"]
        },
        {
            "name": "Hone（管理者培训）",
            "name_en": "Hone (Manager Training)",
            "type": "url",
            "url": "https://www.honehq.com/",
            "tags": ["Training", "Leadership", "Live"]
        },
    ],

    # ===== 高管评估工具 =====
    "高管评估工具": [
        {
            "name": "Korn Ferry KF4D（领导力评估）",
            "name_en": "Korn Ferry KF4D (Leadership Assessment)",
            "type": "url",
            "url": "https://www.kornferry.com/capabilities/assessment-succession",
            "tags": ["Executive", "Assessment", "Leadership"]
        },
        {
            "name": "DDI（领导力发展）",
            "name_en": "DDI (Leadership Development)",
            "type": "url",
            "url": "https://www.ddiworld.com/",
            "tags": ["Executive", "Assessment", "Development"]
        },
    ],

    # ===== 招聘社交媒体 =====
    "招聘社交媒体": [
        {
            "name": "Later（社交媒体排程）",
            "name_en": "Later (Social Media Scheduling)",
            "type": "url",
            "url": "https://later.com/",
            "tags": ["Social Media", "Scheduling", "EB"]
        },
        {
            "name": "Canva社交媒体模板（设计）",
            "name_en": "Canva Social Media Templates",
            "type": "url",
            "url": "https://www.canva.com/templates/social-media/",
            "tags": ["Social Media", "Design", "Templates"]
        },
    ],

    # ===== 设计工具 =====
    "设计工具": [
        {
            "name": "Snappa（快速图形设计）",
            "name_en": "Snappa (Quick Graphic Design)",
            "type": "url",
            "url": "https://snappa.com/",
            "tags": ["Design", "Graphics", "Easy"]
        },
        {
            "name": "Crello/VistaCreate（社交媒体设计）",
            "name_en": "VistaCreate (Social Media Design)",
            "type": "url",
            "url": "https://create.vista.com/",
            "tags": ["Design", "Social", "Templates"]
        },
    ],

    # ===== 行业分析 =====
    "行业分析": [
        {
            "name": "SHRM研究中心（HR研究）",
            "name_en": "SHRM Research Hub",
            "type": "url",
            "url": "https://www.shrm.org/topics-tools/research",
            "tags": ["Research", "HR", "Data"]
        },
        {
            "name": "Gartner HR研究（HR分析）",
            "name_en": "Gartner HR Research",
            "type": "url",
            "url": "https://www.gartner.com/en/human-resources",
            "tags": ["Research", "Enterprise", "Trends"]
        },
    ],

    # ===== 招聘案例研究 =====
    "招聘案例研究": [
        {
            "name": "LinkedIn Talent Solutions案例（客户故事）",
            "name_en": "LinkedIn Talent Solutions Case Studies",
            "type": "url",
            "url": "https://business.linkedin.com/talent-solutions/customer-stories",
            "tags": ["Case Study", "LinkedIn", "Enterprise"]
        },
        {
            "name": "Greenhouse客户故事（招聘案例）",
            "name_en": "Greenhouse Customer Stories",
            "type": "url",
            "url": "https://www.greenhouse.com/customers",
            "tags": ["Case Study", "ATS", "Success"]
        },
    ],

    # ===== 人才流动追踪 =====
    "人才流动追踪": [
        {
            "name": "Workday Skills Cloud（技能云）",
            "name_en": "Workday Skills Cloud",
            "type": "url",
            "url": "https://www.workday.com/en-us/products/human-capital-management/skills-cloud.html",
            "tags": ["Mobility", "Skills", "Enterprise"]
        },
        {
            "name": "Phenom内部流动（内部人才市场）",
            "name_en": "Phenom Internal Mobility",
            "type": "url",
            "url": "https://www.phenom.com/internal-mobility",
            "tags": ["Mobility", "AI", "Marketplace"]
        },
    ],

    # ===== 术语表/词典 =====
    "术语表/词典": [
        {
            "name": "SHRM HR术语表（HR词汇）",
            "name_en": "SHRM HR Glossary",
            "type": "url",
            "url": "https://www.shrm.org/topics-tools/tools/hr-glossary",
            "tags": ["Glossary", "HR", "Reference"]
        },
        {
            "name": "Workable招聘术语表（招聘词汇）",
            "name_en": "Workable Recruiting Glossary",
            "type": "url",
            "url": "https://resources.workable.com/hr-terms/",
            "tags": ["Glossary", "Recruiting", "Reference"]
        },
    ],

    # ===== 招聘文档与知识库 =====
    "招聘文档与知识库": [
        {
            "name": "Lever招聘资源库（模板）",
            "name_en": "Lever Recruiting Resources",
            "type": "url",
            "url": "https://www.lever.co/resources/",
            "tags": ["Templates", "Guides", "ATS"]
        },
        {
            "name": "Gem招聘知识库（指南）",
            "name_en": "Gem Recruiting Knowledge Base",
            "type": "url",
            "url": "https://www.gem.com/resources",
            "tags": ["Templates", "Guides", "CRM"]
        },
    ],

    # ===== 专业招聘机构 =====
    "专业招聘机构": [
        {
            "name": "Robert Half（专业人才）",
            "name_en": "Robert Half (Professional Staffing)",
            "type": "url",
            "url": "https://www.roberthalf.com/",
            "tags": ["Staffing", "Finance", "IT"]
        },
        {
            "name": "Michael Page（专业猎头）",
            "name_en": "Michael Page (Professional Recruiting)",
            "type": "url",
            "url": "https://www.michaelpage.com/",
            "tags": ["Executive", "Professional", "Global"]
        },
    ],

    # ===== 技术招聘专项 =====
    "技术招聘专项": [
        {
            "name": "Stack Overflow Talent（开发者招聘）",
            "name_en": "Stack Overflow Talent",
            "type": "url",
            "url": "https://stackoverflow.com/talent",
            "tags": ["Technical", "Developer", "Community"]
        },
    ],

    # ===== 候选人体验 =====
    "候选人体验": [
        {
            "name": "MokaHR候选人体验（体验调查）",
            "name_en": "MokaHR Candidate Experience Survey",
            "type": "url",
            "url": "https://www.mokahr.io/",
            "tags": ["CX", "Survey", "China"]
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
