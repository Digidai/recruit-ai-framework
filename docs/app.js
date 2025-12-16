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
  const t = node.type || node.data?.type;
  const url = node.url || node.data?.url;
  if(!url) return;

  if(t === "template"){
    const q = prompt("输入关键词（会替换到 URL 里的 {query}）：");
    if(!q) return;
    const finalUrl = url.replaceAll("{query}", encodeURIComponent(q.trim()));
    window.open(finalUrl, "_blank", "noopener");
  }else{
    window.open(url, "_blank", "noopener");
  }
}

function flatten(node, path = []){
  const here = [...path, node.name];
  const out = [];
  if(node.type === "folder" && Array.isArray(node.children)){
    for(const ch of node.children){
      out.push(...flatten(ch, here));
    }
  }else if(node.url){
    out.push({
      name: node.name,
      type: node.type || "url",
      url: node.url,
      tags: node.tags || [],
      path: here.slice(0, -1),
    });
  }
  return out;
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
  const topTags = Object.entries(stats.tagCounts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 8)
    .map(([tag, count]) => `<span class="tag">${escapeHtml(tag)}</span> ${count}`)
    .join("、");

  statsContent.innerHTML = `
    <p><strong>${stats.categories}</strong> 大分类 · <strong>${stats.resources}</strong> 条资源 · <strong>${stats.templates}</strong> 个模板</p>
    <p>热门标签：${topTags}</p>
  `;
}

function renderResults(items, query){
  resultList.innerHTML = "";
  if(!query){
    resultMeta.textContent = `共 ${items.length} 条资源。输入关键词开始搜索。`;
    return;
  }
  const q = query.trim().toLowerCase();
  const hit = items.filter(it => (it.name + " " + it.path.join(" / ") + " " + it.tags.join(" ")).toLowerCase().includes(q));
  resultMeta.textContent = `匹配 ${hit.length} 条（展示前 ${Math.min(MAX_RESULTS, hit.length)} 条）`;

  for(const it of hit.slice(0, MAX_RESULTS)){
    const li = document.createElement("li");
    li.tabIndex = 0; // Make focusable for keyboard navigation
    li.innerHTML = `
      <div class="resultTitle">
        <strong>${escapeHtml(it.name)}</strong>
        ${tagsHtml(it.tags)}
      </div>
      <div class="resultPath">${escapeHtml(it.path.join(" / "))}</div>
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
  const initialTransform = d3.zoomIdentity.translate(40, height/2).scale(1);

  const dx = 14;
  const dy = 220;
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
        .attr("fill", "none")
        .attr("stroke", "#2a2f3a")
        .attr("stroke-width", 1.2)
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
      .attr("class", "node")
      .attr("transform", d => `translate(${source.y0},${source.x0})`)
      .attr("cursor", "pointer")
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
      .attr("r", 4.5)
      .attr("fill", d => (d._children ? "#394b66" : (d.children ? "#394b66" : "#1b2230")))
      .attr("stroke", "#6a7ea6")
      .attr("stroke-width", 1);

    nodeEnter.append("text")
      .attr("dy", "0.32em")
      .attr("x", d => d._children ? -8 : 8)
      .attr("text-anchor", d => d._children ? "end" : "start")
      .attr("fill", "#e6e6e6")
      .style("font-size", "12px")
      .text(d => d.data.name);

    nodeEnter.append("title")
      .text(d => {
        const path = d.ancestors().reverse().map(x => x.data.name).join(" / ");
        const url = d.data.url ? `\n${d.data.url}` : "";
        return path + url;
      });

    const nodeUpdate = nodeEnter.merge(node);

    nodeUpdate.transition()
      .duration(duration)
      .attr("transform", d => `translate(${d.y},${d.x})`);

    nodeUpdate.select("circle")
      .attr("fill", d => (d._children ? "#394b66" : (d.children ? "#394b66" : "#1b2230")));

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
  // Show loading state
  resultMeta.textContent = "正在加载数据...";
  treeSvg.innerHTML = `<text x="20" y="40" fill="#a7a7a7" font-size="14">加载中...</text>`;

  const res = await fetch(DATA_URL);
  if(!res.ok) throw new Error(`HTTP ${res.status}`);
  const data = await res.json();

  const items = flatten(data);
  const stats = countStats(data);
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
  const errorMsg = err.message || "未知错误";
  resultMeta.textContent = `加载失败：${errorMsg}。请检查网络连接和本地服务。`;
  treeSvg.innerHTML = `<text x="20" y="40" fill="#e6e6e6" font-size="14">数据加载失败，请刷新页面重试。</text>`;
  if (statsContent) statsContent.innerHTML = "加载失败";
});
