#!/usr/bin/env python3
"""
Batch 23: Add more verified resources - collaboration, sourcing, and more
All URLs have been cross-validated via web fetch
"""

import json

# Load data
with open("docs/tarf.json", "r", encoding="utf-8") as f:
    data = json.load(f)


def find_category(node, target_name):
    """Recursively find category by name"""
    if node.get("name") == target_name:
        return node
    for child in node.get("children", []):
        result = find_category(child, target_name)
        if result:
            return result
    return None


def get_existing_urls(node):
    """Get all existing URLs to avoid duplicates"""
    urls = set()
    if node.get("url"):
        urls.add(node.get("url").lower().rstrip("/"))
    for child in node.get("children", []):
        urls.update(get_existing_urls(child))
    return urls


def add_to_category(category_name, resources):
    """Add resources directly to a category"""
    category = find_category(data, category_name)
    if not category:
        print(f"  [WARN] Category not found: {category_name}")
        return 0

    existing_urls = get_existing_urls(data)
    added = 0

    for res in resources:
        url_normalized = res["url"].lower().rstrip("/")
        if url_normalized in existing_urls:
            print(f"  [SKIP] Already exists: {res['name']}")
            continue

        new_node = {
            "name": res["name"],
            "name_en": res["name_en"],
            "type": "url",
            "url": res["url"],
            "tags": res.get("tags", []),
        }
        category.setdefault("children", []).append(new_node)
        existing_urls.add(url_normalized)
        added += 1
        print(f"  [ADD] {res['name']}")

    return added


# ============================================================
# New verified resources organized by category
# ============================================================

# 1. Recruitment Collaboration & Team Management (招聘协作与团队管理)
collaboration_resources = [
    {
        "name": "Recruitee（协作式 ATS）",
        "name_en": "Recruitee (Collaborative ATS)",
        "url": "https://recruitee.com/",
        "tags": ["AI", "P"],
    },
    {
        "name": "Recruitee 协作招聘功能",
        "name_en": "Recruitee Collaborative Hiring",
        "url": "https://recruitee.com/collaborative-hiring",
        "tags": ["P"],
    },
    {
        "name": "Ashby（全功能招聘平台）",
        "name_en": "Ashby (All-in-one Recruiting Platform)",
        "url": "https://www.ashbyhq.com/",
        "tags": ["AI", "P"],
    },
    {
        "name": "Zappyhire（AI 协作招聘）",
        "name_en": "Zappyhire (AI Collaborative Hiring)",
        "url": "https://www.zappyhire.com/",
        "tags": ["AI", "P"],
    },
    {
        "name": "Zappyhire 协作招聘功能",
        "name_en": "Zappyhire Collaborative Hiring Features",
        "url": "https://www.zappyhire.com/features/collaborative-hiring",
        "tags": ["AI", "P"],
    },
    {
        "name": "Manatal 协作功能",
        "name_en": "Manatal Collaboration Features",
        "url": "https://www.manatal.com/features/collaboration-and-team-management",
        "tags": ["AI", "P"],
    },
    {
        "name": "MokaHR 实时协作平台指南",
        "name_en": "MokaHR Real-Time Collaboration Guide",
        "url": "https://www.mokahr.io/articles/en/the-best-real-time-hiring-collaboration-platform",
        "tags": ["AI"],
    },
    {
        "name": "Applicantz 协作招聘",
        "name_en": "Applicantz Collaborative Hiring",
        "url": "https://applicantz.io/collaborative-hiring/",
        "tags": ["O"],
    },
    {
        "name": "GetApp 协作招聘软件",
        "name_en": "GetApp Recruiting Software with Collaboration",
        "url": "https://www.getapp.com/hr-employee-management-software/recruitment/f/collaboration-tools/",
        "tags": ["R"],
    },
]

# 2. Boolean Search / X-Ray Templates (搜索模板)
search_resources = [
    {
        "name": "RecruitEm（LinkedIn X-Ray 搜索）",
        "name_en": "RecruitEm (LinkedIn X-Ray Search)",
        "url": "https://recruitin.net/",
        "tags": ["O"],
    },
    {
        "name": "Recruitment Geek X-Ray 工具",
        "name_en": "Recruitment Geek X-Ray Tool",
        "url": "https://recruitmentgeek.com/tools/linkedin",
        "tags": [],
    },
    {
        "name": "Careerflow X-Ray 搜索",
        "name_en": "Careerflow X-Ray Search",
        "url": "https://hiring-search.careerflow.ai/",
        "tags": [],
    },
    {
        "name": "LinkedHelper X-Ray 搜索指南",
        "name_en": "LinkedHelper X-Ray Search Guide",
        "url": "https://www.linkedhelper.com/blog/linkedin-xray-search/",
        "tags": [],
    },
    {
        "name": "SalesRobot X-Ray 搜索指南",
        "name_en": "SalesRobot X-Ray Search Guide",
        "url": "https://www.salesrobot.co/blogs/linkedin-xray-search",
        "tags": [],
    },
    {
        "name": "RecruitRyte Boolean 搜索指南",
        "name_en": "RecruitRyte Boolean Search Guide",
        "url": "https://recruitryte.com/blog/mastering-boolean-search-linkedin-x-ray-searches-guide/",
        "tags": [],
    },
    {
        "name": "FidForward X-Ray 搜索教程",
        "name_en": "FidForward X-Ray Search Tutorial",
        "url": "https://fidforward.com/blog/xray_search/",
        "tags": [],
    },
    {
        "name": "PCRecruiter X-Ray 搜索未来",
        "name_en": "PCRecruiter The Future of X-Ray Search",
        "url": "https://www.pcrecruiter.net/site/2024/04/09/death-of-x-ray-search-for-recruiters/",
        "tags": [],
    },
    {
        "name": "Udemy Boolean 搜索课程",
        "name_en": "Udemy Boolean Search Course",
        "url": "https://www.udemy.com/course/talent-sourcing/",
        "tags": ["P"],
    },
]

# 3. ATS Systems (补充)
ats_resources = [
    {
        "name": "Lever（招聘软件与 CRM）",
        "name_en": "Lever (Recruiting Software & CRM)",
        "url": "https://www.lever.co/",
        "tags": ["AI", "P"],
    },
    {
        "name": "Capterra 人才管理软件",
        "name_en": "Capterra Talent Management Software",
        "url": "https://www.capterra.com/talent-management-software/",
        "tags": ["R"],
    },
    {
        "name": "TechRepublic 最佳招聘软件 2025",
        "name_en": "TechRepublic Best Recruiting Software 2025",
        "url": "https://www.techrepublic.com/article/best-recruiting-software/",
        "tags": [],
    },
]

# 4. Talent Development (人才发展补充)
talent_dev_resources = [
    {
        "name": "Workday 人才管理",
        "name_en": "Workday Talent Management",
        "url": "https://www.workday.com/en-us/products/talent-management/overview.html",
        "tags": ["P"],
    },
    {
        "name": "SC Training 人才发展平台 2025",
        "name_en": "SC Training Talent Development Platforms 2025",
        "url": "https://training.safetyculture.com/blog/talent-development-platform/",
        "tags": [],
    },
]

# ============================================================
# Apply resources to categories
# ============================================================

print("=" * 60)
print("Adding verified resources (Batch 23)")
print("=" * 60)

total_added = 0

print("\n[1] 招聘协作与团队管理")
total_added += add_to_category("招聘协作与团队管理", collaboration_resources)

print("\n[2] 搜索模板（X-Ray/Boolean）")
total_added += add_to_category("搜索模板（X-Ray/Boolean）", search_resources)

print("\n[3] ATS 与招聘系统 (补充)")
# Find the ATS category
ats_cat = find_category(data, "ATS 与招聘系统")
if ats_cat:
    existing_urls = get_existing_urls(data)
    for res in ats_resources:
        url_normalized = res["url"].lower().rstrip("/")
        if url_normalized in existing_urls:
            print(f"  [SKIP] Already exists: {res['name']}")
            continue
        new_node = {
            "name": res["name"],
            "name_en": res["name_en"],
            "type": "url",
            "url": res["url"],
            "tags": res.get("tags", []),
        }
        ats_cat.setdefault("children", []).append(new_node)
        existing_urls.add(url_normalized)
        total_added += 1
        print(f"  [ADD] {res['name']}")

print("\n[4] 人才发展与培训 (补充)")
talent_cat = find_category(data, "人才发展与培训")
if talent_cat:
    existing_urls = get_existing_urls(data)
    for res in talent_dev_resources:
        url_normalized = res["url"].lower().rstrip("/")
        if url_normalized in existing_urls:
            print(f"  [SKIP] Already exists: {res['name']}")
            continue
        new_node = {
            "name": res["name"],
            "name_en": res["name_en"],
            "type": "url",
            "url": res["url"],
            "tags": res.get("tags", []),
        }
        talent_cat.setdefault("children", []).append(new_node)
        existing_urls.add(url_normalized)
        total_added += 1
        print(f"  [ADD] {res['name']}")

# Save data
with open("docs/tarf.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n" + "=" * 60)
print(f"Total resources added: {total_added}")
print("=" * 60)


# Count total resources
def count_resources(node):
    count = 1 if node.get("type") == "url" else 0
    for child in node.get("children", []):
        count += count_resources(child)
    return count


total = count_resources(data)
print(f"Total resources in database: {total}")
