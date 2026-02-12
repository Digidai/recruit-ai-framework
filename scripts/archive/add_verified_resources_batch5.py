#!/usr/bin/env python3
"""
Batch 5: Add verified resources to tarf.json
Cross-validated resources for remaining weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== 批量招聘工具 =====
    "批量招聘工具": [
        {
            "name": "Harver（高流量招聘）",
            "name_en": "Harver (High-Volume Hiring)",
            "type": "url",
            "url": "https://harver.com/",
            "tags": ["High-Volume", "AI"]
        },
        {
            "name": "Oleeo（批量招聘软件）",
            "name_en": "Oleeo (Volume Recruiting Software)",
            "type": "url",
            "url": "https://www.oleeo.com/",
            "tags": ["High-Volume", "Enterprise"]
        },
        {
            "name": "Paradox Olivia（对话式 AI）",
            "name_en": "Paradox Olivia (Conversational AI)",
            "type": "url",
            "url": "https://www.paradox.ai/",
            "tags": ["Chatbot", "AI"]
        },
    ],

    # ===== 游戏化评估 =====
    "游戏化评估": [
        {
            "name": "Pymetrics（游戏化软技能）",
            "name_en": "Pymetrics (Gamified Soft Skills)",
            "type": "url",
            "url": "https://www.pymetrics.ai/",
            "tags": ["Gamification", "AI"]
        },
        {
            "name": "Arctic Shores（行为游戏测评）",
            "name_en": "Arctic Shores (Behavior Game Assessment)",
            "type": "url",
            "url": "https://www.arcticshores.com/",
            "tags": ["Gamification", "Behavior"]
        },
        {
            "name": "HireVue Games（游戏化测评）",
            "name_en": "HireVue Games (Gamified Assessment)",
            "type": "url",
            "url": "https://www.hirevue.com/products/assessments",
            "tags": ["Gamification", "Video"]
        },
    ],

    # ===== EOR（雇主代记录）服务 =====
    "EOR（雇主代记录）服务": [
        {
            "name": "Deel（全球 EOR）",
            "name_en": "Deel (Global EOR)",
            "type": "url",
            "url": "https://www.deel.com/",
            "tags": ["EOR", "Global"]
        },
        {
            "name": "Remote.com（远程雇佣）",
            "name_en": "Remote.com (Remote Employment)",
            "type": "url",
            "url": "https://remote.com/",
            "tags": ["EOR", "Remote"]
        },
        {
            "name": "Oyster HR（全球 HR 平台）",
            "name_en": "Oyster HR (Global HR Platform)",
            "type": "url",
            "url": "https://www.oysterhr.com/",
            "tags": ["EOR", "SMB"]
        },
        {
            "name": "Papaya Global（全球薪酬）",
            "name_en": "Papaya Global (Global Payroll)",
            "type": "url",
            "url": "https://www.papayaglobal.com/",
            "tags": ["EOR", "Payroll"]
        },
        {
            "name": "Velocity Global（国际雇佣）",
            "name_en": "Velocity Global (International Employment)",
            "type": "url",
            "url": "https://velocityglobal.com/",
            "tags": ["EOR", "Enterprise"]
        },
    ],

    # ===== AI 候选人沟通/Chatbot =====
    "AI 候选人沟通/Chatbot": [
        {
            "name": "Mya Systems（AI 聊天机器人）",
            "name_en": "Mya Systems (AI Chatbot)",
            "type": "url",
            "url": "https://www.mya.com/",
            "tags": ["Chatbot", "AI"]
        },
        {
            "name": "XOR AI（多渠道对话）",
            "name_en": "XOR AI (Multichannel Conversation)",
            "type": "url",
            "url": "https://xor.ai/",
            "tags": ["Chatbot", "SMS"]
        },
        {
            "name": "Humanly.io（AI 招聘助手）",
            "name_en": "Humanly.io (AI Recruiting Assistant)",
            "type": "url",
            "url": "https://humanly.io/",
            "tags": ["Chatbot", "DEI"]
        },
        {
            "name": "Sense（人才互动平台）",
            "name_en": "Sense (Talent Engagement Platform)",
            "type": "url",
            "url": "https://www.sensehq.com/",
            "tags": ["Engagement", "AI"]
        },
    ],

    # ===== 员工推荐系统 =====
    "员工推荐系统": [
        {
            "name": "Boon（AI 推荐平台）",
            "name_en": "Boon (AI Referral Platform)",
            "type": "url",
            "url": "https://www.goboon.co/",
            "tags": ["Referral", "AI"]
        },
        {
            "name": "Teamable（社交网络推荐）",
            "name_en": "Teamable (Social Network Referrals)",
            "type": "url",
            "url": "https://www.teamable.com/",
            "tags": ["Referral", "Social"]
        },
        {
            "name": "RolePoint/iCIMS（企业推荐）",
            "name_en": "RolePoint/iCIMS (Enterprise Referrals)",
            "type": "url",
            "url": "https://www.icims.com/products/talent-cloud-platform/engage/",
            "tags": ["Referral", "Enterprise"]
        },
    ],

    # ===== 内部流动平台 =====
    "内部流动平台": [
        {
            "name": "Gloat（人才市场）",
            "name_en": "Gloat (Talent Marketplace)",
            "type": "url",
            "url": "https://www.gloat.com/",
            "tags": ["Mobility", "AI"]
        },
        {
            "name": "Fuel50（职业路径）",
            "name_en": "Fuel50 (Career Pathing)",
            "type": "url",
            "url": "https://fuel50.com/",
            "tags": ["Mobility", "Career"]
        },
        {
            "name": "Hitch Works（内部人才）",
            "name_en": "Hitch Works (Internal Talent)",
            "type": "url",
            "url": "https://www.hitch.works/",
            "tags": ["Mobility", "Platform"]
        },
    ],

    # ===== 继任计划工具 =====
    "继任计划工具": [
        {
            "name": "Lattice（绩效与继任）",
            "name_en": "Lattice (Performance & Succession)",
            "type": "url",
            "url": "https://lattice.com/",
            "tags": ["Performance", "Succession"]
        },
        {
            "name": "Betterworks（目标与绩效）",
            "name_en": "Betterworks (Goals & Performance)",
            "type": "url",
            "url": "https://www.betterworks.com/",
            "tags": ["OKR", "Performance"]
        },
        {
            "name": "Culture Amp（人员分析）",
            "name_en": "Culture Amp (People Analytics)",
            "type": "url",
            "url": "https://www.cultureamp.com/",
            "tags": ["Engagement", "Analytics"]
        },
        {
            "name": "15Five（绩效管理）",
            "name_en": "15Five (Performance Management)",
            "type": "url",
            "url": "https://www.15five.com/",
            "tags": ["Performance", "Feedback"]
        },
    ],

    # ===== 招聘流程外包 (RPO) =====
    "招聘流程外包 (RPO)": [
        {
            "name": "Cielo Talent（全球 RPO）",
            "name_en": "Cielo Talent (Global RPO)",
            "type": "url",
            "url": "https://www.cielotalent.com/",
            "tags": ["RPO", "Global"]
        },
        {
            "name": "AMS（Alexander Mann Solutions）",
            "name_en": "AMS (Alexander Mann Solutions)",
            "type": "url",
            "url": "https://www.weareams.com/",
            "tags": ["RPO", "Enterprise"]
        },
        {
            "name": "Kforce（人才 RPO）",
            "name_en": "Kforce (Talent RPO)",
            "type": "url",
            "url": "https://www.kforce.com/",
            "tags": ["RPO", "Staffing"]
        },
        {
            "name": "Hays RPO（全球 RPO）",
            "name_en": "Hays RPO (Global RPO)",
            "type": "url",
            "url": "https://www.hays.com/recruitment-services/rpo",
            "tags": ["RPO", "Global"]
        },
    ],

    # ===== 职位/技能字典 =====
    "职位/技能字典": [
        {
            "name": "Lightcast Open Skills（开放技能库）",
            "name_en": "Lightcast Open Skills (Open Skills Library)",
            "type": "url",
            "url": "https://lightcast.io/open-skills",
            "tags": ["Skills", "Taxonomy"]
        },
        {
            "name": "O*NET OnLine（职业信息）",
            "name_en": "O*NET OnLine (Occupation Information)",
            "type": "url",
            "url": "https://www.onetonline.org/",
            "tags": ["Occupation", "US"]
        },
        {
            "name": "ESCO（欧洲技能分类）",
            "name_en": "ESCO (European Skills Classification)",
            "type": "url",
            "url": "https://esco.ec.europa.eu/",
            "tags": ["Skills", "EU"]
        },
    ],

    # ===== 招聘数据分析/洞察 =====
    "招聘数据分析/洞察": [
        {
            "name": "Visier Talent Acquisition（人才获取分析）",
            "name_en": "Visier Talent Acquisition Analytics",
            "type": "url",
            "url": "https://www.visier.com/products/talent-acquisition-insights/",
            "tags": ["Analytics", "Enterprise"]
        },
        {
            "name": "Eightfold AI（人才智能）",
            "name_en": "Eightfold AI (Talent Intelligence)",
            "type": "url",
            "url": "https://eightfold.ai/",
            "tags": ["AI", "Analytics"]
        },
        {
            "name": "Findem（人才数据平台）",
            "name_en": "Findem (Talent Data Platform)",
            "type": "url",
            "url": "https://www.findem.ai/",
            "tags": ["AI", "Sourcing"]
        },
    ],

    # ===== VR/AR 招聘 =====
    "VR/AR 招聘": [
        {
            "name": "Strivr（VR 培训与评估）",
            "name_en": "Strivr (VR Training & Assessment)",
            "type": "url",
            "url": "https://www.strivr.com/",
            "tags": ["VR", "Training"]
        },
        {
            "name": "Talespin（XR 学习）",
            "name_en": "Talespin (XR Learning)",
            "type": "url",
            "url": "https://www.talespin.com/",
            "tags": ["VR", "Learning"]
        },
        {
            "name": "Virbela（虚拟工作空间）",
            "name_en": "Virbela (Virtual Workspace)",
            "type": "url",
            "url": "https://www.virbela.com/",
            "tags": ["VR", "Remote"]
        },
    ],

    # ===== JD 模板库 =====
    "JD 模板库": [
        {
            "name": "SHRM Job Descriptions（SHRM 职位描述）",
            "name_en": "SHRM Job Descriptions",
            "type": "url",
            "url": "https://www.shrm.org/topics-tools/tools/job-descriptions",
            "tags": ["Template", "Official"]
        },
        {
            "name": "Indeed Job Description Templates（Indeed 模板）",
            "name_en": "Indeed Job Description Templates",
            "type": "url",
            "url": "https://www.indeed.com/hire/job-description-templates",
            "tags": ["Template", "Free"]
        },
        {
            "name": "Workable Job Descriptions（Workable 模板）",
            "name_en": "Workable Job Descriptions",
            "type": "url",
            "url": "https://resources.workable.com/job-descriptions/",
            "tags": ["Template", "Free"]
        },
        {
            "name": "Betterteam Job Descriptions（Betterteam 模板）",
            "name_en": "Betterteam Job Description Templates",
            "type": "url",
            "url": "https://www.betterteam.com/job-descriptions",
            "tags": ["Template", "Free"]
        },
    ],

    # ===== 招聘漏斗/报告模板 =====
    "招聘漏斗/报告模板": [
        {
            "name": "Workable Recruiting Reports（招聘报告）",
            "name_en": "Workable Recruiting Reports",
            "type": "url",
            "url": "https://www.workable.com/recruiting-reports",
            "tags": ["Reporting", "ATS"]
        },
        {
            "name": "Greenhouse Reporting（招聘报告）",
            "name_en": "Greenhouse Reporting",
            "type": "url",
            "url": "https://www.greenhouse.com/features/reporting",
            "tags": ["Reporting", "ATS"]
        },
        {
            "name": "AIHR Recruitment Metrics（招聘指标指南）",
            "name_en": "AIHR Recruitment Metrics Guide",
            "type": "url",
            "url": "https://www.aihr.com/blog/recruiting-metrics/",
            "tags": ["Metrics", "Guide"]
        },
    ],

    # ===== 面试评分卡/指南 =====
    "面试评分卡/指南": [
        {
            "name": "Lever Interview Scorecard（面试评分卡）",
            "name_en": "Lever Interview Scorecard",
            "type": "url",
            "url": "https://www.lever.co/blog/interview-scorecard/",
            "tags": ["Scorecard", "Guide"]
        },
        {
            "name": "Greenhouse Scorecards（评分卡功能）",
            "name_en": "Greenhouse Scorecards",
            "type": "url",
            "url": "https://www.greenhouse.com/features/scorecards",
            "tags": ["Scorecard", "ATS"]
        },
        {
            "name": "Workable Interview Evaluation（面试评估）",
            "name_en": "Workable Interview Evaluation",
            "type": "url",
            "url": "https://resources.workable.com/interview-evaluation-form",
            "tags": ["Scorecard", "Free"]
        },
    ],

    # ===== 招聘 SOP 资源 =====
    "招聘 SOP 资源": [
        {
            "name": "SHRM Recruitment Process（招聘流程）",
            "name_en": "SHRM Recruitment Process Guide",
            "type": "url",
            "url": "https://www.shrm.org/topics-tools/tools/toolkits/practising-strategic-human-resources-recruitment-selection",
            "tags": ["SOP", "Guide"]
        },
        {
            "name": "SHRM HR Forms（HR 表单）",
            "name_en": "SHRM HR Forms",
            "type": "url",
            "url": "https://www.shrm.org/topics-tools/tools/forms",
            "tags": ["Forms", "Templates"]
        },
        {
            "name": "Process Street Recruiting（招聘清单）",
            "name_en": "Process Street Recruiting Checklists",
            "type": "url",
            "url": "https://www.process.st/checklist-templates/hr-recruiting/",
            "tags": ["SOP", "Checklist"]
        },
    ],

    # ===== 技能图谱/能力模型 =====
    "技能图谱/能力模型": [
        {
            "name": "Lightcast Taxonomies（技能分类）",
            "name_en": "Lightcast Taxonomies (Skills & Jobs)",
            "type": "url",
            "url": "https://lightcast.io/products/data/our-taxonomies",
            "tags": ["Skills", "Data"]
        },
        {
            "name": "TechWolf（技能 AI）",
            "name_en": "TechWolf (Skills AI)",
            "type": "url",
            "url": "https://www.techwolf.com/",
            "tags": ["Skills", "AI"]
        },
        {
            "name": "Workday Skills Cloud（技能云）",
            "name_en": "Workday Skills Cloud",
            "type": "url",
            "url": "https://www.workday.com/en-us/products/human-capital-management/skills-cloud.html",
            "tags": ["Skills", "Enterprise"]
        },
    ],

    # ===== 人才市场数据 =====
    "人才市场数据": [
        {
            "name": "Lightcast（劳动力市场数据）",
            "name_en": "Lightcast (Labor Market Data)",
            "type": "url",
            "url": "https://lightcast.io/",
            "tags": ["Data", "Market"]
        },
        {
            "name": "LinkedIn Talent Insights（人才洞察）",
            "name_en": "LinkedIn Talent Insights",
            "type": "url",
            "url": "https://business.linkedin.com/talent-solutions/talent-insights",
            "tags": ["Data", "LinkedIn"]
        },
        {
            "name": "Bureau of Labor Statistics（美国劳工统计）",
            "name_en": "Bureau of Labor Statistics (US Labor Data)",
            "type": "url",
            "url": "https://www.bls.gov/",
            "tags": ["Data", "US"]
        },
    ],

    # ===== 蓝领招聘平台 =====
    "蓝领招聘平台": [
        {
            "name": "Jobcase（蓝领社区）",
            "name_en": "Jobcase (Blue-Collar Community)",
            "type": "url",
            "url": "https://www.jobcase.com/",
            "tags": ["Blue-Collar", "Community"]
        },
        {
            "name": "TeamBridge（制造业招聘）",
            "name_en": "TeamBridge (Manufacturing Recruiting)",
            "type": "url",
            "url": "https://www.teambridge.com/",
            "tags": ["Blue-Collar", "Manufacturing"]
        },
        {
            "name": "Hireology（服务业招聘）",
            "name_en": "Hireology (Service Industry Recruiting)",
            "type": "url",
            "url": "https://www.hireology.com/",
            "tags": ["Blue-Collar", "Service"]
        },
    ],

    # ===== 招聘 Newsletter =====
    "招聘 Newsletter": [
        {
            "name": "Hung Lee Recruiting Brainfood",
            "name_en": "Hung Lee Recruiting Brainfood",
            "type": "url",
            "url": "https://www.recruitingbrainfood.com/",
            "tags": ["Newsletter", "Weekly"]
        },
        {
            "name": "ERE Daily（招聘新闻）",
            "name_en": "ERE Daily (Recruiting News)",
            "type": "url",
            "url": "https://www.ere.net/",
            "tags": ["Newsletter", "News"]
        },
        {
            "name": "TLNT（HR 新闻）",
            "name_en": "TLNT (HR News)",
            "type": "url",
            "url": "https://www.tlnt.com/",
            "tags": ["Newsletter", "HR"]
        },
        {
            "name": "HR Dive（HR 行业新闻）",
            "name_en": "HR Dive (HR Industry News)",
            "type": "url",
            "url": "https://www.hrdive.com/",
            "tags": ["Newsletter", "Industry"]
        },
    ],

    # ===== 远程协作工具 =====
    "远程协作工具": [
        {
            "name": "Slack（团队协作）",
            "name_en": "Slack (Team Collaboration)",
            "type": "url",
            "url": "https://slack.com/",
            "tags": ["Collaboration", "Chat"]
        },
        {
            "name": "Notion（知识管理）",
            "name_en": "Notion (Knowledge Management)",
            "type": "url",
            "url": "https://www.notion.so/",
            "tags": ["Collaboration", "Wiki"]
        },
        {
            "name": "Miro（可视化协作）",
            "name_en": "Miro (Visual Collaboration)",
            "type": "url",
            "url": "https://miro.com/",
            "tags": ["Collaboration", "Whiteboard"]
        },
    ],

    # ===== 虚拟入职平台 =====
    "虚拟入职平台": [
        {
            "name": "Click Boarding（数字入职）",
            "name_en": "Click Boarding (Digital Onboarding)",
            "type": "url",
            "url": "https://www.clickboarding.com/",
            "tags": ["Onboarding", "Digital"]
        },
        {
            "name": "Talmundo（入职体验）",
            "name_en": "Talmundo (Onboarding Experience)",
            "type": "url",
            "url": "https://talmundo.com/",
            "tags": ["Onboarding", "Experience"]
        },
        {
            "name": "Appical（入职应用）",
            "name_en": "Appical (Onboarding App)",
            "type": "url",
            "url": "https://appical.com/",
            "tags": ["Onboarding", "Mobile"]
        },
    ],

    # ===== 9-Box / 人才矩阵 =====
    "9-Box / 人才矩阵": [
        {
            "name": "AIHR 9-Box Grid Guide（9 格矩阵指南）",
            "name_en": "AIHR 9-Box Grid Guide",
            "type": "url",
            "url": "https://www.aihr.com/blog/9-box-grid/",
            "tags": ["Framework", "Guide"]
        },
        {
            "name": "emPerform Succession（继任规划）",
            "name_en": "emPerform Succession Planning",
            "type": "url",
            "url": "https://employee-performance.com/features/succession/",
            "tags": ["Succession", "Software"]
        },
        {
            "name": "Teamflect 9-Box Templates（模板）",
            "name_en": "Teamflect 9-Box Templates",
            "type": "url",
            "url": "https://teamflect.com/blog/performance-management/9-box-grid-template",
            "tags": ["Template", "Free"]
        },
    ],

    # ===== AI 视频面试 =====
    "AI 视频面试": [
        {
            "name": "HireVue AI Interview（AI 视频面试）",
            "name_en": "HireVue AI Video Interview",
            "type": "url",
            "url": "https://www.hirevue.com/",
            "tags": ["AI", "Video"]
        },
        {
            "name": "Modern Hire（数字面试）",
            "name_en": "Modern Hire (Digital Interviewing)",
            "type": "url",
            "url": "https://modernhire.com/",
            "tags": ["AI", "Assessment"]
        },
        {
            "name": "Talview（远程面试）",
            "name_en": "Talview (Remote Interviewing)",
            "type": "url",
            "url": "https://www.talview.com/",
            "tags": ["AI", "Remote"]
        },
    ],

    # ===== AI 面试助手 =====
    "AI 面试助手": [
        {
            "name": "BrightHire（面试智能）",
            "name_en": "BrightHire (Interview Intelligence)",
            "type": "url",
            "url": "https://www.brighthire.com/",
            "tags": ["AI", "Recording"]
        },
        {
            "name": "Pillar（面试 AI）",
            "name_en": "Pillar (Interview AI)",
            "type": "url",
            "url": "https://www.pillar.hr/",
            "tags": ["AI", "Assistant"]
        },
        {
            "name": "Metaview（面试笔记）",
            "name_en": "Metaview (Interview Notes)",
            "type": "url",
            "url": "https://www.metaview.ai/",
            "tags": ["AI", "Notes"]
        },
    ],

    # ===== 编程挑战/Hackathon =====
    "编程挑战/Hackathon": [
        {
            "name": "HackerRank（编程挑战）",
            "name_en": "HackerRank (Coding Challenges)",
            "type": "url",
            "url": "https://www.hackerrank.com/",
            "tags": ["Coding", "Platform"]
        },
        {
            "name": "LeetCode（算法练习）",
            "name_en": "LeetCode (Algorithm Practice)",
            "type": "url",
            "url": "https://leetcode.com/",
            "tags": ["Coding", "Practice"]
        },
        {
            "name": "Devpost（Hackathon 平台）",
            "name_en": "Devpost (Hackathon Platform)",
            "type": "url",
            "url": "https://devpost.com/",
            "tags": ["Hackathon", "Community"]
        },
        {
            "name": "MLH（Major League Hacking）",
            "name_en": "MLH (Major League Hacking)",
            "type": "url",
            "url": "https://mlh.io/",
            "tags": ["Hackathon", "Student"]
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
