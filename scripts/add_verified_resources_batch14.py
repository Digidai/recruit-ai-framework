#!/usr/bin/env python3
"""
Batch 14: Add verified resources to tarf.json
Cross-validated resources covering weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== 校园招聘与实习 =====
    "校园招聘与实习": [
        {
            "name": "College Recruiter（校园招聘平台）",
            "name_en": "College Recruiter (Campus Job Board)",
            "type": "url",
            "url": "https://www.collegerecruiter.com/",
            "tags": ["Campus", "Internship", "Entry-Level"]
        },
        {
            "name": "WayUp（多元化早期人才）",
            "name_en": "WayUp (Diverse Early Talent)",
            "type": "url",
            "url": "https://www.wayup.com/",
            "tags": ["Campus", "DEI", "Internship"]
        },
        {
            "name": "NACE资源中心（校园招聘研究）",
            "name_en": "NACE Resource Center",
            "type": "url",
            "url": "https://www.naceweb.org/",
            "tags": ["Campus", "Research", "Standards"]
        },
    ],

    # ===== 实习管理平台 =====
    "实习管理平台": [
        {
            "name": "iCIMS校园解决方案（校园ATS）",
            "name_en": "iCIMS Campus Solutions",
            "type": "url",
            "url": "https://www.icims.com/products/industry/college-campus-recruiting-software/",
            "tags": ["Campus", "ATS", "Enterprise"]
        },
        {
            "name": "Joveo校园招聘指南（校招策略）",
            "name_en": "Joveo Campus Recruiting Guide",
            "type": "url",
            "url": "https://www.joveo.com/campus-recruiting-ultimate-guide/",
            "tags": ["Campus", "Guide", "Strategy"]
        },
    ],

    # ===== 多元化招聘平台 (DEI) =====
    "多元化招聘平台 (DEI)": [
        {
            "name": "Diversity.com（多元化招聘网）",
            "name_en": "Diversity.com (Diversity Job Board)",
            "type": "url",
            "url": "https://diversity.com/",
            "tags": ["DEI", "Job Board", "Inclusive"]
        },
        {
            "name": "Kanarys（DEI数据分析）",
            "name_en": "Kanarys (DEI Data Analytics)",
            "type": "url",
            "url": "https://www.kanarys.com/",
            "tags": ["DEI", "Analytics", "Assessment"]
        },
        {
            "name": "Textio（包容性写作）",
            "name_en": "Textio (Inclusive Writing)",
            "type": "url",
            "url": "https://textio.com/",
            "tags": ["DEI", "Writing", "AI"]
        },
        {
            "name": "Fairygodboss（女性职业平台）",
            "name_en": "Fairygodboss (Women's Career Platform)",
            "type": "url",
            "url": "https://fairygodboss.com/",
            "tags": ["DEI", "Women", "Reviews"]
        },
        {
            "name": "Valence（黑人人才平台）",
            "name_en": "Valence (Black Talent Platform)",
            "type": "url",
            "url": "https://valence.community/",
            "tags": ["DEI", "Black Talent", "Community"]
        },
    ],

    # ===== 招聘数据隐私与合规 =====
    "招聘数据隐私与合规": [
        {
            "name": "EEOC招聘指南（平等就业）",
            "name_en": "EEOC Employer Guidance",
            "type": "url",
            "url": "https://www.eeoc.gov/employers",
            "tags": ["Compliance", "EEOC", "US"]
        },
        {
            "name": "GDPR招聘合规指南（欧盟合规）",
            "name_en": "GDPR Recruiting Compliance Guide",
            "type": "url",
            "url": "https://gdpr.eu/what-is-gdpr/",
            "tags": ["Compliance", "GDPR", "EU"]
        },
    ],

    # ===== 合规参考（背调）=====
    "合规参考（背调）": [
        {
            "name": "FCRA合规指南（背调法规）",
            "name_en": "FCRA Compliance Guide",
            "type": "url",
            "url": "https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act",
            "tags": ["Compliance", "FCRA", "Background Check"]
        },
        {
            "name": "Private Eyes背调指南（2025背调）",
            "name_en": "Private Eyes Background Check Guide",
            "type": "url",
            "url": "https://www.privateeyesbackgroundchecks.com/",
            "tags": ["Background Check", "Guide", "Compliance"]
        },
    ],

    # ===== 医疗/护理 =====
    "医疗/护理": [
        {
            "name": "iCIMS医疗招聘（医疗ATS）",
            "name_en": "iCIMS Healthcare Recruiting",
            "type": "url",
            "url": "https://www.icims.com/products/industry/hospital-healthcare-recruiting-software/",
            "tags": ["Healthcare", "ATS", "Hospital"]
        },
        {
            "name": "Cejka Search（医疗高管猎头）",
            "name_en": "Cejka Search (Healthcare Executive Search)",
            "type": "url",
            "url": "https://www.cejkasearch.com/",
            "tags": ["Healthcare", "Executive", "Search"]
        },
        {
            "name": "HCRI（医疗招聘国际）",
            "name_en": "HealthCare Recruiters International",
            "type": "url",
            "url": "https://www.hcrnetwork.com/",
            "tags": ["Healthcare", "Global", "Recruiting"]
        },
    ],

    # ===== 金融/法律 =====
    "金融/法律": [
        {
            "name": "Robert Half Legal（法律招聘）",
            "name_en": "Robert Half Legal Recruiting",
            "type": "url",
            "url": "https://www.roberthalf.com/us/en/legal",
            "tags": ["Legal", "Staffing", "Professional"]
        },
        {
            "name": "Major Lindsey Africa（法律猎头）",
            "name_en": "Major Lindsey Africa (Legal Search)",
            "type": "url",
            "url": "https://www.mlaglobal.com/",
            "tags": ["Legal", "Executive", "Search"]
        },
    ],

    # ===== Board / C-Suite 招聘 =====
    "Board / C-Suite 招聘": [
        {
            "name": "Spencer Stuart（高管猎头）",
            "name_en": "Spencer Stuart (Executive Search)",
            "type": "url",
            "url": "https://www.spencerstuart.com/",
            "tags": ["Executive", "Board", "C-Suite"]
        },
        {
            "name": "Heidrick & Struggles（高管搜索）",
            "name_en": "Heidrick & Struggles (Executive Search)",
            "type": "url",
            "url": "https://www.heidrick.com/",
            "tags": ["Executive", "Board", "Leadership"]
        },
    ],

    # ===== 政府/公共部门 =====
    "政府/公共部门": [
        {
            "name": "USAJOBS（美国政府招聘）",
            "name_en": "USAJOBS (US Government Jobs)",
            "type": "url",
            "url": "https://www.usajobs.gov/",
            "tags": ["Government", "US", "Public Sector"]
        },
        {
            "name": "GovLoop（政府人才社区）",
            "name_en": "GovLoop (Government Talent Community)",
            "type": "url",
            "url": "https://www.govloop.com/",
            "tags": ["Government", "Community", "Career"]
        },
    ],

    # ===== 创意/媒体 =====
    "创意/媒体": [
        {
            "name": "Dribbble Jobs（设计师招聘）",
            "name_en": "Dribbble Jobs (Designer Hiring)",
            "type": "url",
            "url": "https://dribbble.com/jobs",
            "tags": ["Creative", "Design", "Job Board"]
        },
        {
            "name": "Behance Jobs（创意人才）",
            "name_en": "Behance Jobs (Creative Talent)",
            "type": "url",
            "url": "https://www.behance.net/joblist",
            "tags": ["Creative", "Portfolio", "Adobe"]
        },
    ],

    # ===== 设计/产品 =====
    "设计/产品": [
        {
            "name": "Designlab招聘（UX/UI人才）",
            "name_en": "Designlab Hiring (UX/UI Talent)",
            "type": "url",
            "url": "https://designlab.com/",
            "tags": ["Design", "UX", "Learning"]
        },
        {
            "name": "UX Jobs Board（用户体验招聘）",
            "name_en": "UX Jobs Board",
            "type": "url",
            "url": "https://www.uxjobsboard.com/",
            "tags": ["Design", "UX", "Niche"]
        },
    ],

    # ===== 薪酬公平工具 =====
    "薪酬公平工具": [
        {
            "name": "Syndio（薪酬公平分析）",
            "name_en": "Syndio (Pay Equity Analytics)",
            "type": "url",
            "url": "https://synd.io/",
            "tags": ["Pay Equity", "Analytics", "Compliance"]
        },
        {
            "name": "Trusaic PayParity（薪酬透明）",
            "name_en": "Trusaic PayParity",
            "type": "url",
            "url": "https://trusaic.com/",
            "tags": ["Pay Equity", "Transparency", "Compliance"]
        },
    ],

    # ===== 智能寻才/人才匹配 =====
    "智能寻才/人才匹配": [
        {
            "name": "Humanly（对话式筛选）",
            "name_en": "Humanly (Conversational Screening)",
            "type": "url",
            "url": "https://humanly.io/",
            "tags": ["AI", "Matching", "Chatbot"]
        },
        {
            "name": "Ideal（AI候选人匹配）",
            "name_en": "Ideal (AI Candidate Matching)",
            "type": "url",
            "url": "https://ideal.com/",
            "tags": ["AI", "Matching", "Screening"]
        },
    ],

    # ===== RPA（机器人流程自动化）=====
    "RPA（机器人流程自动化）": [
        {
            "name": "UiPath招聘自动化（RPA招聘）",
            "name_en": "UiPath Recruiting Automation",
            "type": "url",
            "url": "https://www.uipath.com/solutions/department/human-resources",
            "tags": ["RPA", "Automation", "HR"]
        },
        {
            "name": "Automation Anywhere HR（HR自动化）",
            "name_en": "Automation Anywhere HR Solutions",
            "type": "url",
            "url": "https://www.automationanywhere.com/solutions/human-resources",
            "tags": ["RPA", "Automation", "Enterprise"]
        },
    ],

    # ===== 负责任 AI 指南 =====
    "负责任 AI 指南": [
        {
            "name": "NIST AI风险管理框架（AI治理）",
            "name_en": "NIST AI Risk Management Framework",
            "type": "url",
            "url": "https://www.nist.gov/itl/ai-risk-management-framework",
            "tags": ["AI", "Governance", "Framework"]
        },
        {
            "name": "Partnership on AI（AI伦理）",
            "name_en": "Partnership on AI (AI Ethics)",
            "type": "url",
            "url": "https://partnershiponai.org/",
            "tags": ["AI", "Ethics", "Research"]
        },
    ],

    # ===== 欧盟 AI 法规 =====
    "欧盟 AI 法规": [
        {
            "name": "EU AI Act官方指南（欧盟AI法案）",
            "name_en": "EU AI Act Official Guide",
            "type": "url",
            "url": "https://artificialintelligenceact.eu/",
            "tags": ["AI", "Regulation", "EU"]
        },
        {
            "name": "AI Act招聘影响分析（HR合规）",
            "name_en": "AI Act HR Impact Analysis",
            "type": "url",
            "url": "https://www.shrm.org/topics-tools/news/technology/eu-ai-act-hr-needs-know",
            "tags": ["AI", "Regulation", "HR"]
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
