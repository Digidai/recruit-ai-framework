#!/usr/bin/env python3
"""Fix final remaining Chinese text in name_en fields."""

import json
import re

# Direct translation mappings for remaining nodes
DIRECT_TRANSLATIONS = {
    # (M) suffix items - Chinese search tools
    "LinkedIn 个人页 X-Ray（M）": "LinkedIn Profile X-Ray (M)",
    "LinkedIn 个人页 X-Ray": "LinkedIn Profile X-Ray",
    "LinkedIn 公司员工 X-Ray（M）": "LinkedIn Company Employee X-Ray (M)",
    "LinkedIn 公司员工 X-Ray": "LinkedIn Company Employee X-Ray",
    "GitHub 用户搜索（M）": "GitHub User Search (M)",
    "GitHub 用户搜索": "GitHub User Search",
    "GitHub 代码搜索（M）": "GitHub Code Search (M)",
    "GitHub 代码搜索": "GitHub Code Search",
    "GitHub 议题/PR 搜索（M）": "GitHub Issues/PR Search (M)",
    "GitHub 组织成员搜索（M）": "GitHub Org Members Search (M)",
    "Kaggle 搜索（M）": "Kaggle Search (M)",
    "Stack Overflow 用户搜索（M）": "Stack Overflow User Search (M)",
    "Twitter/X 搜索（M）": "Twitter/X Search (M)",
    "ResearchGate 搜索（M）": "ResearchGate Search (M)",
    "布尔搜索构建器（M）": "Boolean Search Builder (M)",
    "布尔搜索实战（M）": "Boolean Search Practice (M)",
    "Google CSE 配置（M）": "Google CSE Configuration (M)",
    "X-Ray 生成器（M）": "X-Ray Generator (M)",
    "高级 Google 搜索（M）": "Advanced Google Search (M)",
    "多平台 X-Ray（M）": "Multi-Platform X-Ray (M)",

    # Chinese ATS/HR systems
    "北森｜招聘管理系统": "Beisen (Chinese ATS)",
    "用友大易（招聘云）": "Yonyou Dayi (Chinese Recruiting Cloud)",
    "用友大易": "Yonyou Dayi",
    "谷露招聘管理系统": "Gulu Recruiting System",

    # Legal/Compliance items
    "FTC｜FCRA 背景筛查指南（Employers）": "FTC FCRA Background Check Guide (Employers)",
    "FTC｜FCRA 背景筛查指南": "FTC FCRA Background Check Guide",
    "GDPR｜自动化决策（Article 22）": "GDPR Automated Decision-Making (Article 22)",
    "GDPR｜自动化决策": "GDPR Automated Decision-Making",
    "Deloitte｜NYC LL144 偏差审计服务": "Deloitte NYC LL144 Bias Audit Service",

    # Chinese job platforms
    "实习僧": "Shixiseng (Chinese Internship Platform)",
    "刺猬实习": "Ciwei (Chinese Internship Platform)",
    "大街网": "Dajie (Chinese Job Network)",
    "看准网（中国）": "Kanzhun (Chinese Company Reviews)",
    "看准网": "Kanzhun",
    "职友集（中国）": "Zhiyouji (Chinese Salary Data)",
    "职友集": "Zhiyouji",

    # Chinese legal framework
    "中国｜个人信息保护法（PIPL）": "China Personal Information Protection Law (PIPL)",
    "中国｜个人信息保护法": "China PIPL",
    "中国｜数据安全法": "China Data Security Law",
    "中国｜网络安全法": "China Cybersecurity Law",
    "中国｜劳动法": "China Labor Law",
    "中国｜劳动合同法": "China Labor Contract Law",
    "人力资源和社会保障部": "Ministry of Human Resources and Social Security (China)",
    "中国法律服务网": "China Legal Service Network",
    "学信网（中国学历）": "CHSI (China Education Verification)",
    "学信网": "CHSI",

    # Chinese tech company recruiting
    "字节跳动招聘": "ByteDance Careers",
    "阿里巴巴招聘": "Alibaba Careers",
    "腾讯招聘": "Tencent Careers",
    "美团招聘": "Meituan Careers",
    "京东招聘": "JD.com Careers",
    "百度招聘": "Baidu Careers",
    "网易招聘": "NetEase Careers",
    "小米招聘": "Xiaomi Careers",
    "华为招聘": "Huawei Careers",
    "滴滴招聘": "DiDi Careers",
    "拼多多招聘": "Pinduoduo Careers",
    "快手招聘": "Kuaishou Careers",
    "哔哩哔哩招聘": "Bilibili Careers",

    # Chinese job platforms
    "智联招聘": "Zhaopin (Chinese Job Board)",
    "前程无忧（51job）": "51Job (Chinese Job Board)",
    "BOSS 直聘": "Boss Zhipin (Chinese Direct Hiring)",
    "猎聘": "Liepin (Chinese Executive Recruiting)",
    "拉勾网": "Lagou (Chinese Tech Jobs)",
    "脉脉": "Maimai (Chinese Professional Network)",

    # Other Chinese specific items
    "知乎（技术问答）": "Zhihu (Chinese Q&A Platform)",
    "CSDN（技术博客）": "CSDN (Chinese Tech Blog)",
    "掘金（技术社区）": "Juejin (Chinese Dev Community)",
    "SegmentFault（技术问答）": "SegmentFault (Chinese Tech Q&A)",
    "V2EX（技术论坛）": "V2EX (Chinese Tech Forum)",
    "GitChat（技术分享）": "GitChat (Chinese Tech Sharing)",
    "InfoQ 中国": "InfoQ China",
    "思否": "SegmentFault",
    "开源中国": "OSChina",

    # Additional patterns found
    "个人页 X-Ray": "Profile X-Ray",
    "公司员工 X-Ray": "Company Employee X-Ray",
    "用户搜索": "User Search",
    "代码搜索": "Code Search",
    "议题/PR 搜索": "Issues/PR Search",
    "组织成员搜索": "Org Members Search",
}

def process_node(node):
    """Process a single node and its children."""
    name_en = node.get('name_en', '')

    # Check if name_en contains Chinese
    if name_en and re.search(r'[\u4e00-\u9fff]', name_en):
        # Direct translation lookup
        if name_en in DIRECT_TRANSLATIONS:
            node['name_en'] = DIRECT_TRANSLATIONS[name_en]
        else:
            # Try partial matching for items not in direct list
            for cn, en in DIRECT_TRANSLATIONS.items():
                if cn in name_en:
                    node['name_en'] = name_en.replace(cn, en)
                    break

    # Process children
    for child in node.get('children', []):
        process_node(child)

def main():
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    process_node(data)

    with open('docs/tarf.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Final translations updated!")

if __name__ == "__main__":
    main()
