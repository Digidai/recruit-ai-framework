#!/usr/bin/env python3
"""
Restructure tarf.json to have a better hierarchy.
Groups 58 flat categories into 10 meta-categories for easier navigation.
"""

import json
import re

# Define the new hierarchy structure
# Maps meta-category to list of original category number prefixes
NEW_HIERARCHY = {
    "A 招聘流程与方法论": {
        "name": "A 招聘流程与方法论",
        "name_en": "A Recruiting Process & Methodology",
        "categories": ["01 ", "07 ", "26 ", "33 "],  # 流程、测评面试、面试官培训、心理学
        "description": "招聘方法论、面试技巧、测评体系、行为科学"
    },
    "B 招聘渠道与 Sourcing": {
        "name": "B 招聘渠道与 Sourcing",
        "name_en": "B Recruiting Channels & Sourcing",
        "categories": ["03 ", "04 ", "05 ", "16 ", "17 ", "22 "],  # 职位发布、人才画像、搜索模板、校招、高管、行业
        "description": "职位发布、人才库、搜索技巧、细分人群招聘"
    },
    "C 招聘系统与工具": {
        "name": "C 招聘系统与工具",
        "name_en": "C Recruiting Systems & Tools",
        "categories": ["06 ", "20 ", "25 ", "53 "],  # ATS、API、自动化、效率工具
        "description": "ATS/CRM、招聘自动化、API集成、效率工具"
    },
    "D AI 招聘技术": {
        "name": "D AI 招聘技术",
        "name_en": "D AI in Recruiting",
        "categories": ["09 ", "10 ", "11 ", "15 ", "54 "],  # AI应用、AI治理、开源组件、LLM、AI面试
        "description": "AI招聘工具、风险治理、公平性审计、LLM应用"
    },
    "E 合规与法律": {
        "name": "E 合规与法律",
        "name_en": "E Compliance & Legal",
        "categories": ["08 ", "19 ", "23 ", "34 ", "40 "],  # Offer背调、薪酬透明、数据隐私、劳动法、反欺诈
        "description": "背景调查、数据隐私、劳动法规、薪酬合规"
    },
    "F 多元化与包容性招聘": {
        "name": "F 多元化与包容性招聘",
        "name_en": "F DEI & Inclusive Hiring",
        "categories": ["28 ", "29 ", "47 ", "51 "],  # 退伍军人、残障、伦理公平、神经多样性
        "description": "退伍军人、残障人士、神经多样性、公平招聘"
    },
    "G 雇主品牌与候选人体验": {
        "name": "G 雇主品牌与候选人体验",
        "name_en": "G Employer Brand & Candidate Experience",
        "categories": ["21 ", "36 ", "37 ", "42 ", "49 ", "50 ", "57 "],  # 候选人体验、远程面试、营销、游戏化、视觉、CRM、视频
        "description": "雇主品牌、候选人体验、招聘营销、视频招聘"
    },
    "H 人才管理与规划": {
        "name": "H 人才管理与规划",
        "name_en": "H Talent Management & Planning",
        "categories": ["13 ", "24 ", "48 ", "56 ", "58 "],  # 员工推荐、继任计划、内部流动、人才社区、团队协作
        "description": "内部流动、继任计划、人才库建设、团队协作"
    },
    "I 全球招聘与特殊场景": {
        "name": "I 全球招聘与特殊场景",
        "name_en": "I Global Recruiting & Special Scenarios",
        "categories": ["12 ", "18 ", "30 ", "38 ", "41 ", "52 "],  # 全球EOR、RPO、区域、技术招聘、灵活用工、蓝领
        "description": "全球招聘、RPO外包、技术招聘、蓝领招聘"
    },
    "J 数据分析与行业洞察": {
        "name": "J 数据分析与行业洞察",
        "name_en": "J Data Analytics & Industry Insights",
        "categories": ["02 ", "14 ", "27 ", "31 ", "32 ", "35 ", "39 ", "43 ", "44 ", "45 ", "46 ", "55 "],  # 薪酬字典、学习、活动、播客、模板、分析、情报、预算、实践、文档、职业、报告
        "description": "薪酬数据、招聘分析、行业报告、学习资源"
    },
}

def find_category_by_prefix(categories, prefix):
    """Find a category node by its number prefix."""
    for cat in categories:
        if cat.get('name', '').startswith(prefix):
            return cat
    return None

def restructure():
    # Load current data
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    original_categories = data.get('children', [])

    # Create new structure
    new_children = []
    used_categories = set()

    for meta_key, meta_info in NEW_HIERARCHY.items():
        meta_node = {
            "name": meta_info["name"],
            "name_en": meta_info["name_en"],
            "type": "folder",
            "children": []
        }

        # Find and add original categories to this meta-category
        for prefix in meta_info["categories"]:
            orig_cat = find_category_by_prefix(original_categories, prefix)
            if orig_cat:
                # Remove the number prefix from the original category name for cleaner display
                orig_name = orig_cat.get('name', '')
                orig_name_en = orig_cat.get('name_en', '')

                # Create a copy without modifying original
                cat_copy = dict(orig_cat)

                # Remove number prefix (e.g., "01 " -> "")
                clean_name = re.sub(r'^\d{2}\s+', '', orig_name)
                clean_name_en = re.sub(r'^\d{2}\s+', '', orig_name_en) if orig_name_en else clean_name

                cat_copy['name'] = clean_name
                cat_copy['name_en'] = clean_name_en

                meta_node['children'].append(cat_copy)
                used_categories.add(prefix.strip())

        if meta_node['children']:
            new_children.append(meta_node)

    # Check for any missed categories
    for cat in original_categories:
        prefix = cat.get('name', '')[:3].strip()
        if prefix not in used_categories:
            print(f"Warning: Category not assigned: {cat.get('name', '')}")

    # Update the root node
    data['children'] = new_children

    # Save restructured data
    with open('docs/tarf.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Print summary
    print("=== 重组完成 ===\n")
    print(f"原始分类数: {len(original_categories)}")
    print(f"新大类数: {len(new_children)}")
    print("\n新结构:")
    for meta in new_children:
        print(f"  {meta['name']} ({len(meta['children'])} 子分类)")
        for child in meta['children']:
            print(f"    - {child['name']}")

if __name__ == "__main__":
    restructure()
