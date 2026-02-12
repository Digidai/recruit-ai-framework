#!/usr/bin/env python3
"""
Add more verified resources to tarf.json - Batch 2
Focus on categories with fewer resources.
"""

import json
import re

VERIFIED_RESOURCES_BATCH2 = {
    # A - 招聘流程与方法论 (15 resources, needs more)
    "招聘流程与方法论": [
        {
            "name": "SHRM｜Talent Acquisition Guide",
            "name_en": "SHRM | Talent Acquisition Guide",
            "type": "url",
            "url": "https://www.shrm.org/topics-tools/tools/toolkits/practicing-strategic-human-resources-talent-acquisition",
            "tags": ["Guide", "SHRM"]
        },
        {
            "name": "Talent Board｜Candidate Experience Research",
            "name_en": "Talent Board | Candidate Experience Research",
            "type": "url",
            "url": "https://www.thetalentboard.org/",
            "tags": ["Research", "CX"]
        },
        {
            "name": "ERE｜Recruiting Intelligence",
            "name_en": "ERE | Recruiting Intelligence",
            "type": "url",
            "url": "https://www.ere.net/",
            "tags": ["Media", "Research"]
        },
    ],

    # 招聘心理学与行为科学 (18 resources)
    "招聘心理学与行为科学": [
        {
            "name": "Daniel Kahneman｜Thinking Fast and Slow",
            "name_en": "Daniel Kahneman | Thinking Fast and Slow",
            "type": "url",
            "url": "https://www.goodreads.com/book/show/11468377-thinking-fast-and-slow",
            "tags": ["Book", "Psychology"]
        },
        {
            "name": "BehavioralEconomics.com｜Hiring Biases",
            "name_en": "BehavioralEconomics.com | Hiring Biases",
            "type": "url",
            "url": "https://www.behavioraleconomics.com/",
            "tags": ["Research", "Bias"]
        },
        {
            "name": "Nudge Theory｜Thaler & Sunstein",
            "name_en": "Nudge Theory | Thaler & Sunstein",
            "type": "url",
            "url": "https://www.goodreads.com/book/show/3450744-nudge",
            "tags": ["Book", "Theory"]
        },
    ],

    # B - 校园招聘与实习 (14 resources)
    "校园招聘与实习": [
        {
            "name": "WayUp（美国校招）",
            "name_en": "WayUp (US Campus Recruiting)",
            "type": "url",
            "url": "https://www.wayup.com/",
            "tags": ["Campus", "US"]
        },
        {
            "name": "RippleMatch（校园 AI 匹配）",
            "name_en": "RippleMatch (Campus AI Matching)",
            "type": "url",
            "url": "https://ripplematch.com/",
            "tags": ["Campus", "AI"]
        },
        {
            "name": "Parker Dewey（微实习）",
            "name_en": "Parker Dewey (Micro-Internships)",
            "type": "url",
            "url": "https://www.parkerdewey.com/",
            "tags": ["Internship", "Micro"]
        },
        {
            "name": "Forage（虚拟实习体验）",
            "name_en": "Forage (Virtual Work Experience)",
            "type": "url",
            "url": "https://www.theforage.com/",
            "tags": ["Virtual", "Experience"]
        },
        {
            "name": "Symplicity（校园招聘管理）",
            "name_en": "Symplicity (Campus Recruiting Management)",
            "type": "url",
            "url": "https://www.symplicity.com/",
            "tags": ["Campus", "Platform"]
        },
        {
            "name": "GradLeaders（研究生招聘）",
            "name_en": "GradLeaders (Graduate Recruiting)",
            "type": "url",
            "url": "https://gradleaders.com/",
            "tags": ["Graduate", "Platform"]
        },
    ],

    # B - 高管招聘 (14 resources)
    "高管招聘": [
        {
            "name": "Korn Ferry（全球高管搜寻）",
            "name_en": "Korn Ferry (Global Executive Search)",
            "type": "url",
            "url": "https://www.kornferry.com/",
            "tags": ["Executive", "Global"]
        },
        {
            "name": "Spencer Stuart",
            "name_en": "Spencer Stuart",
            "type": "url",
            "url": "https://www.spencerstuart.com/",
            "tags": ["Executive", "Board"]
        },
        {
            "name": "Russell Reynolds",
            "name_en": "Russell Reynolds",
            "type": "url",
            "url": "https://www.russellreynolds.com/",
            "tags": ["Executive", "Leadership"]
        },
        {
            "name": "Egon Zehnder",
            "name_en": "Egon Zehnder",
            "type": "url",
            "url": "https://www.egonzehnder.com/",
            "tags": ["Executive", "Global"]
        },
        {
            "name": "Heidrick & Struggles",
            "name_en": "Heidrick & Struggles",
            "type": "url",
            "url": "https://www.heidrick.com/",
            "tags": ["Executive", "Strategy"]
        },
        {
            "name": "Boyden（高管搜寻网络）",
            "name_en": "Boyden (Executive Search Network)",
            "type": "url",
            "url": "https://www.boyden.com/",
            "tags": ["Executive", "Network"]
        },
    ],

    # B - 搜索模板 (16 resources)
    "搜索模板（X-Ray/Boolean）": [
        {
            "name": "LinkedIn X-Ray Search Generator",
            "name_en": "LinkedIn X-Ray Search Generator",
            "type": "url",
            "url": "https://recruitin.net/",
            "tags": ["Tool", "Free"]
        },
        {
            "name": "Occupation Thesaurus（职位同义词）",
            "name_en": "Occupation Thesaurus (Job Synonyms)",
            "type": "url",
            "url": "https://www.onetonline.org/find/",
            "tags": ["Reference", "O*NET"]
        },
        {
            "name": "TechCrunch｜Company Database",
            "name_en": "TechCrunch | Company Database",
            "type": "url",
            "url": "https://techcrunch.com/startups/",
            "tags": ["Database", "Startups"]
        },
    ],

    # E - 薪酬透明度法规 (16 resources)
    "薪酬透明度法规": [
        {
            "name": "康涅狄格州｜Pay Transparency Law",
            "name_en": "Connecticut | Pay Transparency Law",
            "type": "url",
            "url": "https://portal.ct.gov/dolui",
            "tags": ["Law", "US", "CT"]
        },
        {
            "name": "内华达州｜SB 293 Wage Disclosure",
            "name_en": "Nevada | SB 293 Wage Disclosure",
            "type": "url",
            "url": "https://www.leg.state.nv.us/",
            "tags": ["Law", "US", "NV"]
        },
        {
            "name": "罗德岛州｜Pay Equity Act",
            "name_en": "Rhode Island | Pay Equity Act",
            "type": "url",
            "url": "https://dlt.ri.gov/",
            "tags": ["Law", "US", "RI"]
        },
        {
            "name": "Syndio（薪酬公平分析）",
            "name_en": "Syndio (Pay Equity Analytics)",
            "type": "url",
            "url": "https://synd.io/",
            "tags": ["Tool", "Analytics"]
        },
        {
            "name": "Trusaic（薪酬合规）",
            "name_en": "Trusaic (Pay Compliance)",
            "type": "url",
            "url": "https://trusaic.com/",
            "tags": ["Tool", "Compliance"]
        },
    ],

    # H - 员工推荐 (16 resources)
    "员工推荐": [
        {
            "name": "Radancy Employee Referrals",
            "name_en": "Radancy Employee Referrals",
            "type": "url",
            "url": "https://www.radancy.com/",
            "tags": ["Referral", "Enterprise"]
        },
        {
            "name": "Jobvite Refer",
            "name_en": "Jobvite Refer",
            "type": "url",
            "url": "https://www.jobvite.com/products/refer/",
            "tags": ["Referral", "ATS"]
        },
        {
            "name": "Firstbird（欧洲推荐平台）",
            "name_en": "Firstbird (European Referral Platform)",
            "type": "url",
            "url": "https://www.firstbird.com/",
            "tags": ["Referral", "EU"]
        },
        {
            "name": "EmployeeReferrals.com",
            "name_en": "EmployeeReferrals.com",
            "type": "url",
            "url": "https://www.employeereferrals.com/",
            "tags": ["Referral", "Platform"]
        },
    ],

    # F - 退伍军人招聘 (17 resources)
    "退伍军人招聘": [
        {
            "name": "RecruitMilitary",
            "name_en": "RecruitMilitary",
            "type": "url",
            "url": "https://recruitmilitary.com/",
            "tags": ["Veteran", "Events"]
        },
        {
            "name": "G.I. Jobs",
            "name_en": "G.I. Jobs",
            "type": "url",
            "url": "https://www.gijobs.com/",
            "tags": ["Veteran", "Media"]
        },
        {
            "name": "Corporate Gray（军转民）",
            "name_en": "Corporate Gray (Military Transition)",
            "type": "url",
            "url": "https://www.corporategray.com/",
            "tags": ["Veteran", "Transition"]
        },
        {
            "name": "Orion Talent（军人人才）",
            "name_en": "Orion Talent (Military Talent)",
            "type": "url",
            "url": "https://www.oriontalent.com/",
            "tags": ["Veteran", "Staffing"]
        },
    ],

    # I - 全球招聘与远程团队 (17 resources)
    "全球招聘与远程团队": [
        {
            "name": "Papaya Global（全球薪资）",
            "name_en": "Papaya Global (Global Payroll)",
            "type": "url",
            "url": "https://www.papayaglobal.com/",
            "tags": ["EOR", "Payroll"]
        },
        {
            "name": "Rippling（全球 HR）",
            "name_en": "Rippling (Global HR)",
            "type": "url",
            "url": "https://www.rippling.com/",
            "tags": ["HRIS", "Global"]
        },
        {
            "name": "Lano（欧洲 EOR）",
            "name_en": "Lano (European EOR)",
            "type": "url",
            "url": "https://www.lano.io/",
            "tags": ["EOR", "EU"]
        },
        {
            "name": "Atlas（全球 EOR）",
            "name_en": "Atlas (Global EOR)",
            "type": "url",
            "url": "https://www.atlashxm.com/",
            "tags": ["EOR", "Global"]
        },
        {
            "name": "Remofirst",
            "name_en": "Remofirst",
            "type": "url",
            "url": "https://www.remofirst.com/",
            "tags": ["EOR", "Startup"]
        },
    ],

    # I - RPO 招聘外包 (18 resources)
    "招聘流程外包 (RPO)": [
        {
            "name": "Cielo（全球 RPO）",
            "name_en": "Cielo (Global RPO)",
            "type": "url",
            "url": "https://www.cielotalent.com/",
            "tags": ["RPO", "Global"]
        },
        {
            "name": "Pontoon（Adecco RPO）",
            "name_en": "Pontoon (Adecco RPO)",
            "type": "url",
            "url": "https://www.integratedsolutions.io/",
            "tags": ["RPO", "Adecco"]
        },
        {
            "name": "PeopleScout",
            "name_en": "PeopleScout",
            "type": "url",
            "url": "https://www.peoplescout.com/",
            "tags": ["RPO", "MSP"]
        },
        {
            "name": "Sevenstep",
            "name_en": "Sevenstep",
            "type": "url",
            "url": "https://www.sevensteprpo.com/",
            "tags": ["RPO", "TA"]
        },
        {
            "name": "WilsonHCG",
            "name_en": "WilsonHCG",
            "type": "url",
            "url": "https://www.wilsonhcg.com/",
            "tags": ["RPO", "Enterprise"]
        },
    ],

    # E - 招聘反欺诈与验证 (19 resources)
    "招聘反欺诈与验证": [
        {
            "name": "Truework（收入验证）",
            "name_en": "Truework (Income Verification)",
            "type": "url",
            "url": "https://www.truework.com/",
            "tags": ["Verification", "Income"]
        },
        {
            "name": "Plaid（收入数据）",
            "name_en": "Plaid (Income Data)",
            "type": "url",
            "url": "https://plaid.com/products/income/",
            "tags": ["API", "Income"]
        },
        {
            "name": "Onfido（身份验证）",
            "name_en": "Onfido (Identity Verification)",
            "type": "url",
            "url": "https://onfido.com/",
            "tags": ["Identity", "AI"]
        },
        {
            "name": "Jumio（身份验证）",
            "name_en": "Jumio (Identity Verification)",
            "type": "url",
            "url": "https://www.jumio.com/",
            "tags": ["Identity", "AI"]
        },
        {
            "name": "Persona（身份平台）",
            "name_en": "Persona (Identity Platform)",
            "type": "url",
            "url": "https://withpersona.com/",
            "tags": ["Identity", "Platform"]
        },
    ],

    # J - 招聘文档与知识库 (18 resources)
    "招聘文档与知识库": [
        {
            "name": "Notion Templates｜HR",
            "name_en": "Notion Templates | HR",
            "type": "url",
            "url": "https://www.notion.so/templates/category/hr",
            "tags": ["Template", "Free"]
        },
        {
            "name": "Airtable Templates｜Recruiting",
            "name_en": "Airtable Templates | Recruiting",
            "type": "url",
            "url": "https://www.airtable.com/templates/human-resources",
            "tags": ["Template", "Free"]
        },
        {
            "name": "Monday.com｜HR Templates",
            "name_en": "Monday.com | HR Templates",
            "type": "url",
            "url": "https://monday.com/templates/hr",
            "tags": ["Template", "Workflow"]
        },
        {
            "name": "ClickUp｜Recruiting Templates",
            "name_en": "ClickUp | Recruiting Templates",
            "type": "url",
            "url": "https://clickup.com/templates/hr",
            "tags": ["Template", "PM"]
        },
        {
            "name": "Coda｜HR Docs",
            "name_en": "Coda | HR Docs",
            "type": "url",
            "url": "https://coda.io/gallery?filter=hr",
            "tags": ["Template", "Docs"]
        },
    ],

    # J - 招聘预算与 ROI (18 resources)
    "招聘预算与 ROI": [
        {
            "name": "Gem Analytics（招聘分析）",
            "name_en": "Gem Analytics (Recruiting Analytics)",
            "type": "url",
            "url": "https://www.gem.com/analytics",
            "tags": ["Analytics", "ROI"]
        },
        {
            "name": "Visier Benchmarks",
            "name_en": "Visier Benchmarks",
            "type": "url",
            "url": "https://www.visier.com/benchmarks/",
            "tags": ["Benchmark", "Analytics"]
        },
        {
            "name": "LinkedIn Cost-Per-Hire Calculator",
            "name_en": "LinkedIn Cost-Per-Hire Calculator",
            "type": "url",
            "url": "https://business.linkedin.com/talent-solutions/resources/talent-strategy/cost-per-hire-calculator",
            "tags": ["Calculator", "Free"]
        },
        {
            "name": "Greenhouse Recruiting Metrics",
            "name_en": "Greenhouse Recruiting Metrics",
            "type": "url",
            "url": "https://www.greenhouse.com/guidance/what-are-recruiting-metrics",
            "tags": ["Guide", "Metrics"]
        },
    ],

    # D - 开源公平性工具 (add more)
    "开源公平性工具": [
        {
            "name": "Alibi Detect（异常检测）",
            "name_en": "Alibi Detect (Anomaly Detection)",
            "type": "url",
            "url": "https://github.com/SeldonIO/alibi-detect",
            "tags": ["Open Source", "ML"]
        },
        {
            "name": "Themis ML（公平性）",
            "name_en": "Themis ML (Fairness)",
            "type": "url",
            "url": "https://github.com/cosmicBboy/themis-ml",
            "tags": ["Open Source", "Fairness"]
        },
        {
            "name": "AI Fairness 360 Documentation",
            "name_en": "AI Fairness 360 Documentation",
            "type": "url",
            "url": "https://aif360.readthedocs.io/",
            "tags": ["Docs", "IBM"]
        },
    ],

    # C - 招聘效率与生产力工具 (add more Chrome extensions)
    "招聘效率与生产力工具": [
        {
            "name": "Hunter.io（邮箱查找）",
            "name_en": "Hunter.io (Email Finder)",
            "type": "url",
            "url": "https://hunter.io/",
            "tags": ["Tool", "Email"]
        },
        {
            "name": "Lusha（联系方式）",
            "name_en": "Lusha (Contact Data)",
            "type": "url",
            "url": "https://www.lusha.com/",
            "tags": ["Tool", "Contact"]
        },
        {
            "name": "RocketReach（联系人搜索）",
            "name_en": "RocketReach (Contact Search)",
            "type": "url",
            "url": "https://rocketreach.co/",
            "tags": ["Tool", "Search"]
        },
        {
            "name": "Clearbit（数据丰富）",
            "name_en": "Clearbit (Data Enrichment)",
            "type": "url",
            "url": "https://clearbit.com/",
            "tags": ["Tool", "Enrichment"]
        },
        {
            "name": "ZoomInfo（B2B 数据）",
            "name_en": "ZoomInfo (B2B Data)",
            "type": "url",
            "url": "https://www.zoominfo.com/",
            "tags": ["Data", "Enterprise"]
        },
    ],

    # G - 远程面试与虚拟招聘
    "远程面试与虚拟招聘": [
        {
            "name": "Gather（虚拟办公空间）",
            "name_en": "Gather (Virtual Office Space)",
            "type": "url",
            "url": "https://www.gather.town/",
            "tags": ["Virtual", "Office"]
        },
        {
            "name": "Hopin（虚拟活动）",
            "name_en": "Hopin (Virtual Events)",
            "type": "url",
            "url": "https://hopin.com/",
            "tags": ["Virtual", "Events"]
        },
        {
            "name": "Brazen（虚拟招聘会）",
            "name_en": "Brazen (Virtual Career Fairs)",
            "type": "url",
            "url": "https://www.brazen.com/",
            "tags": ["Virtual", "Career Fair"]
        },
        {
            "name": "vFairs（虚拟招聘活动）",
            "name_en": "vFairs (Virtual Recruiting Events)",
            "type": "url",
            "url": "https://www.vfairs.com/",
            "tags": ["Virtual", "Events"]
        },
    ],

    # I - 技术招聘专项
    "技术招聘专项": [
        {
            "name": "Qualified.io（技术评估）",
            "name_en": "Qualified.io (Technical Assessment)",
            "type": "url",
            "url": "https://www.qualified.io/",
            "tags": ["Assessment", "Tech"]
        },
        {
            "name": "SkillValue（IT 技能测试）",
            "name_en": "SkillValue (IT Skills Testing)",
            "type": "url",
            "url": "https://www.skillvalue.com/",
            "tags": ["Assessment", "IT"]
        },
        {
            "name": "Codingame for Work",
            "name_en": "Codingame for Work",
            "type": "url",
            "url": "https://www.codingame.com/work/",
            "tags": ["Assessment", "Gaming"]
        },
        {
            "name": "Exercism（编程练习）",
            "name_en": "Exercism (Coding Practice)",
            "type": "url",
            "url": "https://exercism.org/",
            "tags": ["Practice", "Free"]
        },
    ],

    # I - 蓝领与一线员工招聘
    "蓝领与一线员工招聘": [
        {
            "name": "Hireology（零售/汽车招聘）",
            "name_en": "Hireology (Retail/Auto Hiring)",
            "type": "url",
            "url": "https://hireology.com/",
            "tags": ["Frontline", "Retail"]
        },
        {
            "name": "Fountain（高流量招聘）",
            "name_en": "Fountain (High-Volume Hiring)",
            "type": "url",
            "url": "https://www.fountain.com/",
            "tags": ["Frontline", "Volume"]
        },
        {
            "name": "Wonolo（按需用工）",
            "name_en": "Wonolo (On-Demand Staffing)",
            "type": "url",
            "url": "https://www.wonolo.com/",
            "tags": ["Gig", "Frontline"]
        },
        {
            "name": "Instawork（零工平台）",
            "name_en": "Instawork (Gig Platform)",
            "type": "url",
            "url": "https://www.instawork.com/",
            "tags": ["Gig", "Hospitality"]
        },
    ],

    # J - 招聘播客与媒体
    "招聘播客与媒体": [
        {
            "name": "The Chad & Cheese Podcast",
            "name_en": "The Chad & Cheese Podcast",
            "type": "url",
            "url": "https://www.chadcheese.com/",
            "tags": ["Podcast", "HR Tech"]
        },
        {
            "name": "HR Happy Hour",
            "name_en": "HR Happy Hour",
            "type": "url",
            "url": "https://www.hrhappyhour.net/",
            "tags": ["Podcast", "HR"]
        },
        {
            "name": "Talent Cast",
            "name_en": "Talent Cast",
            "type": "url",
            "url": "https://www.intoo.com/resources/podcasts/",
            "tags": ["Podcast", "Talent"]
        },
        {
            "name": "SHRM All Things Work",
            "name_en": "SHRM All Things Work",
            "type": "url",
            "url": "https://www.shrm.org/hr-today/trends-and-forecasting/podcasts/all-things-work/pages/default.aspx",
            "tags": ["Podcast", "SHRM"]
        },
    ],

    # G - 候选人关系管理
    "候选人关系管理": [
        {
            "name": "Avature CRM",
            "name_en": "Avature CRM",
            "type": "url",
            "url": "https://www.avature.net/",
            "tags": ["CRM", "Enterprise"]
        },
        {
            "name": "Bullhorn（猎头 CRM）",
            "name_en": "Bullhorn (Staffing CRM)",
            "type": "url",
            "url": "https://www.bullhorn.com/",
            "tags": ["CRM", "Staffing"]
        },
        {
            "name": "Vincere（猎头软件）",
            "name_en": "Vincere (Recruitment Software)",
            "type": "url",
            "url": "https://www.vincere.io/",
            "tags": ["CRM", "Agency"]
        },
    ],

    # D - 生成式 AI 招聘
    "生成式 AI (LLM) 招聘": [
        {
            "name": "Anthropic Claude API",
            "name_en": "Anthropic Claude API",
            "type": "url",
            "url": "https://www.anthropic.com/api",
            "tags": ["API", "LLM"]
        },
        {
            "name": "OpenAI API",
            "name_en": "OpenAI API",
            "type": "url",
            "url": "https://platform.openai.com/",
            "tags": ["API", "LLM"]
        },
        {
            "name": "Cohere（企业 LLM）",
            "name_en": "Cohere (Enterprise LLM)",
            "type": "url",
            "url": "https://cohere.com/",
            "tags": ["API", "Enterprise"]
        },
        {
            "name": "Hugging Face（模型库）",
            "name_en": "Hugging Face (Model Hub)",
            "type": "url",
            "url": "https://huggingface.co/",
            "tags": ["Open Source", "Models"]
        },
    ],
}

def find_node_by_name(root, target_name):
    """Find a node by its name (partial match) recursively."""
    if target_name in root.get('name', ''):
        return root
    for child in root.get('children', []):
        result = find_node_by_name(child, target_name)
        if result:
            return result
    return None

def validate_resource(resource):
    """Validate resource has required fields."""
    required = ['name', 'name_en', 'type', 'url', 'tags']
    for field in required:
        if field not in resource:
            return False, f"Missing field: {field}"
    url = resource.get('url', '')
    if not url.startswith('http'):
        return False, f"Invalid URL: {url}"
    name_en = resource.get('name_en', '')
    if re.search(r'[\u4e00-\u9fff]', name_en):
        return False, f"Chinese in name_en: {name_en}"
    return True, "OK"

def add_resources():
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    added_count = 0
    skipped_count = 0
    error_count = 0

    for target_name, resources in VERIFIED_RESOURCES_BATCH2.items():
        parent = find_node_by_name(data, target_name)
        if parent is None:
            print(f"❌ Category not found: {target_name}")
            error_count += len(resources)
            continue

        if 'children' not in parent:
            parent['children'] = []

        existing_urls = {child.get('url') for child in parent.get('children', [])}

        for resource in resources:
            valid, msg = validate_resource(resource)
            if not valid:
                print(f"❌ Validation failed: {resource.get('name', 'unknown')} - {msg}")
                error_count += 1
                continue

            if resource.get('url') in existing_urls:
                print(f"⏭️  Skipped (exists): {resource['name_en']}")
                skipped_count += 1
                continue

            parent['children'].append(resource)
            added_count += 1
            print(f"✅ Added: {resource['name_en']}")

    with open('docs/tarf.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*50}")
    print(f"Summary:")
    print(f"  ✅ Added: {added_count}")
    print(f"  ⏭️  Skipped: {skipped_count}")
    print(f"  ❌ Errors: {error_count}")
    print(f"{'='*50}")

if __name__ == "__main__":
    add_resources()
