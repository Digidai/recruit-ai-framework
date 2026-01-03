#!/usr/bin/env python3
"""
AI 招聘工具 资源补充脚本
Cross-validated resources for AI recruiting tools
"""

import json

# New verified resources organized by parent category
NEW_RESOURCES = {
    # ===== JD 写作/招聘文案 =====
    "JD 写作/招聘文案": [
        {
            "name": "Textio（AI招聘文案优化）",
            "name_en": "Textio (AI Recruiting Language)",
            "type": "url",
            "url": "https://textio.com/",
            "tags": ["AI", "JD Writing", "Bias Detection"]
        },
        {
            "name": "GoHire（职位描述生成器）",
            "name_en": "GoHire (Job Description Generator)",
            "type": "url",
            "url": "https://gohire.io/",
            "tags": ["AI", "JD Writing", "ATS"]
        },
        {
            "name": "Ongig（职位页面优化）",
            "name_en": "Ongig (Job Page Optimization)",
            "type": "url",
            "url": "https://www.ongig.com/",
            "tags": ["AI", "JD Writing", "DEI"]
        },
        {
            "name": "Datapeople（JD分析平台）",
            "name_en": "Datapeople (JD Analytics Platform)",
            "type": "url",
            "url": "https://www.datapeople.io/",
            "tags": ["AI", "JD Analytics", "Performance"]
        },
        {
            "name": "TalVista（包容性JD审核）",
            "name_en": "TalVista (Inclusive JD Review)",
            "type": "url",
            "url": "https://www.talvista.com/",
            "tags": ["AI", "JD Writing", "Inclusive"]
        },
    ],

    # ===== 智能寻才/人才匹配 =====
    "智能寻才/人才匹配": [
        {
            "name": "SeekOut（AI人才搜索）",
            "name_en": "SeekOut (AI Talent Search)",
            "type": "url",
            "url": "https://www.seekout.com/",
            "tags": ["AI", "Sourcing", "Diversity"]
        },
        {
            "name": "hireEZ（AI寻才平台）",
            "name_en": "hireEZ (AI Sourcing Platform)",
            "type": "url",
            "url": "https://hireez.com/",
            "tags": ["AI", "Sourcing", "Outbound"]
        },
        {
            "name": "Entelo（预测型人才寻找）",
            "name_en": "Entelo (Predictive Talent Sourcing)",
            "type": "url",
            "url": "https://www.entelo.com/",
            "tags": ["AI", "Sourcing", "Predictive"]
        },
        {
            "name": "Fetcher（AI招聘自动化）",
            "name_en": "Fetcher (AI Recruiting Automation)",
            "type": "url",
            "url": "https://www.fetcher.ai/",
            "tags": ["AI", "Sourcing", "Automation"]
        },
        {
            "name": "Findem（人才数据平台）",
            "name_en": "Findem (Talent Data Platform)",
            "type": "url",
            "url": "https://www.findem.ai/",
            "tags": ["AI", "Sourcing", "Attributes"]
        },
        {
            "name": "AmazingHiring（技术人才寻找）",
            "name_en": "AmazingHiring (Tech Talent Sourcing)",
            "type": "url",
            "url": "https://amazinghiring.com/",
            "tags": ["AI", "Sourcing", "Tech"]
        },
    ],

    # ===== AI 候选人沟通/Chatbot =====
    "AI 候选人沟通/Chatbot": [
        {
            "name": "Humanly.io（对话式招聘AI）",
            "name_en": "Humanly.io (Conversational Recruiting AI)",
            "type": "url",
            "url": "https://humanly.io/",
            "tags": ["AI", "Chatbot", "Screening"]
        },
        {
            "name": "Phenom X+ Chatbot（人才体验聊天机器人）",
            "name_en": "Phenom X+ Chatbot (Talent Experience Bot)",
            "type": "url",
            "url": "https://www.phenom.com/chatbot",
            "tags": ["AI", "Chatbot", "Enterprise"]
        },
        {
            "name": "Sense Messaging（候选人互动平台）",
            "name_en": "Sense Messaging (Candidate Engagement)",
            "type": "url",
            "url": "https://www.sensehq.com/",
            "tags": ["AI", "Chatbot", "Engagement"]
        },
        {
            "name": "AllyO（端到端招聘AI）",
            "name_en": "AllyO (End-to-End Recruiting AI)",
            "type": "url",
            "url": "https://www.allyo.com/",
            "tags": ["AI", "Chatbot", "Automation"]
        },
        {
            "name": "Brazen（虚拟招聘活动）",
            "name_en": "Brazen (Virtual Recruiting Events)",
            "type": "url",
            "url": "https://www.brazen.com/",
            "tags": ["AI", "Chatbot", "Virtual Events"]
        },
    ],

    # ===== AI 简历解析/筛选 =====
    "AI 简历解析/筛选": [
        {
            "name": "Skima AI（AI简历筛选）",
            "name_en": "Skima AI (AI Resume Screening)",
            "type": "url",
            "url": "https://www.skima.ai/",
            "tags": ["AI", "Resume", "Screening"]
        },
        {
            "name": "CVViZ（AI简历解析器）",
            "name_en": "CVViZ (AI Resume Parser)",
            "type": "url",
            "url": "https://cvviz.com/",
            "tags": ["AI", "Resume", "Parsing"]
        },
        {
            "name": "Affinda（文档AI处理）",
            "name_en": "Affinda (Document AI Processing)",
            "type": "url",
            "url": "https://www.affinda.com/",
            "tags": ["AI", "Resume", "Document AI"]
        },
        {
            "name": "DaXtra（简历解析与搜索）",
            "name_en": "DaXtra (Resume Parsing & Search)",
            "type": "url",
            "url": "https://www.daxtra.com/",
            "tags": ["AI", "Resume", "Search"]
        },
        {
            "name": "Rchilli（简历解析API）",
            "name_en": "Rchilli (Resume Parsing API)",
            "type": "url",
            "url": "https://www.rchilli.com/",
            "tags": ["AI", "Resume", "API"]
        },
        {
            "name": "Sovren（HR文档AI）",
            "name_en": "Sovren (HR Document AI)",
            "type": "url",
            "url": "https://www.sovren.com/",
            "tags": ["AI", "Resume", "Matching"]
        },
    ],

    # ===== AI 面试/测评 =====
    "AI 面试/测评": [
        {
            "name": "Glider AI（技能评估平台）",
            "name_en": "Glider AI (Skills Assessment Platform)",
            "type": "url",
            "url": "https://glider.ai/",
            "tags": ["AI", "Assessment", "Skills"]
        },
        {
            "name": "Crosschq（AI推荐人核查）",
            "name_en": "Crosschq (AI Reference Checking)",
            "type": "url",
            "url": "https://www.crosschq.com/",
            "tags": ["AI", "Reference", "Analytics"]
        },
        {
            "name": "Modern Hire（AI招聘平台）",
            "name_en": "Modern Hire (AI Hiring Platform)",
            "type": "url",
            "url": "https://www.modernhire.com/",
            "tags": ["AI", "Interview", "Assessment"]
        },
        {
            "name": "Codility（技术评估平台）",
            "name_en": "Codility (Technical Assessment)",
            "type": "url",
            "url": "https://www.codility.com/",
            "tags": ["AI", "Coding", "Assessment"]
        },
        {
            "name": "Qualified.io（实时编程评估）",
            "name_en": "Qualified.io (Live Coding Assessment)",
            "type": "url",
            "url": "https://www.qualified.io/",
            "tags": ["AI", "Coding", "Live"]
        },
    ],

    # ===== 招聘数据分析/洞察 =====
    "招聘数据分析/洞察": [
        {
            "name": "TalentNeuron（劳动力市场分析）",
            "name_en": "TalentNeuron (Labor Market Analytics)",
            "type": "url",
            "url": "https://www.talentneuron.com/",
            "tags": ["AI", "Analytics", "Labor Market"]
        },
        {
            "name": "Crunchr（人力分析平台）",
            "name_en": "Crunchr (People Analytics Platform)",
            "type": "url",
            "url": "https://www.crunchr.com/",
            "tags": ["AI", "Analytics", "Workforce"]
        },
        {
            "name": "ChartHop（组织分析）",
            "name_en": "ChartHop (Org Analytics)",
            "type": "url",
            "url": "https://www.charthop.com/",
            "tags": ["AI", "Analytics", "Org Chart"]
        },
        {
            "name": "One Model（人力数据分析）",
            "name_en": "One Model (People Data Analytics)",
            "type": "url",
            "url": "https://www.onemodel.co/",
            "tags": ["AI", "Analytics", "Data"]
        },
        {
            "name": "Orgnostic（组织健康分析）",
            "name_en": "Orgnostic (Org Health Analytics)",
            "type": "url",
            "url": "https://www.orgnostic.com/",
            "tags": ["AI", "Analytics", "Health"]
        },
    ],

    # ===== AI 招聘工具 (直接子节点) =====
    "AI 招聘工具": [
        {
            "name": "Beamery（人才生命周期管理）",
            "name_en": "Beamery (Talent Lifecycle Management)",
            "type": "url",
            "url": "https://beamery.com/",
            "tags": ["AI", "TRM", "Enterprise"]
        },
        {
            "name": "Gem（人才互动平台）",
            "name_en": "Gem (Talent Engagement Platform)",
            "type": "url",
            "url": "https://www.gem.com/",
            "tags": ["AI", "CRM", "Sourcing"]
        },
        {
            "name": "Hired（AI人才市场）",
            "name_en": "Hired (AI Talent Marketplace)",
            "type": "url",
            "url": "https://hired.com/",
            "tags": ["AI", "Marketplace", "Tech"]
        },
        {
            "name": "Eightfold.ai（人才智能平台）",
            "name_en": "Eightfold.ai (Talent Intelligence)",
            "type": "url",
            "url": "https://eightfold.ai/",
            "tags": ["AI", "Intelligence", "Matching"]
        },
        {
            "name": "Loxo（招聘CRM与AI）",
            "name_en": "Loxo (Recruiting CRM & AI)",
            "type": "url",
            "url": "https://loxo.co/",
            "tags": ["AI", "CRM", "ATS"]
        },
        {
            "name": "Jobvite（招聘自动化套件）",
            "name_en": "Jobvite (Recruiting Automation Suite)",
            "type": "url",
            "url": "https://www.jobvite.com/",
            "tags": ["AI", "ATS", "Automation"]
        },
        {
            "name": "iCIMS AI（人才云平台）",
            "name_en": "iCIMS AI (Talent Cloud)",
            "type": "url",
            "url": "https://www.icims.com/",
            "tags": ["AI", "ATS", "Enterprise"]
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
