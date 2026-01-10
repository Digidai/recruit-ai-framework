/* Recruitment & AI Hiring Framework - Multi-View Version
 * Supports 5 visualization modes: Tree, Accordion, Table, Explorer, Cards
 */

const DATA_URL = "tarf.json";
const MAX_RESULTS = 80;
const DEBOUNCE_MS = 150;

// ========== i18n ==========
const i18n = {
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

let currentLang = localStorage.getItem("lang") || "zh";
let currentView = localStorage.getItem("view") || "tree";

function t(key, ...args) {
  const val = i18n[currentLang][key];
  if (typeof val === "function") return val(...args);
  return val || key;
}

function applyLanguage(lang) {
  currentLang = lang;
  localStorage.setItem("lang", lang);
  document.getElementById("htmlRoot").lang = lang === "zh" ? "zh-CN" : "en";
  const langLabel = document.getElementById("langLabel");
  if (langLabel) langLabel.textContent = t("langLabel");
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    if (i18n[currentLang][key]) el.textContent = i18n[currentLang][key];
  });
  document.querySelectorAll("[data-i18n-html]").forEach(el => {
    const key = el.getAttribute("data-i18n-html");
    if (i18n[currentLang][key]) el.innerHTML = i18n[currentLang][key];
  });
  document.querySelectorAll("[data-i18n-placeholder]").forEach(el => {
    const key = el.getAttribute("data-i18n-placeholder");
    if (i18n[currentLang][key]) el.placeholder = i18n[currentLang][key];
  });
  document.querySelectorAll("[data-i18n-title]").forEach(el => {
    const key = el.getAttribute("data-i18n-title");
    if (i18n[currentLang][key]) el.title = i18n[currentLang][key];
  });

  // SEO: Update title and meta tags
  if (i18n[currentLang]["pageTitle"]) document.title = i18n[currentLang]["pageTitle"];
  
  document.querySelectorAll("[data-i18n-content]").forEach(el => {
    const key = el.getAttribute("data-i18n-content");
    if (i18n[currentLang][key]) el.setAttribute("content", i18n[currentLang][key]);
  });
}

function toggleLanguage() {
  const newLang = currentLang === "zh" ? "en" : "zh";
  applyLanguage(newLang);
  if (window._appItems) renderResults(window._appItems, searchInput.value || "");
  if (window._appStats) renderStats(window._appStats);
  // Rebuild all views to update language (not just current view)
  rebuildAllViews();
}

function rebuildAllViews() {
  if (!window._appData) return;
  buildTree(window._appData);
  buildAccordion(window._appData);
  buildTable(window._appItems);
  buildExplorer(window._appData);
  buildCards(window._appItems, window._appStats);
}

// ========== DOM Elements ==========
const searchInput = document.getElementById("searchInput");
const btnClear = document.getElementById("btnClear");
const resultMeta = document.getElementById("resultMeta");
const resultList = document.getElementById("resultList");
const treeSvg = document.getElementById("treeSvg");
const statsContent = document.getElementById("statsContent");
const viewTitle = document.getElementById("viewTitle");
const tagFilterSelect = document.getElementById("tagFilterSelect");
const btnExportCSV = document.getElementById("btnExportCSV");
const btnExportJSON = document.getElementById("btnExportJSON");
const ariaLive = document.getElementById("ariaLive");

// Track current search results for export
let currentSearchResults = [];

// ========== Accessibility ==========
function announce(message) {
  if (!ariaLive) return;
  // Clear first to ensure re-announcement
  ariaLive.textContent = "";
  setTimeout(() => { ariaLive.textContent = message; }, 100);
}

// ========== Utilities ==========
function debounce(fn, delay) {
  let timer = null;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

function escapeHtml(str) {
  return String(str).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;");
}

function tagHtml(tag) {
  return `<span class="tag">${escapeHtml(tag)}</span>`;
}

// ========== Favorites ==========
function getFavorites() {
  try {
    return JSON.parse(localStorage.getItem("favorites") || "[]");
  } catch { return []; }
}

function saveFavorites(favs) {
  try {
    localStorage.setItem("favorites", JSON.stringify(favs));
  } catch (e) { console.warn("Failed to save favorites", e); }
}

function isFavorite(url) {
  return getFavorites().some(f => f.url === url);
}

function toggleFavorite(item) {
  const favs = getFavorites();
  const idx = favs.findIndex(f => f.url === item.url);
  if (idx >= 0) {
    favs.splice(idx, 1);
  } else {
    favs.push({ url: item.url, name: item.name, name_en: item.name_en, tags: item.tags, addedAt: new Date().toISOString() });
  }
  saveFavorites(favs);
  renderFavorites();
  return idx < 0; // returns true if added
}

function renderFavorites() {
  const container = document.getElementById("favoritesContent");
  if (!container) return;
  const favs = getFavorites();
  if (favs.length === 0) {
    container.innerHTML = `<p class="no-favorites">${t("noFavorites")}</p>`;
    return;
  }
  container.innerHTML = `<div class="favorites-header"><span>${favs.length} ${t("favorites").toLowerCase()}</span><button class="btnLink" id="clearFavs">${t("clearFavorites")}</button></div><ul class="favorites-list"></ul>`;
  const list = container.querySelector(".favorites-list");
  for (const fav of favs) {
    const li = document.createElement("li");
    li.innerHTML = `<span class="fav-name">${escapeHtml(currentLang === "en" && fav.name_en ? fav.name_en : fav.name)}</span><button class="fav-remove" data-url="${escapeHtml(fav.url)}">×</button>`;
    li.querySelector(".fav-name").addEventListener("click", () => window.open(fav.url, "_blank", "noopener"));
    li.querySelector(".fav-remove").addEventListener("click", (e) => {
      e.stopPropagation();
      const url = e.target.dataset.url;
      const favs = getFavorites().filter(f => f.url !== url);
      saveFavorites(favs);
      renderFavorites();
      // Update any visible favorite buttons
      document.querySelectorAll(".favBtn").forEach(btn => {
        if (btn.dataset.url === url) {
          btn.textContent = "♡";
          btn.title = t("addFavorite");
        }
      });
    });
    list.appendChild(li);
  }
  document.getElementById("clearFavs")?.addEventListener("click", () => {
    saveFavorites([]);
    renderFavorites();
    document.querySelectorAll(".favBtn").forEach(btn => {
      btn.textContent = "♡";
      btn.title = t("addFavorite");
    });
  });
}

function tagsHtml(tags) {
  if (!tags || !tags.length) return "";
  return tags.map(tagHtml).join("");
}

function openNode(node) {
  const nodeType = node.type || node.data?.type;
  const url = node.url || node.data?.url;
  if (!url) return;
  if (nodeType === "template") {
    const q = prompt(t("promptQuery"));
    if (!q) return;
    const finalUrl = url.replaceAll("{query}", encodeURIComponent(q.trim()));
    window.open(finalUrl, "_blank", "noopener");
  } else {
    window.open(url, "_blank", "noopener");
  }
}

function getLocalizedName(node) {
  return (currentLang === "en" && node.name_en) ? node.name_en : node.name;
}

function flatten(node, path = [], pathEn = []) {
  const here = [...path, node.name];
  const hereEn = [...pathEn, node.name_en || node.name];
  const out = [];
  if (node.type === "folder" && Array.isArray(node.children)) {
    for (const ch of node.children) out.push(...flatten(ch, here, hereEn));
  } else if (node.url) {
    out.push({
      name: node.name,
      name_en: node.name_en || node.name,
      type: node.type || "url",
      url: node.url,
      tags: node.tags || [],
      path: here.slice(0, -1),
      path_en: hereEn.slice(0, -1),
    });
  }
  return out;
}

function getDisplayName(item) {
  return currentLang === "en" ? (item.name_en || item.name) : item.name;
}

function getDisplayPath(item) {
  return currentLang === "en" ? (item.path_en || item.path) : item.path;
}

function countStats(data) {
  let categories = 0, resources = 0, templates = 0;
  const tagCounts = {};
  function traverse(node) {
    if (node.type === "folder") {
      if (node.name.match(/^[A-Z]\s/)) categories++;
      if (Array.isArray(node.children)) node.children.forEach(traverse);
    } else if (node.url) {
      resources++;
      if (node.type === "template") templates++;
      if (node.tags) node.tags.forEach(tag => { tagCounts[tag] = (tagCounts[tag] || 0) + 1; });
    }
  }
  traverse(data);
  return { categories, resources, templates, tagCounts };
}

function countChildren(node) {
  let count = 0;
  if (node.url) return 1;
  if (node.children) {
    for (const child of node.children) count += countChildren(child);
  }
  return count;
}

function renderStats(stats) {
  const separator = currentLang === "zh" ? "、" : ", ";
  const topTags = Object.entries(stats.tagCounts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 8)
    .map(([tag, count]) => `<span class="tag">${escapeHtml(tag)}</span> ${count}`)
    .join(separator);
  statsContent.innerHTML = `${t("statsContent", stats.categories, stats.resources, stats.templates)}<p>${t("hotTags")}${topTags}</p>`;
}

function renderResults(items, query) {
  resultList.innerHTML = "";
  const tagFilter = tagFilterSelect?.value || "";

  if (!query && !tagFilter) {
    resultMeta.textContent = t("totalResources", items.length);
    currentSearchResults = [];
    return;
  }

  const q = query.trim().toLowerCase();
  let hit = items;

  // Apply text search
  if (q) {
    hit = hit.filter(it => {
      const searchText = [it.name, it.name_en || "", it.path.join(" / "), (it.path_en || it.path).join(" / "), it.tags.join(" ")].join(" ").toLowerCase();
      return searchText.includes(q);
    });
  }

  // Apply tag filter
  if (tagFilter) {
    hit = hit.filter(it => it.tags.includes(tagFilter));
  }

  currentSearchResults = hit;
  const resultText = t("matchResults", hit.length, Math.min(MAX_RESULTS, hit.length));
  resultMeta.textContent = resultText;
  announce(resultText);

  for (const it of hit.slice(0, MAX_RESULTS)) {
    const li = document.createElement("li");
    li.tabIndex = 0;
    const isFav = isFavorite(it.url);
    li.innerHTML = `
      <div class="resultTitle"><strong>${escapeHtml(getDisplayName(it))}</strong>${tagsHtml(it.tags)}</div>
      <div class="resultPath">${escapeHtml(getDisplayPath(it).join(" / "))}</div>
      <div class="resultActions">
        <span class="resultUrl">${escapeHtml(it.url)}</span>
        <button class="favBtn" data-url="${escapeHtml(it.url)}" title="${isFav ? t("removeFavorite") : t("addFavorite")}">${isFav ? "♥" : "♡"}</button>
        <button class="locateBtn" title="${t("showInTree")}">📍</button>
      </div>`;
    li.querySelector(".resultUrl").addEventListener("click", (e) => { e.stopPropagation(); openNode(it); });
    li.querySelector(".favBtn").addEventListener("click", (e) => {
      e.stopPropagation();
      const btn = e.target;
      const added = toggleFavorite(it);
      btn.textContent = added ? "♥" : "♡";
      btn.title = added ? t("removeFavorite") : t("addFavorite");
    });
    li.querySelector(".locateBtn").addEventListener("click", (e) => {
      e.stopPropagation();
      highlightInTree(it.url);
    });
    li.addEventListener("click", () => openNode(it));
    li.addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); openNode(it); } });
    resultList.appendChild(li);
  }
}

// ========== Export Functions ==========
function escapeCSV(str) {
  // Escape quotes and handle newlines for CSV
  return (str || "").replace(/"/g, '""').replace(/[\r\n]+/g, ' ');
}

function exportToCSV(results) {
  if (!results.length) return;
  const headers = ["Name", "Name (EN)", "URL", "Tags", "Category"];
  const rows = results.map(it => [
    `"${escapeCSV(it.name)}"`,
    `"${escapeCSV(it.name_en)}"`,
    `"${escapeCSV(it.url)}"`,
    `"${escapeCSV((it.tags || []).join(", "))}"`,
    `"${escapeCSV((it.path || []).join(" / "))}"`
  ].join(","));
  const csv = [headers.join(","), ...rows].join("\n");
  downloadFile(csv, "search-results.csv", "text/csv;charset=utf-8;");
}

function exportToJSON(results) {
  if (!results.length) return;
  const data = results.map(it => ({
    name: it.name,
    name_en: it.name_en,
    url: it.url,
    tags: it.tags,
    category: it.path.join(" / ")
  }));
  const json = JSON.stringify(data, null, 2);
  downloadFile(json, "search-results.json", "application/json");
}

function downloadFile(content, filename, type) {
  const blob = new Blob([content], { type });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function populateTagFilter(stats) {
  if (!tagFilterSelect) return;
  // Keep the first "All" option and clear the rest
  while (tagFilterSelect.options.length > 1) {
    tagFilterSelect.remove(1);
  }
  // Add top tags
  const topTags = Object.entries(stats.tagCounts).sort((a, b) => b[1] - a[1]).slice(0, 30);
  for (const [tag, count] of topTags) {
    const opt = document.createElement("option");
    opt.value = tag;
    opt.textContent = `${tag} (${count})`;
    tagFilterSelect.appendChild(opt);
  }
}

function highlightInTree(url) {
  // Switch to tree view if not already
  if (currentView !== "tree") {
    switchView("tree");
  }
  // Wait for tree to render then highlight
  setTimeout(() => {
    if (treeController && treeController.highlightNode) {
      treeController.highlightNode(url);
    }
  }, 100);
}

// ========== View Switching ==========
function switchView(view) {
  currentView = view;
  localStorage.setItem("view", view);

  // Update buttons
  document.querySelectorAll(".view-btn").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.view === view);
    btn.setAttribute("aria-selected", btn.dataset.view === view);
  });

  // Update view containers
  document.querySelectorAll(".view-content").forEach(el => {
    el.classList.toggle("active", el.id === view + "View");
  });

  // Update title
  const titles = { tree: "treeTitle", accordion: "accordionTitle", table: "tableTitle", explorer: "explorerTitle", cards: "cardsTitle" };
  const viewTitleText = t(titles[view] || "treeTitle");
  viewTitle.textContent = viewTitleText;
  announce(viewTitleText);

  // Update controls visibility
  document.getElementById("treeControls").style.display = view === "tree" ? "flex" : "none";
  document.getElementById("accordionControls").style.display = view === "accordion" ? "flex" : "none";
  document.getElementById("tableControls").style.display = view === "table" ? "flex" : "none";

  // Update URL
  updateUrlFromState();

  renderCurrentView();
}

function renderCurrentView() {
  if (!window._appData) return;
  switch (currentView) {
    case "tree": buildTree(window._appData); break;
    case "accordion": buildAccordion(window._appData); break;
    case "table": buildTable(window._appItems); break;
    case "explorer": buildExplorer(window._appData); break;
    case "cards": buildCards(window._appItems, window._appStats); break;
  }
}

// ========== 1. D3 Tree View (Fixed overlap) ==========
let treeController = null;

function buildTree(data) {
  const root = d3.hierarchy(data);
  root.x0 = 0;
  root.y0 = 0;

  root.descendants().forEach((d, i) => {
    d.id = i;
    d._children = d.children;
    if (d.depth >= 2) d.children = null;
  });

  const svg = d3.select(treeSvg);
  svg.selectAll("*").remove();

  const wrap = document.getElementById("treeWrap");
  const width = wrap.clientWidth || 800;
  const height = wrap.clientHeight || 600;

  const g = svg.attr("viewBox", [-40, -height/2, width + 80, height]).append("g");

  const zoom = d3.zoom().scaleExtent([0.1, 10]).on("zoom", (event) => g.attr("transform", event.transform));
  svg.call(zoom);

  const initialTransform = d3.zoomIdentity.translate(40, height / 2).scale(1);

  // Spacing configuration
  const dx = 22;  // Base vertical spacing between nodes
  const dy = 320; // Horizontal spacing between levels (needs to fit text width)

  // Count visible descendants of a node
  const countVisible = (node) => {
    if (!node.children) return 1;
    return node.children.reduce((sum, child) => sum + countVisible(child), 0);
  };

  // Dynamic separation based on subtree sizes to prevent overlap
  const tree = d3.tree().nodeSize([dx, dy]).separation((a, b) => {
    // For siblings, allocate space based on their subtree sizes
    if (a.parent === b.parent) {
      const aSize = countVisible(a);
      const bSize = countVisible(b);
      // Minimum 1, scale up based on larger subtree
      return Math.max(1, Math.sqrt(Math.max(aSize, bSize)) * 0.8);
    }
    // Non-siblings need more separation
    return 2.5;
  });
  const diagonal = d3.linkHorizontal().x(d => d.y).y(d => d.x);

  function update(source) {
    const duration = 250;
    tree(root);

    const nodes = root.descendants();
    const links = root.links();

    // Calculate bounds
    let x0 = Infinity, x1 = -Infinity;
    nodes.forEach(d => {
      if (d.x < x0) x0 = d.x;
      if (d.x > x1) x1 = d.x;
    });

    const viewHeight = Math.max(height, x1 - x0 + 100);
    svg.transition().duration(duration).attr("viewBox", [-40, x0 - 50, width + 80, viewHeight]);

    // Links
    g.selectAll("path.link").data(links, d => d.target.id).join(
      enter => enter.append("path").attr("class", "link")
        .attr("d", () => { const o = {x: source.x0, y: source.y0}; return diagonal({source: o, target: o}); })
        .call(enter => enter.transition().duration(duration).attr("d", diagonal)),
      update => update.call(update => update.transition().duration(duration).attr("d", diagonal)),
      exit => exit.call(exit => exit.transition().duration(duration)
        .attr("d", () => { const o = {x: source.x, y: source.y}; return diagonal({source: o, target: o}); }).remove())
    );

    // Nodes
    const node = g.selectAll("g.node").data(nodes, d => d.id);

    const nodeEnter = node.enter().append("g")
      .attr("class", d => `node ${d._children || d.children ? "is-folder" : "is-leaf"}`)
      .attr("transform", `translate(${source.y0},${source.x0})`)
      .attr("cursor", "pointer")
      .attr("tabindex", 0)
      .attr("role", d => (d._children || d.children) ? "treeitem" : "link")
      .attr("aria-expanded", d => d.children ? "true" : d._children ? "false" : null)
      .on("click", (event, d) => {
        if (d.children) { d._children = d.children; d.children = null; }
        else if (d._children) { d.children = d._children; d._children = null; }
        else { openNode(d.data); return; }
        update(d);
      })
      .on("keydown", (event, d) => {
        const key = event.key;
        if (key === "Enter" || key === " ") {
          event.preventDefault();
          if (d.children) { d._children = d.children; d.children = null; update(d); }
          else if (d._children) { d.children = d._children; d._children = null; update(d); }
          else { openNode(d.data); }
        } else if (key === "ArrowRight") {
          event.preventDefault();
          if (d._children) { d.children = d._children; d._children = null; update(d); }
          else if (d.children && d.children.length > 0) {
            // Focus first child
            setTimeout(() => {
              const firstChild = g.selectAll(".node").filter(n => n.parent === d).node();
              if (firstChild) firstChild.focus();
            }, 300);
          }
        } else if (key === "ArrowLeft") {
          event.preventDefault();
          if (d.children) { d._children = d.children; d.children = null; update(d); }
          else if (d.parent) {
            // Focus parent
            const parentNode = g.selectAll(".node").filter(n => n === d.parent).node();
            if (parentNode) parentNode.focus();
          }
        } else if (key === "ArrowDown") {
          event.preventDefault();
          // Focus next visible sibling or node
          const visibleNodes = root.descendants().filter(n => n.x !== undefined);
          const idx = visibleNodes.indexOf(d);
          if (idx >= 0 && idx < visibleNodes.length - 1) {
            const nextNode = g.selectAll(".node").filter(n => n === visibleNodes[idx + 1]).node();
            if (nextNode) nextNode.focus();
          }
        } else if (key === "ArrowUp") {
          event.preventDefault();
          // Focus previous visible node
          const visibleNodes = root.descendants().filter(n => n.x !== undefined);
          const idx = visibleNodes.indexOf(d);
          if (idx > 0) {
            const prevNode = g.selectAll(".node").filter(n => n === visibleNodes[idx - 1]).node();
            if (prevNode) prevNode.focus();
          }
        } else if (key === "Home") {
          event.preventDefault();
          const firstNode = g.selectAll(".node").filter(n => n === root).node();
          if (firstNode) firstNode.focus();
        } else if (key === "End") {
          event.preventDefault();
          const visibleNodes = root.descendants().filter(n => n.x !== undefined);
          const lastNode = g.selectAll(".node").filter(n => n === visibleNodes[visibleNodes.length - 1]).node();
          if (lastNode) lastNode.focus();
        }
      });

    const isFolder = d => d._children || d.children;
    const isTemplate = d => d.data.type === "template";
    nodeEnter.append("circle").attr("r", 4.5)
      .attr("fill", d => isFolder(d) ? "#394b66" : isTemplate(d) ? "#6b5b95" : "#1b2230")
      .attr("stroke", d => isTemplate(d) ? "#9b8bb5" : "none")
      .attr("stroke-width", d => isTemplate(d) ? 1.5 : 0);
    // Folders: [Text] O ──── (text LEFT of circle, children branch RIGHT)
    // Leaves:  O [Text]      (circle LEFT, text RIGHT)
    // Templates: O ⌨ [Text]  (with keyboard icon indicator)
    nodeEnter.append("text").attr("dy", "0.32em")
      .attr("x", d => isFolder(d) ? -10 : 10)
      .attr("text-anchor", d => isFolder(d) ? "end" : "start")
      .text(d => isTemplate(d) ? "⌨ " + getLocalizedName(d.data) : getLocalizedName(d.data));
    nodeEnter.append("title").text(d => {
      const path = d.ancestors().reverse().map(x => getLocalizedName(x.data)).join(" / ");
      return path + (d.data.url ? `\n${d.data.url}` : "");
    });

    const nodeUpdate = nodeEnter.merge(node);
    nodeUpdate.transition().duration(duration).attr("transform", d => `translate(${d.y},${d.x})`);
    nodeUpdate.select("circle").attr("fill", d => d._children ? "#394b66" : d.children ? "#394b66" : "#1b2230");

    node.exit().transition().duration(duration).attr("transform", `translate(${source.y},${source.x})`).remove()
      .select("circle").attr("r", 1e-6);

    nodes.forEach(d => { d.x0 = d.x; d.y0 = d.y; });
  }

  update(root);
  svg.call(zoom.transform, initialTransform);

  treeController = {
    zoomIn: () => svg.transition().duration(200).call(zoom.scaleBy, 1.5),
    zoomOut: () => svg.transition().duration(200).call(zoom.scaleBy, 0.67),
    zoomReset: () => svg.transition().duration(300).call(zoom.transform, initialTransform),
    expandAll: () => { root.descendants().forEach(d => { if (d._children) d.children = d._children; }); update(root); },
    collapseAll: () => { root.descendants().forEach(d => { if (d.depth >= 1 && d.children) { d._children = d.children; d.children = null; } }); update(root); },
    highlightNode: (url) => {
      // Find node by URL
      const target = root.descendants().find(d => d.data.url === url);
      if (!target) return false;

      // Expand all ancestors
      let node = target;
      while (node.parent) {
        node = node.parent;
        if (node._children) {
          node.children = node._children;
          node._children = null;
        }
      }
      update(root);

      // Remove previous highlights
      g.selectAll(".node").classed("highlighted", false);
      g.selectAll(".node circle").attr("stroke", d => d.data.type === "template" ? "#9b8bb5" : "none");

      // Highlight target node
      setTimeout(() => {
        const targetNode = g.selectAll(".node").filter(d => d.data.url === url);
        targetNode.classed("highlighted", true);
        targetNode.select("circle").attr("stroke", "#ffd700").attr("stroke-width", 3);

        // Pan to target
        const targetData = targetNode.datum();
        if (targetData) {
          const transform = d3.zoomIdentity.translate(width / 3 - targetData.y, height / 2 - targetData.x).scale(1);
          svg.transition().duration(500).call(zoom.transform, transform);
        }

        // Remove highlight after 3 seconds
        setTimeout(() => {
          targetNode.classed("highlighted", false);
          targetNode.select("circle").attr("stroke", d => d.data.type === "template" ? "#9b8bb5" : "none").attr("stroke-width", d => d.data.type === "template" ? 1.5 : 0);
        }, 3000);
      }, 300);

      return true;
    }
  };
}

// ========== 2. Accordion View ==========
function buildAccordion(data) {
  const wrap = document.getElementById("accordionWrap");
  wrap.innerHTML = "";

  function renderNode(node, container) {
    if (node.url) {
      // Leaf node (resource)
      const item = document.createElement("div");
      item.className = "acc-item";
      item.innerHTML = `
        <svg class="acc-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/>
        </svg>
        <span class="acc-item-name">${escapeHtml(getLocalizedName(node))}</span>
        <span class="acc-item-tags">${tagsHtml(node.tags)}</span>
      `;
      item.addEventListener("click", () => openNode(node));
      container.appendChild(item);
    } else if (node.children && node.children.length > 0) {
      // Folder node
      const folder = document.createElement("div");
      folder.className = "acc-folder";

      const count = countChildren(node);
      const header = document.createElement("div");
      header.className = "acc-header";
      header.innerHTML = `
        <svg class="acc-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="9 18 15 12 9 6"/>
        </svg>
        <span class="acc-name">${escapeHtml(getLocalizedName(node))}</span>
        <span class="acc-count">(${count})</span>
      `;
      header.addEventListener("click", () => folder.classList.toggle("open"));

      const children = document.createElement("div");
      children.className = "acc-children";

      for (const child of node.children) {
        renderNode(child, children);
      }

      folder.appendChild(header);
      folder.appendChild(children);
      container.appendChild(folder);
    }
  }

  if (data.children) {
    for (const child of data.children) {
      renderNode(child, wrap);
    }
  }
}

// Accordion controls (bind once)
document.getElementById("btnAccExpandAll")?.addEventListener("click", () => {
  const wrap = document.getElementById("accordionWrap");
  wrap?.querySelectorAll(".acc-folder").forEach(f => f.classList.add("open"));
});
document.getElementById("btnAccCollapseAll")?.addEventListener("click", () => {
  const wrap = document.getElementById("accordionWrap");
  wrap?.querySelectorAll(".acc-folder").forEach(f => f.classList.remove("open"));
});

// ========== 3. Table View ==========
function buildTable(items) {
  const tbody = document.getElementById("tableBody");
  tbody.innerHTML = "";

  const sortedItems = [...items].sort((a, b) => getDisplayName(a).localeCompare(getDisplayName(b)));

  for (const item of sortedItems) {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td><span class="table-name">${escapeHtml(getDisplayName(item))}</span></td>
      <td><span class="table-category">${escapeHtml(getDisplayPath(item).join(" / "))}</span></td>
      <td><span class="table-tags">${tagsHtml(item.tags)}</span></td>
      <td><a href="${escapeHtml(item.url)}" target="_blank" rel="noopener" class="table-link">${escapeHtml(item.url)}</a></td>
    `;
    tr.style.cursor = "pointer";
    tr.addEventListener("click", (e) => {
      if (e.target.tagName !== "A") openNode(item);
    });
    tbody.appendChild(tr);
  }

  // Sort controls
  const sortSelect = document.getElementById("tableSort");
  if (sortSelect) {
    sortSelect.onchange = () => {
      const sortBy = sortSelect.value;
      let sorted;
      switch (sortBy) {
        case "category":
          sorted = [...items].sort((a, b) => getDisplayPath(a).join("/").localeCompare(getDisplayPath(b).join("/")));
          break;
        case "tags":
          sorted = [...items].sort((a, b) => (a.tags[0] || "").localeCompare(b.tags[0] || ""));
          break;
        default:
          sorted = [...items].sort((a, b) => getDisplayName(a).localeCompare(getDisplayName(b)));
      }
      tbody.innerHTML = "";
      for (const item of sorted) {
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td><span class="table-name">${escapeHtml(getDisplayName(item))}</span></td>
          <td><span class="table-category">${escapeHtml(getDisplayPath(item).join(" / "))}</span></td>
          <td><span class="table-tags">${tagsHtml(item.tags)}</span></td>
          <td><a href="${escapeHtml(item.url)}" target="_blank" rel="noopener" class="table-link">${escapeHtml(item.url)}</a></td>
        `;
        tr.style.cursor = "pointer";
        tr.addEventListener("click", (e) => { if (e.target.tagName !== "A") openNode(item); });
        tbody.appendChild(tr);
      }
    };
  }
}

// ========== 4. Explorer View ==========
let explorerState = { currentPath: [], currentNode: null };

function buildExplorer(data) {
  const treeEl = document.getElementById("explorerTree");
  const breadcrumb = document.getElementById("explorerBreadcrumb");
  const itemsEl = document.getElementById("explorerItems");

  treeEl.innerHTML = "";
  explorerState.currentNode = data;
  explorerState.currentPath = [data];

  function renderTreeItem(node, container, depth = 0) {
    if (!node.children && !node.url) return;

    if (node.children) {
      const item = document.createElement("div");
      item.className = "exp-tree-item";
      item.style.paddingLeft = `${10 + depth * 12}px`;
      item.innerHTML = `
        <svg class="exp-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
        </svg>
        <span>${escapeHtml(getLocalizedName(node))}</span>
      `;
      item.addEventListener("click", () => selectFolder(node, [data, node]));
      container.appendChild(item);

      // Show first level children
      if (depth < 1) {
        const childContainer = document.createElement("div");
        childContainer.className = "exp-tree-children";
        for (const child of node.children) {
          if (child.children) renderTreeItem(child, childContainer, depth + 1);
        }
        container.appendChild(childContainer);
      }
    }
  }

  function selectFolder(node, path) {
    explorerState.currentNode = node;
    explorerState.currentPath = path;

    // Update tree selection
    treeEl.querySelectorAll(".exp-tree-item").forEach(el => el.classList.remove("active"));

    renderBreadcrumb();
    renderItems();
  }

  function renderBreadcrumb() {
    breadcrumb.innerHTML = "";
    explorerState.currentPath.forEach((node, i) => {
      const span = document.createElement("span");
      span.textContent = getLocalizedName(node);
      if (i < explorerState.currentPath.length - 1) {
        span.addEventListener("click", () => {
          selectFolder(node, explorerState.currentPath.slice(0, i + 1));
        });
      }
      breadcrumb.appendChild(span);
      if (i < explorerState.currentPath.length - 1) {
        breadcrumb.appendChild(document.createTextNode(" / "));
      }
    });
  }

  function renderItems() {
    itemsEl.innerHTML = "";
    const node = explorerState.currentNode;

    if (!node.children) return;

    // Show folders first, then items
    const folders = node.children.filter(c => c.children);
    const items = node.children.filter(c => c.url);

    for (const folder of folders) {
      const div = document.createElement("div");
      div.className = "exp-list-item";
      div.innerHTML = `
        <div class="exp-list-icon">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
          </svg>
        </div>
        <div class="exp-list-info">
          <div class="exp-list-name">${escapeHtml(getLocalizedName(folder))}</div>
          <div class="exp-list-url">${t("itemsCount", countChildren(folder))}</div>
        </div>
      `;
      div.addEventListener("click", () => {
        selectFolder(folder, [...explorerState.currentPath, folder]);
      });
      itemsEl.appendChild(div);
    }

    for (const item of items) {
      const div = document.createElement("div");
      div.className = "exp-list-item";
      div.innerHTML = `
        <div class="exp-list-icon">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/>
          </svg>
        </div>
        <div class="exp-list-info">
          <div class="exp-list-name">${escapeHtml(getLocalizedName(item))}</div>
          <div class="exp-list-url">${escapeHtml(item.url)}</div>
          <div class="exp-list-tags">${tagsHtml(item.tags)}</div>
        </div>
      `;
      div.addEventListener("click", () => openNode(item));
      itemsEl.appendChild(div);
    }
  }

  // Render initial tree
  if (data.children) {
    for (const child of data.children) {
      renderTreeItem(child, treeEl, 0);
    }
  }

  renderBreadcrumb();
  renderItems();
}

// ========== 5. Cards View ==========
let cardsState = { activeTag: null };

function buildCards(items, stats) {
  const filterEl = document.getElementById("cardsFilter");
  const gridEl = document.getElementById("cardsGrid");

  // Build tag filter
  filterEl.innerHTML = "";
  const topTags = Object.entries(stats.tagCounts).sort((a, b) => b[1] - a[1]).slice(0, 15);

  const allBtn = document.createElement("button");
  allBtn.className = "filter-tag active";
  allBtn.textContent = t("allTags");
  allBtn.addEventListener("click", () => {
    cardsState.activeTag = null;
    filterEl.querySelectorAll(".filter-tag").forEach(b => b.classList.remove("active"));
    allBtn.classList.add("active");
    renderCards();
  });
  filterEl.appendChild(allBtn);

  for (const [tag, count] of topTags) {
    const btn = document.createElement("button");
    btn.className = "filter-tag";
    btn.innerHTML = `${escapeHtml(tag)} <small>${count}</small>`;
    btn.addEventListener("click", () => {
      cardsState.activeTag = tag;
      filterEl.querySelectorAll(".filter-tag").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      renderCards();
    });
    filterEl.appendChild(btn);
  }

  function renderCards() {
    gridEl.innerHTML = "";

    let filtered = items;
    if (cardsState.activeTag) {
      filtered = items.filter(it => it.tags.includes(cardsState.activeTag));
    }

    // Limit to first 100 for performance
    for (const item of filtered.slice(0, 100)) {
      const card = document.createElement("div");
      card.className = "card-item";
      card.innerHTML = `
        <div class="card-header">
          <div class="card-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/>
            </svg>
          </div>
          <div class="card-title">
            <div class="card-name">${escapeHtml(getDisplayName(item))}</div>
            <div class="card-category">${escapeHtml(getDisplayPath(item).slice(-2).join(" / "))}</div>
          </div>
        </div>
        <div class="card-tags">${tagsHtml(item.tags)}</div>
        <div class="card-url">${escapeHtml(item.url)}</div>
      `;
      card.addEventListener("click", () => openNode(item));
      gridEl.appendChild(card);
    }

    if (filtered.length > 100) {
      const more = document.createElement("div");
      more.className = "card-item";
      more.style.display = "flex";
      more.style.alignItems = "center";
      more.style.justifyContent = "center";
      more.style.color = "var(--muted)";
      more.textContent = `+${filtered.length - 100} more...`;
      gridEl.appendChild(more);
    }
  }

  renderCards();
}

// ========== Deep Linking ==========
function getUrlParams() {
  const hash = window.location.hash.slice(1);
  const params = {};
  for (const part of hash.split("&")) {
    const idx = part.indexOf("=");
    if (idx > 0) {
      const key = part.slice(0, idx);
      const val = part.slice(idx + 1);
      if (val) params[key] = decodeURIComponent(val);
    }
  }
  return params;
}

function setUrlParams(params) {
  const parts = [];
  for (const [key, val] of Object.entries(params)) {
    if (val) parts.push(`${key}=${encodeURIComponent(val)}`);
  }
  const hash = parts.length > 0 ? "#" + parts.join("&") : "";
  if (window.location.hash !== hash) {
    history.replaceState(null, "", hash || window.location.pathname);
  }
}

function updateUrlFromState() {
  const params = {};
  if (searchInput.value) params.search = searchInput.value;
  if (tagFilterSelect?.value) params.tag = tagFilterSelect.value;
  if (currentView !== "tree") params.view = currentView;
  setUrlParams(params);
}

function applyUrlParams() {
  const params = getUrlParams();
  if (params.search) searchInput.value = params.search;
  if (params.tag && tagFilterSelect) tagFilterSelect.value = params.tag;
  if (params.view && ["tree", "accordion", "table", "explorer", "cards"].includes(params.view)) {
    currentView = params.view;
    localStorage.setItem("view", currentView);
  }
}

// ========== Initialize ==========
async function init() {
  applyLanguage(currentLang);

  document.getElementById("btnLang")?.addEventListener("click", toggleLanguage);

  // View switching
  document.querySelectorAll(".view-btn").forEach(btn => {
    btn.addEventListener("click", () => switchView(btn.dataset.view));
  });

  resultMeta.textContent = t("loading");
  treeSvg.innerHTML = `<text x="20" y="40" fill="#a7a7a7" font-size="14">${t("loading")}</text>`;

  const res = await fetch(DATA_URL);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const data = await res.json();

  const items = flatten(data);
  const stats = countStats(data);

  window._appData = data;
  window._appItems = items;
  window._appStats = stats;

  renderStats(stats);
  renderFavorites();
  populateTagFilter(stats);

  // Apply URL params before initializing views
  applyUrlParams();

  // Search with URL update
  const onSearch = () => {
    renderResults(items, searchInput.value || "");
    updateUrlFromState();
  };
  const debouncedSearch = debounce(onSearch, DEBOUNCE_MS);
  searchInput.addEventListener("input", debouncedSearch);
  searchInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") { e.preventDefault(); onSearch(); }
    if (e.key === "Escape") { searchInput.value = ""; if (tagFilterSelect) tagFilterSelect.value = ""; onSearch(); searchInput.blur(); }
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "/" && document.activeElement !== searchInput) { e.preventDefault(); searchInput.focus(); }
  });

  btnClear.addEventListener("click", () => { searchInput.value = ""; if (tagFilterSelect) tagFilterSelect.value = ""; onSearch(); searchInput.focus(); });

  // Tag filter with URL update
  tagFilterSelect?.addEventListener("change", onSearch);

  // Handle browser back/forward
  window.addEventListener("hashchange", () => {
    applyUrlParams();
    onSearch();
    switchView(currentView);
  });

  // Export buttons
  btnExportCSV?.addEventListener("click", () => exportToCSV(currentSearchResults));
  btnExportJSON?.addEventListener("click", () => exportToJSON(currentSearchResults));

  // Tree controls
  document.getElementById("btnZoomIn")?.addEventListener("click", () => treeController?.zoomIn());
  document.getElementById("btnZoomOut")?.addEventListener("click", () => treeController?.zoomOut());
  document.getElementById("btnZoomReset")?.addEventListener("click", () => treeController?.zoomReset());
  document.getElementById("btnExpandAll")?.addEventListener("click", () => treeController?.expandAll());
  document.getElementById("btnCollapseAll")?.addEventListener("click", () => treeController?.collapseAll());

  // Initialize current view
  switchView(currentView);
  onSearch();
}

function showError(err) {
  console.error(err);
  resultMeta.innerHTML = `${t("loadError", err.message || "Unknown error")} <button id="retryBtn" class="btnLink">${t("retryBtn")}</button>`;
  treeSvg.innerHTML = `<text x="20" y="40" fill="#e6e6e6" font-size="14">${t("loadErrorTree")}</text>`;
  if (statsContent) statsContent.innerHTML = t("loadFailed");
  document.getElementById("retryBtn")?.addEventListener("click", () => {
    resultMeta.textContent = t("loading");
    init().catch(showError);
  });
}

init().catch(showError);

// ========== Service Worker Registration ==========
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('./sw.js')
      .then(() => {})
      .catch(() => {});
  });
}
