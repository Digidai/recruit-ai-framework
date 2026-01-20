#!/usr/bin/env python3
"""Add English translations to tarf.json"""

import json
import re

# Translation mapping for categories and subcategories
TRANSLATIONS = {
    # Root
    "Recruitment & AI Hiring Framework（招聘 × AI 招聘框架）": "Recruitment & AI Hiring Framework",

    # Main categories (01-58)
    "01 招聘流程与方法论": "01 Recruitment Process & Methodology",
    "02 市场/薪酬/职位与技能字典": "02 Market/Compensation/Job & Skills Dictionary",
    "03 渠道：职位发布 & 招聘营销": "03 Channels: Job Posting & Recruitment Marketing",
    "04 渠道：人才画像（公开档案/社区）": "04 Channels: Talent Profiles (Public Profiles/Communities)",
    "05 Sourcing：搜索模板（X-Ray / Boolean）": "05 Sourcing: Search Templates (X-Ray / Boolean)",
    "06 ATS / CRM / 招聘协作": "06 ATS / CRM / Recruitment Collaboration",
    "07 测评与面试（Assessments & Interviewing）": "07 Assessments & Interviewing",
    "08 Offer / 背调 / 入职": "08 Offer / Background Check / Onboarding",
    "09 AI 招聘应用场景（工具/平台）": "09 AI Recruiting Applications (Tools/Platforms)",
    "10 AI 风险治理与合规（Hiring AI）": "10 AI Risk Governance & Compliance (Hiring AI)",
    "11 开源组件（公平性/审计/工具）": "11 Open Source Components (Fairness/Audit/Tools)",
    "12 全球招聘 / EOR / 远程团队": "12 Global Hiring / EOR / Remote Teams",
    "13 员工推荐 / 内部流动": "13 Employee Referrals / Internal Mobility",
    "14 学习资源 / 研究社区": "14 Learning Resources / Research Communities",
    "15 生成式 AI / LLM 招聘应用": "15 Generative AI / LLM Recruiting Applications",
    "16 校园招聘 / 实习生": "16 Campus Recruiting / Internships",
    "17 高管招聘 / Executive Search": "17 Executive Search",
    "18 RPO / 招聘外包": "18 RPO / Recruitment Outsourcing",
    "19 薪酬透明度法规": "19 Pay Transparency Regulations",
    "20 招聘 API / 开发者资源": "20 Recruiting APIs / Developer Resources",
    "21 候选人体验 / 雇主品牌": "21 Candidate Experience / Employer Brand",
    "22 行业垂直招聘": "22 Industry Vertical Recruiting",
    "23 招聘数据隐私与合规": "23 Recruiting Data Privacy & Compliance",
    "24 人才盘点与继任计划": "24 Talent Review & Succession Planning",
    "25 招聘自动化与工作流": "25 Recruitment Automation & Workflows",
    "26 面试官培训与招聘培训": "26 Interviewer Training & Recruiting Training",
    "27 招聘行业活动与会议": "27 Recruiting Industry Events & Conferences",
    "28 退伍军人招聘": "28 Veteran Recruiting",
    "29 残障人士 / 无障碍招聘": "29 Disability / Accessible Recruiting",
    "30 区域招聘资源": "30 Regional Recruiting Resources",
    "31 招聘播客与媒体": "31 Recruiting Podcasts & Media",
    "32 招聘模板与工具包": "32 Recruiting Templates & Toolkits",
    "33 招聘心理学与行为科学": "33 Recruiting Psychology & Behavioral Science",
    "34 招聘法律与劳动法": "34 Recruiting Law & Employment Law",
    "35 招聘分析与 People Analytics": "35 Recruiting Analytics & People Analytics",
    "36 远程面试与虚拟招聘": "36 Remote Interviews & Virtual Recruiting",
    "37 招聘营销与内容创作": "37 Recruitment Marketing & Content Creation",
    "38 技术招聘专项": "38 Technical Recruiting",
    "39 人才市场情报与竞争分析": "39 Talent Market Intelligence & Competitive Analysis",
    "40 招聘反欺诈与验证": "40 Recruiting Anti-Fraud & Verification",
    "41 灵活用工与零工经济": "41 Flexible Workforce & Gig Economy",
    "42 招聘游戏化与 VR/AR": "42 Gamification & VR/AR in Recruiting",
    "43 招聘预算与 ROI": "43 Recruiting Budget & ROI",
    "44 知名公司招聘实践": "44 Notable Company Recruiting Practices",
    "45 招聘文档与知识库": "45 Recruiting Documentation & Knowledge Base",
    "46 招聘职业发展": "46 Recruiting Career Development",
    "47 招聘伦理与公平招聘": "47 Recruiting Ethics & Fair Hiring",
    "48 内部招聘与人才流动": "48 Internal Recruiting & Talent Mobility",
    "49 招聘视觉与品牌设计": "49 Recruiting Visual & Brand Design",
    "50 候选人关系管理 (CRM)": "50 Candidate Relationship Management (CRM)",
    "51 神经多样性招聘": "51 Neurodiversity Recruiting",
    "52 蓝领与一线员工招聘": "52 Blue-Collar & Frontline Recruiting",
    "53 招聘效率与生产力工具": "53 Recruiting Efficiency & Productivity Tools",
    "54 AI 面试与评估技术": "54 AI Interview & Assessment Technology",
    "55 招聘行业研究与报告": "55 Recruiting Industry Research & Reports",
    "56 人才社区与人才库建设": "56 Talent Communities & Talent Pool Building",
    "57 招聘视频与多媒体": "57 Recruiting Video & Multimedia",
    "58 招聘协作与团队管理": "58 Recruiting Collaboration & Team Management",

    # Subcategories - Category 01
    "结构化面试 / 选拔方法": "Structured Interviews / Selection Methods",
    "合规：选拔/测评/面试": "Compliance: Selection/Assessment/Interviewing",
    "招聘官网/职位结构化数据（SEO）": "Career Sites / Job Posting Structured Data (SEO)",
    "招聘指标与基准": "Recruiting Metrics & Benchmarks",

    # Subcategories - Category 02
    "职位/技能字典": "Job / Skills Dictionary",
    "薪酬/劳动力数据": "Compensation / Labor Market Data",

    # Subcategories - Category 03
    "国际主流招聘平台": "Major International Job Boards",
    "技术/工程人才招聘平台": "Tech / Engineering Talent Platforms",
    "中国招聘平台": "China Job Boards",
    "多元化招聘平台 (DEI)": "Diversity Recruiting Platforms (DEI)",
    "招聘营销平台": "Recruitment Marketing Platforms",
    "自由职业/零工平台": "Freelance / Gig Platforms",

    # Subcategories - Category 04
    "技术/数据": "Tech / Data",
    "设计/产品": "Design / Product",
    "学术/研究": "Academia / Research",
    "职业社交": "Professional Networking",

    # Subcategories - Category 05
    "LinkedIn X-Ray": "LinkedIn X-Ray",
    "GitHub 搜索": "GitHub Search",
    "其他平台搜索": "Other Platform Search",
    "Boolean 搜索指南": "Boolean Search Guides",

    # Subcategories - Category 06
    "ATS（企业级）": "ATS (Enterprise)",
    "ATS（中小企业）": "ATS (SMB)",
    "ATS（中国）": "ATS (China)",
    "开源 ATS": "Open Source ATS",
    "AI Sourcing 工具": "AI Sourcing Tools",
    "面试排期工具": "Interview Scheduling Tools",

    # Subcategories - Category 07
    "技术测评平台": "Technical Assessment Platforms",
    "通用测评/心理测评": "General / Psychometric Assessments",
    "AI 测评/游戏化评估": "AI Assessment / Gamified Assessments",
    "视频面试平台": "Video Interview Platforms",
    "面试指南/资源": "Interview Guides / Resources",

    # Subcategories - Category 08
    "背景调查服务": "Background Check Services",
    "合规参考（背调）": "Compliance Reference (Background Checks)",
    "Offer 管理": "Offer Management",
    "入职软件": "Onboarding Software",

    # Subcategories - Category 09
    "JD 写作/招聘文案": "JD Writing / Recruiting Copy",
    "智能寻才/人才匹配": "Smart Sourcing / Talent Matching",
    "AI 候选人沟通/Chatbot": "AI Candidate Communication / Chatbot",
    "AI 简历解析/筛选": "AI Resume Parsing / Screening",
    "AI 面试/测评": "AI Interview / Assessment",
    "招聘数据分析/洞察": "Recruiting Data Analytics / Insights",

    # Subcategories - Category 10
    "国际标准/框架": "International Standards / Frameworks",
    "美国招聘 AI 法规": "US Hiring AI Regulations",
    "欧盟 AI 法规": "EU AI Regulations",
    "偏差审计/合规服务": "Bias Audit / Compliance Services",
    "透明度/文档化": "Transparency / Documentation",
    "负责任 AI 指南": "Responsible AI Guidelines",

    # Subcategories - Category 11
    "公平性评估/偏差审计": "Fairness Assessment / Bias Audit",
    "可解释 AI (XAI)": "Explainable AI (XAI)",
    "招聘/HR 开源项目": "Recruiting / HR Open Source Projects",

    # Subcategories - Category 12
    "EOR（雇主代记录）服务": "EOR (Employer of Record) Services",
    "国际薪酬/合规": "International Payroll / Compliance",
    "远程工作资源": "Remote Work Resources",

    # Subcategories - Category 13
    "员工推荐平台": "Employee Referral Platforms",
    "内部流动/人才市场": "Internal Mobility / Talent Marketplace",

    # Subcategories - Category 14
    "HR/招聘行业组织": "HR / Recruiting Industry Organizations",
    "AI/ML 公平性研究": "AI/ML Fairness Research",
    "书籍/课程": "Books / Courses",
    "AI 招聘报告/研究": "AI Recruiting Reports / Research",

    # Subcategories - Category 15
    "LLM 招聘助手/Agent": "LLM Recruiting Assistant / Agent",
    "AI 面试/模拟面试": "AI Interview / Mock Interview",
    "AI 简历工具": "AI Resume Tools",
    "LLM 开发框架/API": "LLM Development Frameworks / APIs",

    # Subcategories - Category 16
    "校园招聘平台（国际）": "Campus Recruiting Platforms (International)",
    "校园招聘平台（中国）": "Campus Recruiting Platforms (China)",
    "实习管理平台": "Internship Management Platforms",

    # Subcategories - Category 17
    "全球高管猎头公司": "Global Executive Search Firms",
    "高管评估工具": "Executive Assessment Tools",
    "Board / C-Suite 招聘": "Board / C-Suite Recruiting",

    # Subcategories - Category 18
    "RPO 服务商（全球）": "RPO Providers (Global)",
    "人才外包/派遣": "Talent Outsourcing / Staffing",
    "RPO 行业资源": "RPO Industry Resources",

    # Subcategories - Category 19
    "美国各州法规": "US State Regulations",
    "欧盟/国际法规": "EU / International Regulations",
    "薪酬公平工具": "Pay Equity Tools",

    # Subcategories - Category 20
    "招聘平台 API": "Job Board APIs",
    "HR 数据集成": "HR Data Integration",
    "简历/技能 API": "Resume / Skills APIs",
    "开发者工具/SDK": "Developer Tools / SDKs",

    # Subcategories - Category 21
    "候选人体验平台": "Candidate Experience Platforms",
    "雇主品牌/EVP": "Employer Brand / EVP",
    "员工评价网站": "Employee Review Sites",
    "招聘营销内容": "Recruitment Marketing Content",

    # Subcategories - Category 22
    "医疗/生命科学": "Healthcare / Life Sciences",
    "金融/法律": "Finance / Legal",
    "蓝领/服务业": "Blue-Collar / Service Industry",
    "政府/公共部门": "Government / Public Sector",
    "创意/媒体": "Creative / Media",

    # Subcategories - Category 23
    "GDPR 与招聘": "GDPR & Recruiting",
    "美国数据隐私法": "US Data Privacy Laws",
    "中国数据安全法规": "China Data Security Regulations",
    "隐私合规工具": "Privacy Compliance Tools",
    "候选人数据管理": "Candidate Data Management",

    # Subcategories - Category 24
    "人才盘点平台": "Talent Review Platforms",
    "继任计划工具": "Succession Planning Tools",
    "9-Box / 人才矩阵": "9-Box / Talent Matrix",
    "技能图谱/能力模型": "Skills Mapping / Competency Models",

    # Subcategories - Category 25
    "工作流自动化平台": "Workflow Automation Platforms",
    "招聘自动化工具": "Recruiting Automation Tools",
    "邮件自动化/序列": "Email Automation / Sequences",
    "RPA（机器人流程自动化）": "RPA (Robotic Process Automation)",

    # Subcategories - Category 26
    "面试官培训平台": "Interviewer Training Platforms",
    "招聘技能培训": "Recruiting Skills Training",
    "无意识偏见培训": "Unconscious Bias Training",
    "面试指南/最佳实践": "Interview Guides / Best Practices",

    # Subcategories - Category 27
    "HR Tech 会议": "HR Tech Conferences",
    "招聘/Sourcing 会议": "Recruiting / Sourcing Conferences",
    "DEI / 多元化会议": "DEI / Diversity Conferences",
    "AI / 未来工作会议": "AI / Future of Work Conferences",

    # Subcategories - Category 28
    "退伍军人招聘平台": "Veteran Recruiting Platforms",
    "军转民技能翻译": "Military Skills Translation",
    "退伍军人招聘认证": "Veteran Recruiting Certifications",

    # Subcategories - Category 29
    "残障人士招聘平台": "Disability Recruiting Platforms",
    "无障碍合规": "Accessibility Compliance",
    "无障碍招聘工具": "Accessible Recruiting Tools",
    "神经多样性招聘": "Neurodiversity Recruiting",

    # Subcategories - Category 30
    "亚太地区（APAC）": "Asia-Pacific (APAC)",
    "中东/非洲（MEA）": "Middle East / Africa (MEA)",
    "拉丁美洲（LATAM）": "Latin America (LATAM)",
    "欧洲（补充）": "Europe (Supplementary)",

    # Subcategories - Category 31
    "招聘播客": "Recruiting Podcasts",
    "招聘行业媒体": "Recruiting Industry Media",
    "招聘 Newsletter": "Recruiting Newsletters",
    "YouTube 频道": "YouTube Channels",

    # Subcategories - Category 32
    "JD 模板库": "JD Template Library",
    "面试评分卡/指南": "Interview Scorecards / Guides",
    "招聘漏斗/报告模板": "Recruiting Funnel / Report Templates",
    "Offer Letter / 合同模板": "Offer Letter / Contract Templates",
    "入职检查清单": "Onboarding Checklists",

    # Subcategories - Category 33
    "招聘决策科学": "Recruiting Decision Science",
    "认知偏差与招聘": "Cognitive Bias & Recruiting",
    "人才评估心理学": "Talent Assessment Psychology",
    "候选人体验心理学": "Candidate Experience Psychology",

    # Subcategories - Category 34
    "美国劳动法": "US Employment Law",
    "国际劳动法": "International Employment Law",
    "中国劳动法": "China Labor Law",
    "雇佣法律资源": "Employment Law Resources",

    # Subcategories - Category 35
    "People Analytics 平台": "People Analytics Platforms",
    "招聘仪表盘/BI": "Recruiting Dashboard / BI",
    "招聘指标/KPI 框架": "Recruiting Metrics / KPI Frameworks",
    "People Analytics 学习资源": "People Analytics Learning Resources",

    # Subcategories - Category 36
    "视频面试平台": "Video Interview Platforms",
    "虚拟招聘会平台": "Virtual Career Fair Platforms",
    "远程协作工具": "Remote Collaboration Tools",
    "虚拟入职平台": "Virtual Onboarding Platforms",

    # Subcategories - Category 37
    "招聘营销平台": "Recruitment Marketing Platforms",
    "职位广告优化": "Job Ad Optimization",
    "社交媒体招聘": "Social Media Recruiting",
    "内容创作工具": "Content Creation Tools",

    # Subcategories - Category 38
    "技术面试平台": "Technical Interview Platforms",
    "技术技能评估": "Technical Skills Assessment",
    "技术社区招聘": "Tech Community Recruiting",
    "技术招聘指南": "Technical Recruiting Guides",

    # Subcategories - Category 39
    "人才市场数据": "Talent Market Data",
    "竞争对手分析": "Competitor Analysis",
    "人才流动追踪": "Talent Flow Tracking",
    "招聘趋势报告": "Recruiting Trends Reports",

    # Subcategories - Category 40
    "身份验证": "Identity Verification",
    "学历验证": "Education Verification",
    "就业/工作验证": "Employment Verification",
    "简历欺诈检测": "Resume Fraud Detection",

    # Subcategories - Category 41
    "自由职业平台": "Freelance Platforms",
    "高端人才平台": "High-End Talent Platforms",
    "零工管理平台": "Gig Management Platforms",
    "临时用工/蓝领零工": "Temp Work / Blue-Collar Gig",

    # Subcategories - Category 42
    "游戏化评估": "Gamified Assessments",
    "VR/AR 招聘": "VR/AR Recruiting",
    "编程挑战/Hackathon": "Coding Challenges / Hackathons",

    # Subcategories - Category 43
    "招聘成本计算": "Recruiting Cost Calculation",
    "招聘 ROI 框架": "Recruiting ROI Frameworks",
    "招聘预算管理": "Recruiting Budget Management",
    "招聘供应商管理": "Recruiting Vendor Management",

    # Subcategories - Category 44
    "科技巨头招聘": "Tech Giant Recruiting",
    "创新公司文化": "Innovative Company Culture",
    "中国公司招聘实践": "China Company Recruiting Practices",
    "招聘案例研究": "Recruiting Case Studies",

    # Subcategories - Category 45
    "招聘政策模板": "Recruiting Policy Templates",
    "知识管理平台": "Knowledge Management Platforms",
    "招聘 SOP 资源": "Recruiting SOP Resources",
    "术语表/词典": "Glossary / Dictionary",

    # Subcategories - Category 46
    "招聘职业路径": "Recruiting Career Paths",
    "专业认证": "Professional Certifications",
    "招聘社区": "Recruiting Communities",
    "薪酬基准": "Compensation Benchmarks",

    # Subcategories - Category 47
    "公平招聘框架": "Fair Hiring Frameworks",
    "招聘偏见检测": "Recruiting Bias Detection",
    "AI 招聘伦理": "AI Recruiting Ethics",
    "招聘道德规范": "Recruiting Code of Ethics",

    # Subcategories - Category 48
    "内部流动平台": "Internal Mobility Platforms",
    "技能图谱与职业路径": "Skills Mapping & Career Paths",
    "内部招聘最佳实践": "Internal Recruiting Best Practices",
    "员工推荐系统": "Employee Referral Systems",

    # Subcategories - Category 49
    "设计工具": "Design Tools",
    "雇主品牌视觉": "Employer Brand Visuals",
    "招聘社交媒体": "Recruiting Social Media",
    "招聘网站设计": "Career Site Design",

    # Subcategories - Category 50
    "专业招聘 CRM": "Professional Recruiting CRM",
    "人才库管理": "Talent Pool Management",
    "候选人沟通自动化": "Candidate Communication Automation",
    "候选人体验": "Candidate Experience",

    # Subcategories - Category 51
    "神经多样性项目": "Neurodiversity Programs",
    "专业招聘机构": "Specialized Recruiting Agencies",
    "资源与研究": "Resources & Research",
    "适配工具": "Accommodation Tools",

    # Subcategories - Category 52
    "蓝领招聘平台": "Blue-Collar Recruiting Platforms",
    "行业专业平台": "Industry-Specific Platforms",
    "移动招聘方案": "Mobile Recruiting Solutions",
    "批量招聘工具": "High-Volume Recruiting Tools",

    # Subcategories - Category 53
    "日程协调": "Scheduling",
    "邮件与沟通": "Email & Communication",
    "笔记与协作": "Notes & Collaboration",
    "自动化工具": "Automation Tools",
    "Chrome 扩展": "Chrome Extensions",

    # Subcategories - Category 54
    "AI 视频面试": "AI Video Interview",
    "AI 面试助手": "AI Interview Assistant",
    "AI 编程面试": "AI Coding Interview",
    "心理测评 AI": "Psychometric AI",
    "AI 面试研究": "AI Interview Research",

    # Subcategories - Category 55
    "年度报告": "Annual Reports",
    "咨询公司研究": "Consulting Firm Research",
    "行业分析": "Industry Analysis",
    "学术研究": "Academic Research",
    "数据与统计": "Data & Statistics",

    # Subcategories - Category 56
    "社区平台": "Community Platforms",
    "人才库工具": "Talent Pool Tools",
    "Alumni 网络": "Alumni Networks",
    "社区运营": "Community Operations",

    # Subcategories - Category 57
    "视频制作工具": "Video Production Tools",
    "招聘视频平台": "Recruiting Video Platforms",
    "员工故事": "Employee Stories",
    "虚拟办公室参观": "Virtual Office Tours",

    # Subcategories - Category 58
    "招聘团队协作": "Recruiting Team Collaboration",
    "项目管理": "Project Management",
    "沟通工具": "Communication Tools",
    "绩效与目标": "Performance & Goals",
    "招聘运营 (RecOps)": "Recruiting Operations (RecOps)",
}


def add_translations(node):
    """Recursively add name_en to nodes"""
    name = node.get("name", "")

    # Check if translation exists
    if name in TRANSLATIONS:
        node["name_en"] = TRANSLATIONS[name]
    else:
        # Only fill when name_en is missing or blank to avoid overwriting existing translations.
        existing_en = node.get("name_en", "")
        if not existing_en or not existing_en.strip():
            node["name_en"] = name

    # Process children recursively
    if "children" in node:
        for child in node["children"]:
            add_translations(child)

    return node


def main():
    # Read tarf.json
    with open("docs/tarf.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Add translations
    add_translations(data)

    # Write back
    with open("docs/tarf.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Translations added successfully!")


if __name__ == "__main__":
    main()
