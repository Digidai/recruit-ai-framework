#!/usr/bin/env python3
"""
Batch 20: Add verified resources to tarf.json
Cross-validated resources covering remaining weak categories
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== 视频面试平台 (补充到5+) =====
    "视频面试平台": [
        {
            "name": "Canditech（技能模拟面试）",
            "name_en": "Canditech (Job Simulation Assessment)",
            "type": "url",
            "url": "https://www.canditech.io/",
            "tags": ["Video", "Assessment", "Simulation"]
        },
        {
            "name": "Recright（视频招聘平台）",
            "name_en": "Recright (Video Recruiting Platform)",
            "type": "url",
            "url": "https://recright.com/",
            "tags": ["Video", "Async", "Europe"]
        },
    ],

    # ===== 招聘营销平台 (补充到5+) =====
    "招聘营销平台": [
        {
            "name": "Shazamme（招聘网站构建器）",
            "name_en": "Shazamme (Recruitment Website Builder)",
            "type": "url",
            "url": "https://www.shazamme.com/",
            "tags": ["Marketing", "Career Site", "SEO"]
        },
        {
            "name": "Universum（雇主品牌研究）",
            "name_en": "Universum (Employer Brand Research)",
            "type": "url",
            "url": "https://universumglobal.com/",
            "tags": ["Marketing", "Research", "Branding"]
        },
        {
            "name": "Rally招聘营销社区",
            "name_en": "Rally Recruitment Marketing Community",
            "type": "url",
            "url": "https://rallyrecruitmentmarketing.com/",
            "tags": ["Marketing", "Community", "Education"]
        },
    ],

    # ===== 招聘/HR 开源项目 =====
    "招聘/HR 开源项目": [
        {
            "name": "Odoo HR模块（开源ERP）",
            "name_en": "Odoo HR Module (Open Source ERP)",
            "type": "url",
            "url": "https://www.odoo.com/app/recruitment",
            "tags": ["Open Source", "ERP", "Modular"]
        },
        {
            "name": "MintHCM（开源HCM）",
            "name_en": "MintHCM (Open Source HCM)",
            "type": "url",
            "url": "https://minthcm.org/",
            "tags": ["Open Source", "HCM", "Self-Hosted"]
        },
        {
            "name": "Frappe HR（开源HR系统）",
            "name_en": "Frappe HR (Open Source HR)",
            "type": "url",
            "url": "https://frappehr.com/",
            "tags": ["Open Source", "HRIS", "Python"]
        },
        {
            "name": "Sentrifugo（开源HRM）",
            "name_en": "Sentrifugo (Open Source HRM)",
            "type": "url",
            "url": "https://www.sentrifugo.com/",
            "tags": ["Open Source", "HRM", "Self-Hosted"]
        },
    ],

    # ===== 简历欺诈检测 =====
    "简历欺诈检测": [
        {
            "name": "TurboCheck（招聘反欺诈）",
            "name_en": "TurboCheck (Recruiting Fraud Detection)",
            "type": "url",
            "url": "https://turbocheck.com/",
            "tags": ["Fraud", "Detection", "Verification"]
        },
        {
            "name": "Shareable背景核查",
            "name_en": "Shareable Background Checks",
            "type": "url",
            "url": "https://www.shareable.com/",
            "tags": ["Fraud", "Background", "Verification"]
        },
    ],

    # ===== AI 视频面试 =====
    "AI 视频面试": [
        {
            "name": "BarRaiser（AI面试协作）",
            "name_en": "BarRaiser (AI Interview Copilot)",
            "type": "url",
            "url": "https://www.barraiser.com/",
            "tags": ["AI", "Interview", "Technical"]
        },
        {
            "name": "Elevatus（AI视频筛选）",
            "name_en": "Elevatus (AI Video Screening)",
            "type": "url",
            "url": "https://www.elevatus.io/",
            "tags": ["AI", "Video", "Middle East"]
        },
    ],

    # ===== AI 编程面试 =====
    "AI 编程面试": [
        {
            "name": "Woven（技术面试平台）",
            "name_en": "Woven (Technical Interview Platform)",
            "type": "url",
            "url": "https://www.woven.com/",
            "tags": ["AI", "Coding", "Assessment"]
        },
        {
            "name": "Byteboard（项目制面试）",
            "name_en": "Byteboard (Project-Based Interview)",
            "type": "url",
            "url": "https://byteboard.dev/",
            "tags": ["Coding", "Project", "Realistic"]
        },
    ],

    # ===== 退伍军人招聘认证 =====
    "退伍军人招聘认证": [
        {
            "name": "Hiring Our Heroes（退伍军人项目）",
            "name_en": "Hiring Our Heroes (Military Program)",
            "type": "url",
            "url": "https://www.hiringourheroes.org/",
            "tags": ["Veteran", "Transition", "US Chamber"]
        },
        {
            "name": "DoD SkillBridge（国防部过渡）",
            "name_en": "DoD SkillBridge (Military Transition)",
            "type": "url",
            "url": "https://skillbridge.osd.mil/",
            "tags": ["Veteran", "DoD", "Internship"]
        },
    ],

    # ===== 招聘偏见检测 =====
    "招聘偏见检测": [
        {
            "name": "Textio Lift（招聘语言优化）",
            "name_en": "Textio Lift (Recruiting Language Optimizer)",
            "type": "url",
            "url": "https://textio.com/products/lift",
            "tags": ["Bias", "Language", "AI"]
        },
        {
            "name": "Humantic AI（行为分析）",
            "name_en": "Humantic AI (Behavioral Analysis)",
            "type": "url",
            "url": "https://humantic.ai/",
            "tags": ["AI", "Personality", "Bias-Aware"]
        },
    ],

    # ===== ATS 与招聘协作 =====
    "ATS 与招聘协作": [
        {
            "name": "Comeet（协作招聘平台）",
            "name_en": "Comeet (Collaborative Hiring Platform)",
            "type": "url",
            "url": "https://www.comeet.com/",
            "tags": ["ATS", "Collaboration", "SMB"]
        },
        {
            "name": "Homerun（创意团队招聘）",
            "name_en": "Homerun (Creative Team Hiring)",
            "type": "url",
            "url": "https://www.homerun.co/",
            "tags": ["ATS", "Creative", "Design"]
        },
    ],

    # ===== 职位发布与招聘营销 =====
    "职位发布与招聘营销": [
        {
            "name": "Jobbio（人才市场）",
            "name_en": "Jobbio (Talent Marketplace)",
            "type": "url",
            "url": "https://jobbio.com/",
            "tags": ["Job Board", "Marketing", "Employer Brand"]
        },
        {
            "name": "Adzuna（职位搜索引擎）",
            "name_en": "Adzuna (Job Search Engine)",
            "type": "url",
            "url": "https://www.adzuna.com/",
            "tags": ["Job Board", "Aggregator", "Analytics"]
        },
    ],

    # ===== 远程协作工具 =====
    "远程协作工具": [
        {
            "name": "Miro（远程白板协作）",
            "name_en": "Miro (Remote Whiteboard Collaboration)",
            "type": "url",
            "url": "https://miro.com/",
            "tags": ["Collaboration", "Whiteboard", "Remote"]
        },
        {
            "name": "Figma（设计协作）",
            "name_en": "Figma (Design Collaboration)",
            "type": "url",
            "url": "https://www.figma.com/",
            "tags": ["Collaboration", "Design", "Remote"]
        },
    ],

    # ===== 沟通工具 =====
    "沟通工具": [
        {
            "name": "Loom（异步视频消息）",
            "name_en": "Loom (Async Video Messaging)",
            "type": "url",
            "url": "https://www.loom.com/",
            "tags": ["Communication", "Video", "Async"]
        },
        {
            "name": "Calendly（会议安排）",
            "name_en": "Calendly (Meeting Scheduling)",
            "type": "url",
            "url": "https://calendly.com/",
            "tags": ["Communication", "Scheduling", "Productivity"]
        },
    ],

    # ===== 远程工作资源 =====
    "远程工作资源": [
        {
            "name": "We Work Remotely（远程职位板）",
            "name_en": "We Work Remotely (Remote Job Board)",
            "type": "url",
            "url": "https://weworkremotely.com/",
            "tags": ["Remote", "Job Board", "Global"]
        },
        {
            "name": "FlexJobs（远程灵活工作）",
            "name_en": "FlexJobs (Remote & Flexible Jobs)",
            "type": "url",
            "url": "https://www.flexjobs.com/",
            "tags": ["Remote", "Job Board", "Verified"]
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
