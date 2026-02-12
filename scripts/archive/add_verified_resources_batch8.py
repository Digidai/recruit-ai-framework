#!/usr/bin/env python3
"""
Batch 8: Add verified resources to tarf.json
Cross-validated resources covering weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== ATS 与招聘协作 =====
    "ATS 与招聘协作": [
        {
            "name": "Teamtailor（协作式ATS）",
            "name_en": "Teamtailor (Collaborative ATS)",
            "type": "url",
            "url": "https://www.teamtailor.com/",
            "tags": ["ATS", "Collaboration", "EB"]
        },
        {
            "name": "Recruitee（协作招聘平台）",
            "name_en": "Recruitee (Collaborative Recruiting)",
            "type": "url",
            "url": "https://recruitee.com/",
            "tags": ["ATS", "Collaboration", "SMB"]
        },
        {
            "name": "Workable（招聘软件）",
            "name_en": "Workable (Recruiting Software)",
            "type": "url",
            "url": "https://www.workable.com/",
            "tags": ["ATS", "AI", "SMB"]
        },
    ],

    # ===== Offer、背调与入职 =====
    "Offer、背调与入职": [
        {
            "name": "PandaDoc HR（HR文档自动化）",
            "name_en": "PandaDoc HR (HR Document Automation)",
            "type": "url",
            "url": "https://www.pandadoc.com/teams/hr/",
            "tags": ["Offer", "eSignature", "Automation"]
        },
        {
            "name": "DocuSign HR（HR电子签名）",
            "name_en": "DocuSign HR (HR eSignature)",
            "type": "url",
            "url": "https://www.docusign.com/solutions/industries/hr",
            "tags": ["Offer", "eSignature", "Enterprise"]
        },
        {
            "name": "Dropbox Sign（简易电子签名）",
            "name_en": "Dropbox Sign (Simple eSignature)",
            "type": "url",
            "url": "https://sign.dropbox.com/",
            "tags": ["Offer", "eSignature"]
        },
    ],

    # ===== 绩效与目标 =====
    "绩效与目标": [
        {
            "name": "Lattice（绩效与OKR）",
            "name_en": "Lattice (Performance & OKR)",
            "type": "url",
            "url": "https://lattice.com/",
            "tags": ["Performance", "OKR", "Enterprise"]
        },
        {
            "name": "15Five（持续反馈）",
            "name_en": "15Five (Continuous Feedback)",
            "type": "url",
            "url": "https://www.15five.com/",
            "tags": ["Performance", "Feedback", "SMB"]
        },
        {
            "name": "Culture Amp（员工体验）",
            "name_en": "Culture Amp (Employee Experience)",
            "type": "url",
            "url": "https://www.cultureamp.com/",
            "tags": ["Engagement", "Performance", "Survey"]
        },
        {
            "name": "Leapsome（人员赋能）",
            "name_en": "Leapsome (People Enablement)",
            "type": "url",
            "url": "https://www.leapsome.com/",
            "tags": ["Performance", "OKR", "Learning"]
        },
    ],

    # ===== 职位发布与招聘营销 =====
    "职位发布与招聘营销": [
        {
            "name": "Appcast（程序化招聘广告）",
            "name_en": "Appcast (Programmatic Job Advertising)",
            "type": "url",
            "url": "https://www.appcast.io/",
            "tags": ["Advertising", "Programmatic"]
        },
        {
            "name": "Joveo（AI招聘营销）",
            "name_en": "Joveo (AI Recruitment Marketing)",
            "type": "url",
            "url": "https://www.joveo.com/",
            "tags": ["Advertising", "AI", "Programmatic"]
        },
        {
            "name": "PandoLogic（智能招聘广告）",
            "name_en": "PandoLogic (Intelligent Job Advertising)",
            "type": "url",
            "url": "https://www.pandologic.com/",
            "tags": ["Advertising", "AI"]
        },
        {
            "name": "Recruitics（招聘分析与营销）",
            "name_en": "Recruitics (Recruitment Analytics & Marketing)",
            "type": "url",
            "url": "https://www.recruitics.com/",
            "tags": ["Analytics", "Marketing"]
        },
    ],

    # ===== 退伍军人招聘认证 =====
    "退伍军人招聘认证": [
        {
            "name": "Orion Talent（军人人才招聘）",
            "name_en": "Orion Talent (Military Recruiting)",
            "type": "url",
            "url": "https://www.oriontalent.com/",
            "tags": ["Veteran", "RPO"]
        },
        {
            "name": "RecruitMilitary（退伍军人招聘）",
            "name_en": "RecruitMilitary (Veteran Recruiting)",
            "type": "url",
            "url": "https://recruitmilitary.com/",
            "tags": ["Veteran", "Job Fair"]
        },
        {
            "name": "Hiring Our Heroes（雇用英雄）",
            "name_en": "Hiring Our Heroes (US Chamber)",
            "type": "url",
            "url": "https://www.hiringourheroes.org/",
            "tags": ["Veteran", "Fellowship"]
        },
        {
            "name": "Hire Heroes USA（英雄招聘）",
            "name_en": "Hire Heroes USA",
            "type": "url",
            "url": "https://www.hireheroesusa.org/",
            "tags": ["Veteran", "Nonprofit"]
        },
        {
            "name": "HIRE Vets Medallion（退伍军人勋章计划）",
            "name_en": "HIRE Vets Medallion Program",
            "type": "url",
            "url": "https://www.hirevets.gov/",
            "tags": ["Veteran", "Government"]
        },
    ],

    # ===== 竞争对手分析 =====
    "竞争对手分析": [
        {
            "name": "TalentNeuron（人才市场情报）",
            "name_en": "TalentNeuron (Talent Market Intelligence)",
            "type": "url",
            "url": "https://www.talentneuron.com/",
            "tags": ["Intelligence", "Analytics", "Enterprise"]
        },
        {
            "name": "LinkedIn Talent Insights（领英人才洞察）",
            "name_en": "LinkedIn Talent Insights",
            "type": "url",
            "url": "https://business.linkedin.com/talent-solutions/talent-insights",
            "tags": ["Intelligence", "LinkedIn"]
        },
        {
            "name": "Lightcast（劳动力市场数据）",
            "name_en": "Lightcast (Labor Market Data)",
            "type": "url",
            "url": "https://lightcast.io/",
            "tags": ["Intelligence", "Labor Market"]
        },
        {
            "name": "Revelio Labs（人才数据）",
            "name_en": "Revelio Labs (Workforce Data)",
            "type": "url",
            "url": "https://www.reveliolabs.com/",
            "tags": ["Intelligence", "Analytics"]
        },
    ],

    # ===== 批量招聘工具 =====
    "批量招聘工具": [
        {
            "name": "TalentReef（小时工招聘）",
            "name_en": "TalentReef (Hourly Hiring)",
            "type": "url",
            "url": "https://www.talentreef.com/",
            "tags": ["High-Volume", "Hourly"]
        },
        {
            "name": "Humanly.io（AI招聘平台）",
            "name_en": "Humanly.io (AI Recruiting Platform)",
            "type": "url",
            "url": "https://humanly.io/",
            "tags": ["High-Volume", "AI", "Chatbot"]
        },
    ],

    # ===== 人才盘点与继任计划 =====
    "人才盘点与继任计划": [
        {
            "name": "Peoplebox（绩效与继任）",
            "name_en": "Peoplebox (Performance & Succession)",
            "type": "url",
            "url": "https://www.peoplebox.ai/",
            "tags": ["Succession", "OKR", "9-Box"]
        },
        {
            "name": "Quantum Workplace（人才评估）",
            "name_en": "Quantum Workplace (Talent Review)",
            "type": "url",
            "url": "https://www.quantumworkplace.com/",
            "tags": ["Succession", "Engagement"]
        },
        {
            "name": "365Talents（技能管理）",
            "name_en": "365Talents (Skills Management)",
            "type": "url",
            "url": "https://365talents.com/",
            "tags": ["Skills", "AI", "Mobility"]
        },
    ],

    # ===== 招聘运营 (RecOps) =====
    "招聘运营 (RecOps)": [
        {
            "name": "Findem（人才数据平台）",
            "name_en": "Findem (Talent Data Platform)",
            "type": "url",
            "url": "https://www.findem.ai/",
            "tags": ["RecOps", "AI", "Analytics"]
        },
        {
            "name": "Hireology（分布式招聘）",
            "name_en": "Hireology (Decentralized Hiring)",
            "type": "url",
            "url": "https://www.hireology.com/",
            "tags": ["RecOps", "Franchise"]
        },
    ],

    # ===== 招聘反欺诈与验证 =====
    "招聘反欺诈与验证": [
        {
            "name": "First Advantage（背景筛查）",
            "name_en": "First Advantage (Background Screening)",
            "type": "url",
            "url": "https://fadv.com/",
            "tags": ["Background Check", "Global"]
        },
        {
            "name": "Truework（收入验证）",
            "name_en": "Truework (Income Verification)",
            "type": "url",
            "url": "https://www.truework.com/",
            "tags": ["Verification", "Employment"]
        },
    ],

    # ===== 候选人关系管理 =====
    "候选人关系管理": [
        {
            "name": "Bullhorn CRM（招聘CRM）",
            "name_en": "Bullhorn CRM (Recruiting CRM)",
            "type": "url",
            "url": "https://www.bullhorn.com/",
            "tags": ["CRM", "Staffing"]
        },
        {
            "name": "Radancy（人才获取云）",
            "name_en": "Radancy (Talent Acquisition Cloud)",
            "type": "url",
            "url": "https://www.radancy.com/",
            "tags": ["CRM", "Marketing", "Enterprise"]
        },
    ],

    # ===== 招聘视觉与品牌设计 =====
    "招聘视觉与品牌设计": [
        {
            "name": "Papirfly（雇主品牌管理）",
            "name_en": "Papirfly (Employer Brand Management)",
            "type": "url",
            "url": "https://www.papirfly.com/",
            "tags": ["EB", "Design", "Templates"]
        },
        {
            "name": "Brandfolder（数字资产管理）",
            "name_en": "Brandfolder (Digital Asset Management)",
            "type": "url",
            "url": "https://brandfolder.com/",
            "tags": ["DAM", "Brand"]
        },
    ],

    # ===== 校园招聘与实习 =====
    "校园招聘与实习": [
        {
            "name": "Symplicity（大学职业服务）",
            "name_en": "Symplicity (University Career Services)",
            "type": "url",
            "url": "https://www.symplicity.com/",
            "tags": ["Campus", "Career Center"]
        },
        {
            "name": "Parker Dewey（微实习）",
            "name_en": "Parker Dewey (Micro-Internships)",
            "type": "url",
            "url": "https://www.parkerdewey.com/",
            "tags": ["Campus", "Internship"]
        },
    ],

    # ===== 招聘营销平台 =====
    "招聘营销平台": [
        {
            "name": "Phenom TXM（人才体验管理）",
            "name_en": "Phenom TXM (Talent Experience Management)",
            "type": "url",
            "url": "https://www.phenom.com/",
            "tags": ["TXM", "AI", "Enterprise"]
        },
        {
            "name": "Smashfly（招聘营销平台）",
            "name_en": "Smashfly (Recruitment Marketing)",
            "type": "url",
            "url": "https://www.symphonytalent.com/",
            "tags": ["Marketing", "CRM"]
        },
    ],

    # ===== AI 面试助手 =====
    "AI 面试助手": [
        {
            "name": "Metaview（AI面试笔记）",
            "name_en": "Metaview (AI Interview Notes)",
            "type": "url",
            "url": "https://www.metaview.ai/",
            "tags": ["AI", "Notes", "Interview"]
        },
        {
            "name": "BrightHire（面试智能）",
            "name_en": "BrightHire (Interview Intelligence)",
            "type": "url",
            "url": "https://brighthire.com/",
            "tags": ["AI", "Recording", "Interview"]
        },
        {
            "name": "Pillar（面试记录分析）",
            "name_en": "Pillar (Interview Recording Analytics)",
            "type": "url",
            "url": "https://www.pillar.hr/",
            "tags": ["AI", "Analytics", "Interview"]
        },
    ],

    # ===== 专业招聘机构 =====
    "专业招聘机构": [
        {
            "name": "Korn Ferry（高管搜索）",
            "name_en": "Korn Ferry (Executive Search)",
            "type": "url",
            "url": "https://www.kornferry.com/",
            "tags": ["Executive", "Consulting"]
        },
        {
            "name": "Heidrick & Struggles（高管猎头）",
            "name_en": "Heidrick & Struggles (Executive Search)",
            "type": "url",
            "url": "https://www.heidrick.com/",
            "tags": ["Executive", "Leadership"]
        },
        {
            "name": "Spencer Stuart（高管搜索）",
            "name_en": "Spencer Stuart (Executive Search)",
            "type": "url",
            "url": "https://www.spencerstuart.com/",
            "tags": ["Executive", "Board"]
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
