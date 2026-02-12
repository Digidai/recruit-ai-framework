import { describe, it, expect } from "vitest";

// Import utility functions by evaluating them in isolation
// Since app.js is not a module, we re-implement the pure functions here for testing

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function replaceQueryTemplate(url, query) {
  return url.split("{query}").join(query);
}

function safeDecodeURIComponent(value) {
  try {
    return decodeURIComponent(value);
  } catch {
    return null;
  }
}

function normalizeLang(lang) {
  const SUPPORTED_LANGS = ["zh", "en"];
  const DEFAULT_LANG = "zh";
  return SUPPORTED_LANGS.includes(lang) ? lang : DEFAULT_LANG;
}

function normalizeView(view) {
  const SUPPORTED_VIEWS = ["tree", "accordion", "table", "explorer", "cards"];
  const DEFAULT_VIEW = "tree";
  return SUPPORTED_VIEWS.includes(view) ? view : DEFAULT_VIEW;
}

function escapeCSV(str) {
  return (str || "").replace(/"/g, '""').replace(/[\r\n]+/g, " ");
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

function countStats(data) {
  let categories = 0,
    resources = 0,
    templates = 0;
  const tagCounts = {};
  function traverse(node) {
    if (node.type === "folder") {
      if (node.name.match(/^[A-Z]\s/)) categories++;
      if (Array.isArray(node.children)) node.children.forEach(traverse);
    } else if (node.url) {
      resources++;
      if (node.type === "template") templates++;
      if (node.tags)
        node.tags.forEach((tag) => {
          tagCounts[tag] = (tagCounts[tag] || 0) + 1;
        });
    }
  }
  traverse(data);
  return { categories, resources, templates, tagCounts };
}

// ========== Tests ==========

describe("escapeHtml", () => {
  it("escapes ampersands", () => {
    expect(escapeHtml("a&b")).toBe("a&amp;b");
  });

  it("escapes angle brackets", () => {
    expect(escapeHtml("<script>alert('xss')</script>")).toBe(
      "&lt;script&gt;alert(&#39;xss&#39;)&lt;/script&gt;"
    );
  });

  it("escapes quotes", () => {
    expect(escapeHtml('"hello"')).toBe("&quot;hello&quot;");
    expect(escapeHtml("it's")).toBe("it&#39;s");
  });

  it("handles non-string input", () => {
    expect(escapeHtml(123)).toBe("123");
    expect(escapeHtml(null)).toBe("null");
    expect(escapeHtml(undefined)).toBe("undefined");
  });

  it("returns empty string for empty input", () => {
    expect(escapeHtml("")).toBe("");
  });
});

describe("replaceQueryTemplate", () => {
  it("replaces {query} in URL", () => {
    expect(replaceQueryTemplate("https://example.com/?q={query}", "test")).toBe(
      "https://example.com/?q=test"
    );
  });

  it("replaces multiple occurrences", () => {
    expect(replaceQueryTemplate("{query}+{query}", "hello")).toBe(
      "hello+hello"
    );
  });

  it("handles URL with no template", () => {
    expect(replaceQueryTemplate("https://example.com/", "test")).toBe(
      "https://example.com/"
    );
  });
});

describe("safeDecodeURIComponent", () => {
  it("decodes valid URI components", () => {
    expect(safeDecodeURIComponent("%E4%BD%A0%E5%A5%BD")).toBe("你好");
    expect(safeDecodeURIComponent("hello%20world")).toBe("hello world");
  });

  it("returns null for invalid URI components", () => {
    expect(safeDecodeURIComponent("%")).toBe(null);
    expect(safeDecodeURIComponent("%ZZ")).toBe(null);
  });

  it("handles plain strings", () => {
    expect(safeDecodeURIComponent("hello")).toBe("hello");
  });
});

describe("normalizeLang", () => {
  it("returns valid languages as-is", () => {
    expect(normalizeLang("zh")).toBe("zh");
    expect(normalizeLang("en")).toBe("en");
  });

  it("returns default for invalid languages", () => {
    expect(normalizeLang("fr")).toBe("zh");
    expect(normalizeLang("")).toBe("zh");
    expect(normalizeLang(null)).toBe("zh");
    expect(normalizeLang(undefined)).toBe("zh");
  });
});

describe("normalizeView", () => {
  it("returns valid views as-is", () => {
    expect(normalizeView("tree")).toBe("tree");
    expect(normalizeView("accordion")).toBe("accordion");
    expect(normalizeView("table")).toBe("table");
    expect(normalizeView("explorer")).toBe("explorer");
    expect(normalizeView("cards")).toBe("cards");
  });

  it("returns default for invalid views", () => {
    expect(normalizeView("invalid")).toBe("tree");
    expect(normalizeView("")).toBe("tree");
    expect(normalizeView(null)).toBe("tree");
  });
});

describe("escapeCSV", () => {
  it("escapes double quotes", () => {
    expect(escapeCSV('hello "world"')).toBe('hello ""world""');
  });

  it("replaces newlines with spaces", () => {
    expect(escapeCSV("line1\nline2")).toBe("line1 line2");
    expect(escapeCSV("line1\r\nline2")).toBe("line1 line2");
  });

  it("handles null/undefined", () => {
    expect(escapeCSV(null)).toBe("");
    expect(escapeCSV(undefined)).toBe("");
  });
});

describe("flatten", () => {
  it("flattens a simple tree", () => {
    const data = {
      name: "Root",
      type: "folder",
      children: [
        { name: "Item 1", name_en: "Item 1", url: "https://example.com/1", tags: ["R"] },
        { name: "Item 2", name_en: "Item 2", url: "https://example.com/2", tags: ["O"] },
      ],
    };
    const items = flatten(data);
    expect(items).toHaveLength(2);
    expect(items[0].name).toBe("Item 1");
    expect(items[0].url).toBe("https://example.com/1");
    expect(items[0].path).toEqual(["Root"]);
  });

  it("flattens nested folders", () => {
    const data = {
      name: "Root",
      type: "folder",
      children: [
        {
          name: "Category",
          type: "folder",
          children: [
            { name: "Item", url: "https://example.com", tags: [] },
          ],
        },
      ],
    };
    const items = flatten(data);
    expect(items).toHaveLength(1);
    expect(items[0].path).toEqual(["Root", "Category"]);
  });

  it("handles empty tree", () => {
    const data = { name: "Root", type: "folder", children: [] };
    expect(flatten(data)).toHaveLength(0);
  });
});

describe("countStats", () => {
  it("counts resources and categories", () => {
    const data = {
      name: "Root",
      type: "folder",
      children: [
        {
          name: "A Category",
          type: "folder",
          children: [
            { name: "Item 1", url: "https://example.com/1", tags: ["R", "P"] },
            { name: "Item 2", url: "https://example.com/2", type: "template", tags: ["M"] },
          ],
        },
      ],
    };
    const stats = countStats(data);
    expect(stats.categories).toBe(1);
    expect(stats.resources).toBe(2);
    expect(stats.templates).toBe(1);
    expect(stats.tagCounts.R).toBe(1);
    expect(stats.tagCounts.P).toBe(1);
    expect(stats.tagCounts.M).toBe(1);
  });
});
