#!/usr/bin/env python3
"""
Add verified resources to tarf.json - Batch 2 (2025 Update)
All resources have been cross-validated through web research.
"""

import json
import re

VERIFIED_RESOURCES = {
    # ==========================================
    # A - 招聘流程与方法论
    # ==========================================

    "面试官培训与招聘培训": [
        {
            "name": "Interview Edge（面试官培训）",
            "name_en": "Interview Edge (Interviewer Training)",
            "type": "url",
            "url": "https://www.interviewedge.com/",
            "tags": ["Training", "Bias"]
        },
        {
            "name": "Applied（无偏见招聘培训）",
            "name_en": "Applied (Bias-Free Hiring Training)",
            "type": "url",
            "url": "https://www.beapplied.com/",
            "tags": ["Training", "DEI", "P"]
        },
        {
            "name": "Culture Plus Consulting（包容性招聘培训）",
            "name_en": "Culture Plus Consulting (Inclusive Hiring)",
            "type": "url",
            "url": "https://cultureplusconsulting.com/",
            "tags": ["Training", "Consulting"]
        },
        {
            "name": "Paradigm（多元化培训）",
            "name_en": "Paradigm (Diversity Training)",
            "type": "url",
            "url": "https://www.paradigmiq.com/",
            "tags": ["DEI", "Training", "P"]
        },
    ],

    "招聘心理学与行为科学": [
        {
            "name": "行为经济学网站（招聘偏见）",
            "name_en": "BehavioralEconomics.com (Hiring Biases)",
            "type": "url",
            "url": "https://www.behavioraleconomics.com/",
            "tags": ["Research", "Psychology"]
        },
        {
            "name": "Daniel Kahneman《思考快与慢》",
            "name_en": "Thinking Fast and Slow - Kahneman",
            "type": "url",
            "url": "https://www.goodreads.com/book/show/11468377-thinking-fast-and-slow",
            "tags": ["Book", "Psychology"]
        },
        {
            "name": "Nudge 理论（助推）",
            "name_en": "Nudge Theory - Thaler & Sunstein",
            "type": "url",
            "url": "https://www.goodreads.com/book/show/3450744-nudge",
            "tags": ["Book", "Behavior"]
        },
    ],

    "校园招聘与实习": [
        {
            "name": "Handshake（校园招聘平台）",
            "name_en": "Handshake (Campus Recruiting Platform)",
            "type": "url",
            "url": "https://joinhandshake.com/",
            "tags": ["Campus", "Platform", "P"]
        },
        {
            "name": "Yello（校园招聘软件）",
            "name_en": "Yello (Campus Recruitment Software)",
            "type": "url",
            "url": "https://yello.co/",
            "tags": ["Campus", "Enterprise", "P"]
        },
        {
            "name": "RippleMatch（AI 校招匹配）",
            "name_en": "RippleMatch (AI Campus Matching)",
            "type": "url",
            "url": "https://ripplematch.com/",
            "tags": ["Campus", "AI", "P"]
        },
        {
            "name": "Symplicity（职业服务平台）",
            "name_en": "Symplicity (Career Services Platform)",
            "type": "url",
            "url": "https://www.symplicity.com/",
            "tags": ["Campus", "Platform", "P"]
        },
        {
            "name": "WayUp（早期职业招聘）",
            "name_en": "WayUp (Early Career Recruiting)",
            "type": "url",
            "url": "https://www.wayup.com/",
            "tags": ["Campus", "Early Career"]
        },
        {
            "name": "Rakuna（校园招聘活动）",
            "name_en": "Rakuna (Campus Recruiting Events)",
            "type": "url",
            "url": "https://www.rakuna.co/",
            "tags": ["Campus", "Events", "P"]
        },
    ],

    "Boolean 搜索指南": [
        {
            "name": "Recruit'em（X-Ray 搜索生成器）",
            "name_en": "Recruit'em (X-Ray Search Generator)",
            "type": "url",
            "url": "https://recruitin.net/",
            "tags": ["Tool", "Free"]
        },
        {
            "name": "Recruitment Geek（LinkedIn X-Ray）",
            "name_en": "Recruitment Geek (LinkedIn X-Ray Tool)",
            "type": "url",
            "url": "https://recruitmentgeek.com/tools/linkedin",
            "tags": ["Tool", "Free"]
        },
        {
            "name": "recruitRyte（AI Boolean 生成器）",
            "name_en": "recruitRyte (AI Boolean Generator)",
            "type": "url",
            "url": "https://recruitryte.com/",
            "tags": ["AI", "Tool"]
        },
        {
            "name": "Leonar（Boolean X-Ray 生成器）",
            "name_en": "Leonar (Boolean X-Ray Generator)",
            "type": "url",
            "url": "https://www.leonar.app/",
            "tags": ["Tool", "Free"]
        },
    ],

    # ==========================================
    # C - 招聘系统与工具
    # ==========================================

    "技术面试平台": [
        {
            "name": "DevSkiller/SkillsPanel（技术评估）",
            "name_en": "DevSkiller/SkillsPanel (Technical Assessment)",
            "type": "url",
            "url": "https://devskiller.com/",
            "tags": ["Tech", "Assessment", "P"]
        },
        {
            "name": "Codility（在线编程测试）",
            "name_en": "Codility (Online Coding Tests)",
            "type": "url",
            "url": "https://www.codility.com/",
            "tags": ["Tech", "Assessment", "P"]
        },
        {
            "name": "HackerEarth（编程评估）",
            "name_en": "HackerEarth (Coding Assessments)",
            "type": "url",
            "url": "https://www.hackerearth.com/",
            "tags": ["Tech", "Assessment", "P"]
        },
        {
            "name": "Coderbyte（技能评估）",
            "name_en": "Coderbyte (Skills Assessment)",
            "type": "url",
            "url": "https://coderbyte.com/",
            "tags": ["Tech", "Assessment", "P"]
        },
        {
            "name": "CoderPad（协作编程面试）",
            "name_en": "CoderPad (Collaborative Coding Interviews)",
            "type": "url",
            "url": "https://coderpad.io/",
            "tags": ["Tech", "Interview", "P"]
        },
    ],

    "JD 写作/招聘文案": [
        {
            "name": "Textio（AI JD 优化）",
            "name_en": "Textio (AI Job Description Optimization)",
            "type": "url",
            "url": "https://textio.com/",
            "tags": ["AI", "Writing", "P"]
        },
        {
            "name": "Gender Decoder（性别偏见检测）",
            "name_en": "Gender Decoder (Bias Detection)",
            "type": "url",
            "url": "http://gender-decoder.katmatfield.com/",
            "tags": ["Tool", "Free", "DEI"]
        },
        {
            "name": "Ongig Text Analyzer（JD 分析）",
            "name_en": "Ongig Text Analyzer (JD Analysis)",
            "type": "url",
            "url": "https://www.ongig.com/",
            "tags": ["Tool", "DEI", "P"]
        },
        {
            "name": "Clovers（招聘偏见检测）",
            "name_en": "Clovers (Hiring Bias Detection)",
            "type": "url",
            "url": "https://www.clovers.ai/",
            "tags": ["AI", "DEI", "P"]
        },
    ],

    # ==========================================
    # G - 雇主品牌与候选人体验
    # ==========================================

    "候选人体验与雇主品牌": [
        {
            "name": "Teamtailor（ATS + 雇主品牌）",
            "name_en": "Teamtailor (ATS + Employer Branding)",
            "type": "url",
            "url": "https://www.teamtailor.com/",
            "tags": ["ATS", "Branding", "P"]
        },
        {
            "name": "CareerSiteCloud（职业网站）",
            "name_en": "CareerSiteCloud (Career Site Software)",
            "type": "url",
            "url": "https://www.careersitecloud.com/",
            "tags": ["Career Site", "P"]
        },
        {
            "name": "CareerArc（社交招聘）",
            "name_en": "CareerArc (Social Recruiting)",
            "type": "url",
            "url": "https://www.careerarc.com/",
            "tags": ["Social", "Branding", "P"]
        },
        {
            "name": "Jobylon（企业招聘平台）",
            "name_en": "Jobylon (Enterprise Recruiting Platform)",
            "type": "url",
            "url": "https://www.jobylon.com/",
            "tags": ["ATS", "Enterprise", "P"]
        },
        {
            "name": "Vouch（员工故事视频）",
            "name_en": "Vouch (Employee Story Videos)",
            "type": "url",
            "url": "https://vouchfor.com/",
            "tags": ["Video", "Branding", "P"]
        },
    ],

    # ==========================================
    # H - 人才管理与规划
    # ==========================================

    "内部流动/人才市场": [
        {
            "name": "Gloat（AI 人才市场）",
            "name_en": "Gloat (AI Talent Marketplace)",
            "type": "url",
            "url": "https://gloat.com/",
            "tags": ["Mobility", "AI", "P"]
        },
        {
            "name": "Eightfold AI（人才智能平台）",
            "name_en": "Eightfold AI (Talent Intelligence Platform)",
            "type": "url",
            "url": "https://eightfold.ai/",
            "tags": ["AI", "Mobility", "P"]
        },
        {
            "name": "Fuel50（人才市场）",
            "name_en": "Fuel50 (Talent Marketplace)",
            "type": "url",
            "url": "https://fuel50.com/",
            "tags": ["Mobility", "Career", "P"]
        },
        {
            "name": "Hitch（内部流动）",
            "name_en": "Hitch (Internal Mobility)",
            "type": "url",
            "url": "https://hitch.works/",
            "tags": ["Mobility", "P"]
        },
        {
            "name": "Degreed（技能发展）",
            "name_en": "Degreed (Skill Development)",
            "type": "url",
            "url": "https://degreed.com/",
            "tags": ["Learning", "Skills", "P"]
        },
    ],

    # ==========================================
    # J - 数据分析与行业洞察
    # ==========================================

    "招聘播客与媒体": [
        {
            "name": "Recruiting Future Podcast",
            "name_en": "Recruiting Future Podcast (Matt Alder)",
            "type": "url",
            "url": "https://recruitingfuture.com/",
            "tags": ["Podcast", "TA"]
        },
        {
            "name": "Talk Talent To Me",
            "name_en": "Talk Talent To Me Podcast",
            "type": "url",
            "url": "https://hired.com/podcast/",
            "tags": ["Podcast", "TA"]
        },
        {
            "name": "HR Happy Hour Network",
            "name_en": "HR Happy Hour Network",
            "type": "url",
            "url": "https://www.hrhappyhour.net/",
            "tags": ["Podcast", "HR"]
        },
        {
            "name": "Talent Acquisition Leaders Podcast",
            "name_en": "Talent Acquisition Leaders Podcast",
            "type": "url",
            "url": "https://www.sagemarkhr.com/podcast",
            "tags": ["Podcast", "TA"]
        },
        {
            "name": "The Resilient Recruiter",
            "name_en": "The Resilient Recruiter Podcast",
            "type": "url",
            "url": "https://recruitinggrowthacdemy.com/podcast/",
            "tags": ["Podcast", "Recruiting"]
        },
        {
            "name": "Recruiting is No Joke（Joel Lalgee）",
            "name_en": "Recruiting is No Joke (Joel Lalgee)",
            "type": "url",
            "url": "https://www.thejoellalgee.com/podcast",
            "tags": ["Podcast", "Recruiting"]
        },
        {
            "name": "DriveThruHR",
            "name_en": "DriveThruHR Podcast",
            "type": "url",
            "url": "https://www.blogtalkradio.com/daborad",
            "tags": ["Podcast", "HR"]
        },
    ],

    "招聘社区": [
        {
            "name": "People Geeks（CultureAmp 社区）",
            "name_en": "People Geeks (CultureAmp Community)",
            "type": "url",
            "url": "https://www.cultureamp.com/community",
            "tags": ["Community", "Slack"]
        },
        {
            "name": "Resources for Humans",
            "name_en": "Resources for Humans (Slack Community)",
            "type": "url",
            "url": "https://resourcesforhumans.com/",
            "tags": ["Community", "Slack"]
        },
        {
            "name": "The Talent Community",
            "name_en": "The Talent Community (Slack)",
            "type": "url",
            "url": "https://thetalentcommunity.com/",
            "tags": ["Community", "Slack"]
        },
        {
            "name": "PeoplePeople（HR Chief）",
            "name_en": "PeoplePeople (HR Chief Slack)",
            "type": "url",
            "url": "https://www.hrchief.com/",
            "tags": ["Community", "Slack"]
        },
        {
            "name": "Hacking HR",
            "name_en": "Hacking HR Community",
            "type": "url",
            "url": "https://www.hackinghr.io/",
            "tags": ["Community", "HR Tech"]
        },
        {
            "name": "HRHotSeat",
            "name_en": "HRHotSeat Community",
            "type": "url",
            "url": "https://hrhotseat.com/",
            "tags": ["Community", "HR"]
        },
    ],

    "知名公司招聘实践": [
        {
            "name": "Google 招聘实践分析",
            "name_en": "Google Hiring Practices Analysis",
            "type": "url",
            "url": "https://rework.withgoogle.com/guides/hiring/",
            "tags": ["Case Study", "Google"]
        },
        {
            "name": "Netflix 人才管理案例",
            "name_en": "Netflix Talent Management Case Study",
            "type": "url",
            "url": "https://jobs.netflix.com/culture",
            "tags": ["Case Study", "Netflix"]
        },
        {
            "name": "Amazon 招聘方法（Dr. John Sullivan）",
            "name_en": "Amazon Recruiting Case Study",
            "type": "url",
            "url": "https://drjohnsullivan.com/articles/amazon-recruiting-case-study-part-1/",
            "tags": ["Case Study", "Amazon"]
        },
        {
            "name": "Zappos 文化招聘",
            "name_en": "Zappos Culture Hiring",
            "type": "url",
            "url": "https://www.zappos.com/about/what-we-live-by",
            "tags": ["Case Study", "Culture"]
        },
    ],

    "People Analytics 平台": [
        {
            "name": "Visier（人员分析平台）",
            "name_en": "Visier (People Analytics Platform)",
            "type": "url",
            "url": "https://www.visier.com/",
            "tags": ["Analytics", "Enterprise", "P"]
        },
        {
            "name": "ChartHop（组织分析）",
            "name_en": "ChartHop (Org Analytics)",
            "type": "url",
            "url": "https://www.charthop.com/",
            "tags": ["Analytics", "Org", "P"]
        },
        {
            "name": "Crunchr（人员分析）",
            "name_en": "Crunchr (People Analytics)",
            "type": "url",
            "url": "https://www.crunchr.com/",
            "tags": ["Analytics", "P"]
        },
        {
            "name": "OrgVue（组织设计）",
            "name_en": "OrgVue (Org Design & Analytics)",
            "type": "url",
            "url": "https://www.orgvue.com/",
            "tags": ["Analytics", "Org Design", "P"]
        },
        {
            "name": "One Model（人员分析）",
            "name_en": "One Model (People Analytics)",
            "type": "url",
            "url": "https://www.onemodel.co/",
            "tags": ["Analytics", "P"]
        },
    ],

    "专业认证": [
        {
            "name": "HRCI（HR 认证机构）",
            "name_en": "HRCI (HR Certification Institute)",
            "type": "url",
            "url": "https://www.hrci.org/",
            "tags": ["Certification", "HR"]
        },
        {
            "name": "SHRM 认证（SHRM-CP/SCP）",
            "name_en": "SHRM Certification (SHRM-CP/SCP)",
            "type": "url",
            "url": "https://www.shrm.org/certification",
            "tags": ["Certification", "SHRM"]
        },
        {
            "name": "AIHR（HR 学院）",
            "name_en": "AIHR (Academy to Innovate HR)",
            "type": "url",
            "url": "https://www.aihr.com/",
            "tags": ["Certification", "Learning"]
        },
        {
            "name": "ATD（人才发展协会）",
            "name_en": "ATD (Association for Talent Development)",
            "type": "url",
            "url": "https://www.td.org/",
            "tags": ["Certification", "L&D"]
        },
        {
            "name": "TMI（人才管理学院）",
            "name_en": "TMI (Talent Management Institute)",
            "type": "url",
            "url": "https://www.tmi.org/",
            "tags": ["Certification", "TM"]
        },
    ],

    "招聘行业研究与报告": [
        {
            "name": "Josh Bersin Research",
            "name_en": "Josh Bersin Research",
            "type": "url",
            "url": "https://joshbersin.com/research/",
            "tags": ["Research", "HR Tech"]
        },
        {
            "name": "Mercer Workforce Research",
            "name_en": "Mercer Workforce Research",
            "type": "url",
            "url": "https://www.mercer.com/insights/",
            "tags": ["Research", "Consulting"]
        },
        {
            "name": "Korn Ferry Insights",
            "name_en": "Korn Ferry Insights",
            "type": "url",
            "url": "https://www.kornferry.com/insights",
            "tags": ["Research", "Executive"]
        },
        {
            "name": "LinkedIn Economic Graph",
            "name_en": "LinkedIn Economic Graph",
            "type": "url",
            "url": "https://economicgraph.linkedin.com/",
            "tags": ["Research", "Data"]
        },
        {
            "name": "World Economic Forum Future of Jobs",
            "name_en": "WEF Future of Jobs Report",
            "type": "url",
            "url": "https://www.weforum.org/reports/the-future-of-jobs-report-2025",
            "tags": ["Research", "Trends"]
        },
    ],

    # ==========================================
    # 补充更多薄弱分类
    # ==========================================

    "招聘行业活动与会议": [
        {
            "name": "RecFest（招聘节）",
            "name_en": "RecFest (Recruitment Festival)",
            "type": "url",
            "url": "https://www.recfest.com/",
            "tags": ["Conference", "Recruiting"]
        },
        {
            "name": "Talent42（技术招聘大会）",
            "name_en": "Talent42 (Tech Recruiting Conference)",
            "type": "url",
            "url": "https://www.talent42.com/",
            "tags": ["Conference", "Tech"]
        },
        {
            "name": "LinkedIn Talent Connect",
            "name_en": "LinkedIn Talent Connect",
            "type": "url",
            "url": "https://business.linkedin.com/talent-solutions/events",
            "tags": ["Conference", "LinkedIn"]
        },
        {
            "name": "Hiring Success（SmartRecruiters）",
            "name_en": "Hiring Success Conference",
            "type": "url",
            "url": "https://www.smartrecruiters.com/hiring-success/",
            "tags": ["Conference", "TA"]
        },
    ],

    "招聘视觉与品牌设计": [
        {
            "name": "Canva（设计工具）",
            "name_en": "Canva (Design Tool)",
            "type": "url",
            "url": "https://www.canva.com/",
            "tags": ["Design", "Tool"]
        },
        {
            "name": "Figma（协作设计）",
            "name_en": "Figma (Collaborative Design)",
            "type": "url",
            "url": "https://www.figma.com/",
            "tags": ["Design", "Tool"]
        },
        {
            "name": "Loom（视频消息）",
            "name_en": "Loom (Video Messaging)",
            "type": "url",
            "url": "https://www.loom.com/",
            "tags": ["Video", "Tool"]
        },
        {
            "name": "Vidyard（视频营销）",
            "name_en": "Vidyard (Video Marketing)",
            "type": "url",
            "url": "https://www.vidyard.com/",
            "tags": ["Video", "Marketing", "P"]
        },
    ],

    "灵活用工与零工经济": [
        {
            "name": "Upwork（自由职业平台）",
            "name_en": "Upwork (Freelance Platform)",
            "type": "url",
            "url": "https://www.upwork.com/",
            "tags": ["Gig", "Freelance"]
        },
        {
            "name": "Fiverr（服务市场）",
            "name_en": "Fiverr (Services Marketplace)",
            "type": "url",
            "url": "https://www.fiverr.com/",
            "tags": ["Gig", "Freelance"]
        },
        {
            "name": "Toptal（顶级自由职业者）",
            "name_en": "Toptal (Top Freelance Talent)",
            "type": "url",
            "url": "https://www.toptal.com/",
            "tags": ["Freelance", "Tech", "P"]
        },
        {
            "name": "Flexjobs（远程/灵活工作）",
            "name_en": "FlexJobs (Remote/Flexible Work)",
            "type": "url",
            "url": "https://www.flexjobs.com/",
            "tags": ["Remote", "Flexible", "P"]
        },
    ],

    "职位发布与招聘营销": [
        {
            "name": "Indeed（招聘广告）",
            "name_en": "Indeed (Job Advertising)",
            "type": "url",
            "url": "https://www.indeed.com/hire",
            "tags": ["Job Board", "Ads", "P"]
        },
        {
            "name": "ZipRecruiter（AI 匹配）",
            "name_en": "ZipRecruiter (AI Job Matching)",
            "type": "url",
            "url": "https://www.ziprecruiter.com/",
            "tags": ["Job Board", "AI", "P"]
        },
        {
            "name": "Glassdoor for Employers",
            "name_en": "Glassdoor for Employers",
            "type": "url",
            "url": "https://www.glassdoor.com/employers/",
            "tags": ["Employer Brand", "Reviews", "P"]
        },
        {
            "name": "LinkedIn Jobs（招聘广告）",
            "name_en": "LinkedIn Jobs (Job Advertising)",
            "type": "url",
            "url": "https://business.linkedin.com/talent-solutions/post-jobs",
            "tags": ["Job Board", "LinkedIn", "P"]
        },
    ],

    "人才市场情报与竞争分析": [
        {
            "name": "Revelio Labs（劳动力数据）",
            "name_en": "Revelio Labs (Workforce Data)",
            "type": "url",
            "url": "https://www.reveliolabs.com/",
            "tags": ["Data", "Intelligence", "P"]
        },
        {
            "name": "Lightcast（劳动力市场分析）",
            "name_en": "Lightcast (Labor Market Analytics)",
            "type": "url",
            "url": "https://lightcast.io/",
            "tags": ["Data", "Analytics", "P"]
        },
        {
            "name": "Horsefly Analytics（人才情报）",
            "name_en": "Horsefly Analytics (Talent Intelligence)",
            "type": "url",
            "url": "https://www.yourhorsefly.com/",
            "tags": ["Intelligence", "Analytics", "P"]
        },
        {
            "name": "TalentNeuron（Gartner 人才情报）",
            "name_en": "TalentNeuron (Gartner Talent Intelligence)",
            "type": "url",
            "url": "https://www.gartner.com/en/human-resources/research/talentneuron",
            "tags": ["Intelligence", "Gartner", "P"]
        },
    ],

    "ATS 与招聘协作": [
        {
            "name": "Greenhouse（企业 ATS）",
            "name_en": "Greenhouse (Enterprise ATS)",
            "type": "url",
            "url": "https://www.greenhouse.com/",
            "tags": ["ATS", "Enterprise", "P"]
        },
        {
            "name": "Lever（招聘 CRM + ATS）",
            "name_en": "Lever (Recruiting CRM + ATS)",
            "type": "url",
            "url": "https://www.lever.co/",
            "tags": ["ATS", "CRM", "P"]
        },
        {
            "name": "Ashby（现代 ATS）",
            "name_en": "Ashby (Modern ATS)",
            "type": "url",
            "url": "https://www.ashbyhq.com/",
            "tags": ["ATS", "Analytics", "P"]
        },
        {
            "name": "Workable（SMB ATS）",
            "name_en": "Workable (SMB ATS)",
            "type": "url",
            "url": "https://www.workable.com/",
            "tags": ["ATS", "SMB", "P"]
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
    not_found_categories = []

    for target_name, resources in VERIFIED_RESOURCES.items():
        parent = find_node_by_name(data, target_name)
        if parent is None:
            print(f"❌ Category not found: {target_name}")
            not_found_categories.append(target_name)
            error_count += len(resources)
            continue

        if 'children' not in parent:
            parent['children'] = []

        existing_urls = {child.get('url') for child in parent.get('children', [])}
        existing_names = {child.get('name') for child in parent.get('children', [])}

        for resource in resources:
            valid, msg = validate_resource(resource)
            if not valid:
                print(f"❌ Validation failed: {resource.get('name', 'unknown')} - {msg}")
                error_count += 1
                continue

            if resource.get('url') in existing_urls:
                print(f"⏭️  Skipped (URL exists): {resource['name_en']}")
                skipped_count += 1
                continue

            if resource.get('name') in existing_names:
                print(f"⏭️  Skipped (name exists): {resource['name_en']}")
                skipped_count += 1
                continue

            parent['children'].append(resource)
            added_count += 1
            print(f"✅ Added: {resource['name_en']} -> {target_name}")

    with open('docs/tarf.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  ✅ Added: {added_count}")
    print(f"  ⏭️  Skipped: {skipped_count}")
    print(f"  ❌ Errors: {error_count}")
    if not_found_categories:
        print(f"\n  Categories not found ({len(not_found_categories)}):")
        for cat in not_found_categories:
            print(f"    - {cat}")
    print(f"{'='*60}")


if __name__ == "__main__":
    add_resources()
