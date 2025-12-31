#!/usr/bin/env python3
"""
Batch 4: Add verified resources to tarf.json
Cross-validated resources for remaining weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== 招聘伦理与公平招聘 =====
    "招聘伦理与公平招聘": [
        {
            "name": "EEOC 最佳实践（雇主指南）",
            "name_en": "EEOC Best Practices for Employers",
            "type": "url",
            "url": "https://www.eeoc.gov/initiatives/e-race/best-practices-employers-and-human-resourceseeo-professionals",
            "tags": ["Compliance", "US"]
        },
        {
            "name": "SHRM EEO 管理（公平就业机会）",
            "name_en": "SHRM Managing Equal Employment Opportunity",
            "type": "url",
            "url": "https://www.shrm.org/topics-tools/tools/toolkits/managing-equal-employment-opportunity",
            "tags": ["Compliance", "Guide"]
        },
        {
            "name": "Fair Chance Hiring（公平机会招聘）",
            "name_en": "Fair Chance Hiring Practices",
            "type": "url",
            "url": "https://wellhub.com/en-us/blog/talent-acquisition-and-retention/fair-chance-hiring-practices/",
            "tags": ["DEI", "Guide"]
        },
    ],

    # ===== 招聘心理学与行为科学 =====
    "招聘心理学与行为科学": [
        {
            "name": "CIPD 招聘行为科学报告",
            "name_en": "CIPD Behavioural Science of Recruitment",
            "type": "url",
            "url": "https://www.cipd.org/uk/knowledge/reports/recruitment-behavioural-science/",
            "tags": ["Research", "UK"]
        },
        {
            "name": "Nudge Theory in Recruitment（招聘助推理论）",
            "name_en": "Nudge Theory in Recruitment",
            "type": "url",
            "url": "https://aspect-hq.com/hiring-decisions-psychology/nudge-theory-in-recruitment",
            "tags": ["Theory", "Guide"]
        },
        {
            "name": "McKinsey Behavioral Science（企业行为科学）",
            "name_en": "McKinsey Corporate Behavioral Science",
            "type": "url",
            "url": "https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/lessons-from-the-front-line-of-corporate-nudging",
            "tags": ["Research", "Enterprise"]
        },
        {
            "name": "Cowry Consulting（行为科学招聘）",
            "name_en": "Cowry Consulting (Behavioral Science & Hiring)",
            "type": "url",
            "url": "https://www.cowryconsulting.com/",
            "tags": ["Consulting", "Behavioral"]
        },
    ],

    # ===== 招聘官网/职位结构化数据（SEO）=====
    "招聘官网/职位结构化数据（SEO）": [
        {
            "name": "Google JobPosting 结构化数据（官方文档）",
            "name_en": "Google JobPosting Structured Data (Official)",
            "type": "url",
            "url": "https://developers.google.com/search/docs/appearance/structured-data/job-posting",
            "tags": ["SEO", "Official"]
        },
        {
            "name": "Google for Jobs 指南",
            "name_en": "Google for Jobs Ultimate Guide",
            "type": "url",
            "url": "https://www.joveo.com/google-for-jobs-the-ultimate-guide/",
            "tags": ["SEO", "Guide"]
        },
        {
            "name": "Job Board SEO 指南（2025）",
            "name_en": "SEO for Job Boards Guide 2025",
            "type": "url",
            "url": "https://jboard.io/blog/seo-for-job-boards",
            "tags": ["SEO", "Guide"]
        },
        {
            "name": "Job Posting Schema 实践",
            "name_en": "Job Posting Schema Best Practices",
            "type": "url",
            "url": "https://hashmeta.com/blog/job-posting-seo-implementing-schema-markup-to-land-roles-on-google-for-jobs/",
            "tags": ["SEO", "Technical"]
        },
    ],

    # ===== AI 面试/测评 =====
    "AI 面试/测评": [
        {
            "name": "Wonderlic Select（认知测评）",
            "name_en": "Wonderlic Select (Cognitive Assessment)",
            "type": "url",
            "url": "https://wonderlic.com/",
            "tags": ["Assessment", "Cognitive"]
        },
        {
            "name": "Predictive Index（人才优化）",
            "name_en": "Predictive Index (Talent Optimization)",
            "type": "url",
            "url": "https://www.predictiveindex.com/",
            "tags": ["Assessment", "Behavioral"]
        },
        {
            "name": "SHL（人才测评）",
            "name_en": "SHL (Talent Assessment)",
            "type": "url",
            "url": "https://www.shl.com/",
            "tags": ["Assessment", "Enterprise"]
        },
        {
            "name": "Hogan Assessments（性格测评）",
            "name_en": "Hogan Assessments (Personality Assessment)",
            "type": "url",
            "url": "https://www.hoganassessments.com/",
            "tags": ["Assessment", "Personality"]
        },
        {
            "name": "Talogy（人才管理）",
            "name_en": "Talogy (Talent Management)",
            "type": "url",
            "url": "https://www.talogy.com/",
            "tags": ["Assessment", "Enterprise"]
        },
    ],

    # ===== 开源 ATS =====
    "开源 ATS": [
        {
            "name": "OpenCATS（开源 ATS）",
            "name_en": "OpenCATS (Open Source ATS)",
            "type": "url",
            "url": "https://www.opencats.org/",
            "tags": ["ATS", "Open Source"]
        },
        {
            "name": "Odoo Recruitment（Odoo 招聘模块）",
            "name_en": "Odoo Recruitment Module",
            "type": "url",
            "url": "https://www.odoo.com/app/recruitment",
            "tags": ["ATS", "Open Source"]
        },
        {
            "name": "OrangeHRM（开源 HRM）",
            "name_en": "OrangeHRM (Open Source HRM)",
            "type": "url",
            "url": "https://www.orangehrm.com/",
            "tags": ["HRIS", "Open Source"]
        },
        {
            "name": "CandidATS（安全 ATS）",
            "name_en": "CandidATS (Secure ATS)",
            "type": "url",
            "url": "https://www.candidats.io/",
            "tags": ["ATS", "Open Source"]
        },
    ],

    # ===== 实习管理平台 =====
    "实习管理平台": [
        {
            "name": "RippleMatch（校招 AI 匹配）",
            "name_en": "RippleMatch (Campus AI Matching)",
            "type": "url",
            "url": "https://ripplematch.com/",
            "tags": ["Campus", "AI"]
        },
        {
            "name": "Handshake（校园招聘平台）",
            "name_en": "Handshake (Campus Recruiting Platform)",
            "type": "url",
            "url": "https://joinhandshake.com/",
            "tags": ["Campus", "Platform"]
        },
        {
            "name": "Parker Dewey（微实习）",
            "name_en": "Parker Dewey (Micro-Internships)",
            "type": "url",
            "url": "https://www.parkerdewey.com/",
            "tags": ["Internship", "Micro"]
        },
        {
            "name": "Virtual Internships（虚拟实习）",
            "name_en": "Virtual Internships (Remote Internships)",
            "type": "url",
            "url": "https://www.virtualinternships.com/",
            "tags": ["Internship", "Remote"]
        },
    ],

    # ===== 退伍军人招聘平台 =====
    "退伍军人招聘平台": [
        {
            "name": "Hire Heroes USA（退伍军人求职援助）",
            "name_en": "Hire Heroes USA (Veteran Job Assistance)",
            "type": "url",
            "url": "https://www.hireheroesusa.org/",
            "tags": ["Veteran", "Non-Profit"]
        },
        {
            "name": "Hiring Our Heroes（军人就业）",
            "name_en": "Hiring Our Heroes (Military Employment)",
            "type": "url",
            "url": "https://www.hiringourheroes.org/",
            "tags": ["Veteran", "Program"]
        },
        {
            "name": "RecruitMilitary（军人招聘）",
            "name_en": "RecruitMilitary (Military Recruiting)",
            "type": "url",
            "url": "https://recruitmilitary.com/",
            "tags": ["Veteran", "Platform"]
        },
        {
            "name": "MilitaryHire（军人求职）",
            "name_en": "MilitaryHire (Military Job Board)",
            "type": "url",
            "url": "https://www.militaryhire.com/",
            "tags": ["Veteran", "Job Board"]
        },
        {
            "name": "Orion Talent HirePurpose（军人人才库）",
            "name_en": "Orion Talent HirePurpose (Military Talent)",
            "type": "url",
            "url": "https://www.oriontalent.com/solutions/hirepurpose-military-sourcing/",
            "tags": ["Veteran", "Sourcing"]
        },
    ],

    # ===== 招聘数据隐私与合规 =====
    "招聘数据隐私与合规": [
        {
            "name": "OneTrust（隐私合规平台）",
            "name_en": "OneTrust (Privacy Compliance Platform)",
            "type": "url",
            "url": "https://www.onetrust.com/",
            "tags": ["Privacy", "Enterprise"]
        },
        {
            "name": "TrustArc（隐私管理）",
            "name_en": "TrustArc (Privacy Management)",
            "type": "url",
            "url": "https://trustarc.com/",
            "tags": ["Privacy", "Enterprise"]
        },
        {
            "name": "BigID（数据发现与隐私）",
            "name_en": "BigID (Data Discovery & Privacy)",
            "type": "url",
            "url": "https://bigid.com/",
            "tags": ["Privacy", "AI"]
        },
        {
            "name": "Osano（简易隐私合规）",
            "name_en": "Osano (Simple Privacy Compliance)",
            "type": "url",
            "url": "https://www.osano.com/",
            "tags": ["Privacy", "SMB"]
        },
    ],

    # ===== 候选人数据管理 =====
    "候选人数据管理": [
        {
            "name": "Ketch（AI 时代数据隐私）",
            "name_en": "Ketch (AI-Era Data Privacy)",
            "type": "url",
            "url": "https://www.ketch.com/",
            "tags": ["Privacy", "AI"]
        },
        {
            "name": "Enzuzo（隐私合规简化）",
            "name_en": "Enzuzo (Privacy Compliance Simplified)",
            "type": "url",
            "url": "https://www.enzuzo.com/",
            "tags": ["Privacy", "SMB"]
        },
        {
            "name": "GDPR Compliance for HR（HR GDPR 指南）",
            "name_en": "GDPR Compliance for HR Guide",
            "type": "url",
            "url": "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/",
            "tags": ["GDPR", "Guide"]
        },
    ],

    # ===== 远程面试与虚拟招聘 =====
    "远程面试与虚拟招聘": [
        {
            "name": "Zoom for Recruiting（招聘视频会议）",
            "name_en": "Zoom for Recruiting",
            "type": "url",
            "url": "https://zoom.us/",
            "tags": ["Video", "Meeting"]
        },
        {
            "name": "Microsoft Teams Interviews（团队面试）",
            "name_en": "Microsoft Teams for Interviews",
            "type": "url",
            "url": "https://www.microsoft.com/en-us/microsoft-teams/",
            "tags": ["Video", "Enterprise"]
        },
        {
            "name": "Google Meet for Hiring（招聘视频）",
            "name_en": "Google Meet for Hiring",
            "type": "url",
            "url": "https://meet.google.com/",
            "tags": ["Video", "Free"]
        },
    ],

    # ===== 职位广告优化 =====
    "职位广告优化": [
        {
            "name": "Recruitics（招聘分析与广告）",
            "name_en": "Recruitics (Recruitment Analytics & Advertising)",
            "type": "url",
            "url": "https://www.recruitics.com/",
            "tags": ["Advertising", "Analytics"]
        },
        {
            "name": "PandoLogic（程序化招聘）",
            "name_en": "PandoLogic (Programmatic Recruiting)",
            "type": "url",
            "url": "https://pandologic.com/",
            "tags": ["Advertising", "AI"]
        },
        {
            "name": "Talroo（招聘广告平台）",
            "name_en": "Talroo (Job Advertising Platform)",
            "type": "url",
            "url": "https://www.talroo.com/",
            "tags": ["Advertising", "Platform"]
        },
    ],

    # ===== 招聘运营 (RecOps) =====
    "招聘运营 (RecOps)": [
        {
            "name": "Gem（招聘运营平台）",
            "name_en": "Gem (Recruiting Operations Platform)",
            "type": "url",
            "url": "https://www.gem.com/",
            "tags": ["RecOps", "Platform"]
        },
        {
            "name": "Ashby（现代招聘运营）",
            "name_en": "Ashby (Modern Recruiting Operations)",
            "type": "url",
            "url": "https://www.ashbyhq.com/",
            "tags": ["RecOps", "ATS"]
        },
        {
            "name": "RecOps Collective（招聘运营社区）",
            "name_en": "RecOps Collective (Community)",
            "type": "url",
            "url": "https://www.recopscollective.com/",
            "tags": ["RecOps", "Community"]
        },
    ],

    # ===== 日程协调 =====
    "日程协调": [
        {
            "name": "Doodle（日程投票）",
            "name_en": "Doodle (Scheduling Poll)",
            "type": "url",
            "url": "https://doodle.com/",
            "tags": ["Scheduling", "Free"]
        },
        {
            "name": "Cal.com（开源日程）",
            "name_en": "Cal.com (Open Source Scheduling)",
            "type": "url",
            "url": "https://cal.com/",
            "tags": ["Scheduling", "Open Source"]
        },
        {
            "name": "Reclaim.ai（AI 日程管理）",
            "name_en": "Reclaim.ai (AI Scheduling)",
            "type": "url",
            "url": "https://reclaim.ai/",
            "tags": ["Scheduling", "AI"]
        },
    ],

    # ===== AI 招聘伦理 =====
    "AI 招聘伦理": [
        {
            "name": "Partnership on AI（AI 伙伴关系）",
            "name_en": "Partnership on AI",
            "type": "url",
            "url": "https://partnershiponai.org/",
            "tags": ["AI Ethics", "Research"]
        },
        {
            "name": "AI Now Institute（AI 研究所）",
            "name_en": "AI Now Institute",
            "type": "url",
            "url": "https://ainowinstitute.org/",
            "tags": ["AI Ethics", "Research"]
        },
        {
            "name": "Responsible AI Institute（负责任 AI 研究所）",
            "name_en": "Responsible AI Institute",
            "type": "url",
            "url": "https://www.responsible.ai/",
            "tags": ["AI Ethics", "Certification"]
        },
    ],

    # ===== GitHub 搜索 =====
    "GitHub 搜索": [
        {
            "name": "GitHub Jobs Search（GitHub 搜索）",
            "name_en": "GitHub Job Search",
            "type": "template",
            "url": "https://github.com/search?q={query}&type=users",
            "tags": ["Sourcing", "Tech"]
        },
        {
            "name": "GitHub Topics（技术主题）",
            "name_en": "GitHub Topics",
            "type": "url",
            "url": "https://github.com/topics",
            "tags": ["Sourcing", "Tech"]
        },
        {
            "name": "GitHunt（GitHub 用户搜索）",
            "name_en": "GitHunt (GitHub User Search)",
            "type": "url",
            "url": "https://kamranahmed.info/githunt/",
            "tags": ["Sourcing", "Tech"]
        },
    ],

    # ===== 设计/产品 =====
    "设计/产品": [
        {
            "name": "Dribbble（设计师社区）",
            "name_en": "Dribbble (Designer Community)",
            "type": "url",
            "url": "https://dribbble.com/",
            "tags": ["Design", "Community"]
        },
        {
            "name": "Behance（创意作品集）",
            "name_en": "Behance (Creative Portfolios)",
            "type": "url",
            "url": "https://www.behance.net/",
            "tags": ["Design", "Portfolio"]
        },
        {
            "name": "ProductHire（产品人才）",
            "name_en": "ProductHire (Product Talent)",
            "type": "url",
            "url": "https://producthire.net/",
            "tags": ["Product", "Job Board"]
        },
    ],

    # ===== 职业社交 =====
    "职业社交": [
        {
            "name": "Lunchclub（AI 职业社交）",
            "name_en": "Lunchclub (AI Professional Networking)",
            "type": "url",
            "url": "https://lunchclub.com/",
            "tags": ["Networking", "AI"]
        },
        {
            "name": "Polywork（多元职业社交）",
            "name_en": "Polywork (Multi-faceted Professional)",
            "type": "url",
            "url": "https://www.polywork.com/",
            "tags": ["Networking", "Platform"]
        },
        {
            "name": "Meetup（专业活动）",
            "name_en": "Meetup (Professional Events)",
            "type": "url",
            "url": "https://www.meetup.com/",
            "tags": ["Networking", "Events"]
        },
    ],

    # ===== 面试指南/资源 =====
    "面试指南/资源": [
        {
            "name": "SHRM Interview Guide（SHRM 面试指南）",
            "name_en": "SHRM Interview Guide",
            "type": "url",
            "url": "https://www.shrm.org/topics-tools/tools/how-to-guides/how-to-conduct-effective-job-interviews",
            "tags": ["Interview", "Guide"]
        },
        {
            "name": "Indeed Interview Questions（Indeed 面试题库）",
            "name_en": "Indeed Interview Questions",
            "type": "url",
            "url": "https://www.indeed.com/career-advice/interviewing",
            "tags": ["Interview", "Resource"]
        },
        {
            "name": "Glassdoor Interview Questions（面试问题）",
            "name_en": "Glassdoor Interview Questions",
            "type": "url",
            "url": "https://www.glassdoor.com/Interview/index.htm",
            "tags": ["Interview", "Community"]
        },
    ],

    # ===== Offer、背调与入职 =====
    "Offer、背调与入职": [
        {
            "name": "Verified First（综合背调）",
            "name_en": "Verified First (Comprehensive Background Checks)",
            "type": "url",
            "url": "https://www.verifiedfirst.com/",
            "tags": ["Background", "Platform"]
        },
        {
            "name": "Accurate Background（准确背调）",
            "name_en": "Accurate Background (Background Screening)",
            "type": "url",
            "url": "https://www.accurate.com/",
            "tags": ["Background", "Enterprise"]
        },
        {
            "name": "Hireology（招聘到入职）",
            "name_en": "Hireology (Hire to Onboard)",
            "type": "url",
            "url": "https://www.hireology.com/",
            "tags": ["ATS", "Onboarding"]
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


def add_resources():
    print("Loading tarf.json...")
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    added_count = 0
    skipped_count = 0
    error_count = 0

    for target_name, resources in NEW_RESOURCES.items():
        parent = find_node_by_name(data, target_name)

        if parent is None:
            print(f"❌ Category not found: {target_name}")
            error_count += len(resources)
            continue

        if 'children' not in parent:
            parent['children'] = []

        # Get existing URLs and names to avoid duplicates
        existing_urls = {child.get('url') for child in parent.get('children', [])}
        existing_names = {child.get('name') for child in parent.get('children', [])}

        for resource in resources:
            if resource.get('url') in existing_urls:
                print(f"⏭️  Skipped (URL exists): {resource['name_en']}")
                skipped_count += 1
            elif resource['name'] in existing_names:
                print(f"⏭️  Skipped (name exists): {resource['name_en']}")
                skipped_count += 1
            else:
                parent['children'].append(resource)
                added_count += 1
                print(f"✅ Added: {resource['name_en']} -> {target_name}")

    print("\nSaving tarf.json...")
    with open('docs/tarf.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 60)
    print("Summary:")
    print(f"  ✅ Added: {added_count}")
    print(f"  ⏭️  Skipped: {skipped_count}")
    print(f"  ❌ Errors: {error_count}")
    print("=" * 60)


if __name__ == "__main__":
    add_resources()
