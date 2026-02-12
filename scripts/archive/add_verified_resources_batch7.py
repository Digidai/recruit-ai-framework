#!/usr/bin/env python3
"""
Batch 7: Add verified resources to tarf.json
Cross-validated resources covering weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== 游戏化与 VR/AR 招聘 =====
    "游戏化与 VR/AR 招聘": [
        {
            "name": "Vervoe（AI技能测试）",
            "name_en": "Vervoe (AI Skills Testing)",
            "type": "url",
            "url": "https://vervoe.com/",
            "tags": ["VR", "Assessment", "AI"]
        },
        {
            "name": "Sova Assessment（游戏化评估）",
            "name_en": "Sova Assessment (Gamified Assessment)",
            "type": "url",
            "url": "https://www.sovaassessment.com/",
            "tags": ["Gamification", "Assessment"]
        },
        {
            "name": "The Talent Games（人才游戏）",
            "name_en": "The Talent Games",
            "type": "url",
            "url": "https://thetalentgames.com/",
            "tags": ["Gamification", "Assessment"]
        },
    ],

    # ===== 游戏化评估 =====
    "游戏化评估": [
        {
            "name": "Arctic Shores（行为评估游戏）",
            "name_en": "Arctic Shores (Behavioral Assessment Games)",
            "type": "url",
            "url": "https://www.arcticshores.com/",
            "tags": ["Gamification", "Psychology"]
        },
        {
            "name": "Talegent（人才评估）",
            "name_en": "Talegent (Talent Assessment)",
            "type": "url",
            "url": "https://www.talegent.com/",
            "tags": ["Gamification", "Psychometric"]
        },
    ],

    # ===== 领英 X-Ray =====
    "领英 X-Ray": [
        {
            "name": "RecruitEm（X-Ray搜索工具）",
            "name_en": "RecruitEm (X-Ray Search Tool)",
            "type": "url",
            "url": "https://recruitin.net/",
            "tags": ["Sourcing", "Boolean", "Free"]
        },
        {
            "name": "Careerflow X-Ray Search（职业流搜索）",
            "name_en": "Careerflow X-Ray Search",
            "type": "url",
            "url": "https://hiring-search.careerflow.ai/",
            "tags": ["Sourcing", "LinkedIn"]
        },
    ],

    # ===== AI 视频面试 =====
    "AI 视频面试": [
        {
            "name": "VidCruiter（视频招聘）",
            "name_en": "VidCruiter (Video Recruiting)",
            "type": "url",
            "url": "https://vidcruiter.com/",
            "tags": ["Video", "Interview", "Enterprise"]
        },
        {
            "name": "Willo（异步视频面试）",
            "name_en": "Willo (Async Video Interview)",
            "type": "url",
            "url": "https://www.willo.video/",
            "tags": ["Video", "Async", "SMB"]
        },
        {
            "name": "InterWiz（AI面试平台）",
            "name_en": "InterWiz (AI Interview Platform)",
            "type": "url",
            "url": "https://interwiz.ai/",
            "tags": ["AI", "Interview"]
        },
    ],

    # ===== 视频面试平台 =====
    "视频面试平台": [
        {
            "name": "Spark Hire（视频面试）",
            "name_en": "Spark Hire (Video Interview)",
            "type": "url",
            "url": "https://www.sparkhire.com/",
            "tags": ["Video", "Interview"]
        },
        {
            "name": "Hireflix（单向视频面试）",
            "name_en": "Hireflix (One-way Video Interview)",
            "type": "url",
            "url": "https://www.hireflix.com/",
            "tags": ["Video", "Async"]
        },
        {
            "name": "Jobma（全球视频面试）",
            "name_en": "Jobma (Global Video Interview)",
            "type": "url",
            "url": "https://www.jobma.com/",
            "tags": ["Video", "Global"]
        },
        {
            "name": "Hirevire（AI视频筛选）",
            "name_en": "Hirevire (AI Video Screening)",
            "type": "url",
            "url": "https://hirevire.com/",
            "tags": ["Video", "AI", "SMB"]
        },
    ],

    # ===== 候选人体验平台 =====
    "候选人体验平台": [
        {
            "name": "Medallia（体验管理）",
            "name_en": "Medallia (Experience Management)",
            "type": "url",
            "url": "https://www.medallia.com/",
            "tags": ["CX", "Survey", "Enterprise"]
        },
        {
            "name": "Starred（候选人反馈）",
            "name_en": "Starred (Candidate Feedback)",
            "type": "url",
            "url": "https://www.starred.com/",
            "tags": ["CX", "Survey", "Analytics"]
        },
    ],

    # ===== 候选人关系管理 =====
    "候选人关系管理": [
        {
            "name": "Beamery（人才生命周期管理）",
            "name_en": "Beamery (Talent Lifecycle Management)",
            "type": "url",
            "url": "https://beamery.com/",
            "tags": ["CRM", "AI", "Enterprise"]
        },
        {
            "name": "Avature（招聘CRM）",
            "name_en": "Avature (Recruiting CRM)",
            "type": "url",
            "url": "https://www.avature.net/",
            "tags": ["CRM", "Marketing", "Enterprise"]
        },
        {
            "name": "Phenom（人才体验平台）",
            "name_en": "Phenom (Talent Experience Platform)",
            "type": "url",
            "url": "https://www.phenom.com/",
            "tags": ["TXM", "AI", "Enterprise"]
        },
    ],

    # ===== 校园招聘与实习 =====
    "校园招聘与实习": [
        {
            "name": "Yello（校园招聘）",
            "name_en": "Yello (Campus Recruiting)",
            "type": "url",
            "url": "https://yello.co/",
            "tags": ["Campus", "Events", "Enterprise"]
        },
        {
            "name": "Handshake（大学人才平台）",
            "name_en": "Handshake (University Talent Platform)",
            "type": "url",
            "url": "https://joinhandshake.com/",
            "tags": ["Campus", "Students"]
        },
        {
            "name": "RippleMatch（早期人才）",
            "name_en": "RippleMatch (Early Career Talent)",
            "type": "url",
            "url": "https://ripplematch.com/",
            "tags": ["Campus", "AI", "DEI"]
        },
        {
            "name": "WayUp（学生/毕业生招聘）",
            "name_en": "WayUp (Student/Graduate Recruiting)",
            "type": "url",
            "url": "https://www.wayup.com/",
            "tags": ["Campus", "Diversity"]
        },
    ],

    # ===== DEI / 多元化会议 =====
    "DEI / 多元化会议": [
        {
            "name": "SHRM Inclusion Conference（SHRM多元化会议）",
            "name_en": "SHRM Inclusion Conference",
            "type": "url",
            "url": "https://conferences.shrm.org/inclusion",
            "tags": ["DEI", "Conference", "HR"]
        },
        {
            "name": "D&I Leaders Global Forum（多元化领袖论坛）",
            "name_en": "D&I Leaders Global Forum",
            "type": "url",
            "url": "https://www.dileaders.com/",
            "tags": ["DEI", "Conference", "Global"]
        },
        {
            "name": "Seramount Events（DEI活动）",
            "name_en": "Seramount DEI Events",
            "type": "url",
            "url": "https://seramount.com/events-conferences/",
            "tags": ["DEI", "Conference", "Leadership"]
        },
    ],

    # ===== RPO 行业资源 =====
    "RPO 行业资源": [
        {
            "name": "Cielo Talent（全球RPO）",
            "name_en": "Cielo Talent (Global RPO)",
            "type": "url",
            "url": "https://www.cielotalent.com/",
            "tags": ["RPO", "Global", "Enterprise"]
        },
        {
            "name": "PeopleScout（RPO解决方案）",
            "name_en": "PeopleScout (RPO Solutions)",
            "type": "url",
            "url": "https://www.peoplescout.com/",
            "tags": ["RPO", "MSP", "Enterprise"]
        },
        {
            "name": "Sevenstep（人才收购RPO）",
            "name_en": "Sevenstep (Talent Acquisition RPO)",
            "type": "url",
            "url": "https://www.sevensteprpo.com/",
            "tags": ["RPO", "Analytics"]
        },
        {
            "name": "Hudson RPO（全球人才）",
            "name_en": "Hudson RPO (Global Talent)",
            "type": "url",
            "url": "https://www.hudsonrpo.com/",
            "tags": ["RPO", "Global"]
        },
        {
            "name": "WilsonHCG（人才解决方案）",
            "name_en": "WilsonHCG (Talent Solutions)",
            "type": "url",
            "url": "https://www.wilsonhcg.com/",
            "tags": ["RPO", "Consulting"]
        },
    ],

    # ===== 员工故事 =====
    "员工故事": [
        {
            "name": "PathMotion（员工与候选人社区）",
            "name_en": "PathMotion (Employee-Candidate Community)",
            "type": "url",
            "url": "https://www.pathmotion.com/",
            "tags": ["EB", "Employee Advocacy"]
        },
        {
            "name": "The Martec（AI员工视频）",
            "name_en": "The Martec (AI Employee Videos)",
            "type": "url",
            "url": "https://www.themartec.com/",
            "tags": ["EB", "Video", "AI"]
        },
    ],

    # ===== 招聘反欺诈与验证 =====
    "招聘反欺诈与验证": [
        {
            "name": "Checkr（AI背景调查）",
            "name_en": "Checkr (AI Background Check)",
            "type": "url",
            "url": "https://checkr.com/",
            "tags": ["Background Check", "AI"]
        },
        {
            "name": "HireRight（全球背景筛选）",
            "name_en": "HireRight (Global Background Screening)",
            "type": "url",
            "url": "https://www.hireright.com/",
            "tags": ["Background Check", "Global"]
        },
        {
            "name": "GoodHire（中小企业背调）",
            "name_en": "GoodHire (SMB Background Check)",
            "type": "url",
            "url": "https://www.goodhire.com/",
            "tags": ["Background Check", "SMB"]
        },
    ],

    # ===== 全球招聘与远程团队 =====
    "全球招聘与远程团队": [
        {
            "name": "Remote OK（远程工作平台）",
            "name_en": "Remote OK (Remote Job Platform)",
            "type": "url",
            "url": "https://remoteok.com/",
            "tags": ["Remote", "Job Board"]
        },
        {
            "name": "Remote.co（远程工作资源）",
            "name_en": "Remote.co (Remote Work Resource)",
            "type": "url",
            "url": "https://remote.co/",
            "tags": ["Remote", "Resource"]
        },
        {
            "name": "NoDesk（远程工作社区）",
            "name_en": "NoDesk (Remote Work Community)",
            "type": "url",
            "url": "https://nodesk.co/",
            "tags": ["Remote", "Community"]
        },
        {
            "name": "Crossover（远程人才市场）",
            "name_en": "Crossover (Remote Talent Marketplace)",
            "type": "url",
            "url": "https://www.crossover.com/",
            "tags": ["Remote", "Marketplace"]
        },
    ],

    # ===== 招聘数据分析 =====
    "招聘数据分析": [
        {
            "name": "Visier（人员分析平台）",
            "name_en": "Visier (People Analytics Platform)",
            "type": "url",
            "url": "https://www.visier.com/",
            "tags": ["Analytics", "AI", "Enterprise"]
        },
        {
            "name": "Tableau HR Analytics（人力资源分析）",
            "name_en": "Tableau HR Analytics",
            "type": "url",
            "url": "https://www.tableau.com/solutions/human-resources-analytics",
            "tags": ["Analytics", "BI", "Visualization"]
        },
        {
            "name": "Zoho Analytics HR（HR分析）",
            "name_en": "Zoho Analytics HR",
            "type": "url",
            "url": "https://www.zoho.com/analytics/hr-analytics.html",
            "tags": ["Analytics", "SMB"]
        },
    ],

    # ===== 招聘自动化排程 =====
    "招聘自动化排程": [
        {
            "name": "GoodTime（面试协调）",
            "name_en": "GoodTime (Interview Coordination)",
            "type": "url",
            "url": "https://www.goodtime.io/",
            "tags": ["Scheduling", "AI", "Enterprise"]
        },
        {
            "name": "Cronofy（日历API）",
            "name_en": "Cronofy (Calendar API)",
            "type": "url",
            "url": "https://www.cronofy.com/",
            "tags": ["Scheduling", "API", "Integration"]
        },
        {
            "name": "Calendly Recruiting（招聘排程）",
            "name_en": "Calendly Recruiting",
            "type": "url",
            "url": "https://calendly.com/solutions/recruiting",
            "tags": ["Scheduling", "Free"]
        },
    ],

    # ===== 心理测评 AI =====
    "心理测评 AI": [
        {
            "name": "Hogan Assessments（霍根评估）",
            "name_en": "Hogan Assessments",
            "type": "url",
            "url": "https://www.hoganassessments.com/",
            "tags": ["Psychometric", "Personality"]
        },
        {
            "name": "Criteria Corp（认知与行为测试）",
            "name_en": "Criteria Corp (Cognitive & Behavioral Testing)",
            "type": "url",
            "url": "https://www.criteriacorp.com/",
            "tags": ["Psychometric", "AI"]
        },
        {
            "name": "SHL Assessment（人才评估）",
            "name_en": "SHL Assessment (Talent Assessment)",
            "type": "url",
            "url": "https://www.shl.com/",
            "tags": ["Psychometric", "Enterprise"]
        },
    ],

    # ===== AI 聊天机器人招聘 =====
    "AI 聊天机器人招聘": [
        {
            "name": "Paradox/Olivia（对话式招聘AI）",
            "name_en": "Paradox/Olivia (Conversational Recruiting AI)",
            "type": "url",
            "url": "https://www.paradox.ai/",
            "tags": ["Chatbot", "AI", "Enterprise"]
        },
        {
            "name": "XOR（AI招聘助手）",
            "name_en": "XOR (AI Recruiting Assistant)",
            "type": "url",
            "url": "https://www.xor.ai/",
            "tags": ["Chatbot", "AI", "High-Volume"]
        },
        {
            "name": "Sense（人才参与平台）",
            "name_en": "Sense (Talent Engagement Platform)",
            "type": "url",
            "url": "https://www.sensehq.com/",
            "tags": ["Chatbot", "Engagement"]
        },
    ],

    # ===== 远程面试与虚拟招聘 =====
    "远程面试与虚拟招聘": [
        {
            "name": "Truffle（AI面试分析）",
            "name_en": "Truffle (AI Interview Analysis)",
            "type": "url",
            "url": "https://www.hiretruffle.com/",
            "tags": ["Video", "AI", "SMB"]
        },
        {
            "name": "Zappyhire（招聘自动化）",
            "name_en": "Zappyhire (Recruitment Automation)",
            "type": "url",
            "url": "https://www.zappyhire.com/",
            "tags": ["Automation", "AI"]
        },
    ],

    # ===== 人才盘点与继任计划 =====
    "人才盘点与继任计划": [
        {
            "name": "Eightfold.ai（人才智能）",
            "name_en": "Eightfold.ai (Talent Intelligence)",
            "type": "url",
            "url": "https://eightfold.ai/",
            "tags": ["AI", "Skills", "Enterprise"]
        },
        {
            "name": "TalentGuard（职业路径）",
            "name_en": "TalentGuard (Career Pathing)",
            "type": "url",
            "url": "https://www.talentguard.com/",
            "tags": ["Succession", "Development"]
        },
    ],

    # ===== 招聘运营 (RecOps) =====
    "招聘运营 (RecOps)": [
        {
            "name": "Ashby（现代招聘平台）",
            "name_en": "Ashby (Modern Recruiting Platform)",
            "type": "url",
            "url": "https://www.ashbyhq.com/",
            "tags": ["ATS", "Analytics", "RecOps"]
        },
        {
            "name": "Gem（人才CRM）",
            "name_en": "Gem (Talent CRM)",
            "type": "url",
            "url": "https://www.gem.com/",
            "tags": ["CRM", "Sourcing", "RecOps"]
        },
    ],

    # ===== 批量招聘工具 =====
    "批量招聘工具": [
        {
            "name": "Fountain（高流量招聘）",
            "name_en": "Fountain (High-Volume Hiring)",
            "type": "url",
            "url": "https://www.fountain.com/",
            "tags": ["High-Volume", "Hourly"]
        },
        {
            "name": "Harver（批量招聘评估）",
            "name_en": "Harver (Volume Hiring Assessment)",
            "type": "url",
            "url": "https://harver.com/",
            "tags": ["High-Volume", "Assessment"]
        },
    ],

    # ===== GitHub 搜索 =====
    "GitHub 搜索": [
        {
            "name": "GitHub Talent Search（开发者搜索）",
            "name_en": "GitHub Talent Search",
            "type": "url",
            "url": "https://github.com/search",
            "tags": ["Sourcing", "Developer"]
        },
        {
            "name": "GitHunt（GitHub人才发现）",
            "name_en": "GitHunt (GitHub Talent Discovery)",
            "type": "url",
            "url": "https://kamranahmed.info/githunt/",
            "tags": ["Sourcing", "Open Source"]
        },
    ],

    # ===== 招聘文档与知识库 =====
    "招聘文档与知识库": [
        {
            "name": "Notion HR Templates（HR模板）",
            "name_en": "Notion HR Templates",
            "type": "url",
            "url": "https://www.notion.so/templates/category/hr",
            "tags": ["Templates", "Knowledge"]
        },
        {
            "name": "Confluence HR（协作知识库）",
            "name_en": "Confluence HR (Collaborative KB)",
            "type": "url",
            "url": "https://www.atlassian.com/software/confluence/templates/human-resources",
            "tags": ["Templates", "Collaboration"]
        },
    ],
}


def find_node_by_name(node, target_name):
    """Recursively find a node by name"""
    if node.get('name') == target_name:
        return node
    for child in node.get('children', []):
        result = find_node_by_name(child, target_name)
        if result:
            return result
    return None


def get_all_urls(node):
    """Get all existing URLs in the tree"""
    urls = set()
    if node.get('type') == 'url' and node.get('url'):
        urls.add(node.get('url'))
    for child in node.get('children', []):
        urls.update(get_all_urls(child))
    return urls


def get_all_names(node):
    """Get all existing names in the tree"""
    names = set()
    name = node.get('name', '')
    if name:
        names.add(name)
    for child in node.get('children', []):
        names.update(get_all_names(child))
    return names


def add_resources(data):
    """Add new resources to the appropriate categories"""
    existing_urls = get_all_urls(data)
    existing_names = get_all_names(data)

    added = 0
    skipped = 0
    errors = 0

    for category_name, resources in NEW_RESOURCES.items():
        parent = find_node_by_name(data, category_name)
        if not parent:
            print(f"⚠️  Category not found: {category_name}")
            errors += len(resources)
            continue

        if 'children' not in parent:
            parent['children'] = []

        for resource in resources:
            url = resource.get('url', '')
            name = resource.get('name', '')

            # Check for duplicates
            if url in existing_urls:
                print(f"⏭️  Skipped (URL exists): {resource['name_en']}")
                skipped += 1
                continue

            if name in existing_names:
                print(f"⏭️  Skipped (name exists): {resource['name_en']}")
                skipped += 1
                continue

            parent['children'].append(resource)
            existing_urls.add(url)
            existing_names.add(name)
            print(f"✅ Added: {resource['name_en']} -> {category_name}")
            added += 1

    return added, skipped, errors


def main():
    print("Loading tarf.json...")
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    added, skipped, errors = add_resources(data)

    print("\nSaving tarf.json...")
    with open('docs/tarf.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"""
{'='*60}
Summary:
  ✅ Added: {added}
  ⏭️  Skipped: {skipped}
  ❌ Errors: {errors}
{'='*60}""")


if __name__ == '__main__':
    main()
