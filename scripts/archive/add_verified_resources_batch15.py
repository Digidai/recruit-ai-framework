#!/usr/bin/env python3
"""
Batch 15: Add verified resources to tarf.json
Cross-validated resources covering weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== AI 简历解析/筛选 =====
    "AI 简历解析/筛选": [
        {
            "name": "Affinda（AI简历解析）",
            "name_en": "Affinda (AI Resume Parser)",
            "type": "url",
            "url": "https://www.affinda.com/",
            "tags": ["AI", "Parsing", "Multilingual"]
        },
        {
            "name": "Daxtra（高精度简历解析）",
            "name_en": "Daxtra (High-Accuracy Parsing)",
            "type": "url",
            "url": "https://www.daxtra.com/",
            "tags": ["AI", "Parsing", "Enterprise"]
        },
        {
            "name": "RChilli（简历解析API）",
            "name_en": "RChilli (Resume Parser API)",
            "type": "url",
            "url": "https://www.rchilli.com/",
            "tags": ["AI", "API", "Parsing"]
        },
        {
            "name": "HiPeople（AI候选人筛选）",
            "name_en": "HiPeople (AI Candidate Screening)",
            "type": "url",
            "url": "https://www.hipeople.io/",
            "tags": ["AI", "Screening", "Reference"]
        },
    ],

    # ===== 游戏化与 VR/AR 招聘 =====
    "游戏化与 VR/AR 招聘": [
        {
            "name": "The Talent Games（游戏化招聘平台）",
            "name_en": "The Talent Games (Gamified Recruiting)",
            "type": "url",
            "url": "https://thetalentgames.com/",
            "tags": ["Gamification", "Engagement", "Gen-Z"]
        },
        {
            "name": "Equalture（游戏化评估）",
            "name_en": "Equalture (Game-Based Assessment)",
            "type": "url",
            "url": "https://www.equalture.com/",
            "tags": ["Gamification", "Bias-Free", "Games"]
        },
        {
            "name": "Assess Candidates（游戏化测评）",
            "name_en": "Assess Candidates (Game-Based Tests)",
            "type": "url",
            "url": "https://www.assesscandidates.com/",
            "tags": ["Gamification", "Assessment", "Cognitive"]
        },
    ],

    # ===== 全球招聘与远程团队 =====
    "全球招聘与远程团队": [
        {
            "name": "Globalization Partners（全球EOR）",
            "name_en": "Globalization Partners (Global EOR)",
            "type": "url",
            "url": "https://www.globalization-partners.com/",
            "tags": ["EOR", "Global", "Enterprise"]
        },
        {
            "name": "Velocity Global（全球雇佣）",
            "name_en": "Velocity Global (Global Employment)",
            "type": "url",
            "url": "https://velocityglobal.com/",
            "tags": ["EOR", "Global", "Immigration"]
        },
        {
            "name": "Papaya Global（全球薪酬）",
            "name_en": "Papaya Global (Global Payroll)",
            "type": "url",
            "url": "https://www.papayaglobal.com/",
            "tags": ["EOR", "Payroll", "Compliance"]
        },
        {
            "name": "Atlas HXM（全球EOR平台）",
            "name_en": "Atlas HXM (Global EOR Platform)",
            "type": "url",
            "url": "https://www.atlashxm.com/",
            "tags": ["EOR", "Global", "SaaS"]
        },
        {
            "name": "RemoFirst（经济型EOR）",
            "name_en": "RemoFirst (Cost-Effective EOR)",
            "type": "url",
            "url": "https://www.remofirst.com/",
            "tags": ["EOR", "Affordable", "Global"]
        },
        {
            "name": "Borderless AI（AI驱动EOR）",
            "name_en": "Borderless AI (AI-Powered EOR)",
            "type": "url",
            "url": "https://www.hireborderless.com/",
            "tags": ["EOR", "AI", "Fast"]
        },
    ],

    # ===== 招聘播客与媒体 =====
    "招聘播客与媒体": [
        {
            "name": "Chad & Cheese Podcast（招聘辩论）",
            "name_en": "Chad & Cheese Podcast",
            "type": "url",
            "url": "https://www.chadcheese.com/",
            "tags": ["Podcast", "Recruiting", "Commentary"]
        },
        {
            "name": "DriveThruHR（午间HR播客）",
            "name_en": "DriveThruHR Podcast",
            "type": "url",
            "url": "https://www.drivethruhr.com/",
            "tags": ["Podcast", "HR", "Quick"]
        },
        {
            "name": "HR Happy Hour（HR网络播客）",
            "name_en": "HR Happy Hour Network",
            "type": "url",
            "url": "https://www.hrhappyhour.net/",
            "tags": ["Podcast", "HR", "Network"]
        },
        {
            "name": "Workology Podcast（HR策略）",
            "name_en": "Workology Podcast",
            "type": "url",
            "url": "https://workology.com/podcast/",
            "tags": ["Podcast", "HR", "Strategy"]
        },
    ],

    # ===== 招聘通讯与社区 =====
    "招聘通讯与社区": [
        {
            "name": "Recruiting Headlines（招聘新闻）",
            "name_en": "Recruiting Headlines Newsletter",
            "type": "url",
            "url": "https://recruitingheadlines.com/",
            "tags": ["Newsletter", "News", "Daily"]
        },
        {
            "name": "People Managing People社区（HR社区）",
            "name_en": "People Managing People Community",
            "type": "url",
            "url": "https://peoplemanagingpeople.com/community/",
            "tags": ["Community", "HR", "Leadership"]
        },
        {
            "name": "HRExaminer（HR数字分析）",
            "name_en": "HRExaminer (HR Digital Analysis)",
            "type": "url",
            "url": "https://www.hrexaminer.com/",
            "tags": ["Media", "Analysis", "Research"]
        },
    ],

    # ===== 技术测评平台 =====
    "技术测评平台": [
        {
            "name": "Codility（编程评估平台）",
            "name_en": "Codility (Code Assessment Platform)",
            "type": "url",
            "url": "https://www.codility.com/",
            "tags": ["Technical", "Coding", "Assessment"]
        },
        {
            "name": "SkillsCode（技能测试）",
            "name_en": "iMocha (Skills Assessment)",
            "type": "url",
            "url": "https://www.imocha.io/",
            "tags": ["Technical", "Skills", "AI"]
        },
    ],

    # ===== 透明度/文档化 =====
    "透明度/文档化": [
        {
            "name": "Holistic AI（AI风险管理）",
            "name_en": "Holistic AI (AI Risk Management)",
            "type": "url",
            "url": "https://www.holisticai.com/",
            "tags": ["AI", "Audit", "Compliance"]
        },
        {
            "name": "Credo AI（AI治理平台）",
            "name_en": "Credo AI (AI Governance Platform)",
            "type": "url",
            "url": "https://www.credo.ai/",
            "tags": ["AI", "Governance", "Transparency"]
        },
    ],

    # ===== 可解释 AI (XAI) =====
    "可解释 AI (XAI)": [
        {
            "name": "LIME（本地可解释模型）",
            "name_en": "LIME (Local Interpretable Explanations)",
            "type": "url",
            "url": "https://github.com/marcotcr/lime",
            "tags": ["XAI", "Open Source", "Python"]
        },
        {
            "name": "SHAP（Shapley值解释器）",
            "name_en": "SHAP (Shapley Additive Explanations)",
            "type": "url",
            "url": "https://shap.readthedocs.io/",
            "tags": ["XAI", "Open Source", "ML"]
        },
    ],

    # ===== 退伍军人招聘认证 =====
    "退伍军人招聘认证": [
        {
            "name": "Hire Heroes USA（退伍军人就业）",
            "name_en": "Hire Heroes USA (Veteran Employment)",
            "type": "url",
            "url": "https://www.hireheroesusa.org/",
            "tags": ["Veteran", "Nonprofit", "Transition"]
        },
        {
            "name": "American Corporate Partners（退伍军人辅导）",
            "name_en": "American Corporate Partners (Veteran Mentoring)",
            "type": "url",
            "url": "https://www.acp-usa.org/",
            "tags": ["Veteran", "Mentoring", "Career"]
        },
    ],

    # ===== 招聘/HR 开源项目 =====
    "招聘/HR 开源项目": [
        {
            "name": "OpenCATS（开源ATS）",
            "name_en": "OpenCATS (Open Source ATS)",
            "type": "url",
            "url": "https://www.opencats.org/",
            "tags": ["Open Source", "ATS", "Free"]
        },
        {
            "name": "OrangeHRM（开源HRM）",
            "name_en": "OrangeHRM (Open Source HRM)",
            "type": "url",
            "url": "https://www.orangehrm.com/",
            "tags": ["Open Source", "HRIS", "Free"]
        },
    ],

    # ===== AI 编程面试 =====
    "AI 编程面试": [
        {
            "name": "CodeSignal（AI编程评估）",
            "name_en": "CodeSignal (AI Coding Assessment)",
            "type": "url",
            "url": "https://codesignal.com/",
            "tags": ["AI", "Coding", "Technical"]
        },
        {
            "name": "Qualified（实时编程面试）",
            "name_en": "Qualified (Live Coding Interviews)",
            "type": "url",
            "url": "https://www.qualified.io/",
            "tags": ["Coding", "Live", "Assessment"]
        },
    ],

    # ===== 招聘职业路径 =====
    "招聘职业路径": [
        {
            "name": "Talent Acquisition Career Path指南（职业规划）",
            "name_en": "TA Career Path Guide",
            "type": "url",
            "url": "https://www.shrm.org/topics-tools/tools/career-navigator",
            "tags": ["Career", "TA", "Development"]
        },
        {
            "name": "RecruiterZone职业发展（招聘者社区）",
            "name_en": "RecruiterZone Career Development",
            "type": "url",
            "url": "https://recruiterzone.com/",
            "tags": ["Career", "Community", "Resources"]
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
