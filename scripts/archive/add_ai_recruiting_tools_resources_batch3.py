#!/usr/bin/env python3
"""
AI 招聘工具 资源补充脚本 (Batch 3)
Cross-validated resources from web search 2024-2025
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== JD 写作/招聘文案 =====
    "JD 写作/招聘文案": [
        {
            "name": "Indeed AI职位描述（智能JD生成）",
            "name_en": "Indeed AI Job Description Generator",
            "type": "url",
            "url": "https://www.indeed.com/hire/c/info/job-description-generator",
            "tags": ["AI", "JD Writing", "Free"]
        },
        {
            "name": "Narrato（AI内容工作流）",
            "name_en": "Narrato (AI Content Workflow)",
            "type": "url",
            "url": "https://narrato.io/",
            "tags": ["AI", "JD Writing", "Content"]
        },
        {
            "name": "Recooty（智能招聘软件）",
            "name_en": "Recooty (Smart Hiring Software)",
            "type": "url",
            "url": "https://www.recooty.com/",
            "tags": ["AI", "JD Writing", "ATS"]
        },
        {
            "name": "LogicBalls JD生成器（多类型职位）",
            "name_en": "LogicBalls JD Generator",
            "type": "url",
            "url": "https://logicballs.com/tools/job-description-generator",
            "tags": ["AI", "JD Writing", "Free Tool"]
        },
        {
            "name": "Dweet AI（职位描述秒生成）",
            "name_en": "Dweet AI (Instant JD Generator)",
            "type": "url",
            "url": "https://www.dweet.com/tools/ai-job-description-generator",
            "tags": ["AI", "JD Writing", "Gender Neutral"]
        },
    ],

    # ===== 智能寻才/人才匹配 =====
    "智能寻才/人才匹配": [
        {
            "name": "Arya by Leoforce（AI招聘助手）",
            "name_en": "Arya by Leoforce (AI Recruiting Assistant)",
            "type": "url",
            "url": "https://leoforce.com/arya/",
            "tags": ["AI", "Sourcing", "80+ Channels"]
        },
        {
            "name": "Juicebox/PeopleGPT（AI人才搜索）",
            "name_en": "Juicebox/PeopleGPT (AI Talent Search)",
            "type": "url",
            "url": "https://juicebox.ai/",
            "tags": ["AI", "Sourcing", "800M+ Profiles"]
        },
        {
            "name": "GoPerfect（AI招聘软件）",
            "name_en": "GoPerfect (AI Hiring Software)",
            "type": "url",
            "url": "https://www.goperfect.com/",
            "tags": ["AI", "Sourcing", "Matching"]
        },
        {
            "name": "LinkedIn Hiring Assistant（AI招聘助理）",
            "name_en": "LinkedIn Hiring Assistant",
            "type": "url",
            "url": "https://www.linkedin.com/business/talent/blog/product-tips/hiring-assistant",
            "tags": ["AI", "Sourcing", "LinkedIn"]
        },
    ],

    # ===== AI 候选人沟通/Chatbot =====
    "AI 候选人沟通/Chatbot": [
        {
            "name": "SmartRecruiters Winston（生成式AI聊天）",
            "name_en": "SmartRecruiters Winston Chat (Generative AI)",
            "type": "url",
            "url": "https://www.smartrecruiters.com/recruiting-software/ai-chatbot/",
            "tags": ["AI", "Chatbot", "Multilingual"]
        },
        {
            "name": "PreScreenAI（AI预筛选聊天）",
            "name_en": "PreScreenAI (AI Pre-Screening Chat)",
            "type": "url",
            "url": "https://prescreenai.com/",
            "tags": ["AI", "Chatbot", "Screening"]
        },
        {
            "name": "iCIMS Digital Assistant（数字招聘助理）",
            "name_en": "iCIMS Digital Assistant",
            "type": "url",
            "url": "https://www.icims.com/products/icims-digital-assistant/",
            "tags": ["AI", "Chatbot", "Enterprise"]
        },
        {
            "name": "Workday Recruiter Agent（AI招聘代理）",
            "name_en": "Workday Recruiter Agent",
            "type": "url",
            "url": "https://www.workday.com/en-us/products/platform/ai.html",
            "tags": ["AI", "Agent", "Enterprise"]
        },
    ],

    # ===== AI 简历解析/筛选 =====
    "AI 简历解析/筛选": [
        {
            "name": "Ducknowl（AI简历筛选）",
            "name_en": "Ducknowl (AI Resume Screening)",
            "type": "url",
            "url": "https://ducknowl.com/",
            "tags": ["AI", "Resume", "300ms Parsing"]
        },
        {
            "name": "Recrew AI（简历解析优化）",
            "name_en": "Recrew AI (Resume Parsing)",
            "type": "url",
            "url": "https://www.recrew.ai/",
            "tags": ["AI", "Resume", "Automation"]
        },
        {
            "name": "CVShelf（AI简历筛选）",
            "name_en": "CVShelf (AI Resume Screening)",
            "type": "url",
            "url": "https://cvshelf.com/",
            "tags": ["AI", "Resume", "Screening"]
        },
        {
            "name": "Jobscan（求职者简历优化）",
            "name_en": "Jobscan (Resume Optimization)",
            "type": "url",
            "url": "https://www.jobscan.co/",
            "tags": ["AI", "Resume", "Job Seeker"]
        },
    ],

    # ===== AI 面试/测评 =====
    "AI 面试/测评": [
        {
            "name": "Jobma（多语言视频面试）",
            "name_en": "Jobma (Multilingual Video Interview)",
            "type": "url",
            "url": "https://www.jobma.com/",
            "tags": ["AI", "Interview", "SOC 2"]
        },
        {
            "name": "VidCruiter（企业视频面试）",
            "name_en": "VidCruiter (Enterprise Video Interview)",
            "type": "url",
            "url": "https://www.vidcruiter.com/",
            "tags": ["AI", "Interview", "Enterprise"]
        },
        {
            "name": "iMocha（技能智能平台）",
            "name_en": "iMocha (Skills Intelligence Platform)",
            "type": "url",
            "url": "https://www.imocha.io/",
            "tags": ["AI", "Assessment", "Skills-First"]
        },
        {
            "name": "InCruiter（专家辅助面试）",
            "name_en": "InCruiter (Expert-Led Interviews)",
            "type": "url",
            "url": "https://incruiter.com/",
            "tags": ["AI", "Interview", "Panel"]
        },
        {
            "name": "Veloxhire AI（AI视频面试）",
            "name_en": "Veloxhire AI (AI Video Interview)",
            "type": "url",
            "url": "https://veloxhire.ai/",
            "tags": ["AI", "Interview", "Screening"]
        },
        {
            "name": "TestGorilla（科学测评平台）",
            "name_en": "TestGorilla (Science-Backed Tests)",
            "type": "url",
            "url": "https://www.testgorilla.com/",
            "tags": ["AI", "Assessment", "350+ Tests"]
        },
        {
            "name": "Testlify（技能测评平台）",
            "name_en": "Testlify (Skills Assessment Platform)",
            "type": "url",
            "url": "https://testlify.com/",
            "tags": ["AI", "Assessment", "3000+ Tests"]
        },
        {
            "name": "Vervoe（技能验证平台）",
            "name_en": "Vervoe (Skills Verification Platform)",
            "type": "url",
            "url": "https://vervoe.com/",
            "tags": ["AI", "Assessment", "Job Simulation"]
        },
        {
            "name": "Harver（高容量预筛选）",
            "name_en": "Harver (Volume Hiring Assessment)",
            "type": "url",
            "url": "https://harver.com/",
            "tags": ["AI", "Assessment", "Volume Hiring"]
        },
        {
            "name": "Toggl Hire（技能优先招聘）",
            "name_en": "Toggl Hire (Skills-First Hiring)",
            "type": "url",
            "url": "https://toggl.com/hire/",
            "tags": ["AI", "Assessment", "Anti-Cheat"]
        },
    ],

    # ===== 招聘数据分析/洞察 =====
    "招聘数据分析/洞察": [
        {
            "name": "Fuel50（AI人才市场）",
            "name_en": "Fuel50 (AI Talent Marketplace)",
            "type": "url",
            "url": "https://www.fuel50.com/",
            "tags": ["AI", "Analytics", "Internal Mobility"]
        },
        {
            "name": "Paylocity（HR分析模块）",
            "name_en": "Paylocity (HR Analytics Module)",
            "type": "url",
            "url": "https://www.paylocity.com/",
            "tags": ["AI", "Analytics", "Predictive"]
        },
        {
            "name": "Aura Workforce Analytics（人力分析）",
            "name_en": "Aura (Workforce Analytics)",
            "type": "url",
            "url": "https://getaura.ai/",
            "tags": ["AI", "Analytics", "Workforce"]
        },
        {
            "name": "HiredScore（人才智能分析）",
            "name_en": "HiredScore (Talent Intelligence)",
            "type": "url",
            "url": "https://www.hiredscore.com/",
            "tags": ["AI", "Analytics", "Workday"]
        },
    ],

    # ===== AI 招聘工具 (直接子节点) =====
    "AI 招聘工具": [
        {
            "name": "Radancy（智能人才平台）",
            "name_en": "Radancy (Intelligent Talent Platform)",
            "type": "url",
            "url": "https://radancy.com/",
            "tags": ["AI", "TRM", "Enterprise"]
        },
        {
            "name": "Clinch（招聘营销平台）",
            "name_en": "Clinch (Recruitment Marketing)",
            "type": "url",
            "url": "https://clinch.io/",
            "tags": ["AI", "Marketing", "Career Site"]
        },
        {
            "name": "Recruitics（招聘营销分析）",
            "name_en": "Recruitics (Recruitment Marketing Analytics)",
            "type": "url",
            "url": "https://recruitics.com/",
            "tags": ["AI", "Marketing", "Analytics"]
        },
        {
            "name": "ERIN（员工推荐平台）",
            "name_en": "ERIN (Employee Referral Platform)",
            "type": "url",
            "url": "https://erinapp.com/",
            "tags": ["AI", "Referral", "Gamification"]
        },
        {
            "name": "Boon（敏捷推荐招聘）",
            "name_en": "Boon (Agile Referral Hiring)",
            "type": "url",
            "url": "https://www.goboon.co/",
            "tags": ["AI", "Referral", "52% Faster"]
        },
        {
            "name": "Avature（企业招聘CRM）",
            "name_en": "Avature (Enterprise Recruiting CRM)",
            "type": "url",
            "url": "https://www.avature.net/",
            "tags": ["AI", "CRM", "Enterprise"]
        },
        {
            "name": "Teamable（统一招聘漏斗）",
            "name_en": "Teamable (Unified Hiring Funnel)",
            "type": "url",
            "url": "https://www.teamable.com/",
            "tags": ["AI", "CRM", "Network"]
        },
        {
            "name": "Wintro（AI员工推荐）",
            "name_en": "Wintro (AI Employee Referrals)",
            "type": "url",
            "url": "https://www.wintro.ai/",
            "tags": ["AI", "Referral", "LinkedIn"]
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
        # Normalize URL for comparison
        url = node.get('url').rstrip('/')
        urls.add(url)
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


def normalize_url(url):
    """Normalize URL for comparison"""
    url = url.rstrip('/')
    # Remove trailing slashes and common variations
    return url


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
            url = normalize_url(resource.get('url', ''))
            name = resource.get('name', '')

            # Check for duplicates (check both normalized versions)
            url_exists = url in existing_urls or url + '/' in existing_urls
            if url_exists:
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
