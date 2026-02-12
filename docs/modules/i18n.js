// ========== i18n ==========
export const i18n = {
  zh: {
    pageTitle: "Recruitment & AI Hiring Framework - 招聘与AI招聘工具导航",
    metaDescription: "一个数据驱动的招聘工具导航地图，覆盖300+分类、1900+条资源，包含AI招聘风险治理、DEI、神经多样性等专项。灵感来自 OSINT Framework。",
    metaKeywords: "招聘,AI招聘,人才招聘,ATS,招聘工具,HR科技,招聘合规,AI风险治理,Recruitment,Hiring,HR Tech",
    subtitle: "一个可维护的「招聘 × AI 招聘」工具地图（数据驱动），灵感来自 OSINT Framework。",
    searchPlaceholder: "搜索：工具 / 指南 / 标准 / 会议 …（支持中英文关键词）",
    clearBtn: "清空",
    downloadJson: "下载 tarf.json",
    langLabel: "EN",
    legendR: "需要注册/登录",
    legendP: "付费/商用",
    legendO: "开源",
    legendM: "模板链接（会提示输入 query）",
    legendPDF: "PDF 资源",
    legendLaw: "法规/监管页面",
    legendFramework: "框架/标准",
    treeTitle: "工具树",
    accordionTitle: "目录视图",
    tableTitle: "表格视图",
    explorerTitle: "文件浏览器",
    cardsTitle: "卡片视图",
    resetBtn: "重置",
    expandBtn: "展开",
    collapseBtn: "收起",
    hint1: "点击「文件夹」节点展开/收起。",
    hint2: "点击「链接」节点会在新标签页打开。",
    hint3: '点击带 <span class="tag">M</span> 的节点会弹窗让你输入关键词，并把关键词替换进 URL 里的 <code>{query}</code>。',
    hint4: "<kbd>/</kbd> 聚焦搜索框，<kbd>Esc</kbd> 清空搜索。",
    searchResults: "搜索结果",
    searchHint: "输入关键词开始搜索。",
    statsTitle: "数据统计",
    loading: "加载中...",
    howToExtend: "如何扩展",
    extend1: "编辑 <code>docs/tarf.json</code>（添加/修改节点）。",
    extend2: '本地预览：在项目根目录运行 <code>python -m http.server 8000</code>，然后打开 <code>http://localhost:8000/docs/</code>。',
    extend3: "发布：把 <code>docs/</code> 作为静态站点部署（GitHub Pages / Cloudflare Pages / Vercel 等）。",
    footerWarning: "⚠️ 仅用于招聘工具导航与学习研究；使用任何自动化/AI 招聘能力时请遵守适用法律法规与隐私要求，并进行必要的偏差评估与人类复核。",
    reportIssue: "反馈问题",
    totalResources: (count) => `共 ${count} 条资源。输入关键词开始搜索。`,
    matchResults: (match, show) => `匹配 ${match} 条（展示前 ${show} 条）`,
    statsContent: (cats, res, tpl) => `<p><strong>${cats}</strong> 大分类 · <strong>${res}</strong> 条资源 · <strong>${tpl}</strong> 个模板</p>`,
    hotTags: "热门标签：",
    loadError: (msg) => `加载失败：${msg}。`,
    loadErrorTree: "数据加载失败",
    loadFailed: "加载失败",
    retryBtn: "重试",
    promptQuery: "输入关键词（会替换到 URL 里的 {query}）：",
    allTags: "全部",
    noResults: "没有找到匹配的结果",
    showInTree: "定位",
    addFavorite: "收藏",
    removeFavorite: "取消收藏",
    favorites: "收藏夹",
    noFavorites: "暂无收藏",
    clearFavorites: "清空",
    filterByTag: "按标签筛选",
    exportResults: "导出",
    exportCSV: "导出 CSV",
    exportJSON: "导出 JSON",
    sortByName: "按名称",
    sortByCategory: "按分类",
    sortByTags: "按标签",
    itemsCount: (n) => `${n} 项`,
    viewTree: "树",
    viewAccordion: "列表",
    viewTable: "表格",
    viewExplorer: "浏览",
    viewCards: "卡片",
    viewTreeTitle: "D3 树形图",
    viewAccordionTitle: "折叠列表",
    viewTableTitle: "数据表格",
    viewExplorerTitle: "文件浏览器",
    viewCardsTitle: "卡片网格",
  },
  en: {
    pageTitle: "Recruitment & AI Hiring Framework - Navigation Map",
    metaDescription: "A data-driven recruitment tool navigation map covering 300+ categories and 1900+ resources, including AI hiring governance, DEI, neurodiversity, etc. Inspired by OSINT Framework.",
    metaKeywords: "Recruitment, AI Hiring, Talent Acquisition, ATS, Recruiting Tools, HR Tech, Hiring Compliance, AI Risk Governance",
    subtitle: "A maintainable data-driven Recruitment & AI Hiring tool map, inspired by OSINT Framework.",
    searchPlaceholder: "Search: Tools / Guides / Standards / Events... (supports keywords)",
    clearBtn: "Clear",
    downloadJson: "Download tarf.json",
    langLabel: "中文",
    legendR: "Registration required",
    legendP: "Paid/Commercial",
    legendO: "Open Source",
    legendM: "Template link (prompts for query)",
    legendPDF: "PDF Resource",
    legendLaw: "Law/Regulation",
    legendFramework: "Framework/Standard",
    treeTitle: "Tool Tree",
    accordionTitle: "Accordion View",
    tableTitle: "Table View",
    explorerTitle: "File Explorer",
    cardsTitle: "Cards View",
    resetBtn: "Reset",
    expandBtn: "Expand",
    collapseBtn: "Collapse",
    hint1: "Click folder nodes to expand/collapse.",
    hint2: "Click link nodes to open in new tab.",
    hint3: 'Click nodes with <span class="tag">M</span> tag to enter keywords, which replace <code>{query}</code> in the URL.',
    hint4: "<kbd>/</kbd> to focus search, <kbd>Esc</kbd> to clear.",
    searchResults: "Search Results",
    searchHint: "Enter keywords to search.",
    statsTitle: "Statistics",
    loading: "Loading...",
    howToExtend: "How to Extend",
    extend1: "Edit <code>docs/tarf.json</code> (add/modify nodes).",
    extend2: 'Local preview: Run <code>python -m http.server 8000</code> in project root, then open <code>http://localhost:8000/docs/</code>.',
    extend3: "Deploy: Use <code>docs/</code> as static site (GitHub Pages / Cloudflare Pages / Vercel etc.).",
    footerWarning: "⚠️ For recruitment tool navigation and research only. When using AI/automation in hiring, comply with applicable laws, privacy requirements, and conduct bias assessments with human review.",
    reportIssue: "Report Issue",
    totalResources: (count) => `${count} resources total. Enter keywords to search.`,
    matchResults: (match, show) => `${match} matches (showing first ${show})`,
    statsContent: (cats, res, tpl) => `<p><strong>${cats}</strong> Categories · <strong>${res}</strong> Resources · <strong>${tpl}</strong> Templates</p>`,
    hotTags: "Popular tags: ",
    loadError: (msg) => `Load failed: ${msg}.`,
    loadErrorTree: "Data load failed",
    loadFailed: "Load failed",
    retryBtn: "Retry",
    promptQuery: "Enter keywords (will replace {query} in URL):",
    allTags: "All",
    noResults: "No matching results found",
    showInTree: "Locate",
    addFavorite: "Add to favorites",
    removeFavorite: "Remove from favorites",
    favorites: "Favorites",
    noFavorites: "No favorites yet",
    clearFavorites: "Clear",
    filterByTag: "Filter by tag",
    exportResults: "Export",
    exportCSV: "Export CSV",
    exportJSON: "Export JSON",
    sortByName: "By Name",
    sortByCategory: "By Category",
    sortByTags: "By Tags",
    itemsCount: (n) => `${n} items`,
    viewTree: "Tree",
    viewAccordion: "List",
    viewTable: "Table",
    viewExplorer: "Explorer",
    viewCards: "Cards",
    viewTreeTitle: "D3 Tree View",
    viewAccordionTitle: "Accordion List",
    viewTableTitle: "Data Table",
    viewExplorerTitle: "File Explorer",
    viewCardsTitle: "Card Grid",
  }
};

export const SUPPORTED_LANGS = ["zh", "en"];
export const DEFAULT_LANG = "zh";

export function normalizeLang(lang) {
  return SUPPORTED_LANGS.includes(lang) ? lang : DEFAULT_LANG;
}

export let currentLang = normalizeLang(localStorage.getItem("lang"));

export function setCurrentLang(lang) {
  currentLang = lang;
}

export function t(key, ...args) {
  const lang = normalizeLang(currentLang);
  if (lang !== currentLang) currentLang = lang;
  const val = i18n[lang]?.[key];
  if (typeof val === "function") return val(...args);
  return val || key;
}

export function applyLanguage(lang) {
  const safeLang = normalizeLang(lang);
  currentLang = safeLang;
  localStorage.setItem("lang", safeLang);
  document.getElementById("htmlRoot").lang = safeLang === "zh" ? "zh-CN" : "en";
  const langLabel = document.getElementById("langLabel");
  if (langLabel) langLabel.textContent = t("langLabel");
  const dict = i18n[safeLang];
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    if (dict?.[key]) el.textContent = dict[key];
  });
  document.querySelectorAll("[data-i18n-html]").forEach(el => {
    const key = el.getAttribute("data-i18n-html");
    if (dict?.[key]) el.innerHTML = dict[key];
  });
  document.querySelectorAll("[data-i18n-placeholder]").forEach(el => {
    const key = el.getAttribute("data-i18n-placeholder");
    if (dict?.[key]) el.placeholder = dict[key];
  });
  document.querySelectorAll("[data-i18n-title]").forEach(el => {
    const key = el.getAttribute("data-i18n-title");
    if (dict?.[key]) el.title = dict[key];
  });

  // SEO: Update title and meta tags
  if (dict?.pageTitle) document.title = dict.pageTitle;

  document.querySelectorAll("[data-i18n-content]").forEach(el => {
    const key = el.getAttribute("data-i18n-content");
    if (dict?.[key]) el.setAttribute("content", dict[key]);
  });
}
