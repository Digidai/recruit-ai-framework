/* Recruitment & AI Hiring Framework
 * Data file: tarf.json
 * Node schema (suggested):
 *  - folder: { name, type:"folder", children:[...] }
 *  - url:    { name, type:"url", url:"https://...", tags:[...] }
 *  - template: { name, type:"template", url:"https://...{query}...", tags:["M", ...] }
 */

const DATA_URL = "tarf.json";
const MAX_RESULTS = 80;

const searchInput = document.getElementById("searchInput");
const btnClear = document.getElementById("btnClear");
const resultMeta = document.getElementById("resultMeta");
const resultList = document.getElementById("resultList");
const treeSvg = document.getElementById("treeSvg");

function escapeHtml(str){
  return str.replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;");
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

function renderResults(items, query){
  resultList.innerHTML = "";
  if(!query){
    resultMeta.textContent = "输入关键词开始搜索。";
    return;
  }
  const q = query.trim().toLowerCase();
  const hit = items.filter(it => (it.name + " " + it.path.join(" / ") + " " + it.tags.join(" ")).toLowerCase().includes(q));
  resultMeta.textContent = `匹配 ${hit.length} 条（展示前 ${Math.min(MAX_RESULTS, hit.length)} 条）`;

  for(const it of hit.slice(0, MAX_RESULTS)){
    const li = document.createElement("li");
    li.innerHTML = `
      <div class="resultTitle">
        <strong>${escapeHtml(it.name)}</strong>
        ${tagsHtml(it.tags)}
      </div>
      <div class="resultPath">${escapeHtml(it.path.join(" / "))}</div>
      <div class="resultUrl">${escapeHtml(it.url)}</div>
    `;
    li.addEventListener("click", () => openNode(it));
    resultList.appendChild(li);
  }
}

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
    .scaleExtent([0.3, 2.5])
    .on("zoom", (event) => g.attr("transform", event.transform));

  svg.call(zoom);

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
}

async function init(){
  const res = await fetch(DATA_URL);
  const data = await res.json();

  const items = flatten(data);

  // Search interactions
  const onSearch = () => renderResults(items, searchInput.value || "");
  searchInput.addEventListener("input", onSearch);
  btnClear.addEventListener("click", () => { searchInput.value = ""; onSearch(); searchInput.focus(); });

  // Build tree
  buildTree(data);

  // First render
  onSearch();
}

init().catch(err => {
  console.error(err);
  resultMeta.textContent = "加载 tarf.json 失败，请检查本地服务/路径。";
});
