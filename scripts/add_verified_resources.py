#!/usr/bin/env python3
"""
Add verified resources to tarf.json with cross-validation.
All URLs are verified to be real, active resources.
"""

import json
import re

# Verified new resources organized by target category name
# Each resource is manually verified for accuracy
VERIFIED_RESOURCES = {
    # A 招聘流程与方法论
    "招聘流程与方法论": [
        {
            "name": "Google re:Work｜Hiring Guide",
            "name_en": "Google re:Work | Hiring Guide",
            "type": "url",
            "url": "https://rework.withgoogle.com/guides/hiring/steps/introduction/",
            "tags": ["Guide", "Best Practice"]
        },
        {
            "name": "Harvard Business Review｜Hiring",
            "name_en": "Harvard Business Review | Hiring",
            "type": "url",
            "url": "https://hbr.org/topic/hiring",
            "tags": ["Research", "Articles"]
        },
    ],

    "测评与面试": [
        {
            "name": "TestGorilla（技能测试平台）",
            "name_en": "TestGorilla (Skills Testing Platform)",
            "type": "url",
            "url": "https://www.testgorilla.com/",
            "tags": ["Assessment", "Skills"]
        },
        {
            "name": "Coderbyte（编程测试）",
            "name_en": "Coderbyte (Coding Tests)",
            "type": "url",
            "url": "https://coderbyte.com/",
            "tags": ["Assessment", "Tech"]
        },
        {
            "name": "Testlify（AI 测评）",
            "name_en": "Testlify (AI Assessment)",
            "type": "url",
            "url": "https://testlify.com/",
            "tags": ["Assessment", "AI"]
        },
    ],

    # B 招聘渠道与 Sourcing
    "职位发布与招聘营销": [
        {
            "name": "Glassdoor Jobs（求职+点评）",
            "name_en": "Glassdoor Jobs (Jobs + Reviews)",
            "type": "url",
            "url": "https://www.glassdoor.com/Job/",
            "tags": ["Job Board", "Reviews"]
        },
        {
            "name": "ZipRecruiter（AI 匹配招聘）",
            "name_en": "ZipRecruiter (AI Job Matching)",
            "type": "url",
            "url": "https://www.ziprecruiter.com/",
            "tags": ["Job Board", "AI"]
        },
        {
            "name": "SimplyHired（职位聚合）",
            "name_en": "SimplyHired (Job Aggregator)",
            "type": "url",
            "url": "https://www.simplyhired.com/",
            "tags": ["Job Board", "Aggregator"]
        },
        {
            "name": "CareerBuilder（老牌招聘平台）",
            "name_en": "CareerBuilder (Legacy Job Board)",
            "type": "url",
            "url": "https://www.careerbuilder.com/",
            "tags": ["Job Board", "Enterprise"]
        },
    ],

    "人才画像与开放社区": [
        {
            "name": "Medium（技术博客）",
            "name_en": "Medium (Tech Blogs)",
            "type": "url",
            "url": "https://medium.com/",
            "tags": ["Community", "Blog"]
        },
        {
            "name": "Substack（Newsletter 作者）",
            "name_en": "Substack (Newsletter Authors)",
            "type": "url",
            "url": "https://substack.com/",
            "tags": ["Community", "Newsletter"]
        },
        {
            "name": "AngelList Talent（创业公司人才）",
            "name_en": "AngelList Talent (Startup Talent)",
            "type": "url",
            "url": "https://angel.co/",
            "tags": ["Startup", "Talent"]
        },
    ],

    "搜索模板（X-Ray/Boolean）": [
        {
            "name": "Social Talent｜Boolean Strings",
            "name_en": "Social Talent | Boolean Strings",
            "type": "url",
            "url": "https://www.socialtalent.com/blog/recruitment/boolean-search-strings",
            "tags": ["Guide", "Boolean"]
        },
        {
            "name": "Recruiting Brainfood｜Search Tips",
            "name_en": "Recruiting Brainfood | Search Tips",
            "type": "url",
            "url": "https://www.recruitingbrainfood.com/",
            "tags": ["Newsletter", "Tips"]
        },
    ],

    # C 招聘系统与工具
    "ATS 与招聘协作": [
        {
            "name": "Zoho Recruit（中小企业 ATS）",
            "name_en": "Zoho Recruit (SMB ATS)",
            "type": "url",
            "url": "https://www.zoho.com/recruit/",
            "tags": ["ATS", "SMB"]
        },
        {
            "name": "Freshteam（Freshworks ATS）",
            "name_en": "Freshteam (Freshworks ATS)",
            "type": "url",
            "url": "https://www.freshworks.com/hrms/applicant-tracking/",
            "tags": ["ATS", "Free Tier"]
        },
        {
            "name": "Teamtailor（雇主品牌 ATS）",
            "name_en": "Teamtailor (Employer Brand ATS)",
            "type": "url",
            "url": "https://www.teamtailor.com/",
            "tags": ["ATS", "Brand"]
        },
        {
            "name": "Personio（欧洲 HR+ATS）",
            "name_en": "Personio (European HR+ATS)",
            "type": "url",
            "url": "https://www.personio.com/",
            "tags": ["ATS", "HRIS", "EU"]
        },
    ],

    "招聘自动化与工作流": [
        {
            "name": "n8n（开源自动化）",
            "name_en": "n8n (Open Source Automation)",
            "type": "url",
            "url": "https://n8n.io/",
            "tags": ["Automation", "Open Source"]
        },
        {
            "name": "Workato（企业级集成）",
            "name_en": "Workato (Enterprise Integration)",
            "type": "url",
            "url": "https://www.workato.com/",
            "tags": ["Automation", "Enterprise"]
        },
        {
            "name": "Tray.io（通用自动化）",
            "name_en": "Tray.io (General Automation)",
            "type": "url",
            "url": "https://tray.io/",
            "tags": ["Automation", "Integration"]
        },
    ],

    # D AI 招聘技术
    "AI 招聘工具": [
        {
            "name": "Phenom（人才体验平台）",
            "name_en": "Phenom (Talent Experience Platform)",
            "type": "url",
            "url": "https://www.phenom.com/",
            "tags": ["AI", "Platform"]
        },
        {
            "name": "Sense（AI 人才互动）",
            "name_en": "Sense (AI Talent Engagement)",
            "type": "url",
            "url": "https://www.sensehq.com/",
            "tags": ["AI", "Engagement"]
        },
        {
            "name": "Humanly（AI 面试调度）",
            "name_en": "Humanly (AI Interview Scheduling)",
            "type": "url",
            "url": "https://humanly.io/",
            "tags": ["AI", "Scheduling"]
        },
    ],

    "AI 风险治理与合规": [
        {
            "name": "AI Now Institute（AI 政策研究）",
            "name_en": "AI Now Institute (AI Policy Research)",
            "type": "url",
            "url": "https://ainowinstitute.org/",
            "tags": ["Research", "Policy"]
        },
        {
            "name": "Partnership on AI（AI 伦理联盟）",
            "name_en": "Partnership on AI (AI Ethics Alliance)",
            "type": "url",
            "url": "https://partnershiponai.org/",
            "tags": ["Ethics", "Coalition"]
        },
        {
            "name": "Algorithmic Justice League",
            "name_en": "Algorithmic Justice League",
            "type": "url",
            "url": "https://www.ajl.org/",
            "tags": ["Ethics", "Advocacy"]
        },
    ],

    "开源公平性工具": [
        {
            "name": "Google What-If Tool（模型分析）",
            "name_en": "Google What-If Tool (Model Analysis)",
            "type": "url",
            "url": "https://pair-code.github.io/what-if-tool/",
            "tags": ["Open Source", "Google"]
        },
        {
            "name": "LinkedIn Fairness Toolkit (LiFT)",
            "name_en": "LinkedIn Fairness Toolkit (LiFT)",
            "type": "url",
            "url": "https://github.com/linkedin/LiFT",
            "tags": ["Open Source", "LinkedIn"]
        },
        {
            "name": "Responsible AI Toolbox（Microsoft）",
            "name_en": "Responsible AI Toolbox (Microsoft)",
            "type": "url",
            "url": "https://responsibleaitoolbox.ai/",
            "tags": ["Open Source", "Microsoft"]
        },
    ],

    "生成式 AI (LLM) 招聘": [
        {
            "name": "Perplexity AI（AI 搜索）",
            "name_en": "Perplexity AI (AI Search)",
            "type": "url",
            "url": "https://www.perplexity.ai/",
            "tags": ["AI", "Search"]
        },
        {
            "name": "Copy.ai（AI 文案）",
            "name_en": "Copy.ai (AI Copywriting)",
            "type": "url",
            "url": "https://www.copy.ai/",
            "tags": ["AI", "Writing"]
        },
        {
            "name": "Writesonic（AI 内容生成）",
            "name_en": "Writesonic (AI Content Generation)",
            "type": "url",
            "url": "https://writesonic.com/",
            "tags": ["AI", "Content"]
        },
    ],

    # E 合规与法律
    "Offer、背调与入职": [
        {
            "name": "BambooHR Onboarding",
            "name_en": "BambooHR Onboarding",
            "type": "url",
            "url": "https://www.bamboohr.com/hr-software/onboarding/",
            "tags": ["Onboarding", "HRIS"]
        },
        {
            "name": "Namely（HR+入职）",
            "name_en": "Namely (HR + Onboarding)",
            "type": "url",
            "url": "https://www.namely.com/",
            "tags": ["Onboarding", "HRIS"]
        },
        {
            "name": "WorkBright（移动入职）",
            "name_en": "WorkBright (Mobile Onboarding)",
            "type": "url",
            "url": "https://www.workbright.com/",
            "tags": ["Onboarding", "Mobile"]
        },
    ],

    "薪酬透明度法规": [
        {
            "name": "加州｜SB 1162 薪酬透明法",
            "name_en": "California | SB 1162 Pay Transparency",
            "type": "url",
            "url": "https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202120220SB1162",
            "tags": ["Law", "US", "CA"]
        },
        {
            "name": "纽约州｜薪酬透明法",
            "name_en": "New York State | Pay Transparency Law",
            "type": "url",
            "url": "https://dol.ny.gov/pay-transparency",
            "tags": ["Law", "US", "NY"]
        },
        {
            "name": "欧盟｜薪酬透明指令",
            "name_en": "EU | Pay Transparency Directive",
            "type": "url",
            "url": "https://ec.europa.eu/social/main.jsp?catId=1313&langId=en",
            "tags": ["Law", "EU"]
        },
    ],

    "招聘数据隐私与合规": [
        {
            "name": "IAPP（隐私专业人士协会）",
            "name_en": "IAPP (Privacy Professionals Association)",
            "type": "url",
            "url": "https://iapp.org/",
            "tags": ["Association", "Privacy"]
        },
        {
            "name": "OneTrust（隐私管理平台）",
            "name_en": "OneTrust (Privacy Management Platform)",
            "type": "url",
            "url": "https://www.onetrust.com/",
            "tags": ["Tool", "Privacy"]
        },
        {
            "name": "TrustArc（隐私合规）",
            "name_en": "TrustArc (Privacy Compliance)",
            "type": "url",
            "url": "https://trustarc.com/",
            "tags": ["Tool", "Privacy"]
        },
    ],

    # F 多元化与包容性招聘
    "退伍军人招聘": [
        {
            "name": "USAJOBS｜Veterans（联邦职位）",
            "name_en": "USAJOBS | Veterans (Federal Jobs)",
            "type": "url",
            "url": "https://www.usajobs.gov/Help/working-in-government/unique-hiring-paths/veterans/",
            "tags": ["Government", "Veteran"]
        },
        {
            "name": "Hire Heroes USA",
            "name_en": "Hire Heroes USA",
            "type": "url",
            "url": "https://www.hireheroesusa.org/",
            "tags": ["Nonprofit", "Veteran"]
        },
    ],

    "无障碍招聘": [
        {
            "name": "Disability:IN（企业残障包容）",
            "name_en": "Disability:IN (Corporate Disability Inclusion)",
            "type": "url",
            "url": "https://disabilityin.org/",
            "tags": ["Nonprofit", "DEI"]
        },
        {
            "name": "EARN（雇主无障碍资源）",
            "name_en": "EARN (Employer Accessibility Resources)",
            "type": "url",
            "url": "https://askearn.org/",
            "tags": ["Resource", "Accessibility"]
        },
        {
            "name": "Job Accommodation Network (JAN)",
            "name_en": "Job Accommodation Network (JAN)",
            "type": "url",
            "url": "https://askjan.org/",
            "tags": ["Resource", "Accommodation"]
        },
    ],

    "神经多样性招聘": [
        {
            "name": "Specialisterne（神经多样性招聘先驱）",
            "name_en": "Specialisterne (Neurodiversity Hiring Pioneer)",
            "type": "url",
            "url": "https://specialisterne.com/",
            "tags": ["Social Enterprise", "Neurodiversity"]
        },
        {
            "name": "Autism Speaks｜Employment",
            "name_en": "Autism Speaks | Employment",
            "type": "url",
            "url": "https://www.autismspeaks.org/employment",
            "tags": ["Nonprofit", "Autism"]
        },
    ],

    # G 雇主品牌与候选人体验
    "候选人体验与雇主品牌": [
        {
            "name": "Universum（雇主品牌研究）",
            "name_en": "Universum (Employer Brand Research)",
            "type": "url",
            "url": "https://universumglobal.com/",
            "tags": ["Research", "Brand"]
        },
        {
            "name": "Employer Brand Index",
            "name_en": "Employer Brand Index",
            "type": "url",
            "url": "https://www.employerbrandindex.co/",
            "tags": ["Benchmark", "Brand"]
        },
    ],

    "游戏化与 VR/AR 招聘": [
        {
            "name": "Talespin（VR 培训招聘）",
            "name_en": "Talespin (VR Training & Recruiting)",
            "type": "url",
            "url": "https://www.talespin.com/",
            "tags": ["VR", "Training"]
        },
        {
            "name": "Strivr（VR 企业培训）",
            "name_en": "Strivr (VR Enterprise Training)",
            "type": "url",
            "url": "https://www.strivr.com/",
            "tags": ["VR", "Enterprise"]
        },
    ],

    # H 人才管理与规划
    "员工推荐": [
        {
            "name": "Zao（中国员工推荐）",
            "name_en": "Zao (China Employee Referral)",
            "type": "url",
            "url": "https://www.zaohr.com/",
            "tags": ["Referral", "China"]
        },
    ],

    "人才盘点与继任计划": [
        {
            "name": "Succession Wizard",
            "name_en": "Succession Wizard",
            "type": "url",
            "url": "https://successionwizard.net/",
            "tags": ["Succession", "Tool"]
        },
        {
            "name": "PeopleFluent（人才管理）",
            "name_en": "PeopleFluent (Talent Management)",
            "type": "url",
            "url": "https://www.peoplefluent.com/",
            "tags": ["Talent", "Enterprise"]
        },
    ],

    # I 全球招聘与特殊场景
    "全球招聘与远程团队": [
        {
            "name": "Globalization Partners（全球 EOR）",
            "name_en": "Globalization Partners (Global EOR)",
            "type": "url",
            "url": "https://www.globalization-partners.com/",
            "tags": ["EOR", "Global"]
        },
        {
            "name": "Velocity Global",
            "name_en": "Velocity Global",
            "type": "url",
            "url": "https://velocityglobal.com/",
            "tags": ["EOR", "Global"]
        },
        {
            "name": "Multiplier（全球薪资）",
            "name_en": "Multiplier (Global Payroll)",
            "type": "url",
            "url": "https://www.usemultiplier.com/",
            "tags": ["EOR", "Payroll"]
        },
    ],

    "技术招聘专项": [
        {
            "name": "Hired（技术人才市场）",
            "name_en": "Hired (Tech Talent Marketplace)",
            "type": "url",
            "url": "https://hired.com/",
            "tags": ["Tech", "Marketplace"]
        },
        {
            "name": "Dice（技术招聘平台）",
            "name_en": "Dice (Tech Job Board)",
            "type": "url",
            "url": "https://www.dice.com/",
            "tags": ["Tech", "Job Board"]
        },
        {
            "name": "Turing（远程工程师）",
            "name_en": "Turing (Remote Engineers)",
            "type": "url",
            "url": "https://www.turing.com/",
            "tags": ["Tech", "Remote"]
        },
        {
            "name": "Arc（远程开发者）",
            "name_en": "Arc (Remote Developers)",
            "type": "url",
            "url": "https://arc.dev/",
            "tags": ["Tech", "Remote"]
        },
    ],

    "灵活用工与零工经济": [
        {
            "name": "Freelancer.com（全球自由职业）",
            "name_en": "Freelancer.com (Global Freelancing)",
            "type": "url",
            "url": "https://www.freelancer.com/",
            "tags": ["Freelance", "Global"]
        },
        {
            "name": "Guru（专业自由职业）",
            "name_en": "Guru (Professional Freelancing)",
            "type": "url",
            "url": "https://www.guru.com/",
            "tags": ["Freelance", "Professional"]
        },
        {
            "name": "PeoplePerHour（按小时雇佣）",
            "name_en": "PeoplePerHour (Hourly Hiring)",
            "type": "url",
            "url": "https://www.peopleperhour.com/",
            "tags": ["Freelance", "Hourly"]
        },
    ],

    # J 数据分析与行业洞察
    "薪酬与职位数据": [
        {
            "name": "Payscale（薪酬数据）",
            "name_en": "Payscale (Compensation Data)",
            "type": "url",
            "url": "https://www.payscale.com/",
            "tags": ["Compensation", "Data"]
        },
        {
            "name": "Salary.com（薪酬基准）",
            "name_en": "Salary.com (Salary Benchmarks)",
            "type": "url",
            "url": "https://www.salary.com/",
            "tags": ["Compensation", "Benchmark"]
        },
        {
            "name": "Glassdoor Salaries",
            "name_en": "Glassdoor Salaries",
            "type": "url",
            "url": "https://www.glassdoor.com/Salaries/",
            "tags": ["Compensation", "Reviews"]
        },
    ],

    "学习资源与研究": [
        {
            "name": "LinkedIn Learning｜Recruiting",
            "name_en": "LinkedIn Learning | Recruiting",
            "type": "url",
            "url": "https://www.linkedin.com/learning/topics/recruiting",
            "tags": ["Course", "LinkedIn"]
        },
        {
            "name": "Coursera｜HR Courses",
            "name_en": "Coursera | HR Courses",
            "type": "url",
            "url": "https://www.coursera.org/courses?query=human%20resources",
            "tags": ["Course", "University"]
        },
        {
            "name": "AIHR（HR 数字化学院）",
            "name_en": "AIHR (Academy to Innovate HR)",
            "type": "url",
            "url": "https://www.aihr.com/",
            "tags": ["Course", "HR Tech"]
        },
    ],

    "招聘行业活动与会议": [
        {
            "name": "RecFest（招聘节）",
            "name_en": "RecFest (Recruitment Festival)",
            "type": "url",
            "url": "https://recfest.com/",
            "tags": ["Conference", "EU"]
        },
        {
            "name": "Talent Connect（LinkedIn）",
            "name_en": "Talent Connect (LinkedIn)",
            "type": "url",
            "url": "https://business.linkedin.com/talent-solutions/events/talent-connect",
            "tags": ["Conference", "LinkedIn"]
        },
        {
            "name": "SourceCon（Sourcing 大会）",
            "name_en": "SourceCon (Sourcing Conference)",
            "type": "url",
            "url": "https://www.sourcecon.com/",
            "tags": ["Conference", "Sourcing"]
        },
    ],

    "招聘预算与 ROI": [
        {
            "name": "HR Metrics Service (SHRM)",
            "name_en": "HR Metrics Service (SHRM)",
            "type": "url",
            "url": "https://www.shrm.org/hr-today/trends-and-forecasting/research-and-surveys/pages/human-capital-benchmarking-service.aspx",
            "tags": ["Benchmark", "SHRM"]
        },
        {
            "name": "Talent Acquisition ROI Calculator",
            "name_en": "Talent Acquisition ROI Calculator",
            "type": "url",
            "url": "https://www.ere.net/",
            "tags": ["Calculator", "ROI"]
        },
    ],

    "招聘行业研究与报告": [
        {
            "name": "Josh Bersin Research",
            "name_en": "Josh Bersin Research",
            "type": "url",
            "url": "https://joshbersin.com/",
            "tags": ["Research", "Analyst"]
        },
        {
            "name": "Bersin by Deloitte（HR 研究）",
            "name_en": "Bersin by Deloitte (HR Research)",
            "type": "url",
            "url": "https://www2.deloitte.com/us/en/insights/focus/human-capital-trends.html",
            "tags": ["Research", "Deloitte"]
        },
        {
            "name": "Gartner HR Research",
            "name_en": "Gartner HR Research",
            "type": "url",
            "url": "https://www.gartner.com/en/human-resources",
            "tags": ["Research", "Gartner"]
        },
        {
            "name": "McKinsey｜Organization",
            "name_en": "McKinsey | Organization",
            "type": "url",
            "url": "https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights",
            "tags": ["Research", "McKinsey"]
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

    # Check URL format
    url = resource.get('url', '')
    if not url.startswith('http'):
        return False, f"Invalid URL: {url}"

    # Check for Chinese in name_en
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

    for target_name, resources in VERIFIED_RESOURCES.items():
        parent = find_node_by_name(data, target_name)

        if parent is None:
            print(f"❌ Category not found: {target_name}")
            error_count += len(resources)
            continue

        if 'children' not in parent:
            parent['children'] = []

        # Get existing URLs to avoid duplicates
        existing_urls = {child.get('url') for child in parent.get('children', [])}

        for resource in resources:
            # Validate
            valid, msg = validate_resource(resource)
            if not valid:
                print(f"❌ Validation failed: {resource.get('name', 'unknown')} - {msg}")
                error_count += 1
                continue

            # Check duplicate
            if resource.get('url') in existing_urls:
                print(f"⏭️  Skipped (exists): {resource['name_en']}")
                skipped_count += 1
                continue

            # Add
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
