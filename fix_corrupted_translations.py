#!/usr/bin/env python3
"""
Fix corrupted translations in tarf.json where English letter sequences
were incorrectly translated to Chinese characters.

Patterns found:
- "or" → "或"
- "by" → "通过"
- "to" → "到"
- "on" → "关于"
- "at" → "在"
- "of" → "的"
- "our" → "我们的"
- "and" → "和"
- etc.
"""

import json
import re

# Known corrupted names and their correct versions
KNOWN_FIXES = {
    # Schema.org
    "Schema.或g｜工作帖子在g Schema": "Schema.org｜Job Posting Schema",
    "Schema.或g｜工作帖子ing Schema": "Schema.org｜Job Posting Schema",

    # Behavioral
    "Behavi或al Insights Team": "Behavioral Insights Team",
    "ideas42（Behavi或al Science）": "ideas42（Behavioral Science）",

    # Work/Workday/Workable
    "W或kday API": "Workday API",
    "W或kday Career Hub": "Workday Career Hub",
    "W或kable": "Workable",
    "W或kable 政策 模板": "Workable 政策模板",
    "W或kable HR 术语表": "Workable HR 术语表",
    "W或k在o HR C关于nect或s": "Workato HR Connectors",
    "Workday｜Opp或tunity Graph": "Workday｜Opportunity Graph",
    "VNDLY（W或kday）": "VNDLY（Workday）",
    "We W或k 远程ly": "We Work Remotely",
    "Unleash W或ld": "Unleash World",
    "ILO｜W或ld Employment": "ILO｜World Employment",
    "WES（W或ld Educ在i关于 Services）": "WES（World Education Services）",

    # Ashby
    "Ash通过 API": "Ashby API",
    "Ash通过 自动化s": "Ashby Automations",

    # Glassdoor
    "Glassdo或 为 Employers": "Glassdoor for Employers",
    "Glassdo或 Company 更新s": "Glassdoor Company Updates",
    "Glassdo或 Salaries": "Glassdoor Salaries",
    "Glassdo或": "Glassdoor",

    # Monster
    "M关于ster": "Monster",
    "FoundIt (M关于ster India)": "FoundIt (Monster India)",

    # Upwork
    "Upw或k": "Upwork",

    # Teamtailor
    "Teamtail或": "Teamtailor",

    # TensorFlow
    "Tens或Flow 公平性 Indic在或s": "TensorFlow Fairness Indicators",

    # Colorado/Washington states
    "Col或ado｜Equal 薪酬 为 Equal W或k 法案": "Colorado｜Equal Pay for Equal Work Act",
    "Washing到n｜Equal 薪酬 和 Opp或tunities 法案": "Washington｜Equal Pay and Opportunities Act",

    # Australia
    "Australia｜W或kplace 性别 Equality": "Australia｜Workplace Gender Equality",

    # DOL/NLRB
    "DOL（Department 的 Lab或）": "DOL（Department of Labor）",
    "NLRB（N在i关于al Lab或 Rel在i关于s Board）": "NLRB（National Labor Relations Board）",

    # I-9
    "I-9 Central（W或k Auth或iz在i关于）": "I-9 Central（Work Authorization）",

    # Military
    "Military Skills Transl在或（Military.com）": "Military Skills Translator（Military.com）",
    "Onward 到 Opp或tunity": "Onward to Opportunity",

    # Understood.org
    "Unders到od.或g 工作 资源": "Understood.org 工作资源",
    "Unders到od.org｜W或kplace": "Understood.org｜Workplace",

    # JAN
    "工作 Accommod在i关于 Netw或k（JAN）": "Job Accommodation Network（JAN）",

    # Autism at Work
    "Autism 在 W或k Employer Roundtable": "Autism at Work Employer Roundtable",
    "SAP Autism 在 W或k": "SAP Autism at Work",
    "Autism@W或k（SAP）": "Autism@Work（SAP）",
    "JPM或gan｜Autism 在 W或k": "JPMorgan｜Autism at Work",

    # Iris Bohnet
    "Iris Bohnet｜什么 W或ks（性别 Equality）": "Iris Bohnet｜What Works（Gender Equality）",

    # Big Five
    "大 Five Pers关于ality Model": "Big Five Personality Model",

    # APA
    "APA｜Industrial-Organiz在i关于al Psychology": "APA｜Industrial-Organizational Psychology",

    # Journal
    "Pers关于nel Psychology J我们的nal": "Personnel Psychology Journal",
    "J我们的nal 的 应用lied Psychology": "Journal of Applied Psychology",

    # Jopwell
    "Jopwell（Black/L在在o/原生 American）": "Jopwell（Black/Latino/Native American）",

    # Fiverr
    "Fiverr Bus在ess": "Fiverr Business",

    # ResearchGate
    "研究G在e": "ResearchGate",

    # Egon Zehnder
    "Eg关于 Zehnder": "Egon Zehnder",

    # eFinancialCareers
    "eF在ancialCareers": "eFinancialCareers",

    # Russell Reynolds
    "Russell Reynolds Associ在es": "Russell Reynolds Associates",

    # Finch
    "F在ch（Employment API）": "Finch（Employment API）",

    # Affinda
    "Aff在da 恢复 Parser API": "Affinda Resume Parser API",

    # Textkernel
    "Textkernel Semantic M在ch在g API": "Textkernel Semantic Matching API",

    # ResumeParser
    "恢复Parser（Pyth关于）": "ResumeParser（Python）",

    # Joblib
    "工作lib（机器学习 Pipel在e）": "Joblib（ML Pipeline）",

    # ModernLoop
    "现代Loop｜Schedul在g": "ModernLoop｜Scheduling",

    # Doodle
    "Doodle｜Group Schedul在g": "Doodle｜Group Scheduling",

    # Cal.com
    "Cal.com｜开放 S我们的ce": "Cal.com｜Open Source",

    # Obsidian
    "Obsidian｜没有te Tak在g": "Obsidian｜Note Taking",

    # Roam Research
    "Roam 研究｜Netw或ked Thought": "Roam Research｜Networked Thought",

    # ContactOut/Hunter
    "ContactOut｜Email 找到er": "ContactOut｜Email Finder",
    "Hunter｜Email 找到er": "Hunter｜Email Finder",

    # Clearbit
    "Clearbit C关于nect｜Email": "Clearbit Connect｜Email",

    # Findem
    "找到em（People Intelligence）": "Findem（People Intelligence）",

    # Alibi Explain
    "Alibi Expla在": "Alibi Explain",

    # Anthropic
    "Anthropic｜Claude 为 W或k": "Anthropic｜Claude for Work",

    # LangChain
    "LangCha在": "LangChain",

    # ACM FAccT
    "ACM｜FAccT C关于ference": "ACM｜FAccT Conference",

    # FTC
    "金融时报C｜Employer 背景调查 和 Y我们的 正确s": "FTC｜Employer Background Checks and Your Rights",

    # Sapling
    "Sapl在g（Kallidus）": "Sapling（Kallidus）",

    # ClickBoarding
    "Click Board在g": "ClickBoarding",

    # ClickUp
    "ClickUp｜所有-在-One": "ClickUp｜All-in-One",

    # Interviewstream
    "在terviewstream": "Interviewstream",

    # Textio
    "Textio｜Inclusive Writ在g": "Textio｜Inclusive Writing",

    # Schmidt & Hunter
    "Schmidt & Hunter｜Validity 的 选择i关于 Methods": "Schmidt & Hunter｜Validity of Selection Methods",

    # Cognitive Biases
    "列表 的 Cognitive 偏见es（Wikipedia）": "List of Cognitive Biases（Wikipedia）",

    # Amazon
    "亚马逊 领导力 Pr在ciples": "Amazon Leadership Principles",

    # Cost-Per-Hire
    "领英 Cost-Per-Hire Calcul在或": "LinkedIn Cost-Per-Hire Calculator",

    # When I Work
    "何时 I Work｜Schedul在g": "When I Work｜Scheduling",

    # Gartner
    "高德纳 Reimag在eHR": "Gartner ReimagineHR",

    # Randstad Sourceright
    "任仕达 S我们的ceright": "Randstad Sourceright",

    # Aon
    "A关于 薪酬公平": "Aon Pay Equity",

    # AIHR
    "AIHR（Academy 到 Innov在e HR）": "AIHR（Academy to Innovate HR）",

    # ATP
    "A人才获取P Annual C关于ference": "ATP Annual Conference",

    # APSCo
    "APSCo 代码 的 C关于duct": "APSCo Code of Conduct",

    # Avature
    "Av在ure｜内部 Mobility": "Avature｜Internal Mobility",

    # Beeline
    "Beel在e VMS": "Beeline VMS",

    # Bender Consulting
    "Bender C关于sult在g Services": "Bender Consulting Services",

    # BLS
    "BLS｜Employment St在istics": "BLS｜Employment Statistics",

    # Business Roundtable
    "Bus在ess Roundtable｜Sec关于d Chance": "Business Roundtable｜Second Chance",

    # Catalant
    "C在alant（专家版 市场place）": "Catalant（Expert Marketplace）",

    # Canada Labour
    "Canada Lab我们的 代码": "Canada Labour Code",

    # Appcast
    "应用cast｜专业版gramm在ic ROI": "Appcast｜Programmatic ROI",

    # Confluence
    "C关于fluence（Atlassian）": "Confluence（Atlassian）",

    # CMX
    "CMX｜Community 专业版fessi关于als": "CMX｜Community Professionals",

    # Cornell
    "C或nell｜ILR School": "Cornell｜ILR School",

    # Cornerstone
    "C或nerst关于e OnDem和": "Cornerstone OnDemand",
    "SumTotal（C或nerst关于e）": "SumTotal（Cornerstone）",

    # Codingame
    "Cod在game 为 W或k": "CodinGame for Work",

    # Dave's Killer Bread
    "Dave's Killer Bread Found在i关于": "Dave's Killer Bread Foundation",

    # Descript
    "Descript｜视频 Edit在g": "Descript｜Video Editing",

    # Dev.to
    "Dev.到 工作": "Dev.to Jobs",

    # Discord
    "Disc或d｜Tech Communities": "Discord｜Tech Communities",

    # DOL HIRE Vets
    "DOL HIRE Vets Medalli关于": "DOL HIRE Vets Medallion",

    # Erin Meyer
    "Er在 Meyer 新闻letter": "Erin Meyer Newsletter",

    # ESCO
    "ESCO｜European Skills Tax关于omy": "ESCO｜European Skills Taxonomy",

    # Fuel50
    "Fuel50｜Career P在h在g": "Fuel50｜Career Pathing",

    # Getting Hired
    "Gett在g Hired": "Getting Hired",

    # GitHub Octoverse
    "GitHub Oc到verse": "GitHub Octoverse",

    # Graduway
    "Graduway｜Alumni Netw或k": "Graduway｜Alumni Network",

    # Grammarly
    "Grammarly Bus在ess": "Grammarly Business",
    "Grammarly｜Writ在g 协助ance": "Grammarly｜Writing Assistance",

    # Grayscale
    "Grayscale｜Text在g": "Grayscale｜Texting",

    # Greenhouse
    "Greenhouse Sc或ecard 模板": "Greenhouse Scorecard 模板",

    # Gusto
    "Gus到 录用通知书 模板": "Gusto Offer Letter 模板",

    # Hemingway
    "Hem在gway Edit或": "Hemingway Editor",

    # Hireology
    "Hireology｜Communic在i关于": "Hireology｜Communication",

    # HR Technology
    "HR Technology C关于ference": "HR Technology Conference",

    # HRZone
    "HRZ关于e（UK）": "HRZone（UK）",

    # Hudson RPO
    "Huds关于 RPO": "Hudson RPO",

    # iHireConstruction
    "iHireC关于structi关于": "iHireConstruction",

    # Integrate Autism
    "Integr在e Autism Employment": "Integrate Autism Employment",

    # Globalization Partners
    "全球iz在i关于 Partners (G-P)": "Globalization Partners (G-P)",

    # Jackson Lewis
    "Jacks关于 Lewis": "Jackson Lewis",

    # JetBrains
    "JetBra在s 发展er Ecosystem": "JetBrains Developer Ecosystem",

    # Jobvite
    "Jobvite｜Recruiter N在i关于": "Jobvite｜Recruiter Nation",

    # Josh Bersin
    "Josh Bers在 Academy": "Josh Bersin Academy",
    "Josh Bers在 Irresistible": "Josh Bersin Irresistible",
    "Josh Bers在（HR Tech）": "Josh Bersin（HR Tech）",

    # Kuula
    "Kuula｜360 T我们的s": "Kuula｜360 Tours",

    # Linear
    "L在ear｜Issue 追踪": "Linear｜Issue Tracking",

    # Legion WFM
    "Legi关于 WFM｜H我们的ly": "Legion WFM｜Hourly",

    # Lightcast
    "Lightcast｜Skills Tax关于omy": "Lightcast｜Skills Taxonomy",

    # Monday.com
    "M关于day.com HR 模板": "Monday.com HR 模板",
    "Monday.com｜W或k OS": "Monday.com｜Work OS",

    # Mettl
    "Mettl 在线评估": "Mettl Online Assessment",

    # Mighty Networks
    "Mighty Netw或ks｜Community": "Mighty Networks｜Community",

    # Matterport
    "M在terport｜3D T我们的s": "Matterport｜3D Tours",

    # TalentNeuron
    "人才Neur关于（高德纳）": "TalentNeuron（Gartner）",

    # National Student Clearinghouse
    "N在i关于al Student Clear在ghouse": "National Student Clearinghouse",

    # Natural Reader
    "N在ural Reader｜Text 到 Speech": "Natural Reader｜Text to Speech",

    # Otter.ai
    "Otter.ai｜Transcripti关于": "Otter.ai｜Transcription",

    # Out & Equal
    "Out & Equal W或kplace Summit": "Out & Equal Workplace Summit",

    # Pano2VR
    "Pano2VR｜虚拟 T我们的s": "Pano2VR｜Virtual Tours",

    # PEAT
    "PEAT（Partnership 关于 Employment & Accessible Technology）": "PEAT（Partnership on Employment & Accessible Technology）",

    # PeopleGrove
    "PeopleGrove｜Career Netw或ks": "PeopleGrove｜Career Networks",

    # Personnel Today
    "Pers关于nel Today（UK）": "Personnel Today（UK）",

    # REC
    "REC 代码 的 Practice": "REC Code of Practice",

    # Recruiters Online
    "Recruiters Onl在e（Facebook）": "Recruiters Online（Facebook）",

    # Recruitics
    "Recruitics（专业版gramm在ic Ads）": "Recruitics（Programmatic Ads）",

    # Remofirst
    "Rem的irst": "Remofirst",

    # Roundme
    "Roundme｜VR T我们的s": "Roundme｜VR Tours",

    # RPOA
    "RPOA（RPO Associ在i关于）": "RPOA（RPO Association）",

    # Salesloft
    "Salesl的t": "Salesloft",

    # Section 503
    "Secti关于 503 的 Rehabilit在i关于 法案": "Section 503 of Rehabilitation Act",

    # SHRM
    "SHRM人力资源协会 所有 Th在gs W或k": "SHRM All Things Work",
    "SHRM人力资源协会 Annual C关于ference": "SHRM Annual Conference",

    # Sigma Computing
    "Sigma Comput在g": "Sigma Computing",

    # Slack
    "Slack｜专业版fessi关于al Communities": "Slack｜Professional Communities",

    # Succession Wizard
    "Successi关于 Wizard": "Succession Wizard",

    # Talent Tech Labs
    "Talent Tech Labs｜Innov在i关于": "Talent Tech Labs｜Innovation",

    # Truckstop
    "Trucks到p｜Truck在g 工作": "Truckstop｜Trucking Jobs",

    # BetterUp
    "更好Up｜Coach在g": "BetterUp｜Coaching",

    # Vimeo
    "Vimeo｜Bus在ess 视频": "Vimeo｜Business Video",

    # Virginia
    "Virg在ia CDPA": "Virginia CDPA",

    # WilsonHCG
    "Wils关于HCG": "WilsonHCG",

    # Wistia
    "Wistia｜视频 市场在g": "Wistia｜Video Marketing",

    # CoolWorks
    "酷Works｜Seas关于al 工作": "CoolWorks｜Seasonal Jobs",

    # Beamery
    "Beamery Budget Plann在g": "Beamery Budget Planning",
}

def fix_json():
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply known fixes
    fixed_count = 0
    for old, new in KNOWN_FIXES.items():
        if old in content:
            content = content.replace(old, new)
            fixed_count += 1
            print(f"Fixed: {old} → {new}")

    # Parse and save
    data = json.loads(content)

    with open('docs/tarf.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\nTotal fixes applied: {fixed_count}")

    # Check for remaining issues
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for suspicious patterns (English word with embedded Chinese)
    pattern = r'"name":\s*"([^"]*[a-zA-Z][^"]*[或通过到在关于的我们]+[^"]*)"'
    remaining = re.findall(pattern, content)

    if remaining:
        print(f"\n⚠️  Remaining suspicious names ({len(remaining)}):")
        for name in remaining:
            print(f"  - {name}")
    else:
        print("\n✓ No remaining suspicious patterns found!")

    return fixed_count

if __name__ == "__main__":
    fix_json()
