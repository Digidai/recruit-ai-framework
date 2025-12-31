#!/usr/bin/env python3
"""
Batch 3: Add verified resources to tarf.json
Cross-validated resources for weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== 背景调查服务 =====
    "背景调查服务": [
        {
            "name": "Checkr（AI 背调）",
            "name_en": "Checkr (AI Background Checks)",
            "type": "url",
            "url": "https://checkr.com/",
            "tags": ["Background", "AI"]
        },
        {
            "name": "Sterling（全球背调）",
            "name_en": "Sterling (Global Background Screening)",
            "type": "url",
            "url": "https://www.sterlingcheck.com/",
            "tags": ["Background", "Enterprise"]
        },
        {
            "name": "HireRight（国际背调）",
            "name_en": "HireRight (International Background Checks)",
            "type": "url",
            "url": "https://www.hireright.com/",
            "tags": ["Background", "Global"]
        },
        {
            "name": "GoodHire（SMB 背调）",
            "name_en": "GoodHire (SMB Background Checks)",
            "type": "url",
            "url": "https://www.goodhire.com/",
            "tags": ["Background", "SMB"]
        },
        {
            "name": "Cisive（企业背调）",
            "name_en": "Cisive (Enterprise Background Screening)",
            "type": "url",
            "url": "https://www.cisive.com/",
            "tags": ["Background", "Enterprise"]
        },
    ],

    # ===== Offer 管理 =====
    "Offer 管理": [
        {
            "name": "DocuSign for HR（电子签名）",
            "name_en": "DocuSign for HR (E-Signatures)",
            "type": "url",
            "url": "https://www.docusign.com/solutions/departments/human-resources",
            "tags": ["E-Sign", "Enterprise"]
        },
        {
            "name": "SmartRecruiters Offer（Offer 管理）",
            "name_en": "SmartRecruiters Offer Management",
            "type": "url",
            "url": "https://www.smartrecruiters.com/recruiting-software/offer-management/",
            "tags": ["ATS", "Offer"]
        },
        {
            "name": "Adobe Sign（电子签名）",
            "name_en": "Adobe Acrobat Sign (E-Signatures)",
            "type": "url",
            "url": "https://www.adobe.com/sign.html",
            "tags": ["E-Sign", "Enterprise"]
        },
    ],

    # ===== 入职软件 =====
    "入职软件": [
        {
            "name": "BambooHR Onboarding（入职管理）",
            "name_en": "BambooHR Onboarding",
            "type": "url",
            "url": "https://www.bamboohr.com/platform/onboarding/",
            "tags": ["HRIS", "Onboarding"]
        },
        {
            "name": "Rippling（HR + IT 自动化）",
            "name_en": "Rippling (HR + IT Automation)",
            "type": "url",
            "url": "https://www.rippling.com/",
            "tags": ["HRIS", "Automation"]
        },
        {
            "name": "Kallidus Sapling（入职平台）",
            "name_en": "Kallidus Sapling (Onboarding Platform)",
            "type": "url",
            "url": "https://www.kallidus.com/sapling/",
            "tags": ["Onboarding", "Mid-Market"]
        },
        {
            "name": "Enboarder（入职体验）",
            "name_en": "Enboarder (Onboarding Experience)",
            "type": "url",
            "url": "https://enboarder.com/",
            "tags": ["Onboarding", "Experience"]
        },
    ],

    # ===== 招聘反欺诈与验证 =====
    "招聘反欺诈与验证": [
        {
            "name": "Certn（证书验证）",
            "name_en": "Certn (Credential Verification)",
            "type": "url",
            "url": "https://certn.co/",
            "tags": ["Verification", "AI"]
        },
        {
            "name": "Truework（收入与就业验证）",
            "name_en": "Truework (Income & Employment Verification)",
            "type": "url",
            "url": "https://www.truework.com/",
            "tags": ["Verification", "Payroll"]
        },
        {
            "name": "Crosschq（背景参考检查）",
            "name_en": "Crosschq (Reference Checks)",
            "type": "url",
            "url": "https://www.crosschq.com/",
            "tags": ["Reference", "Analytics"]
        },
        {
            "name": "Veremark（全球验证）",
            "name_en": "Veremark (Global Verification)",
            "type": "url",
            "url": "https://veremark.com/",
            "tags": ["Verification", "Global"]
        },
    ],

    # ===== 面试官培训平台 =====
    "面试官培训平台": [
        {
            "name": "SocialTalent（面试智能平台）",
            "name_en": "SocialTalent (Interview Intelligence Platform)",
            "type": "url",
            "url": "https://www.socialtalent.com/",
            "tags": ["Training", "Enterprise"]
        },
        {
            "name": "BrightHire（面试智能）",
            "name_en": "BrightHire (Interview Intelligence)",
            "type": "url",
            "url": "https://www.brighthire.com/",
            "tags": ["Interview", "AI"]
        },
        {
            "name": "Metaview（AI 面试记录）",
            "name_en": "Metaview (AI Interview Notes)",
            "type": "url",
            "url": "https://www.metaview.ai/",
            "tags": ["Interview", "AI"]
        },
    ],

    # ===== 候选人体验平台 =====
    "候选人体验平台": [
        {
            "name": "Phenom（人才体验平台）",
            "name_en": "Phenom (Talent Experience Platform)",
            "type": "url",
            "url": "https://www.phenom.com/",
            "tags": ["CX", "Enterprise"]
        },
        {
            "name": "Beamery（人才 CRM）",
            "name_en": "Beamery (Talent CRM)",
            "type": "url",
            "url": "https://beamery.com/",
            "tags": ["CRM", "Enterprise"]
        },
        {
            "name": "Avature（人才 CRM）",
            "name_en": "Avature (Talent CRM)",
            "type": "url",
            "url": "https://www.avature.net/",
            "tags": ["CRM", "Enterprise"]
        },
    ],

    # ===== 候选人关系管理 =====
    "候选人关系管理": [
        {
            "name": "Yello（校招 CRM）",
            "name_en": "Yello (Campus Recruiting CRM)",
            "type": "url",
            "url": "https://yello.co/",
            "tags": ["CRM", "Campus"]
        },
        {
            "name": "Clinch（人才 CRM）",
            "name_en": "Clinch (Talent CRM)",
            "type": "url",
            "url": "https://clinchtalent.com/",
            "tags": ["CRM", "Platform"]
        },
        {
            "name": "Talemetry（招聘营销 CRM）",
            "name_en": "Talemetry (Recruitment Marketing CRM)",
            "type": "url",
            "url": "https://www.jobvite.com/products/talemetry/",
            "tags": ["CRM", "Marketing"]
        },
    ],

    # ===== 灵活用工与零工经济 =====
    "灵活用工与零工经济": [
        {
            "name": "Wonolo（按需用工）",
            "name_en": "Wonolo (On-Demand Staffing)",
            "type": "url",
            "url": "https://www.wonolo.com/",
            "tags": ["Gig", "On-Demand"]
        },
        {
            "name": "Instawork（即时排班）",
            "name_en": "Instawork (Instant Shift Staffing)",
            "type": "url",
            "url": "https://www.instawork.com/",
            "tags": ["Gig", "Hospitality"]
        },
        {
            "name": "Shiftgig（零工排班）",
            "name_en": "Shiftgig (Gig Shift Platform)",
            "type": "url",
            "url": "https://www.shiftgig.com/",
            "tags": ["Gig", "Shifts"]
        },
        {
            "name": "GigSmart（零工市场）",
            "name_en": "GigSmart (Gig Worker Marketplace)",
            "type": "url",
            "url": "https://gigsmart.com/",
            "tags": ["Gig", "Marketplace"]
        },
    ],

    # ===== 临时用工/蓝领零工 =====
    "临时用工/蓝领零工": [
        {
            "name": "Fountain（高流量招聘）",
            "name_en": "Fountain (High-Volume Hiring)",
            "type": "url",
            "url": "https://www.fountain.com/",
            "tags": ["Hourly", "High-Volume"]
        },
        {
            "name": "Workstream（短信招聘）",
            "name_en": "Workstream (Text-Based Recruiting)",
            "type": "url",
            "url": "https://www.workstream.us/",
            "tags": ["Hourly", "SMS"]
        },
        {
            "name": "BlueRecruit（蓝领招聘）",
            "name_en": "BlueRecruit (Blue-Collar Recruiting)",
            "type": "url",
            "url": "https://bluerecruit.us/",
            "tags": ["Blue-Collar", "Platform"]
        },
        {
            "name": "JobStack（日结工）",
            "name_en": "JobStack (Daily Pay Jobs)",
            "type": "url",
            "url": "https://www.jobstack.com/",
            "tags": ["Hourly", "Daily Pay"]
        },
    ],

    # ===== 视频面试平台 =====
    "视频面试平台": [
        {
            "name": "VidCruiter（视频招聘）",
            "name_en": "VidCruiter (Video Recruiting)",
            "type": "url",
            "url": "https://vidcruiter.com/",
            "tags": ["Video", "Platform"]
        },
        {
            "name": "Spark Hire（视频面试）",
            "name_en": "Spark Hire (Video Interviews)",
            "type": "url",
            "url": "https://www.sparkhire.com/",
            "tags": ["Video", "SMB"]
        },
        {
            "name": "myInterview（AI 视频面试）",
            "name_en": "myInterview (AI Video Interviews)",
            "type": "url",
            "url": "https://www.myinterview.com/",
            "tags": ["Video", "AI"]
        },
        {
            "name": "Willo（异步视频面试）",
            "name_en": "Willo (Async Video Interviews)",
            "type": "url",
            "url": "https://www.willo.video/",
            "tags": ["Video", "Async"]
        },
    ],

    # ===== 虚拟招聘会平台 =====
    "虚拟招聘会平台": [
        {
            "name": "Brazen（虚拟招聘活动）",
            "name_en": "Brazen (Virtual Hiring Events)",
            "type": "url",
            "url": "https://www.brazen.com/",
            "tags": ["Virtual", "Events"]
        },
        {
            "name": "Remo（虚拟活动平台）",
            "name_en": "Remo (Virtual Event Platform)",
            "type": "url",
            "url": "https://remo.co/",
            "tags": ["Virtual", "Networking"]
        },
        {
            "name": "vFairs（虚拟招聘会）",
            "name_en": "vFairs (Virtual Career Fairs)",
            "type": "url",
            "url": "https://www.vfairs.com/",
            "tags": ["Virtual", "Career Fair"]
        },
        {
            "name": "Hopin（大型虚拟活动）",
            "name_en": "Hopin (Large Virtual Events)",
            "type": "url",
            "url": "https://hopin.com/",
            "tags": ["Virtual", "Enterprise"]
        },
    ],

    # ===== 面试排期工具 =====
    "面试排期工具": [
        {
            "name": "GoodTime（面试编排）",
            "name_en": "GoodTime (Interview Orchestration)",
            "type": "url",
            "url": "https://www.goodtime.io/",
            "tags": ["Scheduling", "AI"]
        },
        {
            "name": "Calendly for Recruiting（招聘排期）",
            "name_en": "Calendly for Recruiting",
            "type": "url",
            "url": "https://calendly.com/solutions/recruiting",
            "tags": ["Scheduling", "Popular"]
        },
        {
            "name": "Cronofy（日历集成）",
            "name_en": "Cronofy (Calendar Integration)",
            "type": "url",
            "url": "https://www.cronofy.com/",
            "tags": ["Scheduling", "API"]
        },
        {
            "name": "Prelude（面试协调）",
            "name_en": "Prelude (Interview Coordination)",
            "type": "url",
            "url": "https://www.prelude.co/",
            "tags": ["Scheduling", "Enterprise"]
        },
    ],

    # ===== 招聘自动化工具 =====
    "招聘自动化工具": [
        {
            "name": "Zapier for HR（HR 自动化）",
            "name_en": "Zapier for HR (HR Automation)",
            "type": "url",
            "url": "https://zapier.com/automation/recruitment-automation",
            "tags": ["Automation", "No-Code"]
        },
        {
            "name": "Workato（企业自动化）",
            "name_en": "Workato (Enterprise Automation)",
            "type": "url",
            "url": "https://www.workato.com/",
            "tags": ["Automation", "Enterprise"]
        },
        {
            "name": "Make（工作流自动化）",
            "name_en": "Make (Workflow Automation)",
            "type": "url",
            "url": "https://www.make.com/",
            "tags": ["Automation", "Visual"]
        },
    ],

    # ===== 残障人士招聘平台 =====
    "残障人士招聘平台": [
        {
            "name": "AbilityJOBS（残障求职平台）",
            "name_en": "AbilityJOBS (Disability Job Board)",
            "type": "url",
            "url": "https://abilityjobs.com/",
            "tags": ["Disability", "Job Board"]
        },
        {
            "name": "Disability Solutions（残障人才）",
            "name_en": "Disability Solutions (Disability Talent)",
            "type": "url",
            "url": "https://www.disabilitytalent.org/",
            "tags": ["Disability", "Consulting"]
        },
        {
            "name": "Getting Hired（无障碍招聘）",
            "name_en": "Getting Hired (Accessible Recruiting)",
            "type": "url",
            "url": "https://www.gettinghired.com/",
            "tags": ["Disability", "Platform"]
        },
        {
            "name": "AskEARN（雇主残障资源网）",
            "name_en": "AskEARN (Employer Disability Resource)",
            "type": "url",
            "url": "https://askearn.org/",
            "tags": ["Disability", "Resource"]
        },
    ],

    # ===== 多元化招聘平台 (DEI) =====
    "多元化招聘平台 (DEI)": [
        {
            "name": "Jopwell（少数族裔职业平台）",
            "name_en": "Jopwell (Underrepresented Professionals)",
            "type": "url",
            "url": "https://www.jopwell.com/",
            "tags": ["DEI", "Platform"]
        },
        {
            "name": "PowerToFly（女性与多元化）",
            "name_en": "PowerToFly (Women & Diversity)",
            "type": "url",
            "url": "https://powertofly.com/",
            "tags": ["DEI", "Women"]
        },
        {
            "name": "Fairygodboss（女性职场社区）",
            "name_en": "Fairygodboss (Women's Career Community)",
            "type": "url",
            "url": "https://fairygodboss.com/",
            "tags": ["DEI", "Women"]
        },
        {
            "name": "Diversity.com（多元化招聘）",
            "name_en": "Diversity.com (Diversity Recruiting)",
            "type": "url",
            "url": "https://diversity.com/",
            "tags": ["DEI", "Job Board"]
        },
        {
            "name": "DiversityJobs（多元化求职）",
            "name_en": "DiversityJobs (Diversity Job Board)",
            "type": "url",
            "url": "https://www.diversityjobs.com/",
            "tags": ["DEI", "Job Board"]
        },
    ],

    # ===== 偏差审计/合规服务 =====
    "偏差审计/合规服务": [
        {
            "name": "IBM AI Fairness 360（公平性工具）",
            "name_en": "IBM AI Fairness 360 (Fairness Toolkit)",
            "type": "url",
            "url": "https://aif360.mybluemix.net/",
            "tags": ["AI", "Open Source"]
        },
        {
            "name": "Microsoft Fairlearn（公平性库）",
            "name_en": "Microsoft Fairlearn (Fairness Library)",
            "type": "url",
            "url": "https://fairlearn.org/",
            "tags": ["AI", "Open Source"]
        },
        {
            "name": "Fiddler AI（模型监控）",
            "name_en": "Fiddler AI (Model Monitoring)",
            "type": "url",
            "url": "https://www.fiddler.ai/",
            "tags": ["AI", "Enterprise"]
        },
        {
            "name": "Truera（AI 质量平台）",
            "name_en": "Truera (AI Quality Platform)",
            "type": "url",
            "url": "https://truera.com/",
            "tags": ["AI", "Quality"]
        },
    ],

    # ===== 雇主品牌/EVP =====
    "雇主品牌/EVP": [
        {
            "name": "Sociabble（员工倡导）",
            "name_en": "Sociabble (Employee Advocacy)",
            "type": "url",
            "url": "https://www.sociabble.com/",
            "tags": ["Advocacy", "Platform"]
        },
        {
            "name": "Sprout Social Advocacy（员工分享）",
            "name_en": "Sprout Social Advocacy (Employee Sharing)",
            "type": "url",
            "url": "https://sproutsocial.com/features/employee-advocacy/",
            "tags": ["Advocacy", "Social"]
        },
        {
            "name": "GaggleAMP（社交倡导）",
            "name_en": "GaggleAMP (Social Advocacy)",
            "type": "url",
            "url": "https://www.gaggleamp.com/",
            "tags": ["Advocacy", "Platform"]
        },
        {
            "name": "PostBeyond（员工倡导）",
            "name_en": "PostBeyond (Employee Advocacy)",
            "type": "url",
            "url": "https://www.postbeyond.com/",
            "tags": ["Advocacy", "Enterprise"]
        },
    ],

    # ===== 招聘指标与基准 =====
    "招聘指标与基准": [
        {
            "name": "PwC Saratoga（HR 基准）",
            "name_en": "PwC Saratoga (HR Benchmarks)",
            "type": "url",
            "url": "https://www.pwc.com/us/en/products/saratoga.html",
            "tags": ["Benchmark", "Enterprise"]
        },
        {
            "name": "AIHR HR Dashboard（HR 仪表盘指南）",
            "name_en": "AIHR HR Dashboard Guide",
            "type": "url",
            "url": "https://www.aihr.com/blog/hr-dashboard/",
            "tags": ["Metrics", "Guide"]
        },
        {
            "name": "iCIMS Analytics（招聘分析）",
            "name_en": "iCIMS Recruiting Analytics",
            "type": "url",
            "url": "https://www.icims.com/platform/analytics/",
            "tags": ["Analytics", "ATS"]
        },
    ],

    # ===== AI Sourcing 工具 =====
    "AI Sourcing 工具": [
        {
            "name": "SeekOut（AI 人才搜索）",
            "name_en": "SeekOut (AI Talent Search)",
            "type": "url",
            "url": "https://www.seekout.com/",
            "tags": ["AI", "Sourcing"]
        },
        {
            "name": "Entelo（预测分析 Sourcing）",
            "name_en": "Entelo (Predictive Analytics Sourcing)",
            "type": "url",
            "url": "https://www.entelo.com/",
            "tags": ["AI", "Sourcing"]
        },
        {
            "name": "hireEZ（AI 招聘外展）",
            "name_en": "hireEZ (AI Recruiting Outreach)",
            "type": "url",
            "url": "https://hireez.com/",
            "tags": ["AI", "Sourcing"]
        },
        {
            "name": "Loxo（AI 招聘 CRM）",
            "name_en": "Loxo (AI Recruiting CRM)",
            "type": "url",
            "url": "https://loxo.co/",
            "tags": ["AI", "CRM"]
        },
    ],

    # ===== 技术测评平台 =====
    "技术测评平台": [
        {
            "name": "TestGorilla（技能测评）",
            "name_en": "TestGorilla (Skills Assessment)",
            "type": "url",
            "url": "https://www.testgorilla.com/",
            "tags": ["Assessment", "Platform"]
        },
        {
            "name": "iMocha（AI 技能评估）",
            "name_en": "iMocha (AI Skills Assessment)",
            "type": "url",
            "url": "https://www.imocha.io/",
            "tags": ["Assessment", "AI"]
        },
        {
            "name": "Vervoe（定制测评）",
            "name_en": "Vervoe (Custom Assessments)",
            "type": "url",
            "url": "https://vervoe.com/",
            "tags": ["Assessment", "Custom"]
        },
        {
            "name": "Qualified（技术筛选）",
            "name_en": "Qualified (Technical Screening)",
            "type": "url",
            "url": "https://www.qualified.io/",
            "tags": ["Assessment", "Tech"]
        },
    ],

    # ===== Chrome 扩展 =====
    "Chrome 扩展": [
        {
            "name": "Dux-Soup（LinkedIn 自动化）",
            "name_en": "Dux-Soup (LinkedIn Automation)",
            "type": "url",
            "url": "https://www.dux-soup.com/",
            "tags": ["Extension", "LinkedIn"]
        },
        {
            "name": "LinkedRadar（LinkedIn 网络管理）",
            "name_en": "LinkedRadar (LinkedIn Network Management)",
            "type": "url",
            "url": "https://linkedradar.com/",
            "tags": ["Extension", "LinkedIn"]
        },
        {
            "name": "Lusha（联系人查找）",
            "name_en": "Lusha (Contact Finder)",
            "type": "url",
            "url": "https://www.lusha.com/",
            "tags": ["Extension", "Contacts"]
        },
        {
            "name": "RocketReach（邮箱查找）",
            "name_en": "RocketReach (Email Finder)",
            "type": "url",
            "url": "https://rocketreach.co/",
            "tags": ["Extension", "Email"]
        },
        {
            "name": "Text Blaze（文本模板）",
            "name_en": "Text Blaze (Text Templates)",
            "type": "url",
            "url": "https://blaze.today/",
            "tags": ["Extension", "Productivity"]
        },
    ],

    # ===== 招聘效率与生产力工具 =====
    "招聘效率与生产力工具": [
        {
            "name": "Recruit CRM Extension（招聘 CRM 扩展）",
            "name_en": "Recruit CRM Chrome Extension",
            "type": "url",
            "url": "https://recruitcrm.io/",
            "tags": ["Extension", "CRM"]
        },
        {
            "name": "Clockify（时间追踪）",
            "name_en": "Clockify (Time Tracking)",
            "type": "url",
            "url": "https://clockify.me/",
            "tags": ["Productivity", "Free"]
        },
        {
            "name": "Grammarly（写作助手）",
            "name_en": "Grammarly (Writing Assistant)",
            "type": "url",
            "url": "https://www.grammarly.com/",
            "tags": ["Writing", "AI"]
        },
    ],

    # ===== 学历验证 =====
    "学历验证": [
        {
            "name": "National Student Clearinghouse（学历验证）",
            "name_en": "National Student Clearinghouse (Education Verification)",
            "type": "url",
            "url": "https://www.studentclearinghouse.org/",
            "tags": ["Verification", "Education"]
        },
        {
            "name": "Parchment（学历证书）",
            "name_en": "Parchment (Academic Credentials)",
            "type": "url",
            "url": "https://www.parchment.com/",
            "tags": ["Verification", "Education"]
        },
        {
            "name": "Credential Solutions（教育记录）",
            "name_en": "Credential Solutions (Education Records)",
            "type": "url",
            "url": "https://www.credentialsolutions.com/",
            "tags": ["Verification", "Education"]
        },
    ],

    # ===== 就业/工作验证 =====
    "就业/工作验证": [
        {
            "name": "The Work Number（Equifax 就业验证）",
            "name_en": "The Work Number (Equifax Employment Verification)",
            "type": "url",
            "url": "https://www.theworknumber.com/",
            "tags": ["Verification", "Employment"]
        },
        {
            "name": "Experian Verify（就业验证）",
            "name_en": "Experian Verify (Employment Verification)",
            "type": "url",
            "url": "https://www.experian.com/employer-services",
            "tags": ["Verification", "Employment"]
        },
    ],

    # ===== 招聘偏见检测 =====
    "招聘偏见检测": [
        {
            "name": "Textio Lift（招聘语言优化）",
            "name_en": "Textio Lift (Recruiting Language Optimization)",
            "type": "url",
            "url": "https://textio.com/lift/",
            "tags": ["Bias", "AI"]
        },
        {
            "name": "Datapeople（JD 分析）",
            "name_en": "Datapeople (Job Posting Analytics)",
            "type": "url",
            "url": "https://datapeople.io/",
            "tags": ["Bias", "Analytics"]
        },
        {
            "name": "TalVista（偏见减少）",
            "name_en": "TalVista (Bias Reduction)",
            "type": "url",
            "url": "https://www.talvista.com/",
            "tags": ["Bias", "Platform"]
        },
    ],

    # ===== 学习资源与研究 =====
    "学习资源与研究": [
        {
            "name": "SHRM Learning System（HR 学习）",
            "name_en": "SHRM Learning System (HR Learning)",
            "type": "url",
            "url": "https://www.shrm.org/credentials-education/shrm-learning-system",
            "tags": ["Learning", "Certification"]
        },
        {
            "name": "LinkedIn Learning HR（HR 课程）",
            "name_en": "LinkedIn Learning HR Courses",
            "type": "url",
            "url": "https://www.linkedin.com/learning/topics/human-resources",
            "tags": ["Learning", "Online"]
        },
        {
            "name": "Coursera HR Courses（HR 课程）",
            "name_en": "Coursera HR Courses",
            "type": "url",
            "url": "https://www.coursera.org/browse/business/human-resource-management",
            "tags": ["Learning", "University"]
        },
        {
            "name": "Josh Bersin Academy（HR 学院）",
            "name_en": "Josh Bersin Academy (HR Academy)",
            "type": "url",
            "url": "https://joshbersin.com/academy/",
            "tags": ["Learning", "Expert"]
        },
    ],

    # ===== ATS 与招聘协作 =====
    "ATS 与招聘协作": [
        {
            "name": "Teamtailor（现代 ATS）",
            "name_en": "Teamtailor (Modern ATS)",
            "type": "url",
            "url": "https://www.teamtailor.com/",
            "tags": ["ATS", "Mid-Market"]
        },
        {
            "name": "Personio（HR + ATS）",
            "name_en": "Personio (HR + ATS)",
            "type": "url",
            "url": "https://www.personio.com/",
            "tags": ["ATS", "Europe"]
        },
        {
            "name": "Breezy HR（可视化 ATS）",
            "name_en": "Breezy HR (Visual ATS)",
            "type": "url",
            "url": "https://breezy.hr/",
            "tags": ["ATS", "SMB"]
        },
    ],

    # ===== 人才市场情报与竞争分析 =====
    "人才市场情报与竞争分析": [
        {
            "name": "Claro Analytics（人才市场分析）",
            "name_en": "Claro Analytics (Talent Market Analytics)",
            "type": "url",
            "url": "https://www.claroanalytics.com/",
            "tags": ["Intelligence", "Data"]
        },
        {
            "name": "Glassdoor Economic Research（经济研究）",
            "name_en": "Glassdoor Economic Research",
            "type": "url",
            "url": "https://www.glassdoor.com/research/",
            "tags": ["Research", "Data"]
        },
        {
            "name": "JobsEQ（劳动力市场数据）",
            "name_en": "JobsEQ (Labor Market Data)",
            "type": "url",
            "url": "https://www.chmuraecon.com/jobseq/",
            "tags": ["Intelligence", "Data"]
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
            "name": "Joveo（招聘营销智能）",
            "name_en": "Joveo (Recruitment Marketing Intelligence)",
            "type": "url",
            "url": "https://www.joveo.com/",
            "tags": ["Marketing", "AI"]
        },
        {
            "name": "Radancy（人才获取云）",
            "name_en": "Radancy (Talent Acquisition Cloud)",
            "type": "url",
            "url": "https://www.radancy.com/",
            "tags": ["Marketing", "Enterprise"]
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
