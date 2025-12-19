/* Recruitment & AI Hiring Framework
 * Data file: tarf.json
 * Node schema (suggested):
 *  - folder: { name, type:"folder", children:[...] }
 *  - url:    { name, type:"url", url:"https://...", tags:[...] }
 *  - template: { name, type:"template", url:"https://...{query}...", tags:["M", ...] }
 */

const DATA_URL = "tarf.json";
const MAX_RESULTS = 80;
const DEBOUNCE_MS = 150;

// ========== i18n (Internationalization) ==========
const i18n = {
  zh: {
    // Header
    subtitle: "一个可维护的「招聘 × AI 招聘」工具地图（数据驱动），灵感来自 OSINT Framework。",
    searchPlaceholder: "搜索：工具 / 指南 / 标准 / 会议 …（支持中英文关键词）",
    clearBtn: "清空",
    downloadJson: "下载 tarf.json",
    langLabel: "EN",
    // Legend
    legendR: "需要注册/登录",
    legendP: "付费/商用",
    legendO: "开源",
    legendM: "模板链接（会提示输入 query）",
    legendPDF: "PDF 资源",
    legendLaw: "法规/监管页面",
    legendFramework: "框架/标准",
    // Tree panel
    treeTitle: "工具树",
    resetBtn: "重置",
    expandBtn: "展开",
    collapseBtn: "收起",
    hint1: "点击「文件夹」节点展开/收起。",
    hint2: "点击「链接」节点会在新标签页打开。",
    hint3: '点击带 <span class="tag">M</span> 的节点会弹窗让你输入关键词，并把关键词替换进 URL 里的 <code>{query}</code>。',
    hint4: "<kbd>/</kbd> 聚焦搜索框，<kbd>Esc</kbd> 清空搜索。",
    // Search panel
    searchResults: "搜索结果",
    searchHint: "输入关键词开始搜索。",
    statsTitle: "数据统计",
    loading: "加载中...",
    howToExtend: "如何扩展",
    extend1: "编辑 <code>docs/tarf.json</code>（添加/修改节点）。",
    extend2: '本地预览：在项目根目录运行 <code>python -m http.server 8000</code>，然后打开 <code>http://localhost:8000/docs/</code>。',
    extend3: "发布：把 <code>docs/</code> 作为静态站点部署（GitHub Pages / Cloudflare Pages / Vercel 等）。",
    // Footer
    footerWarning: "⚠️ 仅用于招聘工具导航与学习研究；使用任何自动化/AI 招聘能力时请遵守适用法律法规与隐私要求，并进行必要的偏差评估与人类复核。",
    reportIssue: "反馈问题",
    // Dynamic content
    totalResources: (count) => `共 ${count} 条资源。输入关键词开始搜索。`,
    matchResults: (match, show) => `匹配 ${match} 条（展示前 ${show} 条）`,
    statsContent: (cats, res, tpl) => `<p><strong>${cats}</strong> 大分类 · <strong>${res}</strong> 条资源 · <strong>${tpl}</strong> 个模板</p>`,
    hotTags: "热门标签：",
    loadError: (msg) => `加载失败：${msg}。请检查网络连接和本地服务。`,
    loadErrorTree: "数据加载失败，请刷新页面重试。",
    loadFailed: "加载失败",
    promptQuery: "输入关键词（会替换到 URL 里的 {query}）：",
  },
  en: {
    // Header
    subtitle: "A maintainable data-driven Recruitment & AI Hiring tool map, inspired by OSINT Framework.",
    searchPlaceholder: "Search: Tools / Guides / Standards / Events... (supports keywords)",
    clearBtn: "Clear",
    downloadJson: "Download tarf.json",
    langLabel: "中文",
    // Legend
    legendR: "Registration required",
    legendP: "Paid/Commercial",
    legendO: "Open Source",
    legendM: "Template link (prompts for query)",
    legendPDF: "PDF Resource",
    legendLaw: "Law/Regulation",
    legendFramework: "Framework/Standard",
    // Tree panel
    treeTitle: "Tool Tree",
    resetBtn: "Reset",
    expandBtn: "Expand",
    collapseBtn: "Collapse",
    hint1: "Click folder nodes to expand/collapse.",
    hint2: "Click link nodes to open in new tab.",
    hint3: 'Click nodes with <span class="tag">M</span> tag to enter keywords, which replace <code>{query}</code> in the URL.',
    hint4: "<kbd>/</kbd> to focus search, <kbd>Esc</kbd> to clear.",
    // Search panel
    searchResults: "Search Results",
    searchHint: "Enter keywords to search.",
    statsTitle: "Statistics",
    loading: "Loading...",
    howToExtend: "How to Extend",
    extend1: "Edit <code>docs/tarf.json</code> (add/modify nodes).",
    extend2: 'Local preview: Run <code>python -m http.server 8000</code> in project root, then open <code>http://localhost:8000/docs/</code>.',
    extend3: "Deploy: Use <code>docs/</code> as static site (GitHub Pages / Cloudflare Pages / Vercel etc.).",
    // Footer
    footerWarning: "⚠️ For recruitment tool navigation and research only. When using AI/automation in hiring, comply with applicable laws, privacy requirements, and conduct bias assessments with human review.",
    reportIssue: "Report Issue",
    // Dynamic content
    totalResources: (count) => `${count} resources total. Enter keywords to search.`,
    matchResults: (match, show) => `${match} matches (showing first ${show})`,
    statsContent: (cats, res, tpl) => `<p><strong>${cats}</strong> Categories · <strong>${res}</strong> Resources · <strong>${tpl}</strong> Templates</p>`,
    hotTags: "Popular tags: ",
    loadError: (msg) => `Load failed: ${msg}. Check network and local server.`,
    loadErrorTree: "Data load failed. Please refresh the page.",
    loadFailed: "Load failed",
    promptQuery: "Enter keywords (will replace {query} in URL):",
  }
};

let currentLang = localStorage.getItem("lang") || "zh";

function t(key, ...args) {
  const val = i18n[currentLang][key];
  if (typeof val === "function") return val(...args);
  return val || key;
}

function applyLanguage(lang) {
  currentLang = lang;
  localStorage.setItem("lang", lang);

  // Update html lang attribute
  document.getElementById("htmlRoot").lang = lang === "zh" ? "zh-CN" : "en";

  // Update lang button label
  const langLabel = document.getElementById("langLabel");
  if (langLabel) langLabel.textContent = t("langLabel");

  // Update all elements with data-i18n attribute
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    if (i18n[currentLang][key]) {
      el.textContent = i18n[currentLang][key];
    }
  });

  // Update elements with data-i18n-html (contains HTML)
  document.querySelectorAll("[data-i18n-html]").forEach(el => {
    const key = el.getAttribute("data-i18n-html");
    if (i18n[currentLang][key]) {
      el.innerHTML = i18n[currentLang][key];
    }
  });

  // Update placeholders
  document.querySelectorAll("[data-i18n-placeholder]").forEach(el => {
    const key = el.getAttribute("data-i18n-placeholder");
    if (i18n[currentLang][key]) {
      el.placeholder = i18n[currentLang][key];
    }
  });
}

function toggleLanguage() {
  const newLang = currentLang === "zh" ? "en" : "zh";
  applyLanguage(newLang);

  // Re-render dynamic content if data is loaded
  if (window._appItems) {
    renderResults(window._appItems, searchInput.value || "");
  }
  if (window._appStats) {
    renderStats(window._appStats);
  }
  // Rebuild tree with new language
  if (window._appData) {
    buildTree(window._appData);
  }
}

// DOM elements
const searchInput = document.getElementById("searchInput");
const btnClear = document.getElementById("btnClear");
const resultMeta = document.getElementById("resultMeta");
const resultList = document.getElementById("resultList");
const treeSvg = document.getElementById("treeSvg");
const statsContent = document.getElementById("statsContent");

// Zoom control buttons
const btnZoomIn = document.getElementById("btnZoomIn");
const btnZoomOut = document.getElementById("btnZoomOut");
const btnZoomReset = document.getElementById("btnZoomReset");
const btnExpandAll = document.getElementById("btnExpandAll");
const btnCollapseAll = document.getElementById("btnCollapseAll");

// Utility: debounce function
function debounce(fn, delay) {
  let timer = null;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

function escapeHtml(str){
  return str
    .replaceAll("&","&amp;")
    .replaceAll("<","&lt;")
    .replaceAll(">","&gt;")
    .replaceAll('"',"&quot;")
    .replaceAll("'","&#39;");
}

function tagHtml(tag){
  return `<span class="tag">${escapeHtml(tag)}</span>`;
}

function tagsHtml(tags){
  if(!tags || !tags.length) return "";
  return tags.map(tagHtml).join("");
}

function openNode(node){
  const nodeType = node.type || node.data?.type;
  const url = node.url || node.data?.url;
  if(!url) return;

  if(nodeType === "template"){
    const q = prompt(t("promptQuery"));
    if(!q) return;
    const finalUrl = url.replaceAll("{query}", encodeURIComponent(q.trim()));
    window.open(finalUrl, "_blank", "noopener");
  }else{
    window.open(url, "_blank", "noopener");
  }
}

// Get localized name for a node
function getLocalizedName(node) {
  if (currentLang === "en" && node.name_en) {
    return node.name_en;
  }
  return node.name;
}

function flatten(node, path = [], pathEn = []){
  const here = [...path, node.name];
  const hereEn = [...pathEn, node.name_en || node.name];
  const out = [];
  if(node.type === "folder" && Array.isArray(node.children)){
    for(const ch of node.children){
      out.push(...flatten(ch, here, hereEn));
    }
  }else if(node.url){
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

// Get display name based on current language
function getDisplayName(item) {
  return currentLang === "en" ? (item.name_en || item.name) : item.name;
}

// Get display path based on current language
function getDisplayPath(item) {
  return currentLang === "en" ? (item.path_en || item.path) : item.path;
}

// Count statistics
function countStats(data) {
  let categories = 0;
  let resources = 0;
  let templates = 0;
  const tagCounts = {};

  function traverse(node) {
    if (node.type === "folder") {
      // Count top-level categories (depth 1)
      if (node.name.match(/^\d{2}\s/)) {
        categories++;
      }
      if (Array.isArray(node.children)) {
        node.children.forEach(traverse);
      }
    } else if (node.url) {
      resources++;
      if (node.type === "template") templates++;
      if (node.tags) {
        node.tags.forEach(tag => {
          tagCounts[tag] = (tagCounts[tag] || 0) + 1;
        });
      }
    }
  }

  traverse(data);
  return { categories, resources, templates, tagCounts };
}

function renderStats(stats) {
  const separator = currentLang === "zh" ? "、" : ", ";
  const topTags = Object.entries(stats.tagCounts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 8)
    .map(([tag, count]) => `<span class="tag">${escapeHtml(tag)}</span> ${count}`)
    .join(separator);

  statsContent.innerHTML = `
    ${t("statsContent", stats.categories, stats.resources, stats.templates)}
    <p>${t("hotTags")}${topTags}</p>
  `;
}

function renderResults(items, query){
  resultList.innerHTML = "";
  if(!query){
    resultMeta.textContent = t("totalResources", items.length);
    return;
  }
  const q = query.trim().toLowerCase();
  // Search both Chinese and English names/paths
  const hit = items.filter(it => {
    const searchText = [
      it.name,
      it.name_en || "",
      it.path.join(" / "),
      (it.path_en || it.path).join(" / "),
      it.tags.join(" ")
    ].join(" ").toLowerCase();
    return searchText.includes(q);
  });
  resultMeta.textContent = t("matchResults", hit.length, Math.min(MAX_RESULTS, hit.length));

  for(const it of hit.slice(0, MAX_RESULTS)){
    const li = document.createElement("li");
    li.tabIndex = 0; // Make focusable for keyboard navigation
    li.innerHTML = `
      <div class="resultTitle">
        <strong>${escapeHtml(getDisplayName(it))}</strong>
        ${tagsHtml(it.tags)}
      </div>
      <div class="resultPath">${escapeHtml(getDisplayPath(it).join(" / "))}</div>
      <div class="resultUrl">${escapeHtml(it.url)}</div>
    `;
    li.addEventListener("click", () => openNode(it));
    li.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        openNode(it);
      }
    });
    resultList.appendChild(li);
  }
}

// Tree controller - stores references to tree functions for button handlers
let treeController = null;

function buildTree(data){
  // D3 collapsible tree (zoomable)
  const root = d3.hierarchy(data);
  root.x0 = 0;
  root.y0 = 0;

  // Collapse all by default except first level
  root.descendants().forEach((d, i) => {
    d.id = i;
    d._children = d.children;
    if(d.depth >= 2) d.children = null;
  });

  const svg = d3.select(treeSvg);
  svg.selectAll("*").remove();

  const wrap = document.getElementById("treeWrap");
  const width = wrap.clientWidth;
  const height = wrap.clientHeight;

  const g = svg
    .attr("viewBox", [-20, -20, width + 40, height + 40])
    .append("g");

  const zoom = d3.zoom()
    .scaleExtent([0.1, 10])
    .on("zoom", (event) => g.attr("transform", event.transform));

  svg.call(zoom);

  // Store initial transform for reset
  const initialTransform = d3.zoomIdentity.translate(60, height/2).scale(1);

  // Increased spacing for better readability
  const dx = 28;  // Vertical spacing (was 14)
  const dy = 260; // Horizontal spacing (was 220)
  const tree = d3.tree().nodeSize([dx, dy]);
  const diagonal = d3.linkHorizontal().x(d => d.y).y(d => d.x);

  let duration = 250;

  function update(source){
    const nodes = root.descendants().reverse();
    const links = root.links();

    tree(root);

    let left = root;
    let right = root;
    root.eachBefore(node => {
      if(node.x < left.x) left = node;
      if(node.x > right.x) right = node;
    });

    const innerHeight = right.x - left.x + 120;

    svg.transition()
      .duration(duration)
      .attr("viewBox", [-40, left.x - 60, width + 80, innerHeight]);

    // Links
    const link = g.selectAll("path.link")
      .data(links, d => d.target.id);

    link.join(
      enter => enter.append("path")
        .attr("class", "link")
        .attr("d", d => {
          const o = {x: source.x0, y: source.y0};
          return diagonal({source: o, target: o});
        })
        .call(enter => enter.transition().duration(duration).attr("d", diagonal)),
      update => update.call(update => update.transition().duration(duration).attr("d", diagonal)),
      exit => exit.call(exit => exit.transition().duration(duration)
        .attr("d", d => {
          const o = {x: source.x, y: source.y};
          return diagonal({source: o, target: o});
        })
        .remove())
    );

    // Nodes
    const node = g.selectAll("g.node")
      .data(nodes, d => d.id);

    const nodeEnter = node.enter().append("g")
      .attr("class", d => "node" + (d.children ? " node--internal" : " node--leaf"))
      .attr("transform", d => `translate(${source.y0},${source.x0})`)
      // .attr("cursor", "pointer") // Handled by CSS
      .on("click", (event, d) => {
        if(d.children){
          d._children = d.children;
          d.children = null;
          update(d);
        }else if(d._children){
          d.children = d._children;
          d._children = null;
          update(d);
        }else{
          openNode(d.data);
        }
      });

    nodeEnter.append("circle")
      .attr("r", 5) // Slightly larger radius
      // Fill and stroke handled by CSS now
      .attr("fill", d => (d._children ? "#555" : (d.children ? "#555" : "#999"))); 
      // Note: Kept inline fill as a fallback or if we want dynamic logic, 
      // but actually we want CSS to handle it completely. 
      // Let's remove the inline attrs so CSS variables take over.
      
    // Re-select to clear any previous attributes if this was a partial replace, 
    // but here we are replacing the block. 
    // Actually, D3 enters need distinct elements. 
    // Let's stick to the cleaner version:

    /* 
       We will remove the inline .attr("fill", ...) and .attr("stroke", ...)
       and let CSS .node circle handle it.
       However, we might want to distinguish open/closed folders visually if CSS isn't enough.
       CSS :has() selector isn't fully supported in all outdated contexts but good enough for modern.
       Alternatively, we can add classes like 'node--closed' or 'node--open'.
    */

    nodeEnter.select("circle").remove(); // Remove if exists (it shouldn't in enter)
    
    nodeEnter.append("circle")
        .attr("r", 5);

    nodeEnter.append("text")
      .attr("dy", "0.32em")
      .attr("x", d => d.children || d._children ? -10 : 10)
      .attr("text-anchor", d => d.children || d._children ? "end" : "start")
      .style("font-size", null) // Controlled by CSS
      .text(d => getLocalizedName(d.data));

    nodeEnter.append("title")
      .text(d => {
        const path = d.ancestors().reverse().map(x => getLocalizedName(x.data)).join(" / ");
        const url = d.data.url ? `\n${d.data.url}` : "";
        return path + url;
      });

    const nodeUpdate = nodeEnter.merge(node);

    nodeUpdate.transition()
      .duration(duration)
      .attr("transform", d => `translate(${d.y},${d.x})`);
    
    // Update classes for open/closed state styling if needed
    nodeUpdate.attr("class", d => "node" + (d.children ? " node--open" : (d._children ? " node--closed" : " node--leaf")));

    // We can remove the inline styling for circles here too
    nodeUpdate.select("circle")
       .attr("r", 5); // Ensure size

    const nodeExit = node.exit().transition()
      .duration(duration)
      .attr("transform", d => `translate(${source.y},${source.x})`)
      .remove();

    nodeExit.select("circle").attr("r", 1e-6);
    nodeExit.select("text").style("fill-opacity", 1e-6);

    // stash old positions
    root.eachBefore(d => {
      d.x0 = d.x;
      d.y0 = d.y;
    });
  }

  update(root);

  // Center view a bit
  svg.call(zoom.transform, d3.zoomIdentity.translate(40, height/2).scale(1));

  // Return controller object for button handlers
  treeController = {
    zoomIn: () => svg.transition().duration(200).call(zoom.scaleBy, 1.5),
    zoomOut: () => svg.transition().duration(200).call(zoom.scaleBy, 0.67),
    zoomReset: () => svg.transition().duration(300).call(zoom.transform, initialTransform),
    expandAll: () => {
      root.descendants().forEach(d => {
        if (d._children) d.children = d._children;
      });
      update(root);
    },
    collapseAll: () => {
      root.descendants().forEach(d => {
        if (d.depth >= 1 && d.children) {
          d._children = d.children;
          d.children = null;
        }
      });
      update(root);
    }
  };
}

async function init(){
  // Apply saved language preference on load
  applyLanguage(currentLang);

  // Set up language toggle button
  const btnLang = document.getElementById("btnLang");
  if (btnLang) {
    btnLang.addEventListener("click", toggleLanguage);
  }

  // Show loading state
  resultMeta.textContent = t("loading");
  treeSvg.innerHTML = `<text x="20" y="40" fill="#a7a7a7" font-size="14">${t("loading")}</text>`;

  const res = await fetch(DATA_URL);
  if(!res.ok) throw new Error(`HTTP ${res.status}`);
  const data = await res.json();

  const items = flatten(data);
  const stats = countStats(data);

  // Store for re-rendering on language change
  window._appData = data;
  window._appItems = items;
  window._appStats = stats;

  renderStats(stats);

  // Search interactions with debounce
  const onSearch = () => renderResults(items, searchInput.value || "");
  const debouncedSearch = debounce(onSearch, DEBOUNCE_MS);

  searchInput.addEventListener("input", debouncedSearch);
  searchInput.addEventListener("keydown", (e) => {
    if(e.key === "Enter"){
      e.preventDefault();
      onSearch(); // Immediate search on Enter
    }
    if(e.key === "Escape"){
      searchInput.value = "";
      onSearch();
      searchInput.blur();
    }
  });

  // Global keyboard shortcuts
  document.addEventListener("keydown", (e) => {
    // "/" to focus search (when not in input)
    if (e.key === "/" && document.activeElement !== searchInput) {
      e.preventDefault();
      searchInput.focus();
    }
  });

  btnClear.addEventListener("click", () => {
    searchInput.value = "";
    onSearch();
    searchInput.focus();
  });

  // Build tree
  buildTree(data);

  // Set up tree control button handlers (once, after tree is built)
  btnZoomIn?.addEventListener("click", () => treeController?.zoomIn());
  btnZoomOut?.addEventListener("click", () => treeController?.zoomOut());
  btnZoomReset?.addEventListener("click", () => treeController?.zoomReset());
  btnExpandAll?.addEventListener("click", () => treeController?.expandAll());
  btnCollapseAll?.addEventListener("click", () => treeController?.collapseAll());

  // First render
  onSearch();
}

init().catch(err => {
  console.error(err);
  const errorMsg = err.message || "Unknown error";
  resultMeta.textContent = t("loadError", errorMsg);
  treeSvg.innerHTML = `<text x="20" y="40" fill="#e6e6e6" font-size="14">${t("loadErrorTree")}</text>`;
  if (statsContent) statsContent.innerHTML = t("loadFailed");
});
