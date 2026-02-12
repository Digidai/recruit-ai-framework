#!/usr/bin/env python3
"""
Batch 12 Fix: Add resources to correct category names
"""

import json

# Resources for correct category names
NEW_RESOURCES = {
    # ===== AI 简历解析/筛选 =====
    "AI 简历解析/筛选": [
        {
            "name": "hireEZ（AI人才搜索）",
            "name_en": "hireEZ (AI Talent Search)",
            "type": "url",
            "url": "https://hireez.com/",
            "tags": ["AI", "Sourcing", "Outreach"]
        },
        {
            "name": "SeekOut（人才智能平台）",
            "name_en": "SeekOut (Talent Intelligence)",
            "type": "url",
            "url": "https://www.seekout.com/",
            "tags": ["AI", "DEI", "Sourcing"]
        },
        {
            "name": "Entelo（预测性招聘）",
            "name_en": "Entelo (Predictive Recruiting)",
            "type": "url",
            "url": "https://www.entelo.com/",
            "tags": ["AI", "Predictive", "Sourcing"]
        },
    ],

    # ===== 自由职业/零工平台 =====
    "自由职业/零工平台": [
        {
            "name": "Contra（无佣金自由职业）",
            "name_en": "Contra (Commission-Free Freelance)",
            "type": "url",
            "url": "https://contra.com/",
            "tags": ["Freelance", "Design", "Tech"]
        },
        {
            "name": "Toptal（顶尖自由职业者）",
            "name_en": "Toptal (Top Freelance Talent)",
            "type": "url",
            "url": "https://www.toptal.com/",
            "tags": ["Freelance", "Elite", "Tech"]
        },
    ],

    # ===== 招聘 ROI 框架 =====
    "招聘 ROI 框架": [
        {
            "name": "SHRM人力资本基准（行业基准）",
            "name_en": "SHRM Human Capital Benchmarking",
            "type": "url",
            "url": "https://www.shrm.org/topics-tools/research/human-capital-benchmarking",
            "tags": ["ROI", "Benchmarking", "Metrics"]
        },
        {
            "name": "SHRM招聘成本计算器（成本分析）",
            "name_en": "SHRM Cost-Per-Hire Calculator",
            "type": "url",
            "url": "https://www.shrm.org/topics-tools/tools/calculators/cost-hire-calculator",
            "tags": ["ROI", "Calculator", "Free"]
        },
    ],

    # ===== 招聘技能培训 =====
    "招聘技能培训": [
        {
            "name": "AIRS招聘认证（专业培训）",
            "name_en": "AIRS Recruiting Certification",
            "type": "url",
            "url": "https://airsdirectory.com/learning/certifications",
            "tags": ["Certification", "Training", "Sourcing"]
        },
        {
            "name": "SourceCon学院（高级寻源）",
            "name_en": "SourceCon Academy",
            "type": "url",
            "url": "https://www.sourcecon.com/",
            "tags": ["Training", "Sourcing", "Conference"]
        },
        {
            "name": "LinkedIn学习招聘课程（在线学习）",
            "name_en": "LinkedIn Learning Recruiting Courses",
            "type": "url",
            "url": "https://www.linkedin.com/learning/topics/recruiting",
            "tags": ["Training", "Online", "Free"]
        },
    ],

    # ===== 雇主品牌/EVP =====
    "雇主品牌/EVP": [
        {
            "name": "Stories Inc（员工故事视频）",
            "name_en": "Stories Inc (Employee Story Videos)",
            "type": "url",
            "url": "https://storiesinc.com/",
            "tags": ["EB", "Video", "Content"]
        },
        {
            "name": "PathMotion（员工对话平台）",
            "name_en": "PathMotion (Employee Chat Platform)",
            "type": "url",
            "url": "https://www.pathmotion.com/",
            "tags": ["EB", "Chat", "Authentic"]
        },
    ],

    # ===== 远程工作资源 =====
    "远程工作资源": [
        {
            "name": "Remote.com（全球雇佣平台）",
            "name_en": "Remote.com (Global Employment Platform)",
            "type": "url",
            "url": "https://remote.com/",
            "tags": ["Remote", "EOR", "Global"]
        },
        {
            "name": "Oyster HR（分布式团队）",
            "name_en": "Oyster HR (Distributed Teams)",
            "type": "url",
            "url": "https://www.oysterhr.com/",
            "tags": ["Remote", "EOR", "Compliance"]
        },
        {
            "name": "Deel（全球薪酬合规）",
            "name_en": "Deel (Global Payroll Compliance)",
            "type": "url",
            "url": "https://www.deel.com/",
            "tags": ["Remote", "Payroll", "Global"]
        },
    ],

    # ===== 多元化招聘平台 (DEI) =====
    "多元化招聘平台 (DEI)": [
        {
            "name": "Jopwell（多元化人才平台）",
            "name_en": "Jopwell (Diverse Talent Platform)",
            "type": "url",
            "url": "https://www.jopwell.com/",
            "tags": ["DEI", "Community", "Enterprise"]
        },
        {
            "name": "PowerToFly（女性科技人才）",
            "name_en": "PowerToFly (Women in Tech)",
            "type": "url",
            "url": "https://powertofly.com/",
            "tags": ["DEI", "Women", "Tech"]
        },
        {
            "name": "Inclusively（残障人才平台）",
            "name_en": "Inclusively (Disability Inclusive)",
            "type": "url",
            "url": "https://www.inclusively.com/",
            "tags": ["DEI", "Disability", "Accommodation"]
        },
    ],

    # ===== 员工推荐平台 =====
    "员工推荐平台": [
        {
            "name": "Boon（AI员工推荐）",
            "name_en": "Boon (AI Employee Referrals)",
            "type": "url",
            "url": "https://www.boon.com/",
            "tags": ["Referral", "AI", "Gamification"]
        },
        {
            "name": "RolePoint（推荐管理）",
            "name_en": "RolePoint (Referral Management)",
            "type": "url",
            "url": "https://www.rolepoint.com/",
            "tags": ["Referral", "Analytics", "Enterprise"]
        },
    ],

    # ===== 虚拟招聘会平台 =====
    "虚拟招聘会平台": [
        {
            "name": "Handshake（校园招聘平台）",
            "name_en": "Handshake (Campus Recruiting Platform)",
            "type": "url",
            "url": "https://joinhandshake.com/",
            "tags": ["Campus", "Events", "Gen-Z"]
        },
        {
            "name": "Symplicity（校园服务）",
            "name_en": "Symplicity (Campus Services)",
            "type": "url",
            "url": "https://www.symplicity.com/",
            "tags": ["Campus", "CSM", "Events"]
        },
    ],

    # ===== 通用测评/心理测评 =====
    "通用测评/心理测评": [
        {
            "name": "SHL工作模拟（情景评估）",
            "name_en": "SHL Work Simulations",
            "type": "url",
            "url": "https://www.shl.com/solutions/assessments/work-simulations/",
            "tags": ["Assessment", "Simulation", "Enterprise"]
        },
        {
            "name": "Revelian工作模拟（认知测试）",
            "name_en": "Revelian Work Simulations",
            "type": "url",
            "url": "https://www.revelian.com/",
            "tags": ["Assessment", "Cognitive", "Australia"]
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
