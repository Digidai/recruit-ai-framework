#!/usr/bin/env python3
"""
Batch 22: Add more verified resources to multiple categories
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

# 1. Employee Referral (员工推荐)
referral_resources = [
    {
        "name": "Boon（敏捷推荐招聘平台）",
        "name_en": "Boon (Agile Referral Hiring Platform)",
        "url": "https://www.goboon.co/",
        "tags": ["AI", "P"],
    },
    {
        "name": "G2 员工推荐软件评测",
        "name_en": "G2 Employee Referral Software Reviews",
        "url": "https://www.g2.com/categories/employee-referral",
        "tags": ["R"],
    },
    {
        "name": "Gartner 员工推荐管理评测",
        "name_en": "Gartner Employee Referral Management Reviews",
        "url": "https://www.gartner.com/reviews/market/employee-referral-management",
        "tags": ["R"],
    },
    {
        "name": "Referral Rock 员工推荐指南",
        "name_en": "Referral Rock Employee Referral Guide",
        "url": "https://referralrock.com/blog/employee-referral-software/",
        "tags": [],
    },
]

# 2. Talent Community & Pool (人才社区与人才库建设)
talent_pool_resources = [
    {
        "name": "Consider（人才情报平台）",
        "name_en": "Consider (Talent Intelligence Platform)",
        "url": "https://consider.com/",
        "tags": ["AI", "P"],
    },
    {
        "name": "iMocha（技能智能平台）",
        "name_en": "iMocha (Skills Intelligence Platform)",
        "url": "https://www.imocha.io/",
        "tags": ["AI", "P"],
    },
    {
        "name": "TalentGuard（人才智能平台）",
        "name_en": "TalentGuard (Talent Intelligence Platform)",
        "url": "https://www.talentguard.com/talent-intelligence-platform",
        "tags": ["AI", "P"],
    },
    {
        "name": "Softgarden 人才社区指南",
        "name_en": "Softgarden Talent Community Guide",
        "url": "https://softgarden.com/en/magazine/glossary/talent-community/",
        "tags": [],
    },
    {
        "name": "TalentNet（人才社区平台）",
        "name_en": "TalentNet (Talent Community Platform)",
        "url": "https://talentnet.com/products/",
        "tags": ["P"],
    },
    {
        "name": "MokaHR AI 人才库发现平台指南",
        "name_en": "MokaHR AI Talent Pool Rediscovery Guide",
        "url": "https://www.mokahr.io/articles/en/the-best-ai-powered-talent-pool-rediscovery-platform",
        "tags": ["AI"],
    },
]

# 3. Gamification & VR/AR Recruitment (游戏化与 VR/AR 招聘)
gamification_resources = [
    {
        "name": "Harver（AI 评估与游戏化）",
        "name_en": "Harver (AI Assessment & Gamification)",
        "url": "https://harver.com/",
        "tags": ["AI", "P"],
    },
    {
        "name": "HR Play（HR 游戏化博客）",
        "name_en": "HR Play (HR Gamification Blog)",
        "url": "https://www.hr-play.com/",
        "tags": [],
    },
    {
        "name": "HR Play 招聘游戏化案例研究",
        "name_en": "HR Play Gamification Case Studies",
        "url": "https://www.hr-play.com/blog/gamification-in-recruitment-case-studies-in-recruitment-gamification",
        "tags": [],
    },
    {
        "name": "Recruitics AR 招聘革命",
        "name_en": "Recruitics AR Recruitment Revolution",
        "url": "https://info.recruitics.com/blog/how-augmented-reality-is-revolutionizing-recruitment-and-candidate-assessments",
        "tags": [],
    },
    {
        "name": "PeopleScout VR 候选人体验",
        "name_en": "PeopleScout VR Candidate Experience",
        "url": "https://www.peoplescout.com/insights/virtual-reality-enhancing-experience/",
        "tags": [],
    },
    {
        "name": "SuperAGI 游戏化 AI 评估指南",
        "name_en": "SuperAGI Gamification in AI Assessments",
        "url": "https://superagi.com/gamification-in-ai-skill-assessments-boosting-candidate-engagement-and-accuracy-in-2025/",
        "tags": ["AI"],
    },
    {
        "name": "4 Corner 游戏化招聘指南",
        "name_en": "4 Corner Gamification in Recruiting",
        "url": "https://www.4cornerresources.com/blog/how-can-gamification-be-used-for-more-effective-recruiting/",
        "tags": [],
    },
    {
        "name": "AptaHire 游戏化评估",
        "name_en": "AptaHire Gamified Assessments",
        "url": "https://aptahire.ai/gamified-assessments-modern-recruitment/",
        "tags": ["AI"],
    },
]

# 4. Recruitment Video & Multimedia (招聘视频与多媒体)
video_resources = [
    {
        "name": "HeroHunt VR 招聘趋势",
        "name_en": "HeroHunt VR in Recruitment Trends",
        "url": "https://www.herohunt.ai/blog/virtual-reality-vr-in-recruitment",
        "tags": ["AI"],
    },
    {
        "name": "Bolt-On VR 游戏化评估指南",
        "name_en": "Bolt-On VR & Gamified Assessments",
        "url": "https://bolt-onrecruitment.com/mastering-virtual-reality-and-gamified-assessments/",
        "tags": [],
    },
]

# 5. Global Recruitment (全球招聘与远程团队)
global_resources = [
    {
        "name": "Salary.com 2025 创新招聘理念",
        "name_en": "Salary.com Innovative Recruitment Ideas 2025",
        "url": "https://www.salary.com/resources/hr-glossary/top-10-innovative-recruitment-ideas-hr-needs-to-know-in-2025",
        "tags": [],
    },
]

# 6. Neurodiversity (神经多样性招聘)
neurodiversity_resources = [
    {
        "name": "TaleroAI 未来招聘愿景",
        "name_en": "TaleroAI Future of Recruitment",
        "url": "https://taleroai.com/2025/04/06/the-future-of-recruitment-ai-gamification-taleros-vision/",
        "tags": ["AI"],
    },
]

# ============================================================
# Apply resources to categories
# ============================================================

print("=" * 60)
print("Adding verified resources (Batch 22)")
print("=" * 60)

total_added = 0

print("\n[1] 员工推荐")
total_added += add_to_category("员工推荐", referral_resources)

print("\n[2] 人才社区与人才库建设")
total_added += add_to_category("人才社区与人才库建设", talent_pool_resources)

print("\n[3] 游戏化与 VR/AR 招聘")
total_added += add_to_category("游戏化与 VR/AR 招聘", gamification_resources)

print("\n[4] 招聘视频与多媒体")
total_added += add_to_category("招聘视频与多媒体", video_resources)

print("\n[5] 全球招聘与远程团队")
total_added += add_to_category("全球招聘与远程团队", global_resources)

print("\n[6] 神经多样性招聘")
total_added += add_to_category("神经多样性招聘", neurodiversity_resources)

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
