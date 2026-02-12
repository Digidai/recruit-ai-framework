#!/usr/bin/env python3
"""
Batch 18: Add verified resources to tarf.json
Cross-validated resources covering weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== ATS 与招聘协作 =====
    "ATS 与招聘协作": [
        {
            "name": "Pinpoint（协作招聘ATS）",
            "name_en": "Pinpoint (Collaborative Hiring ATS)",
            "type": "url",
            "url": "https://www.pinpointhq.com/",
            "tags": ["ATS", "Collaboration", "SMB"]
        },
        {
            "name": "Recruitee（团队协作招聘）",
            "name_en": "Recruitee (Team Collaborative Hiring)",
            "type": "url",
            "url": "https://recruitee.com/",
            "tags": ["ATS", "Collaboration", "Automation"]
        },
        {
            "name": "Freshteam（团队招聘工具）",
            "name_en": "Freshteam (Team Recruiting Tool)",
            "type": "url",
            "url": "https://www.freshworks.com/hrms/",
            "tags": ["ATS", "Collaboration", "Free Tier"]
        },
    ],

    # ===== 退伍军人招聘认证 =====
    "退伍军人招聘认证": [
        {
            "name": "RecruitMilitary（军转民招聘）",
            "name_en": "RecruitMilitary (Military-to-Civilian)",
            "type": "url",
            "url": "https://recruitmilitary.com/",
            "tags": ["Veteran", "Job Fair", "Transition"]
        },
        {
            "name": "Orion Talent（退伍军人猎头）",
            "name_en": "Orion Talent (Military Recruiting)",
            "type": "url",
            "url": "https://www.oriontalent.com/",
            "tags": ["Veteran", "Executive", "Transition"]
        },
        {
            "name": "Blue Signal退伍军人招聘",
            "name_en": "Blue Signal Veteran Recruiting",
            "type": "url",
            "url": "https://bluesignal.com/recruiting-industries/veteran/",
            "tags": ["Veteran", "Search", "Skills Translation"]
        },
    ],

    # ===== 视频面试平台 =====
    "视频面试平台": [
        {
            "name": "Hireflix（一键视频面试）",
            "name_en": "Hireflix (One-Way Video Interviews)",
            "type": "url",
            "url": "https://hireflix.com/",
            "tags": ["Video", "Async", "Affordable"]
        },
        {
            "name": "Willo（异步视频面试）",
            "name_en": "Willo (Async Video Interview)",
            "type": "url",
            "url": "https://www.willo.video/",
            "tags": ["Video", "Async", "AI Transcription"]
        },
    ],

    # ===== 招聘营销平台 =====
    "招聘营销平台": [
        {
            "name": "SmartDreamers（招聘营销自动化）",
            "name_en": "SmartDreamers (Recruitment Marketing Automation)",
            "type": "url",
            "url": "https://www.smartdreamers.com/",
            "tags": ["Marketing", "Automation", "Employer Brand"]
        },
        {
            "name": "Sense（AI候选人沟通）",
            "name_en": "Sense (AI Candidate Communication)",
            "type": "url",
            "url": "https://www.sensehq.com/",
            "tags": ["Marketing", "AI", "Engagement"]
        },
        {
            "name": "Cliquify（雇主品牌展示）",
            "name_en": "Cliquify (Employer Branding Platform)",
            "type": "url",
            "url": "https://cliquify.me/",
            "tags": ["Branding", "Video", "Culture"]
        },
    ],

    # ===== 招聘职业发展 =====
    "招聘职业发展": [
        {
            "name": "HRCI认证（PHR/SPHR）",
            "name_en": "HRCI Certification (PHR/SPHR)",
            "type": "url",
            "url": "https://www.hrci.org/",
            "tags": ["Certification", "HR", "Professional"]
        },
        {
            "name": "eCornell招聘课程（康奈尔大学）",
            "name_en": "eCornell Recruiting Program",
            "type": "url",
            "url": "https://ecornell.cornell.edu/certificates/human-resources/recruiting-and-talent-acquisition/",
            "tags": ["Training", "Cornell", "Certificate"]
        },
        {
            "name": "AIHR人才获取认证",
            "name_en": "AIHR Talent Acquisition Certification",
            "type": "url",
            "url": "https://www.aihr.com/courses/talent-acquisition-certificate-program/",
            "tags": ["Certification", "TA", "Online"]
        },
    ],

    # ===== 行业分析 =====
    "行业分析": [
        {
            "name": "Draup人才智能（AI劳动力分析）",
            "name_en": "Draup Talent Intelligence (AI Workforce Analytics)",
            "type": "url",
            "url": "https://draup.com/talent/",
            "tags": ["Analytics", "AI", "Market Intelligence"]
        },
        {
            "name": "TalentGuard人才智能平台",
            "name_en": "TalentGuard Talent Intelligence Platform",
            "type": "url",
            "url": "https://www.talentguard.com/",
            "tags": ["Analytics", "Skills", "Career Paths"]
        },
        {
            "name": "Randstad人才洞察",
            "name_en": "Randstad Talent Intelligence",
            "type": "url",
            "url": "https://www.randstadenterprise.com/expertise/talent-intelligence/",
            "tags": ["Intelligence", "Market", "Enterprise"]
        },
    ],

    # ===== Board / C-Suite 招聘 =====
    "Board / C-Suite 招聘": [
        {
            "name": "N2Growth（高管猎头）",
            "name_en": "N2Growth (Executive Search)",
            "type": "url",
            "url": "https://www.n2growth.com/",
            "tags": ["Executive", "Board", "C-Suite"]
        },
        {
            "name": "Chief Jobs（C级职位平台）",
            "name_en": "Chief Jobs (C-Suite Job Board)",
            "type": "url",
            "url": "https://www.chiefjobs.com/",
            "tags": ["Executive", "Job Board", "C-Suite"]
        },
        {
            "name": "BlueSteps（AESC高管网络）",
            "name_en": "BlueSteps (AESC Executive Network)",
            "type": "url",
            "url": "https://www.bluesteps.com/",
            "tags": ["Executive", "Network", "AESC"]
        },
        {
            "name": "ExecThread（高管私密职位）",
            "name_en": "ExecThread (Executive Private Network)",
            "type": "url",
            "url": "https://www.execthread.com/",
            "tags": ["Executive", "Private", "Director"]
        },
    ],

    # ===== 自由职业/零工平台 =====
    "自由职业/零工平台": [
        {
            "name": "Freelancer.com（全球自由职业）",
            "name_en": "Freelancer.com (Global Freelance)",
            "type": "url",
            "url": "https://www.freelancer.com/",
            "tags": ["Freelance", "Global", "Marketplace"]
        },
        {
            "name": "PeoplePerHour（欧洲自由职业）",
            "name_en": "PeoplePerHour (Europe Freelance)",
            "type": "url",
            "url": "https://www.peopleperhour.com/",
            "tags": ["Freelance", "Europe", "UK"]
        },
        {
            "name": "Andela（非洲技术人才）",
            "name_en": "Andela (African Tech Talent)",
            "type": "url",
            "url": "https://andela.com/",
            "tags": ["Freelance", "Tech", "Africa"]
        },
    ],

    # ===== AI 视频面试 =====
    "AI 视频面试": [
        {
            "name": "Interviewer.AI（AI面试平台）",
            "name_en": "Interviewer.AI (AI Interview Platform)",
            "type": "url",
            "url": "https://interviewer.ai/",
            "tags": ["AI", "Video", "Assessment"]
        },
        {
            "name": "Jobma（多语言AI面试）",
            "name_en": "Jobma (Multilingual AI Interview)",
            "type": "url",
            "url": "https://www.jobma.com/",
            "tags": ["AI", "Video", "Multilingual"]
        },
    ],

    # ===== 技术招聘专项 =====
    "技术招聘专项": [
        {
            "name": "Dice（IT技术招聘平台）",
            "name_en": "Dice (IT Tech Recruiting)",
            "type": "url",
            "url": "https://www.dice.com/",
            "tags": ["Tech", "IT", "Job Board"]
        },
        {
            "name": "daily.dev Recruiter（开发者招聘）",
            "name_en": "daily.dev Recruiter (Developer Recruiting)",
            "type": "url",
            "url": "https://recruiter.daily.dev/",
            "tags": ["Tech", "Developer", "Community"]
        },
    ],

    # ===== 员工推荐系统 =====
    "员工推荐系统": [
        {
            "name": "ERIN（员工推荐平台）",
            "name_en": "ERIN (Employee Referral Platform)",
            "type": "url",
            "url": "https://erinapp.com/",
            "tags": ["Referral", "Mobile", "Automation"]
        },
        {
            "name": "Boon（Slack内推工具）",
            "name_en": "Boon (Slack Referral Tool)",
            "type": "url",
            "url": "https://www.goboon.co/",
            "tags": ["Referral", "Slack", "Gamification"]
        },
        {
            "name": "EmployeeReferrals.com（AI内推）",
            "name_en": "EmployeeReferrals.com (AI Referrals)",
            "type": "url",
            "url": "https://www.employeereferrals.com/",
            "tags": ["Referral", "AI", "Enterprise"]
        },
    ],

    # ===== 人才市场情报与竞争分析 =====
    "人才市场情报与竞争分析": [
        {
            "name": "Findem（人才市场智能）",
            "name_en": "Findem (Talent Market Intelligence)",
            "type": "url",
            "url": "https://www.findem.ai/",
            "tags": ["Intelligence", "AI", "Sourcing"]
        },
        {
            "name": "JobsPikr（劳动力数据分析）",
            "name_en": "JobsPikr (Workforce Data Analytics)",
            "type": "url",
            "url": "https://www.jobspikr.com/",
            "tags": ["Intelligence", "Data", "Market"]
        },
    ],

    # ===== 校园招聘平台 - 需要确认准确名称 =====
    # 注：需要确认tarf.json中的校园招聘分类准确名称

    # ===== 面试安排 =====
    "面试安排": [
        {
            "name": "GoodTime（智能面试安排）",
            "name_en": "GoodTime (Intelligent Interview Scheduling)",
            "type": "url",
            "url": "https://www.goodtime.io/",
            "tags": ["Scheduling", "AI", "Automation"]
        },
        {
            "name": "ModernLoop（零点击安排）",
            "name_en": "ModernLoop (Zero-Click Scheduling)",
            "type": "url",
            "url": "https://www.modernloop.com/",
            "tags": ["Scheduling", "Automation", "Integration"]
        },
        {
            "name": "Paradox（AI对话式安排）",
            "name_en": "Paradox (AI Conversational Scheduling)",
            "type": "url",
            "url": "https://www.paradox.ai/",
            "tags": ["Scheduling", "AI", "Conversational"]
        },
    ],

    # ===== 远程面试与虚拟招聘 =====
    "远程面试与虚拟招聘": [
        {
            "name": "Brazen（虚拟招聘会平台）",
            "name_en": "Brazen (Virtual Career Fair Platform)",
            "type": "url",
            "url": "https://www.brazen.com/",
            "tags": ["Virtual", "Career Fair", "Events"]
        },
        {
            "name": "Premier Virtual（虚拟招聘活动）",
            "name_en": "Premier Virtual (Virtual Hiring Events)",
            "type": "url",
            "url": "https://premiervirtual.com/",
            "tags": ["Virtual", "Events", "Job Fair"]
        },
    ],

    # ===== 技术面试平台 =====
    "技术面试平台": [
        {
            "name": "HackerEarth（技术评估招聘）",
            "name_en": "HackerEarth (Tech Assessment Recruiting)",
            "type": "url",
            "url": "https://www.hackerearth.com/recruit/",
            "tags": ["Technical", "Coding", "Assessment"]
        },
        {
            "name": "Brokee（技术面试平台）",
            "name_en": "Brokee (Tech Interview Platform)",
            "type": "url",
            "url": "https://brokee.io/",
            "tags": ["Technical", "Interview", "Coding"]
        },
    ],

    # ===== 专业认证 =====
    "专业认证": [
        {
            "name": "AIRS认证（招聘认证）",
            "name_en": "AIRS Certification (Recruiting Certification)",
            "type": "url",
            "url": "https://www.airsdirectory.com/",
            "tags": ["Certification", "Recruiting", "Professional"]
        },
        {
            "name": "Recruiter Academy认证",
            "name_en": "Recruiter Academy RACR Certification",
            "type": "url",
            "url": "https://recruiteracademy.com/",
            "tags": ["Certification", "Training", "Recruiter"]
        },
    ],

    # ===== 校园招聘 =====
    "校园招聘平台": [
        {
            "name": "Handshake（校园招聘平台）",
            "name_en": "Handshake (Campus Recruiting Platform)",
            "type": "url",
            "url": "https://joinhandshake.com/employers/",
            "tags": ["Campus", "Early Career", "University"]
        },
        {
            "name": "Yello（企业校园招聘）",
            "name_en": "Yello (Enterprise Campus Recruiting)",
            "type": "url",
            "url": "https://yello.co/",
            "tags": ["Campus", "Enterprise", "Events"]
        },
        {
            "name": "RippleMatch（校园匹配平台）",
            "name_en": "RippleMatch (Campus Matching Platform)",
            "type": "url",
            "url": "https://ripplematch.com/",
            "tags": ["Campus", "AI", "Matching"]
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
