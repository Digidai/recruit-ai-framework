#!/usr/bin/env python3
"""
Batch 6: Add verified resources to tarf.json
Cross-validated resources for remaining weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== 招聘营销平台 =====
    "招聘营销平台": [
        {
            "name": "Rally Recruitment Marketing（招聘营销社区）",
            "name_en": "Rally Recruitment Marketing (Community)",
            "type": "url",
            "url": "https://rallyrecruitmentmarketing.com/",
            "tags": ["Marketing", "Community"]
        },
        {
            "name": "Symphony Talent（人才获取软件）",
            "name_en": "Symphony Talent (Talent Acquisition Software)",
            "type": "url",
            "url": "https://www.symphonytalent.com/",
            "tags": ["Marketing", "Enterprise"]
        },
        {
            "name": "TalentLyft（招聘营销）",
            "name_en": "TalentLyft (Recruitment Marketing)",
            "type": "url",
            "url": "https://www.talentlyft.com/",
            "tags": ["Marketing", "SMB"]
        },
    ],

    # ===== 技术技能评估 =====
    "技术技能评估": [
        {
            "name": "CodeSignal（技术评估）",
            "name_en": "CodeSignal (Technical Assessment)",
            "type": "url",
            "url": "https://codesignal.com/",
            "tags": ["Coding", "AI"]
        },
        {
            "name": "Codility（编程挑战）",
            "name_en": "Codility (Coding Challenges)",
            "type": "url",
            "url": "https://www.codility.com/",
            "tags": ["Coding", "Enterprise"]
        },
        {
            "name": "CoderPad（实时编程面试）",
            "name_en": "CoderPad (Live Coding Interviews)",
            "type": "url",
            "url": "https://coderpad.io/",
            "tags": ["Coding", "Live"]
        },
    ],

    # ===== 视频制作工具 =====
    "视频制作工具": [
        {
            "name": "Vouch（员工证言视频）",
            "name_en": "Vouch (Employee Testimonial Videos)",
            "type": "url",
            "url": "https://vouchfor.com/",
            "tags": ["Video", "Testimonial"]
        },
        {
            "name": "VideoMyJob（雇主品牌视频）",
            "name_en": "VideoMyJob (Employer Branding Videos)",
            "type": "url",
            "url": "https://www.videomyjob.com/",
            "tags": ["Video", "EB"]
        },
        {
            "name": "iCIMS Video Studio（视频制作）",
            "name_en": "iCIMS Video Studio",
            "type": "url",
            "url": "https://www.icims.com/products/recruitment-marketing-software/employee-testimonial-videos/",
            "tags": ["Video", "ATS"]
        },
        {
            "name": "Pitchy HR Video（HR 视频制作）",
            "name_en": "Pitchy HR Video Maker",
            "type": "url",
            "url": "https://www.pitchy.io/hr-video-maker",
            "tags": ["Video", "DIY"]
        },
    ],

    # ===== 生成式 AI (LLM) 招聘 =====
    "生成式 AI (LLM) 招聘": [
        {
            "name": "ChatGPT for Recruiting（招聘 GPT）",
            "name_en": "ChatGPT for Recruiting",
            "type": "url",
            "url": "https://chat.openai.com/",
            "tags": ["LLM", "AI"]
        },
        {
            "name": "Claude for HR（Claude AI）",
            "name_en": "Claude for HR (Anthropic)",
            "type": "url",
            "url": "https://claude.ai/",
            "tags": ["LLM", "AI"]
        },
        {
            "name": "Gemini（Google AI）",
            "name_en": "Gemini (Google AI)",
            "type": "url",
            "url": "https://gemini.google.com/",
            "tags": ["LLM", "Google"]
        },
        {
            "name": "NotebookLM（Google 笔记 AI）",
            "name_en": "NotebookLM (Google Note AI)",
            "type": "url",
            "url": "https://notebooklm.google.com/",
            "tags": ["LLM", "Research"]
        },
    ],

    # ===== HR/招聘行业组织 =====
    "HR/招聘行业组织": [
        {
            "name": "SHRM（人力资源管理学会）",
            "name_en": "SHRM (Society for Human Resource Management)",
            "type": "url",
            "url": "https://www.shrm.org/",
            "tags": ["Association", "US"]
        },
        {
            "name": "CIPD（英国人事与发展协会）",
            "name_en": "CIPD (Chartered Institute of Personnel and Development)",
            "type": "url",
            "url": "https://www.cipd.org/",
            "tags": ["Association", "UK"]
        },
        {
            "name": "ATD（人才发展协会）",
            "name_en": "ATD (Association for Talent Development)",
            "type": "url",
            "url": "https://www.td.org/",
            "tags": ["Association", "L&D"]
        },
        {
            "name": "HRCI（人力资源认证协会）",
            "name_en": "HRCI (Human Resources Certification Institute)",
            "type": "url",
            "url": "https://www.hrci.org/",
            "tags": ["Certification", "Global"]
        },
        {
            "name": "WorldatWork（全球薪酬协会）",
            "name_en": "WorldatWork (Total Rewards Association)",
            "type": "url",
            "url": "https://www.worldatwork.org/",
            "tags": ["Association", "Compensation"]
        },
    ],

    # ===== 候选人体验 =====
    "候选人体验": [
        {
            "name": "Survale（候选人体验调查）",
            "name_en": "Survale (Candidate Experience Surveys)",
            "type": "url",
            "url": "https://survale.com/",
            "tags": ["CX", "Survey"]
        },
        {
            "name": "Qualtrics Candidate Experience（候选人体验）",
            "name_en": "Qualtrics Candidate Experience",
            "type": "url",
            "url": "https://www.qualtrics.com/employee-experience/candidate-experience/",
            "tags": ["CX", "Enterprise"]
        },
        {
            "name": "Candidate.fyi（候选人门户）",
            "name_en": "Candidate.fyi (Candidate Portal)",
            "type": "url",
            "url": "https://candidate.fyi/",
            "tags": ["CX", "Platform"]
        },
    ],

    # ===== 自由职业平台 =====
    "自由职业平台": [
        {
            "name": "Toptal（顶级自由职业者）",
            "name_en": "Toptal (Top 3% Freelancers)",
            "type": "url",
            "url": "https://www.toptal.com/",
            "tags": ["Freelance", "Elite"]
        },
        {
            "name": "Upwork（综合自由职业）",
            "name_en": "Upwork (General Freelance)",
            "type": "url",
            "url": "https://www.upwork.com/",
            "tags": ["Freelance", "Global"]
        },
        {
            "name": "Fiverr（零工服务市场）",
            "name_en": "Fiverr (Gig Service Marketplace)",
            "type": "url",
            "url": "https://www.fiverr.com/",
            "tags": ["Freelance", "Gigs"]
        },
        {
            "name": "99designs（设计师平台）",
            "name_en": "99designs (Designer Platform)",
            "type": "url",
            "url": "https://99designs.com/",
            "tags": ["Freelance", "Design"]
        },
    ],

    # ===== 国际薪酬/合规 =====
    "国际薪酬/合规": [
        {
            "name": "Globalization Partners（全球雇佣）",
            "name_en": "Globalization Partners (Global Employment)",
            "type": "url",
            "url": "https://www.g-p.com/",
            "tags": ["EOR", "Global"]
        },
        {
            "name": "Multiplier（国际 HR）",
            "name_en": "Multiplier (International HR)",
            "type": "url",
            "url": "https://www.usemultiplier.com/",
            "tags": ["EOR", "SMB"]
        },
        {
            "name": "Remofirst（远程团队合规）",
            "name_en": "Remofirst (Remote Team Compliance)",
            "type": "url",
            "url": "https://www.remofirst.com/",
            "tags": ["EOR", "Affordable"]
        },
    ],

    # ===== 技术招聘专项 =====
    "技术招聘专项": [
        {
            "name": "Hired（技术人才市场）",
            "name_en": "Hired (Tech Talent Marketplace)",
            "type": "url",
            "url": "https://hired.com/",
            "tags": ["Tech", "Marketplace"]
        },
        {
            "name": "AngelList Talent（创业公司招聘）",
            "name_en": "AngelList Talent (Startup Recruiting)",
            "type": "url",
            "url": "https://angel.co/",
            "tags": ["Tech", "Startup"]
        },
        {
            "name": "Dice（技术招聘网站）",
            "name_en": "Dice (Tech Job Board)",
            "type": "url",
            "url": "https://www.dice.com/",
            "tags": ["Tech", "Job Board"]
        },
    ],

    # ===== 设计工具 =====
    "设计工具": [
        {
            "name": "Canva（简易设计）",
            "name_en": "Canva (Easy Design)",
            "type": "url",
            "url": "https://www.canva.com/",
            "tags": ["Design", "Free"]
        },
        {
            "name": "Figma（协作设计）",
            "name_en": "Figma (Collaborative Design)",
            "type": "url",
            "url": "https://www.figma.com/",
            "tags": ["Design", "Pro"]
        },
        {
            "name": "Adobe Express（快速设计）",
            "name_en": "Adobe Express (Quick Design)",
            "type": "url",
            "url": "https://www.adobe.com/express/",
            "tags": ["Design", "Adobe"]
        },
    ],

    # ===== 雇主品牌视觉 =====
    "雇主品牌视觉": [
        {
            "name": "Visme（视觉内容平台）",
            "name_en": "Visme (Visual Content Platform)",
            "type": "url",
            "url": "https://www.visme.co/",
            "tags": ["Visual", "Content"]
        },
        {
            "name": "Piktochart（信息图表）",
            "name_en": "Piktochart (Infographics)",
            "type": "url",
            "url": "https://piktochart.com/",
            "tags": ["Visual", "Infographic"]
        },
        {
            "name": "Prezi（演示文稿）",
            "name_en": "Prezi (Presentations)",
            "type": "url",
            "url": "https://prezi.com/",
            "tags": ["Visual", "Presentation"]
        },
    ],

    # ===== 招聘社交媒体 =====
    "招聘社交媒体": [
        {
            "name": "LinkedIn Recruiter（领英招聘）",
            "name_en": "LinkedIn Recruiter",
            "type": "url",
            "url": "https://business.linkedin.com/talent-solutions/recruiter",
            "tags": ["Social", "LinkedIn"]
        },
        {
            "name": "Buffer（社交媒体管理）",
            "name_en": "Buffer (Social Media Management)",
            "type": "url",
            "url": "https://buffer.com/",
            "tags": ["Social", "Scheduling"]
        },
        {
            "name": "Hootsuite（社交媒体套件）",
            "name_en": "Hootsuite (Social Media Suite)",
            "type": "url",
            "url": "https://www.hootsuite.com/",
            "tags": ["Social", "Enterprise"]
        },
    ],

    # ===== 招聘网站设计 =====
    "招聘网站设计": [
        {
            "name": "Ongig（职位页面优化）",
            "name_en": "Ongig (Job Page Optimization)",
            "type": "url",
            "url": "https://www.ongig.com/",
            "tags": ["Career Site", "SEO"]
        },
        {
            "name": "Recruit Rooster（职业网站建设）",
            "name_en": "Recruit Rooster (Career Site Builder)",
            "type": "url",
            "url": "https://recruitrooster.com/",
            "tags": ["Career Site", "Design"]
        },
        {
            "name": "CareerSiteCloud（职业网站）",
            "name_en": "CareerSiteCloud (Career Sites)",
            "type": "url",
            "url": "https://careersitecloud.com/",
            "tags": ["Career Site", "Platform"]
        },
    ],

    # ===== 人才画像与开放社区 =====
    "人才画像与开放社区": [
        {
            "name": "Stack Overflow Talent（开发者社区）",
            "name_en": "Stack Overflow Talent (Developer Community)",
            "type": "url",
            "url": "https://stackoverflow.com/talent",
            "tags": ["Tech", "Community"]
        },
        {
            "name": "Kaggle（数据科学社区）",
            "name_en": "Kaggle (Data Science Community)",
            "type": "url",
            "url": "https://www.kaggle.com/",
            "tags": ["Data", "Community"]
        },
        {
            "name": "Reddit r/recruiting（招聘社区）",
            "name_en": "Reddit r/recruiting (Recruiting Community)",
            "type": "url",
            "url": "https://www.reddit.com/r/recruiting/",
            "tags": ["Community", "Discussion"]
        },
    ],

    # ===== 薪酬与职位数据 =====
    "薪酬与职位数据": [
        {
            "name": "Levels.fyi（科技薪酬数据）",
            "name_en": "Levels.fyi (Tech Salary Data)",
            "type": "url",
            "url": "https://www.levels.fyi/",
            "tags": ["Salary", "Tech"]
        },
        {
            "name": "PayScale（薪酬数据）",
            "name_en": "PayScale (Compensation Data)",
            "type": "url",
            "url": "https://www.payscale.com/",
            "tags": ["Salary", "Platform"]
        },
        {
            "name": "Salary.com（薪酬研究）",
            "name_en": "Salary.com (Compensation Research)",
            "type": "url",
            "url": "https://www.salary.com/",
            "tags": ["Salary", "Research"]
        },
    ],

    # ===== 薪酬基准 =====
    "薪酬基准": [
        {
            "name": "Radford（薪酬调研）",
            "name_en": "Radford (Compensation Surveys)",
            "type": "url",
            "url": "https://radford.aon.com/",
            "tags": ["Benchmark", "Enterprise"]
        },
        {
            "name": "Mercer（薪酬数据）",
            "name_en": "Mercer (Compensation Data)",
            "type": "url",
            "url": "https://www.mercer.com/",
            "tags": ["Benchmark", "Consulting"]
        },
        {
            "name": "Willis Towers Watson（薪酬调研）",
            "name_en": "Willis Towers Watson (Compensation Surveys)",
            "type": "url",
            "url": "https://www.wtwco.com/",
            "tags": ["Benchmark", "Global"]
        },
    ],

    # ===== 笔记与协作 =====
    "笔记与协作": [
        {
            "name": "Coda（协作文档）",
            "name_en": "Coda (Collaborative Docs)",
            "type": "url",
            "url": "https://coda.io/",
            "tags": ["Docs", "Collaboration"]
        },
        {
            "name": "Airtable（数据库表格）",
            "name_en": "Airtable (Database Spreadsheet)",
            "type": "url",
            "url": "https://www.airtable.com/",
            "tags": ["Database", "Collaboration"]
        },
        {
            "name": "Monday.com（工作管理）",
            "name_en": "Monday.com (Work Management)",
            "type": "url",
            "url": "https://monday.com/",
            "tags": ["PM", "Collaboration"]
        },
    ],

    # ===== 人才库工具 =====
    "人才库工具": [
        {
            "name": "Lever Nurture（人才培育）",
            "name_en": "Lever Nurture (Talent Nurturing)",
            "type": "url",
            "url": "https://www.lever.co/platform/nurture/",
            "tags": ["CRM", "Nurture"]
        },
        {
            "name": "SmartRecruiters CRM（招聘 CRM）",
            "name_en": "SmartRecruiters CRM",
            "type": "url",
            "url": "https://www.smartrecruiters.com/recruiting-software/crm/",
            "tags": ["CRM", "ATS"]
        },
        {
            "name": "TalentSoft（人才管理）",
            "name_en": "TalentSoft (Talent Management)",
            "type": "url",
            "url": "https://www.cegid.com/en/solutions/talentsoft/",
            "tags": ["TMS", "Europe"]
        },
    ],

    # ===== 候选人沟通自动化 =====
    "候选人沟通自动化": [
        {
            "name": "TextRecruit（短信招聘）",
            "name_en": "TextRecruit (SMS Recruiting)",
            "type": "url",
            "url": "https://www.icims.com/products/talent-cloud-platform/engage/text-engagement/",
            "tags": ["SMS", "Automation"]
        },
        {
            "name": "Grayscale（候选人通信）",
            "name_en": "Grayscale (Candidate Communication)",
            "type": "url",
            "url": "https://www.grayscaleapp.com/",
            "tags": ["SMS", "Platform"]
        },
        {
            "name": "Emissary.ai（对话式 AI）",
            "name_en": "Emissary.ai (Conversational AI)",
            "type": "url",
            "url": "https://emissary.ai/",
            "tags": ["AI", "SMS"]
        },
    ],

    # ===== 远程工作资源 =====
    "远程工作资源": [
        {
            "name": "FlexJobs（远程工作）",
            "name_en": "FlexJobs (Remote Jobs)",
            "type": "url",
            "url": "https://www.flexjobs.com/",
            "tags": ["Remote", "Job Board"]
        },
        {
            "name": "We Work Remotely（远程招聘）",
            "name_en": "We Work Remotely (Remote Recruiting)",
            "type": "url",
            "url": "https://weworkremotely.com/",
            "tags": ["Remote", "Job Board"]
        },
        {
            "name": "Remote OK（远程工作平台）",
            "name_en": "Remote OK (Remote Work Platform)",
            "type": "url",
            "url": "https://remoteok.com/",
            "tags": ["Remote", "Platform"]
        },
    ],

    # ===== YouTube 频道 =====
    "YouTube 频道": [
        {
            "name": "SHRM YouTube（HR 视频）",
            "name_en": "SHRM YouTube (HR Videos)",
            "type": "url",
            "url": "https://www.youtube.com/@ABORDSHRM",
            "tags": ["YouTube", "HR"]
        },
        {
            "name": "Recruiting Brainfood YouTube",
            "name_en": "Recruiting Brainfood YouTube",
            "type": "url",
            "url": "https://www.youtube.com/@RecruitingBrainfood",
            "tags": ["YouTube", "Recruiting"]
        },
        {
            "name": "Josh Bersin YouTube（HR 分析）",
            "name_en": "Josh Bersin YouTube (HR Analytics)",
            "type": "url",
            "url": "https://www.youtube.com/@JoshBersin",
            "tags": ["YouTube", "Expert"]
        },
    ],

    # ===== 书籍/课程 =====
    "书籍/课程": [
        {
            "name": "AIHR（HR 在线学习）",
            "name_en": "AIHR (HR Online Learning)",
            "type": "url",
            "url": "https://www.aihr.com/",
            "tags": ["Learning", "Certification"]
        },
        {
            "name": "Udemy HR Courses（HR 课程）",
            "name_en": "Udemy HR Courses",
            "type": "url",
            "url": "https://www.udemy.com/topic/human-resources/",
            "tags": ["Learning", "Online"]
        },
        {
            "name": "edX HR Programs（HR 项目）",
            "name_en": "edX HR Programs",
            "type": "url",
            "url": "https://www.edx.org/learn/human-resources",
            "tags": ["Learning", "University"]
        },
    ],

    # ===== 入职检查清单 =====
    "入职检查清单": [
        {
            "name": "Trello Onboarding Templates（入职模板）",
            "name_en": "Trello Onboarding Templates",
            "type": "url",
            "url": "https://trello.com/templates/hr-operations",
            "tags": ["Template", "Free"]
        },
        {
            "name": "ClickUp Onboarding（入职清单）",
            "name_en": "ClickUp Onboarding Checklists",
            "type": "url",
            "url": "https://clickup.com/templates/hr",
            "tags": ["Template", "PM"]
        },
        {
            "name": "Asana Onboarding（入职工作流）",
            "name_en": "Asana Onboarding Workflows",
            "type": "url",
            "url": "https://asana.com/templates/employee-onboarding",
            "tags": ["Template", "PM"]
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
