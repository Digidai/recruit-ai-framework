#!/usr/bin/env python3
"""
Batch 3: Add more verified resources to tarf.json
Focus on categories with fewer resources.
"""

import json
import re

# New verified resources to add
NEW_RESOURCES = {
    # ===== A 招聘流程与方法论 =====
    "招聘流程与方法论": [
        {
            "name": "Workable｜招聘流程指南",
            "name_en": "Workable | Hiring Process Guide",
            "type": "url",
            "url": "https://resources.workable.com/tutorial/hiring-process",
            "tags": ["流程", "指南", "best practice"]
        },
        {
            "name": "Indeed｜招聘最佳实践",
            "name_en": "Indeed | Hiring Best Practices",
            "type": "url",
            "url": "https://www.indeed.com/hire/c/info/hiring-best-practices",
            "tags": ["招聘", "最佳实践", "指南"]
        },
        {
            "name": "Recruiterbox｜招聘流程优化",
            "name_en": "Recruiterbox | Hiring Process Optimization",
            "type": "url",
            "url": "https://recruiterbox.com/blog/hiring-process",
            "tags": ["流程优化", "招聘效率"]
        },
        {
            "name": "Toggl Hire｜技能测试招聘",
            "name_en": "Toggl Hire | Skills-Based Hiring",
            "type": "url",
            "url": "https://toggl.com/hire/",
            "tags": ["技能测试", "招聘工具"]
        },
        {
            "name": "BambooHR｜招聘流程模板",
            "name_en": "BambooHR | Hiring Process Templates",
            "type": "url",
            "url": "https://www.bamboohr.com/resources/hr-glossary/hiring-process",
            "tags": ["模板", "HR", "流程"]
        },
    ],

    "面试官培训与招聘培训": [
        {
            "name": "SocialTalent｜招聘培训平台",
            "name_en": "SocialTalent | Recruiter Training Platform",
            "type": "url",
            "url": "https://www.socialtalent.com/",
            "tags": ["培训", "招聘技能", "平台"]
        },
        {
            "name": "LinkedIn Learning｜面试技巧课程",
            "name_en": "LinkedIn Learning | Interviewing Skills",
            "type": "url",
            "url": "https://www.linkedin.com/learning/topics/interviewing",
            "tags": ["面试", "课程", "LinkedIn"]
        },
        {
            "name": "AIRS｜招聘认证培训",
            "name_en": "AIRS | Recruiting Certification Training",
            "type": "url",
            "url": "https://www.airsdirectory.com/",
            "tags": ["认证", "培训", "AIRS"]
        },
        {
            "name": "SourceCon｜Sourcing培训资源",
            "name_en": "SourceCon | Sourcing Training Resources",
            "type": "url",
            "url": "https://www.sourcecon.com/",
            "tags": ["sourcing", "培训", "社区"]
        },
    ],

    "招聘心理学与行为科学": [
        {
            "name": "Applied｜行为科学招聘平台",
            "name_en": "Applied | Behavioral Science Hiring Platform",
            "type": "url",
            "url": "https://www.beapplied.com/",
            "tags": ["行为科学", "去偏见", "平台"]
        },
        {
            "name": "Predictive Index｜人才优化",
            "name_en": "Predictive Index | Talent Optimization",
            "type": "url",
            "url": "https://www.predictiveindex.com/",
            "tags": ["人才评估", "行为分析", "优化"]
        },
        {
            "name": "Hogan Assessments｜人格测评",
            "name_en": "Hogan Assessments | Personality Assessment",
            "type": "url",
            "url": "https://www.hoganassessments.com/",
            "tags": ["人格测评", "心理学", "评估"]
        },
        {
            "name": "BetterUp｜领导力与职业发展",
            "name_en": "BetterUp | Leadership & Career Development",
            "type": "url",
            "url": "https://www.betterup.com/",
            "tags": ["领导力", "发展", "coaching"]
        },
    ],

    # ===== B 招聘渠道与 Sourcing =====
    "搜索模板（X-Ray/Boolean）": [
        {
            "name": "Boolean Strings｜高级搜索技巧",
            "name_en": "Boolean Strings | Advanced Search Techniques",
            "type": "url",
            "url": "https://booleanstrings.com/",
            "tags": ["boolean", "搜索", "技巧"]
        },
        {
            "name": "RecruitEm｜LinkedIn X-Ray搜索",
            "name_en": "RecruitEm | LinkedIn X-Ray Search",
            "type": "url",
            "url": "https://recruitin.net/",
            "tags": ["X-Ray", "LinkedIn", "搜索"]
        },
        {
            "name": "Sourcing Games｜Sourcing练习",
            "name_en": "Sourcing Games | Sourcing Practice",
            "type": "url",
            "url": "https://sourcing.games/",
            "tags": ["练习", "sourcing", "游戏"]
        },
        {
            "name": "Pipl｜深度人员搜索",
            "name_en": "Pipl | Deep People Search",
            "type": "url",
            "url": "https://pipl.com/",
            "tags": ["人员搜索", "深度搜索", "identity"]
        },
        {
            "name": "Hunter.io｜邮箱查找工具",
            "name_en": "Hunter.io | Email Finder Tool",
            "type": "url",
            "url": "https://hunter.io/",
            "tags": ["邮箱", "查找", "联系方式"]
        },
        {
            "name": "Lusha｜B2B联系人数据",
            "name_en": "Lusha | B2B Contact Data",
            "type": "url",
            "url": "https://www.lusha.com/",
            "tags": ["联系人", "B2B", "数据"]
        },
    ],

    "校园招聘与实习": [
        {
            "name": "Handshake｜校园招聘平台",
            "name_en": "Handshake | Campus Recruiting Platform",
            "type": "url",
            "url": "https://joinhandshake.com/",
            "tags": ["校园招聘", "平台", "大学"]
        },
        {
            "name": "WayUp｜大学生与应届生招聘",
            "name_en": "WayUp | College & Early Career Hiring",
            "type": "url",
            "url": "https://www.wayup.com/",
            "tags": ["应届生", "实习", "平台"]
        },
        {
            "name": "RippleMatch｜校园招聘匹配",
            "name_en": "RippleMatch | Campus Recruiting Matching",
            "type": "url",
            "url": "https://ripplematch.com/",
            "tags": ["匹配", "校园", "AI"]
        },
        {
            "name": "Symplicity｜大学职业服务",
            "name_en": "Symplicity | University Career Services",
            "type": "url",
            "url": "https://www.symplicity.com/",
            "tags": ["职业服务", "大学", "平台"]
        },
        {
            "name": "Parker Dewey｜微实习平台",
            "name_en": "Parker Dewey | Micro-Internship Platform",
            "type": "url",
            "url": "https://www.parkerdewey.com/",
            "tags": ["微实习", "项目制", "平台"]
        },
    ],

    "高管招聘": [
        {
            "name": "Korn Ferry｜高管猎头服务",
            "name_en": "Korn Ferry | Executive Search Services",
            "type": "url",
            "url": "https://www.kornferry.com/",
            "tags": ["高管", "猎头", "咨询"]
        },
        {
            "name": "Spencer Stuart｜高管搜索与领导力咨询",
            "name_en": "Spencer Stuart | Executive Search & Leadership",
            "type": "url",
            "url": "https://www.spencerstuart.com/",
            "tags": ["高管搜索", "领导力", "咨询"]
        },
        {
            "name": "Russell Reynolds｜领导力咨询",
            "name_en": "Russell Reynolds | Leadership Consulting",
            "type": "url",
            "url": "https://www.russellreynolds.com/",
            "tags": ["领导力", "高管", "咨询"]
        },
        {
            "name": "Egon Zehnder｜高管搜索与评估",
            "name_en": "Egon Zehnder | Executive Search & Assessment",
            "type": "url",
            "url": "https://www.egonzehnder.com/",
            "tags": ["高管搜索", "评估", "咨询"]
        },
        {
            "name": "Heidrick & Struggles｜高管人才方案",
            "name_en": "Heidrick & Struggles | Executive Talent Solutions",
            "type": "url",
            "url": "https://www.heidrick.com/",
            "tags": ["高管", "人才方案", "咨询"]
        },
    ],

    "行业垂直招聘": [
        {
            "name": "Dice｜科技人才招聘",
            "name_en": "Dice | Tech Talent Recruitment",
            "type": "url",
            "url": "https://www.dice.com/",
            "tags": ["科技", "IT", "招聘"]
        },
        {
            "name": "Hired｜技术人才市场",
            "name_en": "Hired | Tech Talent Marketplace",
            "type": "url",
            "url": "https://hired.com/",
            "tags": ["技术", "市场", "人才"]
        },
        {
            "name": "Dribbble Jobs｜设计师招聘",
            "name_en": "Dribbble Jobs | Designer Recruitment",
            "type": "url",
            "url": "https://dribbble.com/jobs",
            "tags": ["设计", "创意", "招聘"]
        },
        {
            "name": "AngelList Talent｜创业公司招聘",
            "name_en": "AngelList Talent | Startup Recruitment",
            "type": "url",
            "url": "https://angel.co/jobs",
            "tags": ["创业公司", "startup", "招聘"]
        },
        {
            "name": "Mediabistro｜媒体行业招聘",
            "name_en": "Mediabistro | Media Industry Recruitment",
            "type": "url",
            "url": "https://www.mediabistro.com/",
            "tags": ["媒体", "新闻", "招聘"]
        },
    ],

    # ===== F 多元化与包容性招聘 =====
    "退伍军人招聘": [
        {
            "name": "Hiring Our Heroes｜军人就业项目",
            "name_en": "Hiring Our Heroes | Military Employment Program",
            "type": "url",
            "url": "https://www.hiringourheroes.org/",
            "tags": ["军人", "就业", "项目"]
        },
        {
            "name": "Military.com｜退伍军人职业",
            "name_en": "Military.com | Veteran Careers",
            "type": "url",
            "url": "https://www.military.com/veteran-jobs",
            "tags": ["退伍军人", "职业", "招聘"]
        },
        {
            "name": "RecruitMilitary｜军人招聘服务",
            "name_en": "RecruitMilitary | Military Recruitment Services",
            "type": "url",
            "url": "https://recruitmilitary.com/",
            "tags": ["军人", "招聘", "服务"]
        },
        {
            "name": "VetJobs｜退伍军人招聘板",
            "name_en": "VetJobs | Veteran Job Board",
            "type": "url",
            "url": "https://vetjobs.com/",
            "tags": ["退伍军人", "招聘板", "职位"]
        },
        {
            "name": "American Corporate Partners｜退伍军人导师计划",
            "name_en": "American Corporate Partners | Veteran Mentorship",
            "type": "url",
            "url": "https://www.acp-usa.org/",
            "tags": ["退伍军人", "导师", "职业发展"]
        },
        {
            "name": "Veterati｜退伍军人职业导师网络",
            "name_en": "Veterati | Veteran Career Mentorship Network",
            "type": "url",
            "url": "https://www.veterati.com/",
            "tags": ["退伍军人", "导师", "网络"]
        },
    ],

    "神经多样性招聘": [
        {
            "name": "Specialisterne｜自闭症人才招聘",
            "name_en": "Specialisterne | Autism Talent Recruitment",
            "type": "url",
            "url": "https://specialisterne.com/",
            "tags": ["自闭症", "神经多样性", "招聘"]
        },
        {
            "name": "Autism at Work｜自闭症就业计划",
            "name_en": "Autism at Work | Autism Employment Programs",
            "type": "url",
            "url": "https://www.sap.com/about/company/diversity/differently-abled.html",
            "tags": ["自闭症", "就业", "SAP"]
        },
        {
            "name": "Neurodiversity Hub｜神经多样性资源中心",
            "name_en": "Neurodiversity Hub | Neurodiversity Resource Center",
            "type": "url",
            "url": "https://www.neurodiversityhub.org/",
            "tags": ["神经多样性", "资源", "教育"]
        },
        {
            "name": "Mentra｜神经多样性人才平台",
            "name_en": "Mentra | Neurodivergent Talent Platform",
            "type": "url",
            "url": "https://www.mentra.com/",
            "tags": ["神经多样性", "平台", "人才"]
        },
    ],

    "招聘伦理与公平招聘": [
        {
            "name": "Fair Chance Business Pledge｜公平机会商业承诺",
            "name_en": "Fair Chance Business Pledge | Fair Chance Hiring",
            "type": "url",
            "url": "https://www.whitehouse.gov/the-press-office/2016/04/11/fact-sheet-white-house-launches-fair-chance-business-pledge",
            "tags": ["公平机会", "承诺", "政策"]
        },
        {
            "name": "Ban the Box｜前科公平招聘运动",
            "name_en": "Ban the Box | Fair Chance Hiring Movement",
            "type": "url",
            "url": "https://bantheboxcampaign.org/",
            "tags": ["前科", "公平", "运动"]
        },
        {
            "name": "SHRM Getting Talent Back to Work｜返岗计划",
            "name_en": "SHRM Getting Talent Back to Work | Reentry Program",
            "type": "url",
            "url": "https://www.shrm.org/about/together-forward-work/second-chance-employment",
            "tags": ["返岗", "二次机会", "SHRM"]
        },
    ],

    # ===== G 雇主品牌与候选人体验 =====
    "游戏化与 VR/AR 招聘": [
        {
            "name": "Pymetrics｜AI游戏化评估",
            "name_en": "Pymetrics | AI Gamified Assessment",
            "type": "url",
            "url": "https://www.pymetrics.ai/",
            "tags": ["游戏化", "AI", "评估"]
        },
        {
            "name": "Arctic Shores｜行为游戏评估",
            "name_en": "Arctic Shores | Behavioral Game Assessment",
            "type": "url",
            "url": "https://www.arcticshores.com/",
            "tags": ["游戏", "行为", "评估"]
        },
        {
            "name": "Knack｜游戏化人才评估",
            "name_en": "Knack | Gamified Talent Assessment",
            "type": "url",
            "url": "https://www.knack.it/",
            "tags": ["游戏化", "人才", "评估"]
        },
        {
            "name": "Strivr｜VR培训与招聘",
            "name_en": "Strivr | VR Training & Hiring",
            "type": "url",
            "url": "https://www.strivr.com/",
            "tags": ["VR", "培训", "沉浸式"]
        },
        {
            "name": "Talespin｜VR软技能培训",
            "name_en": "Talespin | VR Soft Skills Training",
            "type": "url",
            "url": "https://www.talespin.com/",
            "tags": ["VR", "软技能", "培训"]
        },
    ],

    "候选人体验与雇主品牌": [
        {
            "name": "Glassdoor for Employers｜雇主评价管理",
            "name_en": "Glassdoor for Employers | Employer Review Management",
            "type": "url",
            "url": "https://www.glassdoor.com/employers/",
            "tags": ["雇主品牌", "评价", "管理"]
        },
        {
            "name": "Comparably｜企业文化与薪酬透明",
            "name_en": "Comparably | Company Culture & Pay Transparency",
            "type": "url",
            "url": "https://www.comparably.com/",
            "tags": ["企业文化", "薪酬", "透明度"]
        },
        {
            "name": "Kununu｜德语区雇主评价平台",
            "name_en": "Kununu | German Employer Review Platform",
            "type": "url",
            "url": "https://www.kununu.com/",
            "tags": ["德国", "雇主评价", "平台"]
        },
        {
            "name": "InHerSight｜女性职场评价平台",
            "name_en": "InHerSight | Women's Workplace Review Platform",
            "type": "url",
            "url": "https://www.inhersight.com/",
            "tags": ["女性", "职场", "评价"]
        },
    ],

    "招聘视觉与品牌设计": [
        {
            "name": "Canva｜招聘视觉设计工具",
            "name_en": "Canva | Recruitment Visual Design Tool",
            "type": "url",
            "url": "https://www.canva.com/templates/?query=recruitment",
            "tags": ["设计", "模板", "视觉"]
        },
        {
            "name": "Visme｜招聘信息图制作",
            "name_en": "Visme | Recruitment Infographic Creator",
            "type": "url",
            "url": "https://www.visme.co/",
            "tags": ["信息图", "设计", "视觉"]
        },
        {
            "name": "Piktochart｜可视化内容创建",
            "name_en": "Piktochart | Visual Content Creation",
            "type": "url",
            "url": "https://piktochart.com/",
            "tags": ["可视化", "内容", "设计"]
        },
    ],

    # ===== J 数据分析与行业洞察 =====
    "薪酬与职位数据": [
        {
            "name": "Payscale｜薪酬数据与分析",
            "name_en": "Payscale | Compensation Data & Analytics",
            "type": "url",
            "url": "https://www.payscale.com/",
            "tags": ["薪酬", "数据", "分析"]
        },
        {
            "name": "Salary.com｜薪酬数据库",
            "name_en": "Salary.com | Salary Database",
            "type": "url",
            "url": "https://www.salary.com/",
            "tags": ["薪酬", "数据库", "基准"]
        },
        {
            "name": "Glassdoor Salaries｜薪酬透明数据",
            "name_en": "Glassdoor Salaries | Salary Transparency Data",
            "type": "url",
            "url": "https://www.glassdoor.com/Salaries/",
            "tags": ["薪酬", "透明", "数据"]
        },
        {
            "name": "Levels.fyi｜科技公司薪酬对比",
            "name_en": "Levels.fyi | Tech Company Salary Comparison",
            "type": "url",
            "url": "https://www.levels.fyi/",
            "tags": ["科技", "薪酬", "对比"]
        },
        {
            "name": "Compensation.BLS｜劳工统计局薪酬数据",
            "name_en": "BLS Compensation | Bureau of Labor Statistics",
            "type": "url",
            "url": "https://www.bls.gov/bls/wages.htm",
            "tags": ["政府", "统计", "薪酬"]
        },
        {
            "name": "Mercer｜薪酬调研与咨询",
            "name_en": "Mercer | Compensation Survey & Consulting",
            "type": "url",
            "url": "https://www.mercer.com/what-we-do/workforce-and-careers/talent-strategy/compensation-benchmarking.html",
            "tags": ["咨询", "薪酬调研", "基准"]
        },
    ],

    "招聘职业发展": [
        {
            "name": "SHRM Certification｜HR认证项目",
            "name_en": "SHRM Certification | HR Certification Programs",
            "type": "url",
            "url": "https://www.shrm.org/certification/",
            "tags": ["认证", "SHRM", "HR"]
        },
        {
            "name": "HRCI｜HR专业认证",
            "name_en": "HRCI | HR Professional Certification",
            "type": "url",
            "url": "https://www.hrci.org/",
            "tags": ["认证", "HRCI", "专业"]
        },
        {
            "name": "ATD｜人才发展协会",
            "name_en": "ATD | Association for Talent Development",
            "type": "url",
            "url": "https://www.td.org/",
            "tags": ["人才发展", "协会", "培训"]
        },
        {
            "name": "Recruiting Brainfood｜招聘行业资讯",
            "name_en": "Recruiting Brainfood | Recruiting Industry News",
            "type": "url",
            "url": "https://www.recruitingbrainfood.com/",
            "tags": ["资讯", "newsletter", "行业"]
        },
        {
            "name": "HRD｜人力资源董事社区",
            "name_en": "HRD | HR Directors Community",
            "type": "url",
            "url": "https://www.hrdconnect.com/",
            "tags": ["社区", "HR领导", "网络"]
        },
        {
            "name": "Recruiter.com｜招聘者资源与社区",
            "name_en": "Recruiter.com | Recruiter Resources & Community",
            "type": "url",
            "url": "https://www.recruiter.com/",
            "tags": ["招聘者", "资源", "社区"]
        },
    ],

    "人才市场情报与竞争分析": [
        {
            "name": "LinkedIn Talent Insights｜人才市场洞察",
            "name_en": "LinkedIn Talent Insights | Talent Market Intelligence",
            "type": "url",
            "url": "https://business.linkedin.com/talent-solutions/talent-insights",
            "tags": ["人才洞察", "市场", "LinkedIn"]
        },
        {
            "name": "Revelio Labs｜劳动力市场分析",
            "name_en": "Revelio Labs | Workforce Analytics",
            "type": "url",
            "url": "https://www.reveliolabs.com/",
            "tags": ["劳动力", "分析", "数据"]
        },
        {
            "name": "Lightcast｜劳动力市场数据",
            "name_en": "Lightcast | Labor Market Data",
            "type": "url",
            "url": "https://lightcast.io/",
            "tags": ["劳动力市场", "数据", "分析"]
        },
        {
            "name": "Horsefly Analytics｜人才市场情报",
            "name_en": "Horsefly Analytics | Talent Market Intelligence",
            "type": "url",
            "url": "https://www.horsefly.ai/",
            "tags": ["市场情报", "人才", "分析"]
        },
        {
            "name": "TalentNeuron｜人才竞争情报",
            "name_en": "TalentNeuron | Talent Competitive Intelligence",
            "type": "url",
            "url": "https://www.talentneuron.com/",
            "tags": ["竞争情报", "人才", "分析"]
        },
    ],

    "招聘预算与 ROI": [
        {
            "name": "SHRM Benchmarking｜HR指标基准",
            "name_en": "SHRM Benchmarking | HR Metrics Benchmarks",
            "type": "url",
            "url": "https://www.shrm.org/resourcesandtools/business-solutions/Pages/benchmarking-service.aspx",
            "tags": ["基准", "指标", "SHRM"]
        },
        {
            "name": "ERE Cost Per Hire｜招聘成本分析",
            "name_en": "ERE Cost Per Hire | Hiring Cost Analysis",
            "type": "url",
            "url": "https://www.ere.net/category/cost-per-hire/",
            "tags": ["成本", "分析", "ROI"]
        },
        {
            "name": "Workday Recruiting Analytics｜招聘分析报告",
            "name_en": "Workday Recruiting Analytics | Recruiting Reports",
            "type": "url",
            "url": "https://www.workday.com/en-us/products/talent-management/recruiting.html",
            "tags": ["分析", "报告", "Workday"]
        },
    ],

    "知名公司招聘实践": [
        {
            "name": "Netflix Culture Deck｜Netflix文化手册",
            "name_en": "Netflix Culture Deck | Netflix Culture Handbook",
            "type": "url",
            "url": "https://jobs.netflix.com/culture",
            "tags": ["文化", "Netflix", "实践"]
        },
        {
            "name": "Spotify HR Blog｜Spotify人力资源博客",
            "name_en": "Spotify HR Blog | Spotify HR Insights",
            "type": "url",
            "url": "https://hrblog.spotify.com/",
            "tags": ["Spotify", "HR", "博客"]
        },
        {
            "name": "HubSpot Culture Code｜HubSpot文化准则",
            "name_en": "HubSpot Culture Code | HubSpot Culture Guide",
            "type": "url",
            "url": "https://www.hubspot.com/company/culture",
            "tags": ["HubSpot", "文化", "准则"]
        },
        {
            "name": "Stripe Atlas｜创业公司招聘指南",
            "name_en": "Stripe Atlas | Startup Hiring Guide",
            "type": "url",
            "url": "https://stripe.com/atlas/guides/hiring",
            "tags": ["Stripe", "创业", "指南"]
        },
    ],

    # ===== H 人才管理与规划 =====
    "员工推荐": [
        {
            "name": "Drafted｜员工推荐网络",
            "name_en": "Drafted | Employee Referral Network",
            "type": "url",
            "url": "https://www.drafted.us/",
            "tags": ["推荐", "网络", "平台"]
        },
        {
            "name": "RolePoint｜员工推荐平台",
            "name_en": "RolePoint | Employee Referral Platform",
            "type": "url",
            "url": "https://www.rolepoint.com/",
            "tags": ["推荐", "平台", "自动化"]
        },
        {
            "name": "Teamable｜人才网络挖掘",
            "name_en": "Teamable | Talent Network Mining",
            "type": "url",
            "url": "https://www.teamable.com/",
            "tags": ["人才网络", "挖掘", "推荐"]
        },
        {
            "name": "EmployeeReferrals.com｜推荐管理平台",
            "name_en": "EmployeeReferrals.com | Referral Management",
            "type": "url",
            "url": "https://www.employeereferrals.com/",
            "tags": ["推荐", "管理", "平台"]
        },
    ],

    "人才社区与人才库建设": [
        {
            "name": "Beamery｜人才关系管理",
            "name_en": "Beamery | Talent Relationship Management",
            "type": "url",
            "url": "https://beamery.com/",
            "tags": ["TRM", "人才库", "CRM"]
        },
        {
            "name": "Avature｜人才获取与CRM",
            "name_en": "Avature | Talent Acquisition & CRM",
            "type": "url",
            "url": "https://www.avature.net/",
            "tags": ["人才获取", "CRM", "平台"]
        },
        {
            "name": "Phenom｜人才体验平台",
            "name_en": "Phenom | Talent Experience Platform",
            "type": "url",
            "url": "https://www.phenom.com/",
            "tags": ["人才体验", "平台", "AI"]
        },
        {
            "name": "Clinch｜人才参与平台",
            "name_en": "Clinch | Talent Engagement Platform",
            "type": "url",
            "url": "https://clinchtalent.com/",
            "tags": ["人才参与", "平台", "营销"]
        },
    ],

    "人才盘点与继任计划": [
        {
            "name": "9-Box Grid｜人才九宫格模型",
            "name_en": "9-Box Grid | Talent Assessment Model",
            "type": "url",
            "url": "https://www.aihr.com/blog/9-box-grid/",
            "tags": ["九宫格", "评估", "模型"]
        },
        {
            "name": "Lattice｜绩效与人才管理",
            "name_en": "Lattice | Performance & Talent Management",
            "type": "url",
            "url": "https://lattice.com/",
            "tags": ["绩效", "人才管理", "平台"]
        },
        {
            "name": "Culture Amp｜员工体验平台",
            "name_en": "Culture Amp | Employee Experience Platform",
            "type": "url",
            "url": "https://www.cultureamp.com/",
            "tags": ["员工体验", "反馈", "分析"]
        },
        {
            "name": "15Five｜持续绩效管理",
            "name_en": "15Five | Continuous Performance Management",
            "type": "url",
            "url": "https://www.15five.com/",
            "tags": ["绩效", "持续", "反馈"]
        },
    ],

    # ===== I 全球招聘与特殊场景 =====
    "全球招聘与远程团队": [
        {
            "name": "Deel｜全球薪酬与合规",
            "name_en": "Deel | Global Payroll & Compliance",
            "type": "url",
            "url": "https://www.deel.com/",
            "tags": ["全球", "薪酬", "合规"]
        },
        {
            "name": "Remote｜全球远程雇佣",
            "name_en": "Remote | Global Remote Employment",
            "type": "url",
            "url": "https://remote.com/",
            "tags": ["远程", "雇佣", "全球"]
        },
        {
            "name": "Oyster｜全球雇佣平台",
            "name_en": "Oyster | Global Employment Platform",
            "type": "url",
            "url": "https://www.oysterhr.com/",
            "tags": ["全球雇佣", "平台", "HR"]
        },
        {
            "name": "Papaya Global｜全球薪酬管理",
            "name_en": "Papaya Global | Global Payroll Management",
            "type": "url",
            "url": "https://www.papayaglobal.com/",
            "tags": ["全球薪酬", "管理", "自动化"]
        },
    ],

    "招聘流程外包 (RPO)": [
        {
            "name": "Cielo｜RPO服务提供商",
            "name_en": "Cielo | RPO Service Provider",
            "type": "url",
            "url": "https://www.cielotalent.com/",
            "tags": ["RPO", "服务", "全球"]
        },
        {
            "name": "AMS｜人才外包服务",
            "name_en": "AMS | Talent Outsourcing Services",
            "type": "url",
            "url": "https://www.weareams.com/",
            "tags": ["外包", "人才", "服务"]
        },
        {
            "name": "PeopleScout｜RPO与MSP服务",
            "name_en": "PeopleScout | RPO & MSP Services",
            "type": "url",
            "url": "https://www.peoplescout.com/",
            "tags": ["RPO", "MSP", "服务"]
        },
    ],

    "灵活用工与零工经济": [
        {
            "name": "Upwork｜自由职业者平台",
            "name_en": "Upwork | Freelancer Platform",
            "type": "url",
            "url": "https://www.upwork.com/",
            "tags": ["自由职业", "平台", "远程"]
        },
        {
            "name": "Toptal｜顶级自由人才",
            "name_en": "Toptal | Top Freelance Talent",
            "type": "url",
            "url": "https://www.toptal.com/",
            "tags": ["精英", "自由职业", "人才"]
        },
        {
            "name": "Fiverr Business｜企业自由职业服务",
            "name_en": "Fiverr Business | Enterprise Freelance Services",
            "type": "url",
            "url": "https://business.fiverr.com/",
            "tags": ["企业", "自由职业", "服务"]
        },
        {
            "name": "Catalant｜按需专业服务",
            "name_en": "Catalant | On-Demand Expert Services",
            "type": "url",
            "url": "https://gocatalant.com/",
            "tags": ["按需", "专业", "咨询"]
        },
    ],
}

def validate_resource(resource):
    """Validate a single resource."""
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

def find_node_by_name(node, target_name):
    """Find a node by partial name match (recursive)."""
    name = node.get('name', '')
    if target_name in name or name in target_name:
        return node

    for child in node.get('children', []):
        result = find_node_by_name(child, target_name)
        if result:
            return result
    return None

def add_resources():
    """Add new resources to tarf.json."""
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    added_count = 0
    errors = []

    for category_name, resources in NEW_RESOURCES.items():
        # Find the category node
        cat_node = find_node_by_name(data, category_name)

        if not cat_node:
            errors.append(f"Category not found: {category_name}")
            continue

        # Ensure children array exists
        if 'children' not in cat_node:
            cat_node['children'] = []

        # Get existing URLs to avoid duplicates
        existing_urls = set()
        def collect_urls(node):
            if node.get('url'):
                existing_urls.add(node['url'])
            for child in node.get('children', []):
                collect_urls(child)
        collect_urls(data)

        # Add each resource
        for resource in resources:
            valid, msg = validate_resource(resource)
            if not valid:
                errors.append(f"Invalid resource in {category_name}: {msg}")
                continue

            if resource['url'] in existing_urls:
                print(f"  Skipping duplicate: {resource['name']}")
                continue

            cat_node['children'].append(resource)
            existing_urls.add(resource['url'])
            added_count += 1

    # Save updated data
    with open('docs/tarf.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return added_count, errors

def cross_validate():
    """Cross-validate the data."""
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    errors = []
    urls = []

    def check_node(node, path=""):
        current_path = f"{path}/{node.get('name', '')}"

        # Check name_en for Chinese
        name_en = node.get('name_en', '')
        if re.search(r'[\u4e00-\u9fff]', name_en):
            errors.append(f"Chinese in name_en: {current_path}")

        # Collect URLs
        if node.get('url'):
            urls.append((node['url'], current_path))

        for child in node.get('children', []):
            check_node(child, current_path)

    check_node(data)

    # Check for duplicate URLs
    url_counts = {}
    for url, path in urls:
        if url in url_counts:
            url_counts[url].append(path)
        else:
            url_counts[url] = [path]

    duplicates = {url: paths for url, paths in url_counts.items() if len(paths) > 1}

    return errors, duplicates, len(urls)

def count_nodes(node):
    """Count total nodes."""
    count = 1
    for child in node.get('children', []):
        count += count_nodes(child)
    return count

if __name__ == "__main__":
    print("=== Batch 3: Adding Verified Resources ===\n")

    # Add resources
    added, add_errors = add_resources()
    print(f"Added {added} new resources")

    if add_errors:
        print(f"\nAdd errors:")
        for err in add_errors:
            print(f"  - {err}")

    # Cross-validate
    print("\n=== Cross-Validation ===")
    val_errors, duplicates, url_count = cross_validate()

    if val_errors:
        print(f"\nValidation errors ({len(val_errors)}):")
        for err in val_errors[:10]:
            print(f"  - {err}")
    else:
        print("✓ No Chinese found in name_en fields")

    if duplicates:
        print(f"\nDuplicate URLs ({len(duplicates)}):")
        for url, paths in list(duplicates.items())[:5]:
            print(f"  - {url}")
    else:
        print("✓ No duplicate URLs found")

    # Final stats
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    total_nodes = count_nodes(data)
    print(f"\n=== Final Statistics ===")
    print(f"Total nodes: {total_nodes}")
    print(f"Total URLs: {url_count}")
    print(f"Unique URLs: {len(set(u for u, _ in cross_validate()[2:]))}")
