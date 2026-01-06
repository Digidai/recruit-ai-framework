#!/usr/bin/env python3
"""
Batch 21: Add verified resources to multiple categories
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


def add_resources_to_category(category_name, subcategory_name, resources):
    """Add resources to a specific subcategory"""
    category = find_category(data, category_name)
    if not category:
        print(f"  [WARN] Category not found: {category_name}")
        return 0

    subcategory = find_category(category, subcategory_name)
    if not subcategory:
        print(f"  [WARN] Subcategory not found: {subcategory_name}")
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
        subcategory.setdefault("children", []).append(new_node)
        existing_urls.add(url_normalized)
        added += 1
        print(f"  [ADD] {res['name']}")

    return added


# ============================================================
# New verified resources organized by category
# ============================================================

# 1. Internal Mobility & Talent Flow (内部招聘与人才流动)
internal_mobility_resources = [
    {
        "name": "Gloat（AI 内部人才市场）",
        "name_en": "Gloat (AI Internal Talent Marketplace)",
        "url": "https://www.gloat.com/",
        "tags": ["AI", "P"],
    },
    {
        "name": "Fuel50（技能智能与职业路径）",
        "name_en": "Fuel50 (Skills Intelligence & Career Pathing)",
        "url": "https://fuel50.com/",
        "tags": ["AI", "P"],
    },
    {
        "name": "365Talents（AI 技能与内部流动）",
        "name_en": "365Talents (AI Skills & Internal Mobility)",
        "url": "https://www.365talents.com/",
        "tags": ["AI", "P"],
    },
    {
        "name": "Eightfold AI（人才智能平台）",
        "name_en": "Eightfold AI (Talent Intelligence Platform)",
        "url": "https://eightfold.ai/",
        "tags": ["AI", "P"],
    },
    {
        "name": "Gartner 内部人才市场评测",
        "name_en": "Gartner Internal Talent Marketplaces Reviews",
        "url": "https://www.gartner.com/reviews/market/internal-talent-marketplaces",
        "tags": ["R"],
    },
]

# 2. Compensation & Job Data (薪酬与职位数据)
compensation_resources = [
    {
        "name": "PayScale（薪酬数据与对标）",
        "name_en": "PayScale (Compensation Data & Benchmarking)",
        "url": "https://www.payscale.com/",
        "tags": ["P"],
    },
    {
        "name": "Levels.fyi（科技行业薪资透明）",
        "name_en": "Levels.fyi (Tech Salary Transparency)",
        "url": "https://www.levels.fyi/",
        "tags": [],
    },
    {
        "name": "Pave（实时薪酬智能）",
        "name_en": "Pave (Real-time Compensation Intelligence)",
        "url": "https://www.pave.com/",
        "tags": ["AI", "P"],
    },
    {
        "name": "Ravio（实时薪酬对标）",
        "name_en": "Ravio (Real-time Compensation Benchmarking)",
        "url": "https://ravio.com/",
        "tags": ["P"],
    },
    {
        "name": "Radford McLagan 薪酬数据库",
        "name_en": "Radford McLagan Compensation Database (Aon)",
        "url": "https://www.aon.com/en/capabilities/human-capital-analytics/radford-mclagan-compensation-database",
        "tags": ["P"],
    },
    {
        "name": "Carta Total Compensation",
        "name_en": "Carta Total Compensation",
        "url": "https://carta.com/learn/startups/compensation/benchmarking/",
        "tags": ["P"],
    },
    {
        "name": "Gartner 薪酬管理软件评测",
        "name_en": "Gartner Compensation Management Software Reviews",
        "url": "https://www.gartner.com/reviews/market/compensation-management-software",
        "tags": ["R"],
    },
]

# 3. Frontline & Hourly Hiring (蓝领与一线员工招聘)
frontline_resources = [
    {
        "name": "Fountain（一线员工招聘平台）",
        "name_en": "Fountain (Frontline Workforce Platform)",
        "url": "https://www.fountain.com/",
        "tags": ["AI", "P"],
    },
    {
        "name": "Chattr（小时工 AI 招聘）",
        "name_en": "Chattr (Hourly Hiring AI)",
        "url": "https://chattr.ai/",
        "tags": ["AI", "P"],
    },
    {
        "name": "Fountain 一线招聘指南",
        "name_en": "Fountain Frontline Hiring Guide",
        "url": "https://www.fountain.com/frontline-hiring",
        "tags": [],
    },
    {
        "name": "Talroo 一线员工指数",
        "name_en": "Talroo Frontline Worker Index",
        "url": "https://www.talroo.com/talroo-frontline-worker-index/",
        "tags": [],
    },
    {
        "name": "iCIMS 一线招聘报告 2025",
        "name_en": "iCIMS State of Frontline Hiring Report 2025",
        "url": "https://www.icims.com/company/newsroom/2025stateoffrontlinehiringreport/",
        "tags": [],
    },
]

# 4. Executive Search (高管招聘)
executive_resources = [
    {
        "name": "Korn Ferry（全球最大猎头）",
        "name_en": "Korn Ferry (World's Largest Executive Search)",
        "url": "https://www.kornferry.com/",
        "tags": ["P"],
    },
    {
        "name": "Spencer Stuart（高管与董事会搜寻）",
        "name_en": "Spencer Stuart (Executive & Board Search)",
        "url": "https://www.spencerstuart.com/",
        "tags": ["P"],
    },
    {
        "name": "Heidrick & Struggles（高管猎头）",
        "name_en": "Heidrick & Struggles (Executive Search)",
        "url": "https://www.heidrick.com/",
        "tags": ["P"],
    },
    {
        "name": "Russell Reynolds Associates（高管搜寻）",
        "name_en": "Russell Reynolds Associates (Executive Search)",
        "url": "https://www.russellreynolds.com/",
        "tags": ["P"],
    },
    {
        "name": "高管猎头公司列表（维基百科）",
        "name_en": "List of Executive Search Firms (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/List_of_executive_search_firms",
        "tags": [],
    },
]

# 5. Veteran Hiring (退伍军人招聘)
veteran_resources = [
    {
        "name": "RecruitMilitary（军人招聘平台）",
        "name_en": "RecruitMilitary (Military Hiring Platform)",
        "url": "https://recruitmilitary.com/",
        "tags": ["P"],
    },
    {
        "name": "Hiring Our Heroes（美国商会军人就业）",
        "name_en": "Hiring Our Heroes (US Chamber Foundation)",
        "url": "https://www.hiringourheroes.org/",
        "tags": [],
    },
    {
        "name": "VetJobs（退伍军人职位市场）",
        "name_en": "VetJobs (Veteran Jobs Marketplace)",
        "url": "https://vetjobs.org/",
        "tags": [],
    },
    {
        "name": "Hire Veterans（退伍军人职位）",
        "name_en": "Hire Veterans (Veteran Jobs)",
        "url": "https://hireveterans.com/",
        "tags": [],
    },
    {
        "name": "HIRE Vets Medallion（劳工部认证）",
        "name_en": "HIRE Vets Medallion (DOL Recognition)",
        "url": "https://www.hirevets.gov/",
        "tags": ["Law"],
    },
    {
        "name": "VA for Vets（退伍军人职业门户）",
        "name_en": "VA for Vets (Career Gateway)",
        "url": "https://www.vaforvets.va.gov/",
        "tags": [],
    },
    {
        "name": "Military.com 顶级雇主 2025",
        "name_en": "Military.com Top Veteran Employers 2025",
        "url": "https://www.military.com/veteran-jobs/top-25-veteran-employers-2025.html",
        "tags": [],
    },
]

# 6. Recruitment Marketing (招聘营销与内容创作)
marketing_resources = [
    {
        "name": "Rally Recruitment Marketing（社区与工具）",
        "name_en": "Rally Recruitment Marketing (Community & Tools)",
        "url": "https://rallyrecruitmentmarketing.com/",
        "tags": [],
    },
    {
        "name": "Rally Inside（AI 招聘营销平台）",
        "name_en": "Rally Inside (AI Recruitment Marketing Platform)",
        "url": "https://www.rallyinside.io/",
        "tags": ["AI"],
    },
    {
        "name": "SmartDreamers（招聘营销操作系统）",
        "name_en": "SmartDreamers (Recruitment Marketing OS)",
        "url": "https://www.smartdreamers.com/",
        "tags": ["AI", "P"],
    },
    {
        "name": "Beamery（人才 CRM 与营销）",
        "name_en": "Beamery (Talent CRM & Marketing)",
        "url": "https://www.beamery.com/",
        "tags": ["AI", "P"],
    },
    {
        "name": "SHRM 2025 招聘营销趋势",
        "name_en": "SHRM Recruitment Marketing Trends 2025",
        "url": "https://www.shrm.org/topics-tools/news/talent-acquisition/recruitment-marketing-trends-2025-ai-employer-branding",
        "tags": [],
    },
    {
        "name": "Vouch 雇主品牌指南 2025",
        "name_en": "Vouch Employer Branding Guide 2025",
        "url": "https://vouchfor.com/blog/employer-branding-guide",
        "tags": [],
    },
    {
        "name": "Recruiterflow 招聘营销指南",
        "name_en": "Recruiterflow Recruitment Marketing Guide",
        "url": "https://recruiterflow.com/blog/recruitment-marketing/",
        "tags": [],
    },
]

# ============================================================
# Apply resources to categories
# ============================================================

print("=" * 60)
print("Adding verified resources to tarf.json")
print("=" * 60)

total_added = 0

# Internal Mobility
print("\n[1] 内部招聘与人才流动 - 内部流动平台")
total_added += add_resources_to_category(
    "内部招聘与人才流动", "内部流动平台", internal_mobility_resources
)

# Compensation
print("\n[2] 薪酬与职位数据")
# Find or create appropriate subcategory
comp_cat = find_category(data, "薪酬与职位数据")
if comp_cat:
    # Add directly to the category's children
    existing_urls = get_existing_urls(data)
    for res in compensation_resources:
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
        comp_cat.setdefault("children", []).append(new_node)
        existing_urls.add(url_normalized)
        total_added += 1
        print(f"  [ADD] {res['name']}")

# Frontline Hiring
print("\n[3] 蓝领与一线员工招聘")
frontline_cat = find_category(data, "蓝领与一线员工招聘")
if frontline_cat:
    existing_urls = get_existing_urls(data)
    for res in frontline_resources:
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
        frontline_cat.setdefault("children", []).append(new_node)
        existing_urls.add(url_normalized)
        total_added += 1
        print(f"  [ADD] {res['name']}")

# Executive Search
print("\n[4] 高管招聘")
exec_cat = find_category(data, "高管招聘")
if exec_cat:
    existing_urls = get_existing_urls(data)
    for res in executive_resources:
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
        exec_cat.setdefault("children", []).append(new_node)
        existing_urls.add(url_normalized)
        total_added += 1
        print(f"  [ADD] {res['name']}")

# Veteran Hiring
print("\n[5] 退伍军人招聘")
vet_cat = find_category(data, "退伍军人招聘")
if vet_cat:
    existing_urls = get_existing_urls(data)
    for res in veteran_resources:
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
        vet_cat.setdefault("children", []).append(new_node)
        existing_urls.add(url_normalized)
        total_added += 1
        print(f"  [ADD] {res['name']}")

# Recruitment Marketing
print("\n[6] 招聘营销与内容创作")
mkt_cat = find_category(data, "招聘营销与内容创作")
if mkt_cat:
    existing_urls = get_existing_urls(data)
    for res in marketing_resources:
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
        mkt_cat.setdefault("children", []).append(new_node)
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
