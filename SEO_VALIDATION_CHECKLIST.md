# SEO 验证清单

## 使用此清单验证 SEO 优化的实施情况

### 📋 在线验证工具

#### 1. 结构化数据验证
- **Google Rich Results Test**: https://search.google.com/test/rich-results
  - 输入网址：`https://digidai.github.io/recruit-ai-framework/`
  - 检查是否识别到：
    - [ ] WebSite 结构化数据
    - [ ] FAQPage 结构化数据
    - [ ] BreadcrumbList 结构化数据
    - [ ] ItemList 结构化数据
    - [ ] SoftwareApplication 结构化数据

- **Schema Markup Validator**: https://validator.schema.org/
  - 验证 JSON-LD 语法
  - 检查所有结构化数据类型

#### 2. 性能验证
- **Google PageSpeed Insights**: https://pagespeed.web.dev/
  - 测试移动端性能
  - 测试桌面端性能
  - 目标：
    - [ ] Performance Score > 90
    - [ ] FCP < 1.8s
    - [ ] LCP < 2.5s
    - [ ] TTI < 3.8s

#### 3. 移动友好性测试
- **Mobile-Friendly Test**: https://search.google.com/test/mobile-friendly
  - [ ] 页面是移动友好的

#### 4. SEO 基础检查
- **Google Search Console**: https://search.google.com/search-console
  - [ ] 验证网站所有权
  - [ ] 提交 sitemap
  - [ ] 检查覆盖率
  - [ ] 检查是否有爬虫错误

#### 5. 元数据检查
打开浏览器开发者工具（F12），检查：

**Head 部分**:
```html
<!-- 检查以下标签是否存在 -->
<title>Recruitment & AI Hiring Framework - 招聘与AI招聘工具导航</title>
<meta name="description" content="..."/>
<meta name="keywords" content="..."/>
<link rel="canonical" href="..."/>
<meta property="og:title" content="..."/>
<meta property="og:description" content="..."/>
<meta name="twitter:card" content="..."/>
<link rel="manifest" href="manifest.json"/>
```

#### 6. Robots.txt 验证
- **Google Robots Testing Tool**: https://search.google.com/test/robots.txt
  - 输入：`https://digidai.github.io/recruit-ai-framework/robots.txt`
  - 检查：
    - [ ] 允许主要搜索引擎
    - [ ] Sitemap URL 正确

#### 7. Sitemap 验证
- 访问：`https://digidai.github.io/recruit-ai-framework/sitemap.xml`
  - [ ] XML 格式正确
  - [ ] 包含所有重要页面
  - [ ] lastmod 日期是最近的
  - [ ] 样式表正常加载（美观显示）

### 🔍 手动验证步骤

#### 1. 页面源代码检查
1. 打开 `https://digidai.github.io/recruit-ai-framework/`
2. 右键点击 → "查看页面源代码"
3. 搜索以下内容：
   - [ ] `<script type="application/ld+json">` - 应该找到 5 个
   - [ ] `rel="canonical"` - 应该指向正确 URL
   - [ ] `property="og:"` - 应该有多个 OG 标签
   - [ ] `name="twitter:"` - 应该有 Twitter 标签

#### 2. 浏览器开发者工具检查
1. 打开开发者工具（F12）
2. 切换到 Network 标签
3. 刷新页面
4. 检查：
   - [ ] manifest.json 已加载
   - [ ] style.css 已预加载
   - [ ] app.js 已预加载

#### 3. 结构化数据检查
1. 打开开发者工具（F12）
2. 切换到 Console 标签
3. 粘贴以下代码：
```javascript
// 检查所有 JSON-LD
const scripts = document.querySelectorAll('script[type="application/ld+json"]');
console.log(`找到 ${scripts.length} 个 JSON-LD 块`);
scripts.forEach((script, index) => {
  const data = JSON.parse(script.textContent);
  console.log(`块 ${index + 1}: ${data['@type']}`);
});
```
4. 应该输出：
   ```
   找到 5 个 JSON-LD 块
   块 1: WebSite
   块 2: ItemList
   块 3: FAQPage
   块 4: BreadcrumbList
   块 5: SoftwareApplication
   ```

#### 4. 社交媒体预览检查
使用以下工具验证社交媒体显示效果：

- **Facebook Sharing Debugger**: https://developers.facebook.com/tools/debug/
  - 输入网址并检查预览

- **Twitter Card Validator**: https://cards-dev.twitter.com/validator
  - 输入网址并检查预览

- **LinkedIn Post Inspector**: https://www.linkedin.com/post-inspector/
  - 输入网址并检查预览

#### 5. PWA 检查
1. 打开 Chrome DevTools（F12）
2. 切换到 Application 标签
3. 检查：
   - [ ] Manifest 显示正确
   - [ ] Service Worker 已注册
   - [ ] 可以添加到主屏幕

### 📊 SEO 评分

使用以下工具进行综合评分：

- **SEOptimer**: https://www.seoptimer.com/
- **WooRank**: https://www.woorank.com/
- **Ahrefs Webmaster Tools**: https://ahrefs.com/webmaster-tools/

目标分数：
- [ ] 总体 SEO 分数 > 90/100
- [ ] 技术 SEO 分数 > 90/100
- [ ] 内容分数 > 85/100

### 🎯 关键指标

#### 搜索引擎索引
- [ ] Google: `site:digidai.github.io/recruit-ai-framework`
- [ ] Bing: `site:digidai.github.io/recruit-ai-framework`
- [ ] 应该返回首页结果

#### Meta 标签检查
- [ ] Title 长度：50-60 字符 ✓
- [ ] Description 长度：150-160 字符 ✓
- [ ] Keywords 相关性 ✓

#### 性能指标
- [ ] FCP (First Contentful Paint) < 1.8s
- [ ] LCP (Largest Contentful Paint) < 2.5s
- [ ] TTI (Time to Interactive) < 3.8s
- [ ] CLS (Cumulative Layout Shift) < 0.1

### ✅ 验证完成检查表

完成所有验证后，在以下项打勾：

#### 结构化数据
- [ ] 所有 JSON-LD 块通过验证
- [ ] Google Rich Results Test 显示有效结果
- [ ] 无语法错误

#### 性能
- [ ] PageSpeed Insights 分数 > 90
- [ ] 所有 Core Web Vitals 指标达标
- [ ] 资源正确预加载

#### 技术文件
- [ ] robots.txt 可访问且正确
- [ ] sitemap.xml 可访问且正确
- [ ] manifest.json 可访问且正确
- [ ] 404.html 正确返回 404 状态

#### 元数据
- [ ] 所有 meta 标签存在且正确
- [ ] Canonical URL 正确
- [ ] Hreflang 标签正确

#### 可访问性
- [ ] ARIA landmarks 正确
- [ ] 语义化 HTML 标签
- [ ] 屏幕阅读器友好

### 📝 问题记录

记录发现的问题：

```
日期：
问题：
解决方案：
状态：
```

### 🔄 持续监控

设置定期检查：
- [ ] 每月检查 Search Console
- [ ] 每月运行 PageSpeed Insights
- [ ] 每季度审查结构化数据
- [ ] 每季度更新 sitemap

---

**验证日期**: ___________
**验证人**: ___________
**总体状态**: ⬜ 通过 / ⬜ 需要改进
