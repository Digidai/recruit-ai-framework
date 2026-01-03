#!/usr/bin/env python3
"""
Batch 17: Add verified resources to tarf.json
Cross-validated resources covering weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== 美国数据隐私法 =====
    "美国数据隐私法": [
        {
            "name": "CCPA雇主合规指南（加州隐私法）",
            "name_en": "CCPA Employer Compliance Guide",
            "type": "url",
            "url": "https://oag.ca.gov/privacy/ccpa",
            "tags": ["Privacy", "CCPA", "California"]
        },
        {
            "name": "SmartRecruiters CCPA合规（招聘隐私）",
            "name_en": "SmartRecruiters CCPA Compliance",
            "type": "url",
            "url": "https://www.smartrecruiters.com/resources/ccpa/",
            "tags": ["Privacy", "CCPA", "ATS"]
        },
    ],

    # ===== 隐私合规工具 =====
    "隐私合规工具": [
        {
            "name": "SecurePrivacy（隐私合规自动化）",
            "name_en": "SecurePrivacy (Privacy Compliance Automation)",
            "type": "url",
            "url": "https://secureprivacy.ai/",
            "tags": ["Privacy", "Automation", "GDPR"]
        },
        {
            "name": "Vault Verify（招聘数据安全）",
            "name_en": "Vault Verify (Recruiting Data Security)",
            "type": "url",
            "url": "https://www.vaultverify.com/",
            "tags": ["Privacy", "Verification", "Security"]
        },
    ],

    # ===== 招聘偏见检测 =====
    "招聘偏见检测": [
        {
            "name": "IBM AIF360（AI公平工具包）",
            "name_en": "IBM AIF360 (AI Fairness Toolkit)",
            "type": "url",
            "url": "https://aif360.mybluemix.net/",
            "tags": ["Bias", "AI", "Open Source"]
        },
        {
            "name": "Google What-If Tool（模型公平分析）",
            "name_en": "Google What-If Tool (Model Fairness)",
            "type": "url",
            "url": "https://pair-code.github.io/what-if-tool/",
            "tags": ["Bias", "Google", "Visualization"]
        },
        {
            "name": "Microsoft Fairlearn（公平性评估）",
            "name_en": "Microsoft Fairlearn (Fairness Assessment)",
            "type": "url",
            "url": "https://fairlearn.org/",
            "tags": ["Bias", "Microsoft", "Open Source"]
        },
        {
            "name": "Fiddler AI（ML监控平台）",
            "name_en": "Fiddler AI (ML Monitoring Platform)",
            "type": "url",
            "url": "https://www.fiddler.ai/",
            "tags": ["Bias", "Monitoring", "Enterprise"]
        },
    ],

    # ===== AI 招聘伦理 =====
    "AI 招聘伦理": [
        {
            "name": "Mitratech AI伦理指南（招聘AI伦理）",
            "name_en": "Mitratech AI Ethics Guide",
            "type": "url",
            "url": "https://mitratech.com/",
            "tags": ["Ethics", "AI", "Compliance"]
        },
        {
            "name": "Index.dev公平招聘指南（偏见检测）",
            "name_en": "Index.dev Fair Hiring Guide",
            "type": "url",
            "url": "https://www.index.dev/blog/ai-platforms-fair-impartial-hiring",
            "tags": ["Ethics", "Fairness", "Guide"]
        },
    ],

    # ===== 简历欺诈检测 =====
    "简历欺诈检测": [
        {
            "name": "Crosschq（人才智能验证）",
            "name_en": "Crosschq (Talent Intelligence Verification)",
            "type": "url",
            "url": "https://www.crosschq.com/",
            "tags": ["Fraud", "Verification", "Reference"]
        },
        {
            "name": "Sterling背调（综合背景调查）",
            "name_en": "Sterling Background Check",
            "type": "url",
            "url": "https://www.sterlingcheck.com/",
            "tags": ["Fraud", "Background Check", "Enterprise"]
        },
        {
            "name": "Cisive（就业验证）",
            "name_en": "Cisive (Employment Verification)",
            "type": "url",
            "url": "https://www.cisive.com/",
            "tags": ["Fraud", "Verification", "Compliance"]
        },
    ],

    # ===== 招聘反欺诈与验证 =====
    "招聘反欺诈与验证": [
        {
            "name": "Equifax工作验证（就业数据）",
            "name_en": "Equifax Workforce Solutions",
            "type": "url",
            "url": "https://workforce.equifax.com/",
            "tags": ["Verification", "Employment", "Data"]
        },
        {
            "name": "Sumsub就业验证（身份验证）",
            "name_en": "Sumsub Employment Verification",
            "type": "url",
            "url": "https://sumsub.com/",
            "tags": ["Verification", "Identity", "Global"]
        },
    ],

    # ===== 军转民技能翻译 =====
    "军转民技能翻译": [
        {
            "name": "Military.com技能翻译器（军转民）",
            "name_en": "Military.com Skills Translator",
            "type": "url",
            "url": "https://www.military.com/veteran-jobs/skills-translator/",
            "tags": ["Veteran", "Skills", "Translator"]
        },
        {
            "name": "O*NET军事技能交叉（职业匹配）",
            "name_en": "O*NET Military Skills Crosswalk",
            "type": "url",
            "url": "https://www.onetonline.org/crosswalk/",
            "tags": ["Veteran", "O*NET", "Crosswalk"]
        },
        {
            "name": "My Next Move退伍军人版（职业探索）",
            "name_en": "My Next Move for Veterans",
            "type": "url",
            "url": "https://www.mynextmove.org/vets/",
            "tags": ["Veteran", "Career", "DOL"]
        },
        {
            "name": "VA for Vets职业中心（退伍军人服务）",
            "name_en": "VA for Vets Career Center",
            "type": "url",
            "url": "https://www.vaforvets.va.gov/",
            "tags": ["Veteran", "VA", "Career"]
        },
    ],

    # ===== 招聘道德规范 =====
    "招聘道德规范": [
        {
            "name": "SHRM招聘伦理准则（行业标准）",
            "name_en": "SHRM Recruiting Ethics Guidelines",
            "type": "url",
            "url": "https://www.shrm.org/topics-tools/topics/ethics",
            "tags": ["Ethics", "SHRM", "Standards"]
        },
        {
            "name": "ASA道德规范（人才机构）",
            "name_en": "ASA Code of Ethics (Staffing)",
            "type": "url",
            "url": "https://americanstaffing.net/",
            "tags": ["Ethics", "Staffing", "Association"]
        },
    ],

    # ===== 欧盟/国际法规 =====
    "欧盟/国际法规": [
        {
            "name": "EU AI Act招聘指南（高风险AI）",
            "name_en": "EU AI Act Recruiting Guide",
            "type": "url",
            "url": "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai",
            "tags": ["Regulation", "EU", "AI"]
        },
        {
            "name": "Littler全球劳动法（国际合规）",
            "name_en": "Littler Global Labor Law",
            "type": "url",
            "url": "https://www.littler.com/",
            "tags": ["Regulation", "Global", "Labor"]
        },
    ],

    # ===== 中国劳动法 =====
    "中国劳动法": [
        {
            "name": "中国劳动法全文（官方法规）",
            "name_en": "China Labor Law Full Text",
            "type": "url",
            "url": "http://www.npc.gov.cn/npc/c2191/c2201/c19845/",
            "tags": ["China", "Labor Law", "Official"]
        },
        {
            "name": "NNRoad中国招聘指南（实操指南）",
            "name_en": "NNRoad China Hiring Guide",
            "type": "url",
            "url": "https://nnroad.com/blog/hire-workers-in-china/",
            "tags": ["China", "Hiring", "Guide"]
        },
    ],

    # ===== 合规：选拔/测评/面试 =====
    "合规：选拔/测评/面试": [
        {
            "name": "EEOC选拔程序指南（测评合规）",
            "name_en": "EEOC Selection Procedures Guide",
            "type": "url",
            "url": "https://www.eeoc.gov/laws/guidance/employment-tests-and-selection-procedures",
            "tags": ["Compliance", "EEOC", "Testing"]
        },
        {
            "name": "SIOP测评指南（工业心理学）",
            "name_en": "SIOP Assessment Guidelines",
            "type": "url",
            "url": "https://www.siop.org/",
            "tags": ["Compliance", "Psychology", "Standards"]
        },
    ],

    # ===== AI 面试助手 =====
    "AI 面试助手": [
        {
            "name": "BrightHire（面试智能平台）",
            "name_en": "BrightHire (Interview Intelligence)",
            "type": "url",
            "url": "https://brighthire.com/",
            "tags": ["AI", "Interview", "Recording"]
        },
        {
            "name": "Metaview（AI面试笔记）",
            "name_en": "Metaview (AI Interview Notes)",
            "type": "url",
            "url": "https://www.metaview.ai/",
            "tags": ["AI", "Interview", "Notes"]
        },
    ],

    # ===== 视频面试平台 =====
    "视频面试平台": [
        {
            "name": "Zoom招聘面试（视频会议）",
            "name_en": "Zoom for Recruiting",
            "type": "url",
            "url": "https://explore.zoom.us/en/products/meetings/",
            "tags": ["Video", "Meeting", "Enterprise"]
        },
        {
            "name": "Microsoft Teams面试（协作招聘）",
            "name_en": "Microsoft Teams for Interviews",
            "type": "url",
            "url": "https://www.microsoft.com/en-us/microsoft-teams/group-chat-software",
            "tags": ["Video", "Collaboration", "Enterprise"]
        },
    ],

    # ===== 心理测评 AI =====
    "心理测评 AI": [
        {
            "name": "AssessFirst（预测招聘）",
            "name_en": "AssessFirst (Predictive Recruiting)",
            "type": "url",
            "url": "https://www.assessfirst.com/",
            "tags": ["Psychometric", "AI", "Predictive"]
        },
        {
            "name": "Aon Assessment（全球评估）",
            "name_en": "Aon Assessment Solutions",
            "type": "url",
            "url": "https://assessment.aon.com/",
            "tags": ["Psychometric", "Enterprise", "Global"]
        },
    ],

    # ===== 适配工具 =====
    "适配工具": [
        {
            "name": "Culture Amp（文化适配）",
            "name_en": "Culture Amp (Culture Fit)",
            "type": "url",
            "url": "https://www.cultureamp.com/",
            "tags": ["Culture", "Fit", "Analytics"]
        },
        {
            "name": "The Predictive Index（行为评估）",
            "name_en": "The Predictive Index (Behavioral)",
            "type": "url",
            "url": "https://www.predictiveindex.com/",
            "tags": ["Fit", "Behavioral", "Assessment"]
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
