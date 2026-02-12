#!/usr/bin/env python3
"""
Batch 19: Add verified resources to tarf.json
Cross-validated resources covering weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== 视频面试平台 (3资源→补充) =====
    "视频面试平台": [
        {
            "name": "Spark Hire（视频面试软件）",
            "name_en": "Spark Hire (Video Interview Software)",
            "type": "url",
            "url": "https://www.sparkhire.com/",
            "tags": ["Video", "Interview", "One-Way"]
        },
        {
            "name": "VidCruiter（SOC2认证视频）",
            "name_en": "VidCruiter (SOC2 Certified Video)",
            "type": "url",
            "url": "https://vidcruiter.com/",
            "tags": ["Video", "Compliance", "Enterprise"]
        },
        {
            "name": "interviewstream（视频面试平台）",
            "name_en": "interviewstream (Video Interview Platform)",
            "type": "url",
            "url": "https://interviewstream.com/",
            "tags": ["Video", "Async", "Enterprise"]
        },
    ],

    # ===== 招聘营销平台 (3资源→补充) =====
    "招聘营销平台": [
        {
            "name": "Teamtailor（雇主品牌平台）",
            "name_en": "Teamtailor (Employer Branding Platform)",
            "type": "url",
            "url": "https://www.teamtailor.com/",
            "tags": ["Marketing", "Branding", "Career Site"]
        },
        {
            "name": "Symphony Talent（品牌讲故事）",
            "name_en": "Symphony Talent (Brand Storytelling)",
            "type": "url",
            "url": "https://www.symphonytalent.com/",
            "tags": ["Marketing", "Branding", "Enterprise"]
        },
    ],

    # ===== 候选人体验平台 =====
    "候选人体验平台": [
        {
            "name": "Avature CRM（人才关系管理）",
            "name_en": "Avature CRM (Talent Relationship Management)",
            "type": "url",
            "url": "https://www.avature.net/",
            "tags": ["CRM", "Candidate Experience", "Enterprise"]
        },
        {
            "name": "iSmartRecruit 2.0（AI招聘CRM）",
            "name_en": "iSmartRecruit 2.0 (AI Recruiting CRM)",
            "type": "url",
            "url": "https://www.ismartrecruit.com/",
            "tags": ["CRM", "AI", "Chatbot"]
        },
        {
            "name": "Manatal招聘CRM",
            "name_en": "Manatal Recruiting CRM",
            "type": "url",
            "url": "https://www.manatal.com/",
            "tags": ["CRM", "AI", "Sourcing"]
        },
    ],

    # ===== 负责任 AI 指南 =====
    "负责任 AI 指南": [
        {
            "name": "英国政府AI招聘责任指南",
            "name_en": "UK Government Responsible AI in Recruitment",
            "type": "url",
            "url": "https://www.gov.uk/government/publications/responsible-ai-in-recruitment-guide",
            "tags": ["AI Ethics", "Government", "UK"]
        },
        {
            "name": "Oleeo AI治理计划指南",
            "name_en": "Oleeo AI Governance Plan Guide",
            "type": "url",
            "url": "https://www.oleeo.com/blog/how-to-create-an-ai-governance-plan-for-recruitment/",
            "tags": ["AI Ethics", "Governance", "Framework"]
        },
        {
            "name": "TRAPS框架（可信责任AI）",
            "name_en": "TRAPS Framework (Trusted Responsible AI)",
            "type": "url",
            "url": "https://aisera.com/platform/aisera-trust-center/",
            "tags": ["AI Ethics", "Framework", "Security"]
        },
    ],

    # ===== 专业招聘机构 =====
    "专业招聘机构": [
        {
            "name": "Aerotek（专业人力资源）",
            "name_en": "Aerotek (Professional Staffing)",
            "type": "url",
            "url": "https://www.aerotek.com/",
            "tags": ["Staffing", "Professional", "Engineering"]
        },
        {
            "name": "Robert Half（专业招聘）",
            "name_en": "Robert Half (Professional Recruiting)",
            "type": "url",
            "url": "https://www.roberthalf.com/",
            "tags": ["Staffing", "Finance", "Professional"]
        },
        {
            "name": "Kelly Services（人力资源服务）",
            "name_en": "Kelly Services (Workforce Solutions)",
            "type": "url",
            "url": "https://www.kellyservices.us/",
            "tags": ["Staffing", "Temporary", "Enterprise"]
        },
        {
            "name": "Spherion（灵活人力派遣）",
            "name_en": "Spherion (Flexible Staffing)",
            "type": "url",
            "url": "https://www.spherion.com/",
            "tags": ["Staffing", "Temp-to-Hire", "Flexible"]
        },
    ],

    # ===== 薪酬公平工具 =====
    "薪酬公平工具": [
        {
            "name": "Syndio PayEQ（薪酬公平分析）",
            "name_en": "Syndio PayEQ (Pay Equity Analysis)",
            "type": "url",
            "url": "https://synd.io/",
            "tags": ["Pay Equity", "Analytics", "Compliance"]
        },
        {
            "name": "PayAnalytics by beqom",
            "name_en": "PayAnalytics by beqom (Pay Gap Analysis)",
            "type": "url",
            "url": "https://www.payanalytics.com/",
            "tags": ["Pay Equity", "Analytics", "EU"]
        },
        {
            "name": "Trusaic PayParity（薪酬透明）",
            "name_en": "Trusaic PayParity (Pay Transparency)",
            "type": "url",
            "url": "https://trusaic.com/payparity/",
            "tags": ["Pay Equity", "ESG", "Reporting"]
        },
    ],

    # ===== 透明度/文档化 =====
    "透明度/文档化": [
        {
            "name": "oxethica AI审计工具",
            "name_en": "oxethica AI Audit Tool",
            "type": "url",
            "url": "https://www.oxethica.com/",
            "tags": ["AI Audit", "Transparency", "Compliance"]
        },
        {
            "name": "Centraleyes AI合规工具",
            "name_en": "Centraleyes AI Compliance Tools",
            "type": "url",
            "url": "https://www.centraleyes.com/",
            "tags": ["Compliance", "GRC", "Automation"]
        },
    ],

    # ===== 欧盟/国际法规 =====
    "欧盟/国际法规": [
        {
            "name": "EU AI Act高风险分类指南",
            "name_en": "EU AI Act High-Risk Classification Guide",
            "type": "url",
            "url": "https://artificialintelligenceact.eu/high-risk-ai-systems/",
            "tags": ["Regulation", "EU", "High-Risk"]
        },
        {
            "name": "EU薪酬透明度指令",
            "name_en": "EU Pay Transparency Directive",
            "type": "url",
            "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023L0970",
            "tags": ["Regulation", "EU", "Pay Equity"]
        },
    ],

    # ===== 合规：选拔/测评/面试 =====
    "合规：选拔/测评/面试": [
        {
            "name": "NYC AEDT偏见审计法规",
            "name_en": "NYC AEDT Bias Audit Regulation",
            "type": "url",
            "url": "https://rules.cityofnewyork.us/rule/automated-employment-decision-tools/",
            "tags": ["Compliance", "NYC", "Bias Audit"]
        },
        {
            "name": "加州CCPA自动化决策规则",
            "name_en": "California CCPA ADMT Regulations",
            "type": "url",
            "url": "https://cppa.ca.gov/regulations/",
            "tags": ["Compliance", "California", "Privacy"]
        },
    ],

    # ===== AI 面试助手 =====
    "AI 面试助手": [
        {
            "name": "Truffle AI面试分析",
            "name_en": "Truffle AI Interview Analytics",
            "type": "url",
            "url": "https://www.hiretruffle.com/",
            "tags": ["AI", "Interview", "Analytics"]
        },
        {
            "name": "Honeit面试智能平台",
            "name_en": "Honeit Interview Intelligence Platform",
            "type": "url",
            "url": "https://www.honeit.com/",
            "tags": ["AI", "Interview", "Recording"]
        },
    ],

    # ===== 远程面试与虚拟招聘 =====
    "远程面试与虚拟招聘": [
        {
            "name": "Veritone虚拟招聘会",
            "name_en": "Veritone Virtual Career Fair",
            "type": "url",
            "url": "https://veritone.com/solutions/human-resources/",
            "tags": ["Virtual", "Career Fair", "AI"]
        },
    ],

    # ===== 职位发布与招聘营销 =====
    "职位发布与招聘营销": [
        {
            "name": "Wonderkind（程序化招聘广告）",
            "name_en": "Wonderkind (Programmatic Job Ads)",
            "type": "url",
            "url": "https://www.wonderkind.com/",
            "tags": ["Marketing", "Programmatic", "Ads"]
        },
        {
            "name": "TalentLyft（招聘营销套件）",
            "name_en": "TalentLyft (Recruitment Marketing Suite)",
            "type": "url",
            "url": "https://www.talentlyft.com/",
            "tags": ["Marketing", "ATS", "Career Site"]
        },
    ],

    # ===== 适配工具 =====
    "适配工具": [
        {
            "name": "Plum（人才适配评估）",
            "name_en": "Plum (Talent Fit Assessment)",
            "type": "url",
            "url": "https://www.plum.io/",
            "tags": ["Fit", "Assessment", "Behavioral"]
        },
        {
            "name": "Traitify（视觉性格评估）",
            "name_en": "Traitify (Visual Personality Assessment)",
            "type": "url",
            "url": "https://www.traitify.com/",
            "tags": ["Fit", "Personality", "Fast"]
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
