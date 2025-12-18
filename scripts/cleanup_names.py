#!/usr/bin/env python3
"""Clean up category names for better readability."""

import json
import re

# Name cleanup mappings
NAME_CLEANUPS = {
    # Remove redundant prefixes and simplify names
    "渠道：职位发布 & 招聘营销": "职位发布与招聘营销",
    "渠道：人才画像（公开档案/社区）": "人才画像与开放社区",
    "Sourcing：搜索模板（X-Ray / Boolean）": "搜索模板（X-Ray/Boolean）",
    "测评与面试（Assessments & Interviewing）": "测评与面试",
    "AI 招聘应用场景（工具/平台）": "AI 招聘工具",
    "AI 风险治理与合规（Hiring AI）": "AI 风险治理与合规",
    "开源组件（公平性/审计/工具）": "开源公平性工具",
    "生成式 AI / LLM 招聘应用": "生成式 AI (LLM) 招聘",
    "校园招聘 / 实习生": "校园招聘与实习",
    "高管招聘 / Executive Search": "高管招聘",
    "全球招聘 / EOR / 远程团队": "全球招聘与远程团队",
    "RPO / 招聘外包": "招聘流程外包 (RPO)",
    "员工推荐 / 内部流动": "员工推荐",
    "残障人士 / 无障碍招聘": "无障碍招聘",
    "候选人体验 / 雇主品牌": "候选人体验与雇主品牌",
    "候选人关系管理 (CRM)": "候选人关系管理",
    "市场/薪酬/职位与技能字典": "薪酬与职位数据",
    "学习资源 / 研究社区": "学习资源与研究",
    "招聘分析与 People Analytics": "招聘分析 (People Analytics)",
    "招聘游戏化与 VR/AR": "游戏化与 VR/AR 招聘",
    "ATS / CRM / 招聘协作": "ATS 与招聘协作",
    "招聘 API / 开发者资源": "招聘 API 与开发者资源",
    "Offer / 背调 / 入职": "Offer、背调与入职",
}

# English name cleanups
NAME_EN_CLEANUPS = {
    "Recruiting Channels & Sourcing": "Channels & Sourcing",
    "Recruiting Systems & Tools": "Systems & Tools",
    "AI in Recruiting": "AI Recruiting",
    "Compliance & Legal": "Compliance & Legal",
    "DEI & Inclusive Hiring": "DEI & Inclusive Hiring",
    "Employer Brand & Candidate Experience": "Employer Brand & CX",
    "Talent Management & Planning": "Talent Management",
    "Global Recruiting & Special Scenarios": "Global & Special Scenarios",
    "Data Analytics & Industry Insights": "Data & Insights",
    "职位发布与招聘营销": "Job Posting & Recruitment Marketing",
    "人才画像与开放社区": "Talent Profiles & Communities",
    "搜索模板（X-Ray/Boolean）": "Search Templates (X-Ray/Boolean)",
    "测评与面试": "Assessment & Interviewing",
    "AI 招聘工具": "AI Recruiting Tools",
    "AI 风险治理与合规": "AI Governance & Compliance",
    "开源公平性工具": "Open Source Fairness Tools",
    "生成式 AI (LLM) 招聘": "Generative AI (LLM) Recruiting",
    "校园招聘与实习": "Campus Recruiting & Internships",
    "高管招聘": "Executive Search",
    "全球招聘与远程团队": "Global Hiring & Remote Teams",
    "招聘流程外包 (RPO)": "Recruitment Process Outsourcing (RPO)",
    "员工推荐": "Employee Referrals",
    "无障碍招聘": "Accessible Hiring",
    "候选人体验与雇主品牌": "Candidate Experience & Employer Brand",
    "候选人关系管理": "Candidate Relationship Management",
    "薪酬与职位数据": "Compensation & Job Data",
    "学习资源与研究": "Learning Resources & Research",
    "招聘分析 (People Analytics)": "Recruiting Analytics (People Analytics)",
    "游戏化与 VR/AR 招聘": "Gamification & VR/AR Recruiting",
    "ATS 与招聘协作": "ATS & Recruiting Collaboration",
    "招聘 API 与开发者资源": "Recruiting API & Developer Resources",
    "Offer、背调与入职": "Offer, Background Check & Onboarding",
}

def cleanup_names(node):
    """Recursively clean up node names."""
    name = node.get('name', '')
    name_en = node.get('name_en', '')

    # Apply cleanup
    if name in NAME_CLEANUPS:
        node['name'] = NAME_CLEANUPS[name]
        name = node['name']

    # Update English name
    if name in NAME_EN_CLEANUPS:
        node['name_en'] = NAME_EN_CLEANUPS[name]
    elif name_en in NAME_EN_CLEANUPS:
        node['name_en'] = NAME_EN_CLEANUPS[name_en]

    # Process children
    for child in node.get('children', []):
        cleanup_names(child)

def main():
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    cleanup_names(data)

    with open('docs/tarf.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Names cleaned up!")

    # Show updated structure
    print("\n=== 清理后的结构 ===\n")
    for meta in data.get('children', []):
        print(f"📁 {meta['name']}")
        print(f"   {meta.get('name_en', '')}")
        for cat in meta.get('children', [])[:3]:
            print(f"   └─ {cat['name']}")
        if len(meta.get('children', [])) > 3:
            print(f"   └─ ... +{len(meta['children']) - 3} more")
        print()

if __name__ == "__main__":
    main()
