# Recruitment & AI Hiring Framework

<p align="center">
  <strong>招聘 × AI 招聘工具导航地图</strong>
</p>

<p align="center">
  <em>一个数据驱动的招聘全流程工具库，覆盖 AI 招聘风险治理与合规</em>
</p>

<p align="center">
  <a href="#特色亮点">特色亮点</a> •
  <a href="#快速开始">快速开始</a> •
  <a href="#58大分类导览">分类导览</a> •
  <a href="#ai-招聘风险治理">AI 风险治理</a> •
  <a href="#贡献指南">贡献指南</a>
</p>

---

## 项目简介

**Recruitment & AI Hiring Framework** 是一个灵感来源于 [OSINT Framework](https://osintframework.com/) 的招聘工具导航项目。它将「树形导航」方式迁移到招聘与 AI 招聘领域，帮助 HR、招聘专业人士、AI/ML 工程师和合规专家快速定位工具、法规标准、最佳实践与开源组件。

### 为什么需要这个项目？

- **工具碎片化**：招聘涉及数百种工具，从职位发布到背景调查，缺乏统一入口
- **AI 风险意识薄弱**：AI 招聘带来公平性、透明度、法律合规等新挑战
- **信息分散**：NIST、ISO、EEOC 等标准散落各处，难以系统学习
- **区域差异大**：中国、美国、欧盟的招聘生态和法规各不相同

本项目旨在提供一个**开放、透明、负责任**的招聘 AI 生态导航。

---

## 特色亮点

| 特性 | 说明 |
|------|------|
| **交互式树形导航** | D3.js 可视化，支持缩放（0.1x~10x）、展开/收起全部、平滑动画 |
| **智能全文搜索** | 支持中英文关键词，防抖优化，`/` 快捷聚焦，`Esc` 清空 |
| **中英文双语界面** | 一键切换中文/英文界面，语言偏好自动保存 |
| **58大分类体系** | 覆盖招聘全流程，从 JD 撰写到入职，包含 AI 风险治理、DEI、神经多样性等专项 |
| **1288 精选资源** | 工具、标准、法规、最佳实践、开源组件、学习资源 |
| **实时数据统计** | 自动统计分类数、资源数、热门标签分布 |
| **键盘无障碍** | 完整键盘导航支持，ARIA 标签，屏幕阅读器友好 |
| **模板链接支持** | 动态搜索模板（含 `{query}` 占位符），输入关键词即可打开 |
| **多维度标签系统** | R(注册)/P(付费)/O(开源)/M(模板)/Law/Framework 等 |
| **SEO 优化** | Open Graph、Twitter Card、canonical URL、sitemap 完备 |
| **零构建部署** | 纯静态站点，无需 npm/webpack，JSON 数据驱动 |
| **MIT 开源** | 自由使用、修改和分发，社区贡献友好 |

---

## 快速开始

### 在线访问

**GitHub Pages**：[https://digidai.github.io/recruit-ai-framework/](https://digidai.github.io/recruit-ai-framework/)

### 本地预览

```bash
# 进入项目目录
cd recruit-ai-framework

# 启动本地 HTTP 服务（任选一种）
python -m http.server 8000        # Python 3
# 或
python3 -m http.server 8000       # macOS/Linux
# 或
npx http-server ./docs -p 8000    # Node.js

# 打开浏览器访问
open http://localhost:8000/docs/
```

> **注意**：直接双击打开 `index.html` 会因浏览器 CORS 安全策略无法读取 `tarf.json`，必须通过 HTTP 服务访问。

### 部署到生产环境

#### GitHub Pages

1. 进入仓库 Settings → Pages
2. Source 选择 **Deploy from a branch**
3. Branch 选择 **main**，目录选择 **/docs**
4. 点击 Save，等待部署完成
5. 访问：`https://<username>.github.io/recruit-ai-framework/`

#### Vercel / Netlify / Cloudflare Pages

1. 连接 GitHub 仓库
2. 设置 Output Directory 为 `docs`
3. 自动部署完成

---

## 58大分类导览

本框架包含 58 个分类，覆盖招聘全流程。以下为各分类概览：

<details>
<summary><strong>点击展开完整分类列表（58个）</strong></summary>

| 分类 | 覆盖范围 | 核心价值 |
|------|---------|---------|
| **01 招聘流程与方法论** | 结构化面试、选拔框架、合规指导 | 建立科学的招聘方法论基础 |
| **02 市场/薪酬/职位与技能字典** | O*NET、ESCO、SFIA、薪酬数据库 | 职位标准化和市场定价参考 |
| **03 渠道：职位发布与招聘营销** | LinkedIn、Indeed、智联、Boss 直聘 | 多渠道发布和雇主品牌建设 |
| **04 渠道：人才画像** | GitHub、Kaggle、Behance、技术社区 | 精准定位被动候选人 |
| **05 Sourcing：搜索模板** | Boolean 搜索、X-Ray、高级搜索技巧 | 提升人才搜索效率 |
| **06 ATS/CRM 招聘协作** | Greenhouse、Lever、OpenCATS、北森 | 招聘流程管理和协作 |
| **07 测评与面试** | HackerRank、Codility、HireVue | 技能验证和面试评估 |
| **08 Offer/背调/入职** | 背景调查、合规模板、入职系统 | 风险控制和合规落地 |
| **09 AI 招聘应用场景** | Textio、Eightfold、SeekOut、Paradox | 最新 AI 招聘工具汇总 |
| **10 AI 风险治理与合规** | NIST RMF、ISO 42001、NYC Law 144 | **项目核心价值** |
| **11 开源组件** | Fairlearn、AIF360、Aequitas | AI 公平性审计工具 |
| **12 全球招聘/EOR/远程团队** | Deel、Remote、Oyster、合规出海 | 跨境雇佣与全球化招聘 |
| **13 员工推荐/内部流动** | 推荐激励、内部竞聘、人才流动 | 激活内部人才网络 |
| **14 学习资源/研究社区** | SHRM、CIPD、ACM FAccT | 持续学习和行业连接 |
| **15 生成式 AI/LLM 招聘应用** | ChatGPT、Claude、JD 生成、AI 面试 | 生成式 AI 在招聘的应用 |
| **16 校园招聘/实习生** | Handshake、校园活动、实习项目 | 早期人才获取 |
| **17 高管招聘/Executive Search** | 猎头、高管评估、领导力测评 | C-level 与高端人才招聘 |
| **18 RPO/招聘外包** | RPO 供应商、招聘流程外包 | 规模化招聘能力输出 |
| **19 薪酬透明度法规** | 各州/国家薪酬披露要求 | 薪酬合规与透明度 |
| **20 招聘 API/开发者资源** | LinkedIn API、Indeed API、集成开发 | 技术集成与自动化 |
| **21 候选人体验/雇主品牌** | Glassdoor、雇主品牌建设、体验优化 | 提升候选人转化率 |
| **22 行业垂直招聘** | 医疗、金融、零售等行业特殊需求 | 垂直领域精准招聘 |
| **23 招聘数据隐私与合规** | GDPR、CCPA、数据保护 | 候选人数据合规 |
| **24 人才盘点与继任计划** | 九宫格、继任者识别、人才梯队 | 战略人才规划 |
| **25 招聘自动化与工作流** | Zapier、Make、自动化流程 | 效率提升与流程优化 |
| **26 面试官培训与招聘培训** | 面试技巧、招聘官认证、偏差培训 | 提升招聘团队能力 |
| **27 招聘行业活动与会议** | HR Tech、SHRM 年会、行业峰会 | 行业交流与趋势洞察 |
| **28 退伍军人招聘** | 军转民、技能转化、专项计划 | 支持退伍军人就业 |
| **29 残障人士/无障碍招聘** | 无障碍设计、包容性招聘、合规 | 促进残障人士就业 |
| **30 区域招聘资源** | 中国、美国、欧洲、东南亚等区域 | 区域化招聘支持 |
| **31 招聘播客与媒体** | Recruiting Future、HR 播客 | 行业知识获取 |
| **32 招聘模板与工具包** | JD 模板、面试评分表、入职清单 | 即用型招聘工具 |
| **33 招聘心理学与行为科学** | 决策偏差、候选人行为、动机理论 | 科学招聘决策 |
| **34 招聘法律与劳动法** | 劳动合同、竞业限制、用工风险 | 法律风险防控 |
| **35 招聘分析与 People Analytics** | 招聘漏斗、效能指标、数据分析 | 数据驱动招聘决策 |
| **36 远程面试与虚拟招聘** | Zoom、Teams、虚拟招聘会 | 远程招聘能力建设 |
| **37 招聘营销与内容创作** | 招聘文案、社交媒体、内容营销 | 吸引被动候选人 |
| **38 技术招聘专项** | 技术面试、代码评估、工程师招聘 | 技术人才精准招聘 |
| **39 人才市场情报与竞争分析** | 竞对分析、市场薪酬、人才流动 | 战略招聘规划 |
| **40 招聘反欺诈与验证** | 简历验证、学历核查、背景调查 | 招聘风险控制 |
| **41 灵活用工与零工经济** | 自由职业者、外包、灵活用工平台 | 多元用工模式 |
| **42 招聘游戏化与 VR/AR** | 游戏化测评、VR 面试、沉浸体验 | 创新招聘体验 |
| **43 招聘预算与 ROI** | 成本核算、ROI 分析、预算规划 | 招聘投资回报优化 |
| **44 知名公司招聘实践** | Google、Netflix、字节等案例 | 最佳实践借鉴 |
| **45 招聘文档与知识库** | 招聘 SOP、政策文档、知识管理 | 招聘知识沉淀 |
| **46 招聘职业发展** | 招聘官成长、职业路径、技能提升 | 招聘从业者发展 |
| **47 招聘伦理与公平招聘** | 反歧视、公平机会、伦理准则 | 负责任招聘 |
| **48 内部招聘与人才流动** | 内部竞聘、轮岗、人才市场 | 内部人才激活 |
| **49 招聘视觉与品牌设计** | 招聘海报、JD 设计、视觉呈现 | 招聘品牌视觉 |
| **50 候选人关系管理 (CRM)** | 人才库、候选人培育、长期关系 | 候选人资产管理 |
| **51 神经多样性招聘** | 自闭症、ADHD、神经多样性包容 | 神经多样性人才招聘 |
| **52 蓝领与一线员工招聘** | 制造业、物流、零售一线招聘 | 蓝领人才规模招聘 |
| **53 招聘效率与生产力工具** | Chrome 插件、效率工具、自动化 | 招聘官效率提升 |
| **54 AI 面试与评估技术** | 视频面试 AI、语音分析、表情识别 | AI 面试技术应用 |
| **55 招聘行业研究与报告** | 行业白皮书、趋势报告、市场研究 | 行业洞察与趋势 |
| **56 人才社区与人才库建设** | 社区运营、人才池、长期培育 | 人才资产建设 |
| **57 招聘视频与多媒体** | 视频 JD、雇主品牌视频、直播招聘 | 多媒体招聘内容 |
| **58 招聘协作与团队管理** | 招聘团队协作、目标管理、绩效 | 招聘团队效能 |

</details>

---

## AI 招聘风险治理

本项目特别强调 AI 招聘中的**公平性、透明度和法律合规**，这是区别于普通工具导航的核心价值。

### 国际标准框架

| 标准 | 发布机构 | 核心内容 |
|------|---------|---------|
| **NIST AI RMF** | 美国国家标准与技术研究院 | AI 风险管理框架，涵盖治理、映射、度量、管理 |
| **ISO/IEC 42001** | 国际标准化组织 | AI 管理体系标准，提供认证基础 |
| **ISO/IEC 23894** | 国际标准化组织 | AI 系统风险管理指南 |

### 地区法规监管

| 法规 | 地区 | 影响 |
|------|------|------|
| **NYC Local Law 144** | 美国纽约市 | 自动化招聘决策工具须进行年度偏差审计 |
| **EEOC AI & ADA 指南** | 美国联邦 | AI 招聘与残障人士权益保护 |
| **EU AI Act** | 欧盟 | 招聘 AI 被列为高风险类别，需强制合规 |
| **DOJ 无障碍招聘指导** | 美国联邦 | AI 招聘中的残障歧视风险 |

### 开源公平性工具

| 工具 | 维护者 | 功能 |
|------|--------|------|
| **Fairlearn** | Microsoft | 模型公平性诊断和缓解算法 |
| **AIF360** | IBM Trusted-AI | AI 公平性算法工具箱（Python/R） |
| **Aequitas** | DSSG | 机器学习偏差审计框架 |

---

## 数据结构规范

所有资源存储在 `docs/tarf.json` 中，采用树形 JSON 结构。

### 节点类型

所有节点都支持 `name_en` 字段用于英文显示（可选，缺省时使用 `name`）。

#### Folder（文件夹/分类）

```json
{
  "name": "01 招聘流程与方法论",
  "name_en": "01 Recruitment Process & Methodology",
  "type": "folder",
  "children": [...]
}
```

#### URL（普通链接）

```json
{
  "name": "CIPD｜Selection methods（结构化面试等）",
  "name_en": "CIPD | Selection methods (Structured Interviews)",
  "type": "url",
  "url": "https://www.cipd.org/en/knowledge/factsheets/selection-factsheet/",
  "tags": ["Guide"]
}
```

#### Template（模板链接）

```json
{
  "name": "LinkedIn 个人页 X-Ray",
  "name_en": "LinkedIn Profile X-Ray",
  "type": "template",
  "url": "https://www.google.com/search?q=site%3Alinkedin.com%2Fin+{query}",
  "tags": ["M"]
}
```

用户点击时会弹窗输入关键词，`{query}` 将被替换后打开。

### 标签系统

| 标签 | 含义 | 使用场景 |
|------|------|---------|
| `R` | 需要注册/登录 | LinkedIn、Glassdoor 等 |
| `P` | 付费/商用 | Greenhouse、HackerRank Pro 等 |
| `O` | 开源 | OpenCATS、Fairlearn 等 |
| `M` | 模板链接 | 含 `{query}` 占位符的动态 URL |
| `PDF` | PDF 资源 | 白皮书、指南文档 |
| `Law` | 法律/监管 | EEOC、NYC Local Law 144 |
| `Framework` | 框架/标准 | NIST AI RMF、ISO 42001 |
| `Guide` | 指南/教程 | SHRM、CIPD 发布的指南 |
| `CN` | 中国区域 | 拉勾、Boss 直聘、北森 |

标签可自由扩展，建议保持简短一致。

---

## 技术栈

| 技术 | 用途 | 版本 |
|------|------|------|
| HTML5 | 页面结构 | - |
| CSS3 | 样式（CSS 变量、Grid、Flexbox） | - |
| JavaScript | 核心逻辑（ES6+） | - |
| D3.js | 树形图可视化 | v7 (CDN) |
| JSON | 数据存储格式 | - |

**零构建依赖**：无 webpack、Vite、npm、TypeScript，纯原生开发。

---

## 项目结构

```
recruit-ai-framework/
├── docs/                        # 前端静态资源（GitHub Pages 部署目录）
│   ├── index.html               # 主应用页面（SEO + 无障碍 + i18n）
│   ├── app.js                   # D3 树形图 + 搜索 + 国际化逻辑
│   ├── style.css                # 暗色主题 + 响应式 + 打印样式
│   ├── tarf.json                # 数据文件（1288 条资源，58 大分类，双语）
│   ├── robots.txt               # SEO 爬虫规则
│   ├── sitemap.xml              # 站点地图
│   └── 404.html                 # 404 错误页面（双语）
├── scripts/                     # 工具脚本
│   └── add_translations.py      # 添加英文翻译到 tarf.json
├── .gitignore                   # Git 忽略文件配置
├── LICENSE                      # MIT 许可证
└── README.md                    # 项目文档
```

---

## 贡献指南

欢迎通过 Pull Request 扩展本项目！

### 贡献流程

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/add-xxx-resources`
3. 编辑 `docs/tarf.json` 添加资源
4. 本地测试搜索和导航功能
5. 提交 PR，描述添加的分类和资源

### 贡献建议

**优先补齐的方向**：

- **区域化**：东南亚、中东、拉美等地区的招聘渠道与合规
- **行业垂直**：制造、零售、医疗、金融等行业特殊需求
- **AI 工具评测**：收录社区评论和对比数据
- **最新法规**：跟踪各国 AI 招聘监管动态

**贡献规范**：

- 每次 PR 只做一类变更（方便 Review）
- 优先使用官网/一手资料链接
- 避免博客/转载等二手资源
- 确保链接可访问且内容相关

---

## 合规与伦理提示

> **非常重要**

- 仅收录**公开可访问**或**有明确授权**的资源/工具入口
- 使用 AI/自动化做招聘决策时，建议遵循：

| 原则 | 说明 |
|------|------|
| **人类在环** | Human-in-the-loop，AI 辅助而非替代人类决策 |
| **透明告知** | 向候选人披露 AI 使用情况，必要时获得同意 |
| **偏差评估** | 进行公平性审计，记录风险评估过程 |
| **法律合规** | 遵守隐私保护、反歧视、背调合规等法规 |
| **持续监控** | 定期评估 AI 系统表现，及时发现和纠正问题 |

---

## 常见问题

### Q: 为什么不能直接打开 index.html？

浏览器 CORS 安全策略限制。本地文件协议 (`file://`) 不允许 JavaScript 读取 JSON 文件。必须通过 HTTP(S) 协议访问。

### Q: 如何添加新的资源分类？

编辑 `docs/tarf.json`，在对应位置添加 folder 节点：

```json
{
  "name": "新分类名称",
  "type": "folder",
  "children": [
    { "name": "资源1", "type": "url", "url": "https://...", "tags": ["标签"] }
  ]
}
```

### Q: 搜索支持哪些内容？

搜索会匹配：资源名称、分类路径、标签。支持中英文，不区分大小写。

### Q: 项目更新频率？

根据社区贡献。AI 招聘工具生态发展迅速，欢迎提交最新工具和法规。

### Q: 可以用于商业项目吗？

可以。项目采用 MIT 许可证，允许商业使用、修改和分发。

---

## 浏览器兼容性

| 浏览器 | 最低版本 |
|--------|---------|
| Chrome | 60+ |
| Firefox | 55+ |
| Safari | 12+ |
| Edge | 79+ |
| IE | 不支持 |

需要支持：ES6+、Fetch API、SVG、D3.js v7

---

## 许可证

[MIT License](LICENSE) © 2025

自由使用、修改和分发。

---

## 致谢

- [OSINT Framework](https://osintframework.com/) - 项目灵感来源
- [D3.js](https://d3js.org/) - 数据可视化库
- 所有资源的原始作者和维护者

---

## 联系与反馈

- **GitHub Issues**：报告问题或功能建议
- **Pull Requests**：贡献资源或修复
- **Discussions**：讨论招聘 AI 的最佳实践

---

<p align="center">
  <strong>构建负责任的 AI 招聘生态</strong><br>
  <em>Build Responsible AI Hiring Ecosystem</em>
</p>
