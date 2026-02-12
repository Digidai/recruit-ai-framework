#!/usr/bin/env python3
"""
Add verified resources to tarf.json - 2025 Update
All resources have been cross-validated through web research.
"""

import json
import re

VERIFIED_RESOURCES = {
    # ==========================================
    # D - AI 招聘技术
    # ==========================================

    "AI 视频面试": [
        {
            "name": "Spark Hire（一站式视频面试）",
            "name_en": "Spark Hire (One-Way & Live Video)",
            "type": "url",
            "url": "https://www.sparkhire.com/",
            "tags": ["Video", "SMB", "P"]
        },
        {
            "name": "Willo（异步视频面试）",
            "name_en": "Willo (Async Video Interviews)",
            "type": "url",
            "url": "https://www.willo.video/",
            "tags": ["Video", "Remote", "P"]
        },
        {
            "name": "Hireflix（单向视频面试）",
            "name_en": "Hireflix (One-Way Video)",
            "type": "url",
            "url": "https://www.hireflix.com/",
            "tags": ["Video", "Simple", "P"]
        },
        {
            "name": "Hirevire（AI 视频筛选）",
            "name_en": "Hirevire (AI Video Screening)",
            "type": "url",
            "url": "https://hirevire.com/",
            "tags": ["AI", "Video", "P"]
        },
        {
            "name": "Metaview（AI 面试助手）",
            "name_en": "Metaview (AI Interview Assistant)",
            "type": "url",
            "url": "https://www.metaview.ai/",
            "tags": ["AI", "Notes", "P"]
        },
        {
            "name": "Jobma（全球视频面试）",
            "name_en": "Jobma (Global Video Interviewing)",
            "type": "url",
            "url": "https://www.jobma.com/",
            "tags": ["Video", "Global", "P"]
        },
    ],

    "AI 面试助手": [
        {
            "name": "BarRaiser（AI 面试协作）",
            "name_en": "BarRaiser (AI Interview Copilot)",
            "type": "url",
            "url": "https://www.barraiser.com/",
            "tags": ["AI", "Interview", "P"]
        },
        {
            "name": "BrightHire（面试智能）",
            "name_en": "BrightHire (Interview Intelligence)",
            "type": "url",
            "url": "https://brighthire.com/",
            "tags": ["AI", "Analytics", "P"]
        },
        {
            "name": "Pillar（面试记录分析）",
            "name_en": "Pillar (Interview Recording & Analysis)",
            "type": "url",
            "url": "https://www.pillar.hr/",
            "tags": ["AI", "Recording", "P"]
        },
    ],

    "游戏化评估": [
        {
            "name": "Arctic Shores（游戏化心理测评）",
            "name_en": "Arctic Shores (Gamified Psychometrics)",
            "type": "url",
            "url": "https://www.arcticshores.com/",
            "tags": ["Gamification", "Assessment", "P"]
        },
        {
            "name": "Pymetrics/Harver（神经科学游戏）",
            "name_en": "Pymetrics/Harver (Neuroscience Games)",
            "type": "url",
            "url": "https://www.harver.com/",
            "tags": ["AI", "Gamification", "P"]
        },
        {
            "name": "Knack（游戏化人才识别）",
            "name_en": "Knack (Gamified Talent Discovery)",
            "type": "url",
            "url": "https://www.knack.it/",
            "tags": ["Gamification", "AI", "P"]
        },
        {
            "name": "Owiwi（软技能游戏测评）",
            "name_en": "Owiwi (Gamified Soft Skills)",
            "type": "url",
            "url": "https://owiwi.co.uk/",
            "tags": ["Gamification", "Soft Skills", "P"]
        },
        {
            "name": "Criteria Corp（AI 测评平台）",
            "name_en": "Criteria Corp (AI Assessment Platform)",
            "type": "url",
            "url": "https://www.criteriacorp.com/",
            "tags": ["Assessment", "AI", "P"]
        },
    ],

    "AI 简历解析/筛选": [
        {
            "name": "Textkernel（多语言简历解析）",
            "name_en": "Textkernel (Multilingual Resume Parsing)",
            "type": "url",
            "url": "https://www.textkernel.com/",
            "tags": ["AI", "Parsing", "P"]
        },
        {
            "name": "Daxtra（简历解析 API）",
            "name_en": "Daxtra (Resume Parsing API)",
            "type": "url",
            "url": "https://www.daxtra.com/",
            "tags": ["API", "Parsing", "P"]
        },
        {
            "name": "HireAbility（简历数据提取）",
            "name_en": "HireAbility (Resume Data Extraction)",
            "type": "url",
            "url": "https://www.hireability.com/",
            "tags": ["API", "Parsing", "P"]
        },
        {
            "name": "Affinda（AI 文档解析）",
            "name_en": "Affinda (AI Document Parsing)",
            "type": "url",
            "url": "https://www.affinda.com/",
            "tags": ["AI", "Parsing", "P"]
        },
    ],

    # ==========================================
    # E - 合规与法律
    # ==========================================

    "Offer、背调与入职": [
        {
            "name": "Checkr（AI 背景调查）",
            "name_en": "Checkr (AI Background Checks)",
            "type": "url",
            "url": "https://checkr.com/",
            "tags": ["Background Check", "AI", "P"]
        },
        {
            "name": "Sterling（全球背调服务）",
            "name_en": "Sterling (Global Background Screening)",
            "type": "url",
            "url": "https://www.sterlingcheck.com/",
            "tags": ["Background Check", "Global", "P"]
        },
        {
            "name": "GoodHire（中小企业背调）",
            "name_en": "GoodHire (SMB Background Checks)",
            "type": "url",
            "url": "https://www.goodhire.com/",
            "tags": ["Background Check", "SMB", "P"]
        },
        {
            "name": "HireRight（企业背调）",
            "name_en": "HireRight (Enterprise Screening)",
            "type": "url",
            "url": "https://www.hireright.com/",
            "tags": ["Background Check", "Enterprise", "P"]
        },
        {
            "name": "Certn（快速背调）",
            "name_en": "Certn (Fast Background Checks)",
            "type": "url",
            "url": "https://certn.co/",
            "tags": ["Background Check", "Fast", "P"]
        },
        {
            "name": "VerifiedFirst（ATS 集成背调）",
            "name_en": "VerifiedFirst (ATS-Integrated Screening)",
            "type": "url",
            "url": "https://www.verifiedfirst.com/",
            "tags": ["Background Check", "Integration", "P"]
        },
    ],

    "招聘数据隐私与合规": [
        {
            "name": "OneTrust（隐私管理平台）",
            "name_en": "OneTrust (Privacy Management Platform)",
            "type": "url",
            "url": "https://www.onetrust.com/",
            "tags": ["Privacy", "GDPR", "P"]
        },
        {
            "name": "TrustArc（隐私合规）",
            "name_en": "TrustArc (Privacy Compliance)",
            "type": "url",
            "url": "https://trustarc.com/",
            "tags": ["Privacy", "CCPA", "P"]
        },
        {
            "name": "Osano（Cookie 与隐私合规）",
            "name_en": "Osano (Cookie & Privacy Compliance)",
            "type": "url",
            "url": "https://www.osano.com/",
            "tags": ["Privacy", "Consent", "P"]
        },
        {
            "name": "Didomi（同意管理平台）",
            "name_en": "Didomi (Consent Management Platform)",
            "type": "url",
            "url": "https://www.didomi.io/",
            "tags": ["Privacy", "Consent", "P"]
        },
    ],

    "招聘反欺诈与验证": [
        {
            "name": "Truework（收入验证）",
            "name_en": "Truework (Income Verification)",
            "type": "url",
            "url": "https://www.truework.com/",
            "tags": ["Verification", "Income", "P"]
        },
        {
            "name": "Onfido（身份验证 AI）",
            "name_en": "Onfido (AI Identity Verification)",
            "type": "url",
            "url": "https://onfido.com/",
            "tags": ["Identity", "AI", "P"]
        },
        {
            "name": "Jumio（身份验证平台）",
            "name_en": "Jumio (Identity Verification Platform)",
            "type": "url",
            "url": "https://www.jumio.com/",
            "tags": ["Identity", "AI", "P"]
        },
        {
            "name": "Persona（身份验证基础设施）",
            "name_en": "Persona (Identity Infrastructure)",
            "type": "url",
            "url": "https://withpersona.com/",
            "tags": ["Identity", "Platform", "P"]
        },
        {
            "name": "National Student Clearinghouse（学历验证）",
            "name_en": "National Student Clearinghouse (Education Verification)",
            "type": "url",
            "url": "https://www.studentclearinghouse.org/",
            "tags": ["Education", "Verification"]
        },
    ],

    # ==========================================
    # F - 多元化与包容性招聘
    # ==========================================

    "无障碍招聘": [
        {
            "name": "abilityJOBS（残障人士招聘平台）",
            "name_en": "abilityJOBS (Disability Job Board)",
            "type": "url",
            "url": "https://abilityjobs.com/",
            "tags": ["Disability", "Job Board"]
        },
        {
            "name": "Disability Solutions（残障人才服务）",
            "name_en": "Disability Solutions (Disability Talent Services)",
            "type": "url",
            "url": "https://www.disabilitytalent.org/",
            "tags": ["Disability", "Consulting"]
        },
        {
            "name": "EARN（雇主无障碍资源网络）",
            "name_en": "EARN (Employer Assistance Resource Network)",
            "type": "url",
            "url": "https://askearn.org/",
            "tags": ["Disability", "Resource"]
        },
        {
            "name": "JAN（工作场所适配网络）",
            "name_en": "JAN (Job Accommodation Network)",
            "type": "url",
            "url": "https://askjan.org/",
            "tags": ["Disability", "Accommodation"]
        },
        {
            "name": "TalentWorks PEAT（无障碍招聘技术）",
            "name_en": "TalentWorks PEAT (Accessible Recruiting Tech)",
            "type": "url",
            "url": "https://www.peatworks.org/",
            "tags": ["Disability", "Technology"]
        },
    ],

    # ==========================================
    # G - 雇主品牌与候选人体验
    # ==========================================

    "远程面试与虚拟招聘": [
        {
            "name": "vFairs（虚拟招聘会平台）",
            "name_en": "vFairs (Virtual Career Fair Platform)",
            "type": "url",
            "url": "https://www.vfairs.com/",
            "tags": ["Virtual", "Career Fair", "P"]
        },
        {
            "name": "Premier Virtual（虚拟招聘套件）",
            "name_en": "Premier Virtual (Virtual Recruitment Suite)",
            "type": "url",
            "url": "https://premiervirtual.com/",
            "tags": ["Virtual", "Events", "P"]
        },
        {
            "name": "Career Fair Plus（混合招聘活动）",
            "name_en": "Career Fair Plus (Hybrid Recruiting Events)",
            "type": "url",
            "url": "https://www.careerfairplus.com/",
            "tags": ["Virtual", "Hybrid", "P"]
        },
        {
            "name": "Remo（虚拟招聘空间）",
            "name_en": "Remo (Virtual Event Space)",
            "type": "url",
            "url": "https://remo.co/",
            "tags": ["Virtual", "Networking", "P"]
        },
        {
            "name": "Brazen（虚拟招聘会）",
            "name_en": "Brazen (Virtual Career Fairs)",
            "type": "url",
            "url": "https://www.brazen.com/",
            "tags": ["Virtual", "Career Fair", "P"]
        },
    ],

    # ==========================================
    # H - 人才管理与规划
    # ==========================================

    "人才库工具": [
        {
            "name": "Beamery（AI 人才 CRM）",
            "name_en": "Beamery (AI Talent CRM)",
            "type": "url",
            "url": "https://beamery.com/",
            "tags": ["CRM", "AI", "P"]
        },
        {
            "name": "Phenom（人才体验平台）",
            "name_en": "Phenom (Talent Experience Platform)",
            "type": "url",
            "url": "https://www.phenom.com/",
            "tags": ["CRM", "AI", "P"]
        },
        {
            "name": "Avature（企业招聘 CRM）",
            "name_en": "Avature (Enterprise Recruiting CRM)",
            "type": "url",
            "url": "https://www.avature.net/",
            "tags": ["CRM", "Enterprise", "P"]
        },
        {
            "name": "Gem（人才关系管理）",
            "name_en": "Gem (Talent Engagement Platform)",
            "type": "url",
            "url": "https://www.gem.com/",
            "tags": ["CRM", "Outreach", "P"]
        },
    ],

    "员工推荐系统": [
        {
            "name": "Teamable（员工网络推荐）",
            "name_en": "Teamable (Employee Network Referrals)",
            "type": "url",
            "url": "https://www.teamable.com/",
            "tags": ["Referral", "Network", "P"]
        },
        {
            "name": "Boon（敏捷推荐平台）",
            "name_en": "Boon (Agile Referral Platform)",
            "type": "url",
            "url": "https://www.goboon.co/",
            "tags": ["Referral", "AI", "P"]
        },
        {
            "name": "ERIN（员工推荐应用）",
            "name_en": "ERIN (Employee Referral App)",
            "type": "url",
            "url": "https://erinapp.com/",
            "tags": ["Referral", "Mobile", "P"]
        },
        {
            "name": "RolePoint（推荐自动化）",
            "name_en": "RolePoint (Referral Automation)",
            "type": "url",
            "url": "https://www.rolepoint.com/",
            "tags": ["Referral", "Automation", "P"]
        },
        {
            "name": "EmployeeReferrals.com（推荐管理）",
            "name_en": "EmployeeReferrals.com (Referral Management)",
            "type": "url",
            "url": "https://www.employeereferrals.com/",
            "tags": ["Referral", "Platform", "P"]
        },
    ],

    # ==========================================
    # C - 招聘系统与工具
    # ==========================================

    "面试排期工具": [
        {
            "name": "GoodTime（智能面试排程）",
            "name_en": "GoodTime (Intelligent Interview Scheduling)",
            "type": "url",
            "url": "https://www.goodtime.io/",
            "tags": ["Scheduling", "AI", "P"]
        },
        {
            "name": "Calendly（日程自动化）",
            "name_en": "Calendly (Scheduling Automation)",
            "type": "url",
            "url": "https://calendly.com/",
            "tags": ["Scheduling", "Tool", "P"]
        },
        {
            "name": "ModernLoop（招聘排程）",
            "name_en": "ModernLoop (Recruiting Scheduling)",
            "type": "url",
            "url": "https://www.modernloop.com/",
            "tags": ["Scheduling", "Recruiting", "P"]
        },
        {
            "name": "Prelude（协调式排程）",
            "name_en": "Prelude (Coordinated Scheduling)",
            "type": "url",
            "url": "https://www.prelude.co/",
            "tags": ["Scheduling", "Coordination", "P"]
        },
    ],

    "入职软件": [
        {
            "name": "Rippling（统一 HR/IT 入职）",
            "name_en": "Rippling (Unified HR/IT Onboarding)",
            "type": "url",
            "url": "https://www.rippling.com/",
            "tags": ["Onboarding", "HRIS", "P"]
        },
        {
            "name": "BambooHR（SMB 入职）",
            "name_en": "BambooHR (SMB Onboarding)",
            "type": "url",
            "url": "https://www.bamboohr.com/",
            "tags": ["Onboarding", "HRIS", "P"]
        },
        {
            "name": "Enboarder（体验驱动入职）",
            "name_en": "Enboarder (Experience-Driven Onboarding)",
            "type": "url",
            "url": "https://enboarder.com/",
            "tags": ["Onboarding", "Experience", "P"]
        },
        {
            "name": "WorkBright（远程入职）",
            "name_en": "WorkBright (Remote Onboarding)",
            "type": "url",
            "url": "https://www.workbright.com/",
            "tags": ["Onboarding", "Remote", "P"]
        },
        {
            "name": "ClearCompany（入职合规）",
            "name_en": "ClearCompany (Compliant Onboarding)",
            "type": "url",
            "url": "https://www.clearcompany.com/",
            "tags": ["Onboarding", "Compliance", "P"]
        },
    ],

    # ==========================================
    # I - 全球招聘与特殊场景
    # ==========================================

    "亚太地区（APAC）": [
        {
            "name": "JobStreet（东南亚招聘）",
            "name_en": "JobStreet (Southeast Asia Recruiting)",
            "type": "url",
            "url": "https://www.jobstreet.com/",
            "tags": ["APAC", "Job Board", "R"]
        },
        {
            "name": "JobsDB（港泰招聘）",
            "name_en": "JobsDB (Hong Kong & Thailand)",
            "type": "url",
            "url": "https://www.jobsdb.com/",
            "tags": ["APAC", "Job Board", "R"]
        },
        {
            "name": "Glints（东南亚人才）",
            "name_en": "Glints (Southeast Asia Talent)",
            "type": "url",
            "url": "https://glints.com/",
            "tags": ["APAC", "Tech", "R"]
        },
        {
            "name": "FastJobs（东南亚蓝领）",
            "name_en": "FastJobs (Southeast Asia Hourly)",
            "type": "url",
            "url": "https://www.fastjobs.sg/",
            "tags": ["APAC", "Hourly", "R"]
        },
        {
            "name": "Bossjob（东南亚直聊招聘）",
            "name_en": "Bossjob (SE Asia Direct Chat Hiring)",
            "type": "url",
            "url": "https://www.bossjob.com/",
            "tags": ["APAC", "Chat", "R"]
        },
        {
            "name": "Seek（澳洲/新西兰）",
            "name_en": "Seek (Australia & New Zealand)",
            "type": "url",
            "url": "https://www.seek.com.au/",
            "tags": ["APAC", "Job Board", "R"]
        },
    ],

    "拉丁美洲（LATAM）": [
        {
            "name": "Computrabajo（拉美招聘）",
            "name_en": "Computrabajo (Latin America Recruiting)",
            "type": "url",
            "url": "https://www.computrabajo.com/",
            "tags": ["LATAM", "Job Board", "R"]
        },
        {
            "name": "Bumeran（阿根廷/秘鲁招聘）",
            "name_en": "Bumeran (Argentina & Peru Jobs)",
            "type": "url",
            "url": "https://www.bumeran.com.ar/",
            "tags": ["LATAM", "Job Board", "R"]
        },
        {
            "name": "OCC Mundial（墨西哥招聘）",
            "name_en": "OCC Mundial (Mexico Jobs)",
            "type": "url",
            "url": "https://www.occ.com.mx/",
            "tags": ["LATAM", "Mexico", "R"]
        },
        {
            "name": "Vagas（巴西招聘）",
            "name_en": "Vagas (Brazil Jobs)",
            "type": "url",
            "url": "https://www.vagas.com.br/",
            "tags": ["LATAM", "Brazil", "R"]
        },
        {
            "name": "InfoJobs BR（巴西招聘）",
            "name_en": "InfoJobs Brazil (Brazil Jobs)",
            "type": "url",
            "url": "https://www.infojobs.com.br/",
            "tags": ["LATAM", "Brazil", "R"]
        },
        {
            "name": "HireLatam（拉美远程人才）",
            "name_en": "HireLatam (Remote LATAM Talent)",
            "type": "url",
            "url": "https://hirelatam.com/",
            "tags": ["LATAM", "Remote", "P"]
        },
        {
            "name": "Near（拉美人才招聘）",
            "name_en": "Near (LATAM Talent Recruitment)",
            "type": "url",
            "url": "https://www.hirewithnear.com/",
            "tags": ["LATAM", "Remote", "P"]
        },
    ],

    # ==========================================
    # J - 数据分析与行业洞察
    # ==========================================

    "学习资源与研究": [
        {
            "name": "SHRM（人力资源管理协会）",
            "name_en": "SHRM (Society for Human Resource Management)",
            "type": "url",
            "url": "https://www.shrm.org/",
            "tags": ["Association", "Learning"]
        },
        {
            "name": "CIPD（英国人力资源协会）",
            "name_en": "CIPD (Chartered Institute of Personnel)",
            "type": "url",
            "url": "https://www.cipd.org/",
            "tags": ["Association", "UK"]
        },
        {
            "name": "ERE（招聘情报）",
            "name_en": "ERE (Recruiting Intelligence)",
            "type": "url",
            "url": "https://www.ere.net/",
            "tags": ["Media", "Research"]
        },
        {
            "name": "Talent Board（候选人体验研究）",
            "name_en": "Talent Board (Candidate Experience Research)",
            "type": "url",
            "url": "https://www.thetalentboard.org/",
            "tags": ["Research", "CX"]
        },
        {
            "name": "Josh Bersin Academy（HR 学习）",
            "name_en": "Josh Bersin Academy (HR Learning)",
            "type": "url",
            "url": "https://joshbersin.com/",
            "tags": ["Learning", "Research"]
        },
    ],

    "招聘行业活动与会议": [
        {
            "name": "HR Technology Conference",
            "name_en": "HR Technology Conference",
            "type": "url",
            "url": "https://www.hrtechnologyconference.com/",
            "tags": ["Conference", "HR Tech"]
        },
        {
            "name": "UNLEASH World",
            "name_en": "UNLEASH World",
            "type": "url",
            "url": "https://www.unleash.ai/",
            "tags": ["Conference", "Global"]
        },
        {
            "name": "Transform（未来工作峰会）",
            "name_en": "Transform (Future of Work Summit)",
            "type": "url",
            "url": "https://www.transformconference.co/",
            "tags": ["Conference", "Future of Work"]
        },
        {
            "name": "RecFest（招聘节）",
            "name_en": "RecFest (Recruitment Festival)",
            "type": "url",
            "url": "https://www.recfest.com/",
            "tags": ["Conference", "Recruiting"]
        },
        {
            "name": "Talent Connect（LinkedIn 年会）",
            "name_en": "Talent Connect (LinkedIn Conference)",
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

    "招聘行业研究与报告": [
        {
            "name": "LinkedIn Talent Insights",
            "name_en": "LinkedIn Talent Insights",
            "type": "url",
            "url": "https://business.linkedin.com/talent-solutions/talent-insights",
            "tags": ["Research", "Data", "P"]
        },
        {
            "name": "Gartner HR Research",
            "name_en": "Gartner HR Research",
            "type": "url",
            "url": "https://www.gartner.com/en/human-resources",
            "tags": ["Research", "Analyst"]
        },
        {
            "name": "Deloitte Human Capital Trends",
            "name_en": "Deloitte Human Capital Trends",
            "type": "url",
            "url": "https://www2.deloitte.com/us/en/insights/focus/human-capital-trends.html",
            "tags": ["Research", "Trends"]
        },
        {
            "name": "McKinsey People & Organization",
            "name_en": "McKinsey People & Organization",
            "type": "url",
            "url": "https://www.mckinsey.com/capabilities/people-and-organizational-performance",
            "tags": ["Research", "Consulting"]
        },
        {
            "name": "Aptitude Research",
            "name_en": "Aptitude Research",
            "type": "url",
            "url": "https://www.aptituderesearch.com/",
            "tags": ["Research", "HR Tech"]
        },
    ],

    # ==========================================
    # 技术社区招聘
    # ==========================================

    "技术社区招聘": [
        {
            "name": "Stack Overflow Jobs",
            "name_en": "Stack Overflow Jobs",
            "type": "url",
            "url": "https://stackoverflow.com/jobs",
            "tags": ["Tech", "Developer", "R"]
        },
        {
            "name": "GitHub Jobs（已停用，用 LinkedIn）",
            "name_en": "GitHub Jobs (Archived, Use LinkedIn)",
            "type": "url",
            "url": "https://www.linkedin.com/company/github/jobs/",
            "tags": ["Tech", "Developer", "R"]
        },
        {
            "name": "AngelList/Wellfound（创业公司招聘）",
            "name_en": "AngelList/Wellfound (Startup Jobs)",
            "type": "url",
            "url": "https://wellfound.com/",
            "tags": ["Startup", "Tech", "R"]
        },
        {
            "name": "Hacker News: Who is Hiring",
            "name_en": "Hacker News: Who is Hiring",
            "type": "url",
            "url": "https://news.ycombinator.com/jobs",
            "tags": ["Tech", "Startup"]
        },
        {
            "name": "Dev.to Jobs",
            "name_en": "Dev.to Jobs",
            "type": "url",
            "url": "https://dev.to/listings/jobs",
            "tags": ["Tech", "Developer"]
        },
    ],

    # ==========================================
    # 零工管理平台
    # ==========================================

    "零工管理平台": [
        {
            "name": "Fountain（高流量招聘）",
            "name_en": "Fountain (High-Volume Hiring)",
            "type": "url",
            "url": "https://www.fountain.com/",
            "tags": ["Gig", "High-Volume", "P"]
        },
        {
            "name": "Wonolo（按需用工）",
            "name_en": "Wonolo (On-Demand Staffing)",
            "type": "url",
            "url": "https://www.wonolo.com/",
            "tags": ["Gig", "On-Demand", "P"]
        },
        {
            "name": "Instawork（零工平台）",
            "name_en": "Instawork (Gig Work Platform)",
            "type": "url",
            "url": "https://www.instawork.com/",
            "tags": ["Gig", "Hospitality", "P"]
        },
        {
            "name": "ShiftSmart（灵活用工）",
            "name_en": "ShiftSmart (Flexible Workforce)",
            "type": "url",
            "url": "https://www.shiftsmart.com/",
            "tags": ["Gig", "Flexible", "P"]
        },
        {
            "name": "Bluecrew（W-2 零工）",
            "name_en": "Bluecrew (W-2 Gig Workers)",
            "type": "url",
            "url": "https://www.bluecrew.com/",
            "tags": ["Gig", "W-2", "P"]
        },
    ],

    # ==========================================
    # 批量招聘工具
    # ==========================================

    "批量招聘工具": [
        {
            "name": "SmartRecruiters（高流量招聘）",
            "name_en": "SmartRecruiters (High-Volume Hiring)",
            "type": "url",
            "url": "https://www.smartrecruiters.com/",
            "tags": ["ATS", "Volume", "P"]
        },
        {
            "name": "iCIMS（企业级批量招聘）",
            "name_en": "iCIMS (Enterprise High-Volume)",
            "type": "url",
            "url": "https://www.icims.com/",
            "tags": ["ATS", "Enterprise", "P"]
        },
        {
            "name": "Paradox/Olivia（AI 招聘助手）",
            "name_en": "Paradox/Olivia (AI Recruiting Assistant)",
            "type": "url",
            "url": "https://www.paradox.ai/",
            "tags": ["AI", "Chatbot", "P"]
        },
        {
            "name": "XOR（AI 招聘自动化）",
            "name_en": "XOR (AI Recruiting Automation)",
            "type": "url",
            "url": "https://www.xor.ai/",
            "tags": ["AI", "Automation", "P"]
        },
        {
            "name": "Sense（人才互动平台）",
            "name_en": "Sense (Talent Engagement Platform)",
            "type": "url",
            "url": "https://www.sensehq.com/",
            "tags": ["Engagement", "Automation", "P"]
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
