import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { describe, expect, it } from "vitest";

function extractFunction(source, name) {
  const signature = new RegExp(`function\\s+${name}\\s*\\(`);
  const match = signature.exec(source);
  if (!match) {
    throw new Error(`Function not found in app.js: ${name}`);
  }

  const start = match.index;
  const bodyStart = source.indexOf("{", match.index);
  if (bodyStart < 0) {
    throw new Error(`Function body not found in app.js: ${name}`);
  }

  let depth = 0;
  let end = -1;
  for (let i = bodyStart; i < source.length; i++) {
    const ch = source[i];
    if (ch === "{") depth += 1;
    if (ch === "}") depth -= 1;
    if (depth === 0) {
      end = i + 1;
      break;
    }
  }

  if (end < 0) {
    throw new Error(`Unclosed function in app.js: ${name}`);
  }

  return source.slice(start, end);
}

function loadFunction(source, name) {
  return new Function(`${extractFunction(source, name)}; return ${name};`)();
}

function extractConst(source, name) {
  const pattern = new RegExp(`const\\s+${name}\\s*=\\s*[^;]+;`);
  const match = pattern.exec(source);
  if (!match) {
    throw new Error(`Constant not found in app.js: ${name}`);
  }
  return match[0];
}

function loadFunctionWithConsts(source, name, constNames) {
  const constCode = constNames.map((constName) => extractConst(source, constName)).join("\n");
  return new Function(`${constCode}\n${extractFunction(source, name)}; return ${name};`)();
}

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const appPath = path.resolve(__dirname, "../docs/app.js");
const appSource = fs.readFileSync(appPath, "utf8");

const escapeHtml = loadFunction(appSource, "escapeHtml");
const replaceQueryTemplate = loadFunction(appSource, "replaceQueryTemplate");
const safeDecodeURIComponent = loadFunction(appSource, "safeDecodeURIComponent");
const normalizeLang = loadFunctionWithConsts(appSource, "normalizeLang", ["SUPPORTED_LANGS", "DEFAULT_LANG"]);
const normalizeView = loadFunctionWithConsts(appSource, "normalizeView", ["SUPPORTED_VIEWS", "DEFAULT_VIEW"]);
const escapeCSV = loadFunction(appSource, "escapeCSV");
const flatten = loadFunction(appSource, "flatten");
const countStats = loadFunction(appSource, "countStats");

describe("escapeHtml", () => {
  it("escapes ampersands", () => {
    expect(escapeHtml("a&b")).toBe("a&amp;b");
  });

  it("escapes angle brackets", () => {
    expect(escapeHtml("<script>alert('xss')</script>")).toBe("&lt;script&gt;alert(&#39;xss&#39;)&lt;/script&gt;");
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
    expect(replaceQueryTemplate("https://example.com/?q={query}", "test")).toBe("https://example.com/?q=test");
  });

  it("replaces multiple occurrences", () => {
    expect(replaceQueryTemplate("{query}+{query}", "hello")).toBe("hello+hello");
  });

  it("handles URL with no template", () => {
    expect(replaceQueryTemplate("https://example.com/", "test")).toBe("https://example.com/");
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
        {
          name: "Item 1",
          name_en: "Item 1",
          url: "https://example.com/1",
          tags: ["R"],
        },
        {
          name: "Item 2",
          name_en: "Item 2",
          url: "https://example.com/2",
          tags: ["O"],
        },
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
          children: [{ name: "Item", url: "https://example.com", tags: [] }],
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
            {
              name: "Item 2",
              url: "https://example.com/2",
              type: "template",
              tags: ["M"],
            },
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
