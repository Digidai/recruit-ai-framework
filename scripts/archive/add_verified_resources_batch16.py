#!/usr/bin/env python3
"""
Batch 16: Add verified resources to tarf.json
Cross-validated resources covering weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== 领英 X-Ray =====
    "领英 X-Ray": [
        {
            "name": "Linked Helper（领英自动化）",
            "name_en": "Linked Helper (LinkedIn Automation)",
            "type": "url",
            "url": "https://www.linkedhelper.com/",
            "tags": ["Sourcing", "LinkedIn", "Automation"]
        },
        {
            "name": "Recruitin.net（免费X-Ray工具）",
            "name_en": "RecruitEm/Recruitin.net (Free X-Ray Tool)",
            "type": "url",
            "url": "https://recruitin.net/",
            "tags": ["Sourcing", "Boolean", "Free"]
        },
        {
            "name": "Evaboot（Sales Navigator导出）",
            "name_en": "Evaboot (Sales Navigator Export)",
            "type": "url",
            "url": "https://evaboot.com/",
            "tags": ["Sourcing", "LinkedIn", "Export"]
        },
    ],

    # ===== 远程面试与虚拟招聘 =====
    "远程面试与虚拟招聘": [
        {
            "name": "Willo（异步视频面试）",
            "name_en": "Willo (Async Video Interview)",
            "type": "url",
            "url": "https://www.willo.video/",
            "tags": ["Video", "Async", "Remote"]
        },
        {
            "name": "Hireflix（一键视频面试）",
            "name_en": "Hireflix (One-Way Video Interview)",
            "type": "url",
            "url": "https://www.hireflix.com/",
            "tags": ["Video", "Simple", "Async"]
        },
    ],

    # ===== 员工推荐平台 =====
    "员工推荐平台": [
        {
            "name": "ERIN（员工推荐自动化）",
            "name_en": "ERIN (Employee Referral Automation)",
            "type": "url",
            "url": "https://erinapp.com/",
            "tags": ["Referral", "Mobile", "Automation"]
        },
        {
            "name": "EmployeeReferrals.com（AI推荐平台）",
            "name_en": "EmployeeReferrals.com (AI Referral Platform)",
            "type": "url",
            "url": "https://www.employeereferrals.com/",
            "tags": ["Referral", "AI", "Enterprise"]
        },
    ],

    # ===== 候选人关系管理 =====
    "候选人关系管理": [
        {
            "name": "Talention CRM（候选人CRM）",
            "name_en": "Talention CRM (Candidate CRM)",
            "type": "url",
            "url": "https://www.talention.com/",
            "tags": ["CRM", "Marketing", "Nurture"]
        },
        {
            "name": "Oleeo CRM（人才CRM）",
            "name_en": "Oleeo CRM (Talent CRM)",
            "type": "url",
            "url": "https://www.oleeo.com/",
            "tags": ["CRM", "Enterprise", "DEI"]
        },
    ],

    # ===== 职位广告优化 =====
    "职位广告优化": [
        {
            "name": "Joveo（程序化招聘广告）",
            "name_en": "Joveo (Programmatic Job Advertising)",
            "type": "url",
            "url": "https://www.joveo.com/",
            "tags": ["Advertising", "Programmatic", "AI"]
        },
        {
            "name": "Appcast（招聘广告优化）",
            "name_en": "Appcast (Job Ad Optimization)",
            "type": "url",
            "url": "https://www.appcast.io/",
            "tags": ["Advertising", "Programmatic", "Data"]
        },
        {
            "name": "PandoLogic（智能招聘广告）",
            "name_en": "PandoLogic (Intelligent Job Advertising)",
            "type": "url",
            "url": "https://www.pandologic.com/",
            "tags": ["Advertising", "AI", "Automation"]
        },
        {
            "name": "Recruitics（招聘营销分析）",
            "name_en": "Recruitics (Recruitment Marketing Analytics)",
            "type": "url",
            "url": "https://www.recruitics.com/",
            "tags": ["Advertising", "Analytics", "Marketing"]
        },
    ],

    # ===== 招聘视频平台 =====
    "招聘视频平台": [
        {
            "name": "VideoMyJob（雇主品牌视频）",
            "name_en": "VideoMyJob (Employer Branding Video)",
            "type": "url",
            "url": "https://www.videomyjob.com/",
            "tags": ["Video", "EB", "Content"]
        },
        {
            "name": "Vouch（员工故事视频）",
            "name_en": "Vouch (Employee Story Videos)",
            "type": "url",
            "url": "https://vouchfor.com/",
            "tags": ["Video", "Stories", "Testimonials"]
        },
        {
            "name": "PlayPlay（视频创作平台）",
            "name_en": "PlayPlay (Video Creation Platform)",
            "type": "url",
            "url": "https://playplay.com/",
            "tags": ["Video", "Creation", "Easy"]
        },
    ],

    # ===== 员工故事 =====
    "员工故事": [
        {
            "name": "StoryPrompt（员工故事收集）",
            "name_en": "StoryPrompt (Employee Story Collection)",
            "type": "url",
            "url": "https://storyprompt.com/",
            "tags": ["Stories", "Collection", "Authentic"]
        },
        {
            "name": "Jamyr by Recruitics（招聘视频平台）",
            "name_en": "Jamyr by Recruitics (Recruitment Video)",
            "type": "url",
            "url": "https://www.recruitics.com/jamyr",
            "tags": ["Stories", "Video", "EB"]
        },
    ],

    # ===== ATS（中国）=====
    "ATS（中国）": [
        {
            "name": "iSmartRecruit（亚洲ATS）",
            "name_en": "iSmartRecruit (Asia ATS)",
            "type": "url",
            "url": "https://www.ismartrecruit.com/",
            "tags": ["ATS", "Asia", "AI"]
        },
        {
            "name": "Manatal（AI招聘软件）",
            "name_en": "Manatal (AI Recruitment Software)",
            "type": "url",
            "url": "https://www.manatal.com/",
            "tags": ["ATS", "AI", "Global"]
        },
    ],

    # ===== 人才库管理 =====
    "人才库管理": [
        {
            "name": "Jobvite人才CRM（人才库）",
            "name_en": "Jobvite Talent CRM",
            "type": "url",
            "url": "https://www.jobvite.com/products/evolve-talent-acquisition-suite/",
            "tags": ["CRM", "Talent Pool", "Enterprise"]
        },
        {
            "name": "VanillaHR（人才管道）",
            "name_en": "VanillaHR (Talent Pipeline)",
            "type": "url",
            "url": "https://www.vanillahr.com/",
            "tags": ["CRM", "Pipeline", "SMB"]
        },
    ],

    # ===== 智能寻才/人才匹配 =====
    "智能寻才/人才匹配": [
        {
            "name": "Teamable（网络寻源）",
            "name_en": "Teamable (Network Sourcing)",
            "type": "url",
            "url": "https://www.teamable.com/",
            "tags": ["Sourcing", "Network", "AI"]
        },
        {
            "name": "AmazingHiring（技术人才搜索）",
            "name_en": "AmazingHiring (Tech Talent Search)",
            "type": "url",
            "url": "https://amazinghiring.com/",
            "tags": ["Sourcing", "Technical", "AI"]
        },
    ],

    # ===== 招聘营销内容 =====
    "招聘营销内容": [
        {
            "name": "Wonderkind（程序化招聘）",
            "name_en": "Wonderkind (Programmatic Recruiting)",
            "type": "url",
            "url": "https://www.wonderkind.com/",
            "tags": ["Marketing", "Social", "Programmatic"]
        },
        {
            "name": "JobTarget（招聘广告分发）",
            "name_en": "JobTarget (Job Ad Distribution)",
            "type": "url",
            "url": "https://www.jobtarget.com/",
            "tags": ["Marketing", "Distribution", "Aggregator"]
        },
    ],

    # ===== 招聘社交媒体 =====
    "招聘社交媒体": [
        {
            "name": "Hootsuite招聘（社交管理）",
            "name_en": "Hootsuite for Recruiting",
            "type": "url",
            "url": "https://www.hootsuite.com/",
            "tags": ["Social Media", "Management", "Scheduling"]
        },
        {
            "name": "Buffer招聘版（社交发布）",
            "name_en": "Buffer for Recruiting",
            "type": "url",
            "url": "https://buffer.com/",
            "tags": ["Social Media", "Publishing", "Analytics"]
        },
    ],

    # ===== 候选人体验 =====
    "候选人体验": [
        {
            "name": "SurveyMonkey候选人调查（体验调研）",
            "name_en": "SurveyMonkey Candidate Survey",
            "type": "url",
            "url": "https://www.surveymonkey.com/mp/candidate-experience-survey-template/",
            "tags": ["CX", "Survey", "Feedback"]
        },
        {
            "name": "Typeform候选人反馈（互动调查）",
            "name_en": "Typeform Candidate Feedback",
            "type": "url",
            "url": "https://www.typeform.com/surveys/candidate-experience-survey/",
            "tags": ["CX", "Survey", "Interactive"]
        },
    ],

    # ===== 虚拟入职平台 =====
    "虚拟入职平台": [
        {
            "name": "Sapling入职（员工入职）",
            "name_en": "Sapling Onboarding",
            "type": "url",
            "url": "https://www.saplinghr.com/",
            "tags": ["Onboarding", "HRIS", "Automation"]
        },
        {
            "name": "Enboarder（入职体验）",
            "name_en": "Enboarder (Onboarding Experience)",
            "type": "url",
            "url": "https://enboarder.com/",
            "tags": ["Onboarding", "Experience", "Engagement"]
        },
    ],

    # ===== 远程协作工具 =====
    "远程协作工具": [
        {
            "name": "Miro（远程协作白板）",
            "name_en": "Miro (Remote Collaboration Whiteboard)",
            "type": "url",
            "url": "https://miro.com/",
            "tags": ["Collaboration", "Whiteboard", "Remote"]
        },
        {
            "name": "Notion招聘模板（招聘工作空间）",
            "name_en": "Notion Recruiting Templates",
            "type": "url",
            "url": "https://www.notion.so/templates/category/recruiting",
            "tags": ["Collaboration", "Templates", "Documentation"]
        },
    ],

    # ===== 编程挑战/Hackathon =====
    "编程挑战/Hackathon": [
        {
            "name": "Devpost（黑客马拉松平台）",
            "name_en": "Devpost (Hackathon Platform)",
            "type": "url",
            "url": "https://devpost.com/",
            "tags": ["Hackathon", "Developer", "Community"]
        },
        {
            "name": "MLH（学生黑客马拉松）",
            "name_en": "MLH (Student Hackathons)",
            "type": "url",
            "url": "https://mlh.io/",
            "tags": ["Hackathon", "Campus", "Tech"]
        },
    ],

    # ===== 游戏化评估 =====
    "游戏化评估": [
        {
            "name": "Cognisess（认知游戏评估）",
            "name_en": "Cognisess (Cognitive Game Assessment)",
            "type": "url",
            "url": "https://cognisess.com/",
            "tags": ["Gamification", "Cognitive", "AI"]
        },
        {
            "name": "Harver游戏化（体验式评估）",
            "name_en": "Harver Gamified Assessments",
            "type": "url",
            "url": "https://harver.com/solutions/assessments/",
            "tags": ["Gamification", "Experience", "High-Volume"]
        },
    ],

    # ===== 招聘视觉与品牌设计 =====
    "招聘视觉与品牌设计": [
        {
            "name": "Figma招聘模板（设计协作）",
            "name_en": "Figma Recruiting Templates",
            "type": "url",
            "url": "https://www.figma.com/community/tag/recruiting/files",
            "tags": ["Design", "Templates", "Collaboration"]
        },
        {
            "name": "Piktochart（信息图设计）",
            "name_en": "Piktochart (Infographic Design)",
            "type": "url",
            "url": "https://piktochart.com/",
            "tags": ["Design", "Infographic", "Easy"]
        },
    ],

    # ===== 专业招聘 CRM =====
    "专业招聘 CRM": [
        {
            "name": "Bullhorn（招聘CRM）",
            "name_en": "Bullhorn (Staffing CRM)",
            "type": "url",
            "url": "https://www.bullhorn.com/",
            "tags": ["CRM", "Staffing", "Enterprise"]
        },
        {
            "name": "Vincere（猎头CRM）",
            "name_en": "Vincere (Executive Search CRM)",
            "type": "url",
            "url": "https://www.vincere.io/",
            "tags": ["CRM", "Executive Search", "Agency"]
        },
    ],

    # ===== 人才盘点与继任计划 =====
    "人才盘点与继任计划": [
        {
            "name": "Succession HR（继任规划）",
            "name_en": "SuccessionHR (Succession Planning)",
            "type": "url",
            "url": "https://www.successionhr.com/",
            "tags": ["Succession", "Planning", "Talent"]
        },
        {
            "name": "TalentGuard（职业发展规划）",
            "name_en": "TalentGuard (Career Development)",
            "type": "url",
            "url": "https://www.talentguard.com/",
            "tags": ["Succession", "Career", "Skills"]
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
