#!/usr/bin/env python3
"""
AI 招聘工具 资源补充脚本 (Batch 2)
Additional cross-validated resources for AI recruiting tools
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== JD 写作/招聘文案 =====
    "JD 写作/招聘文案": [
        {
            "name": "Applied（包容性招聘平台）",
            "name_en": "Applied (Inclusive Hiring Platform)",
            "type": "url",
            "url": "https://www.beapplied.com/",
            "tags": ["AI", "JD Writing", "Blind Hiring"]
        },
        {
            "name": "Gender Decoder（性别偏见检测）",
            "name_en": "Gender Decoder (Gender Bias Detection)",
            "type": "url",
            "url": "https://gender-decoder.katmatfield.com/",
            "tags": ["AI", "JD Writing", "Free Tool"]
        },
        {
            "name": "Recruitee JD Templates（职位模板库）",
            "name_en": "Recruitee JD Templates (Job Description Library)",
            "type": "url",
            "url": "https://recruitee.com/job-descriptions",
            "tags": ["Templates", "JD Writing", "Free"]
        },
    ],

    # ===== 智能寻才/人才匹配 =====
    "智能寻才/人才匹配": [
        {
            "name": "Talentful（嵌入式招聘）",
            "name_en": "Talentful (Embedded Recruiting)",
            "type": "url",
            "url": "https://www.talentful.com/",
            "tags": ["AI", "Sourcing", "Embedded"]
        },
        {
            "name": "Toptal（顶级人才市场）",
            "name_en": "Toptal (Top Talent Marketplace)",
            "type": "url",
            "url": "https://www.toptal.com/",
            "tags": ["AI", "Marketplace", "Freelance"]
        },
        {
            "name": "Turing（全球开发者平台）",
            "name_en": "Turing (Global Developer Platform)",
            "type": "url",
            "url": "https://www.turing.com/",
            "tags": ["AI", "Sourcing", "Remote"]
        },
        {
            "name": "Talent.io（欧洲科技招聘）",
            "name_en": "Talent.io (European Tech Recruiting)",
            "type": "url",
            "url": "https://www.talent.io/",
            "tags": ["AI", "Marketplace", "Europe"]
        },
        {
            "name": "HackerRank Sourcing（技术人才发现）",
            "name_en": "HackerRank Sourcing (Tech Talent Discovery)",
            "type": "url",
            "url": "https://www.hackerrank.com/products/developer-sourcing/",
            "tags": ["AI", "Sourcing", "Technical"]
        },
    ],

    # ===== AI 候选人沟通/Chatbot =====
    "AI 候选人沟通/Chatbot": [
        {
            "name": "Talkpush（高容量招聘聊天）",
            "name_en": "Talkpush (High-Volume Recruiting Chat)",
            "type": "url",
            "url": "https://talkpush.com/",
            "tags": ["AI", "Chatbot", "High Volume"]
        },
        {
            "name": "Wade & Wendy（AI招聘助手）",
            "name_en": "Wade & Wendy (AI Recruiting Assistant)",
            "type": "url",
            "url": "https://wadeandwendy.ai/",
            "tags": ["AI", "Chatbot", "Assistant"]
        },
        {
            "name": "JobPal（多渠道招聘聊天）",
            "name_en": "JobPal (Multi-Channel Recruiting Chat)",
            "type": "url",
            "url": "https://www.jobpal.ai/",
            "tags": ["AI", "Chatbot", "Multi-Channel"]
        },
        {
            "name": "Dialpad AI（智能语音通话）",
            "name_en": "Dialpad AI (AI-Powered Voice)",
            "type": "url",
            "url": "https://www.dialpad.com/",
            "tags": ["AI", "Communication", "Voice"]
        },
    ],

    # ===== AI 简历解析/筛选 =====
    "AI 简历解析/筛选": [
        {
            "name": "Textkernel（AI匹配与解析）",
            "name_en": "Textkernel (AI Matching & Parsing)",
            "type": "url",
            "url": "https://www.textkernel.com/",
            "tags": ["AI", "Resume", "Matching"]
        },
        {
            "name": "Hireability（无障碍简历解析）",
            "name_en": "Hireability (Accessible Resume Parsing)",
            "type": "url",
            "url": "https://www.hireability.com/",
            "tags": ["AI", "Resume", "Accessibility"]
        },
        {
            "name": "ResumeParser.ai（简历解析服务）",
            "name_en": "ResumeParser.ai (Resume Parsing Service)",
            "type": "url",
            "url": "https://resumeparser.ai/",
            "tags": ["AI", "Resume", "API"]
        },
        {
            "name": "Ideal（AI候选人筛选）",
            "name_en": "Ideal (AI Candidate Screening)",
            "type": "url",
            "url": "https://ideal.com/",
            "tags": ["AI", "Screening", "Automation"]
        },
    ],

    # ===== AI 面试/测评 =====
    "AI 面试/测评": [
        {
            "name": "TripleByte（技术评估）",
            "name_en": "TripleByte (Technical Assessment)",
            "type": "url",
            "url": "https://triplebyte.com/",
            "tags": ["AI", "Assessment", "Technical"]
        },
        {
            "name": "Korn Ferry Assessment（领导力评估）",
            "name_en": "Korn Ferry Assessment (Leadership Assessment)",
            "type": "url",
            "url": "https://www.kornferry.com/solutions/products/assessments",
            "tags": ["AI", "Assessment", "Leadership"]
        },
        {
            "name": "SHL（人才测评）",
            "name_en": "SHL (Talent Assessment)",
            "type": "url",
            "url": "https://www.shl.com/",
            "tags": ["AI", "Assessment", "Enterprise"]
        },
        {
            "name": "Criteria（认知与性格测评）",
            "name_en": "Criteria (Cognitive & Personality Testing)",
            "type": "url",
            "url": "https://www.criteriacorp.com/",
            "tags": ["AI", "Assessment", "Psychometric"]
        },
        {
            "name": "Prevue HR（员工潜力评估）",
            "name_en": "Prevue HR (Employee Potential Assessment)",
            "type": "url",
            "url": "https://www.prevuehr.com/",
            "tags": ["AI", "Assessment", "Predictive"]
        },
    ],

    # ===== 招聘数据分析/洞察 =====
    "招聘数据分析/洞察": [
        {
            "name": "Lightcast（劳动力市场数据）",
            "name_en": "Lightcast (Labor Market Data)",
            "type": "url",
            "url": "https://lightcast.io/",
            "tags": ["AI", "Analytics", "Labor Market"]
        },
        {
            "name": "Talent Insights LinkedIn（LinkedIn人才洞察）",
            "name_en": "LinkedIn Talent Insights",
            "type": "url",
            "url": "https://business.linkedin.com/talent-solutions/talent-insights",
            "tags": ["AI", "Analytics", "LinkedIn"]
        },
        {
            "name": "Revelio Labs（人力资本智能）",
            "name_en": "Revelio Labs (Workforce Intelligence)",
            "type": "url",
            "url": "https://www.reveliolabs.com/",
            "tags": ["AI", "Analytics", "Intelligence"]
        },
        {
            "name": "Dataiku HR Analytics（HR数据科学）",
            "name_en": "Dataiku HR Analytics",
            "type": "url",
            "url": "https://www.dataiku.com/solutions/hr-analytics/",
            "tags": ["AI", "Analytics", "Data Science"]
        },
        {
            "name": "Peakon（员工参与度分析）",
            "name_en": "Peakon (Employee Engagement Analytics)",
            "type": "url",
            "url": "https://www.workday.com/en-us/products/employee-voice/overview.html",
            "tags": ["AI", "Analytics", "Engagement"]
        },
    ],

    # ===== AI 招聘工具 (直接子节点) =====
    "AI 招聘工具": [
        {
            "name": "Workable（一体化招聘软件）",
            "name_en": "Workable (All-in-One Recruiting Software)",
            "type": "url",
            "url": "https://www.workable.com/",
            "tags": ["AI", "ATS", "SMB"]
        },
        {
            "name": "Breezy HR（现代招聘平台）",
            "name_en": "Breezy HR (Modern Recruiting Platform)",
            "type": "url",
            "url": "https://breezy.hr/",
            "tags": ["AI", "ATS", "Visual Pipeline"]
        },
        {
            "name": "Zoho Recruit（招聘管理系统）",
            "name_en": "Zoho Recruit (Recruiting Management)",
            "type": "url",
            "url": "https://www.zoho.com/recruit/",
            "tags": ["AI", "ATS", "Affordable"]
        },
        {
            "name": "Recruitee（协作招聘平台）",
            "name_en": "Recruitee (Collaborative Hiring)",
            "type": "url",
            "url": "https://recruitee.com/",
            "tags": ["AI", "ATS", "Collaboration"]
        },
        {
            "name": "Fountain（小时工招聘平台）",
            "name_en": "Fountain (Hourly Workforce Hiring)",
            "type": "url",
            "url": "https://www.fountain.com/",
            "tags": ["AI", "High Volume", "Hourly"]
        },
        {
            "name": "Ashby（现代ATS与分析）",
            "name_en": "Ashby (Modern ATS & Analytics)",
            "type": "url",
            "url": "https://www.ashbyhq.com/",
            "tags": ["AI", "ATS", "Analytics"]
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
