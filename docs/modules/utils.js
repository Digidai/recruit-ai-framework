// ========== Utilities ==========

export function debounce(fn, delay) {
  let timer = null;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

export function safeDecodeURIComponent(value) {
  try {
    return decodeURIComponent(value);
  } catch {
    return null;
  }
}

export function escapeHtml(str) {
  return String(str).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;");
}

export function tagHtml(tag) {
  return `<span class="tag">${escapeHtml(tag)}</span>`;
}

export function tagsHtml(tags) {
  if (!tags || !tags.length) return "";
  return tags.map(tagHtml).join("");
}

export function replaceQueryTemplate(url, query) {
  return url.split("{query}").join(query);
}

export function escapeCSV(str) {
  return (str || "").replace(/"/g, '""').replace(/[\r\n]+/g, ' ');
}

export function downloadFile(content, filename, type) {
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

// ========== Data Utilities ==========

export function flatten(node, path = [], pathEn = []) {
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

export function countStats(data) {
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

export function countChildren(node) {
  let count = 0;
  if (node.url) return 1;
  if (node.children) {
    for (const child of node.children) count += countChildren(child);
  }
  return count;
}

// ========== Display Helpers ==========
import { currentLang, t } from "./i18n.js";

export function getLocalizedName(node) {
  return (currentLang === "en" && node.name_en) ? node.name_en : node.name;
}

export function getDisplayName(item) {
  return currentLang === "en" ? (item.name_en || item.name) : item.name;
}

export function getDisplayPath(item) {
  return currentLang === "en" ? (item.path_en || item.path) : item.path;
}

export function openNode(node) {
  const nodeType = node.type || node.data?.type;
  const url = node.url || node.data?.url;
  if (!url) return;
  if (nodeType === "template") {
    const q = prompt(t("promptQuery"));
    if (!q) return;
    const finalUrl = replaceQueryTemplate(url, encodeURIComponent(q.trim()));
    window.open(finalUrl, "_blank", "noopener");
  } else {
    window.open(url, "_blank", "noopener");
  }
}

// ========== Accessibility ==========
export function announce(message) {
  const ariaLive = document.getElementById("ariaLive");
  if (!ariaLive) return;
  ariaLive.textContent = "";
  setTimeout(() => { ariaLive.textContent = message; }, 100);
}
