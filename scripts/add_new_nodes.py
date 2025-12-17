#!/usr/bin/env python3
"""Add new leaf nodes to tarf.json with bilingual support."""

import json

# New nodes to add, organized by parent category path
# Path format: "Category Name/Subcategory Name"
NEW_NODES = {
    # 05 Boolean 搜索指南
    "Boolean 搜索指南": [
        {
            "name": "Irina Shamaeva 博客（高级 Sourcing）",
            "name_en": "Irina Shamaeva Blog (Advanced Sourcing)",
            "type": "url",
            "url": "https://booleanstrings.com/blog/",
            "tags": ["Blog", "Expert"]
        },
        {
            "name": "Glen Cathey｜Boolean Black Belt",
            "name_en": "Glen Cathey | Boolean Black Belt",
            "type": "url",
            "url": "https://booleanblackbelt.com/",
            "tags": ["Blog", "Expert"]
        },
    ],

    # 04 技术/数据
    "技术/数据": [
        {
            "name": "Dev.to（开发者社区）",
            "name_en": "Dev.to (Developer Community)",
            "type": "url",
            "url": "https://dev.to/",
            "tags": ["Community", "Dev"]
        },
        {
            "name": "Hashnode（技术博客平台）",
            "name_en": "Hashnode (Tech Blog Platform)",
            "type": "url",
            "url": "https://hashnode.com/",
            "tags": ["Blog", "Dev"]
        },
        {
            "name": "IndieHackers（独立开发者）",
            "name_en": "IndieHackers (Indie Developers)",
            "type": "url",
            "url": "https://www.indiehackers.com/",
            "tags": ["Community", "Startup"]
        },
        {
            "name": "Product Hunt（产品社区）",
            "name_en": "Product Hunt (Product Community)",
            "type": "url",
            "url": "https://www.producthunt.com/",
            "tags": ["Community", "Product"]
        },
        {
            "name": "Hacker News（YC 社区）",
            "name_en": "Hacker News (YC Community)",
            "type": "url",
            "url": "https://news.ycombinator.com/",
            "tags": ["Community", "Tech"]
        },
    ],

    # 09 JD 写作/招聘文案
    "JD 写作/招聘文案": [
        {
            "name": "ChatGPT（OpenAI LLM）",
            "name_en": "ChatGPT (OpenAI LLM)",
            "type": "url",
            "url": "https://chat.openai.com/",
            "tags": ["AI", "LLM"]
        },
        {
            "name": "Claude（Anthropic LLM）",
            "name_en": "Claude (Anthropic LLM)",
            "type": "url",
            "url": "https://claude.ai/",
            "tags": ["AI", "LLM"]
        },
        {
            "name": "Jasper（AI 写作助手）",
            "name_en": "Jasper (AI Writing Assistant)",
            "type": "url",
            "url": "https://www.jasper.ai/",
            "tags": ["AI", "Writing"]
        },
    ],

    # 06 ATS（企业级）
    "ATS（企业级）": [
        {
            "name": "Pinpoint（招聘软件）",
            "name_en": "Pinpoint (Recruiting Software)",
            "type": "url",
            "url": "https://www.pinpointhq.com/",
            "tags": ["ATS", "SMB"]
        },
        {
            "name": "Recruitee（协作招聘）",
            "name_en": "Recruitee (Collaborative Hiring)",
            "type": "url",
            "url": "https://recruitee.com/",
            "tags": ["ATS", "Collaboration"]
        },
        {
            "name": "Manatal（AI ATS）",
            "name_en": "Manatal (AI ATS)",
            "type": "url",
            "url": "https://www.manatal.com/",
            "tags": ["ATS", "AI"]
        },
        {
            "name": "JazzHR（SMB ATS）",
            "name_en": "JazzHR (SMB ATS)",
            "type": "url",
            "url": "https://www.jazzhr.com/",
            "tags": ["ATS", "SMB"]
        },
    ],

    # 10 国际标准/框架
    "国际标准/框架": [
        {
            "name": "ISO/IEC 42001（AI 管理体系）",
            "name_en": "ISO/IEC 42001 (AI Management System)",
            "type": "url",
            "url": "https://www.iso.org/standard/81230.html",
            "tags": ["Standard", "Global"]
        },
        {
            "name": "IEEE 7000（伦理设计系统）",
            "name_en": "IEEE 7000 (Ethical Design Systems)",
            "type": "url",
            "url": "https://ethicsinaction.ieee.org/",
            "tags": ["Standard", "Ethics"]
        },
    ],

    # 10 美国招聘 AI 法规
    "美国招聘 AI 法规": [
        {
            "name": "科罗拉多州｜AI Act（SB21-169）",
            "name_en": "Colorado | AI Act (SB21-169)",
            "type": "url",
            "url": "https://leg.colorado.gov/bills/sb21-169",
            "tags": ["Law", "US"]
        },
        {
            "name": "伊利诺伊州｜AIPA（人工智能视频面试法）",
            "name_en": "Illinois | AIPA (AI Video Interview Act)",
            "type": "url",
            "url": "https://www.ilga.gov/legislation/publicacts/fulltext.asp?Name=101-0260",
            "tags": ["Law", "US"]
        },
    ],

    # 智能寻才/人才匹配
    "智能寻才/人才匹配": [
        {
            "name": "Findem（AI 人才搜索）",
            "name_en": "Findem (AI Talent Search)",
            "type": "url",
            "url": "https://www.findem.ai/",
            "tags": ["AI", "Sourcing"]
        },
        {
            "name": "HiredScore（AI 人才匹配）",
            "name_en": "HiredScore (AI Talent Matching)",
            "type": "url",
            "url": "https://www.hiredscore.com/",
            "tags": ["AI", "Matching"]
        },
        {
            "name": "Gem（人才关系管理）",
            "name_en": "Gem (Talent Relationship Management)",
            "type": "url",
            "url": "https://www.gem.com/",
            "tags": ["CRM", "Sourcing"]
        },
    ],

    # AI 面试/测评
    "AI 面试/测评": [
        {
            "name": "Interviewer.AI（AI 视频分析）",
            "name_en": "Interviewer.AI (AI Video Analytics)",
            "type": "url",
            "url": "https://www.interviewer.ai/",
            "tags": ["AI", "Video"]
        },
        {
            "name": "Sapia.ai（对话式 AI 面试）",
            "name_en": "Sapia.ai (Conversational AI Interview)",
            "type": "url",
            "url": "https://sapia.ai/",
            "tags": ["AI", "Chat"]
        },
        {
            "name": "Criteria Corp（AI 测评）",
            "name_en": "Criteria Corp (AI Assessment)",
            "type": "url",
            "url": "https://www.criteriacorp.com/",
            "tags": ["AI", "Assessment"]
        },
    ],

    # 13 新增员工推荐子类
    "员工推荐 / 内部流动": [
        {
            "name": "Teamable（员工推荐网络）",
            "name_en": "Teamable (Employee Referral Network)",
            "type": "url",
            "url": "https://www.teamable.com/",
            "tags": ["Referral", "Platform"]
        },
        {
            "name": "Drafted（智能推荐）",
            "name_en": "Drafted (Smart Referrals)",
            "type": "url",
            "url": "https://drafted.us/",
            "tags": ["Referral", "AI"]
        },
        {
            "name": "RolePoint（推荐自动化）",
            "name_en": "RolePoint (Referral Automation)",
            "type": "url",
            "url": "https://www.rolepoint.com/",
            "tags": ["Referral", "Automation"]
        },
        {
            "name": "ERIN（员工推荐应用）",
            "name_en": "ERIN (Employee Referral App)",
            "type": "url",
            "url": "https://erinapp.com/",
            "tags": ["Referral", "Mobile"]
        },
        {
            "name": "Boon（AI 推荐平台）",
            "name_en": "Boon (AI Referral Platform)",
            "type": "url",
            "url": "https://www.boon.io/",
            "tags": ["Referral", "AI"]
        },
    ],

    # 17 高管招聘
    "猎头与高管搜寻": [
        {
            "name": "BlueSteps（高管职业管理）",
            "name_en": "BlueSteps (Executive Career Management)",
            "type": "url",
            "url": "https://www.bluesteps.com/",
            "tags": ["Executive", "Career"]
        },
        {
            "name": "ExecuNet（高管网络）",
            "name_en": "ExecuNet (Executive Network)",
            "type": "url",
            "url": "https://www.execunet.com/",
            "tags": ["Executive", "Network"]
        },
        {
            "name": "BoardEx（董事会关系网络）",
            "name_en": "BoardEx (Board Relationship Network)",
            "type": "url",
            "url": "https://www.boardex.com/",
            "tags": ["Executive", "Data"]
        },
        {
            "name": "Thrive TRM（高管搜寻平台）",
            "name_en": "Thrive TRM (Executive Search Platform)",
            "type": "url",
            "url": "https://www.thrivetrm.com/",
            "tags": ["Executive", "Platform"]
        },
    ],

    # 42 游戏化
    "游戏化评估": [
        {
            "name": "Arctic Shores（游戏化心理测评）",
            "name_en": "Arctic Shores (Gamified Psychometrics)",
            "type": "url",
            "url": "https://www.arcticshores.com/",
            "tags": ["Gamification", "Assessment"]
        },
        {
            "name": "Knack（游戏化人才识别）",
            "name_en": "Knack (Gamified Talent Discovery)",
            "type": "url",
            "url": "https://www.knack.it/",
            "tags": ["Gamification", "AI"]
        },
        {
            "name": "Owiwi（游戏化软技能测评）",
            "name_en": "Owiwi (Gamified Soft Skills)",
            "type": "url",
            "url": "https://owiwi.co.uk/",
            "tags": ["Gamification", "Soft Skills"]
        },
    ],

    # 51 神经多样性
    "神经多样性招聘项目": [
        {
            "name": "Autism at Work（SAP）",
            "name_en": "Autism at Work (SAP)",
            "type": "url",
            "url": "https://www.sap.com/about/company/diversity/differently-abled.html",
            "tags": ["Program", "Enterprise"]
        },
        {
            "name": "Microsoft Neurodiversity Hiring",
            "name_en": "Microsoft Neurodiversity Hiring",
            "type": "url",
            "url": "https://www.microsoft.com/en-us/diversity/inside-microsoft/cross-disability/neurodiversityhiring",
            "tags": ["Program", "Enterprise"]
        },
        {
            "name": "JPMorgan Autism at Work",
            "name_en": "JPMorgan Autism at Work",
            "type": "url",
            "url": "https://www.jpmorganchase.com/impact/people/autism-at-work",
            "tags": ["Program", "Finance"]
        },
        {
            "name": "Ultranauts（神经多样性优先公司）",
            "name_en": "Ultranauts (Neurodiversity-First Company)",
            "type": "url",
            "url": "https://ultranauts.co/",
            "tags": ["Company", "QA"]
        },
    ],

    # 43 ROI 计算
    "招聘 ROI 计算": [
        {
            "name": "Cost-per-Hire Calculator（SHRM）",
            "name_en": "Cost-per-Hire Calculator (SHRM)",
            "type": "url",
            "url": "https://www.shrm.org/topics-tools/tools/hr-answers/how-do-i-calculate-cost-per-hire",
            "tags": ["Calculator", "Free"]
        },
        {
            "name": "Recruiting ROI Benchmark（Aptitude Research）",
            "name_en": "Recruiting ROI Benchmark (Aptitude Research)",
            "type": "url",
            "url": "https://www.aptituderesearch.com/",
            "tags": ["Research", "Benchmark"]
        },
        {
            "name": "Time-to-Fill Benchmark（SHRM）",
            "name_en": "Time-to-Fill Benchmark (SHRM)",
            "type": "url",
            "url": "https://www.shrm.org/",
            "tags": ["Benchmark", "Free"]
        },
    ],

    # 38 技术面试平台
    "技术面试平台": [
        {
            "name": "Karat（技术面试外包）",
            "name_en": "Karat (Technical Interview Outsourcing)",
            "type": "url",
            "url": "https://karat.com/",
            "tags": ["Interview", "Tech"]
        },
        {
            "name": "Triplebyte（技术人才评估）",
            "name_en": "Triplebyte (Tech Talent Assessment)",
            "type": "url",
            "url": "https://triplebyte.com/",
            "tags": ["Assessment", "Tech"]
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

def add_nodes():
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    added_count = 0

    for target_name, nodes in NEW_NODES.items():
        parent = find_node_by_name(data, target_name)

        if parent is None:
            print(f"Warning: Could not find: {target_name}")
            continue

        if 'children' not in parent:
            parent['children'] = []

        # Get existing node names/urls to avoid duplicates
        existing_urls = {child.get('url') for child in parent.get('children', [])}
        existing_names = {child.get('name') for child in parent.get('children', [])}

        for node in nodes:
            if node.get('url') not in existing_urls and node['name'] not in existing_names:
                parent['children'].append(node)
                added_count += 1
                print(f"Added: {node['name_en']}")
            else:
                print(f"Skipped (exists): {node['name_en']}")

    with open('docs/tarf.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\nTotal nodes added: {added_count}")

if __name__ == "__main__":
    add_nodes()
