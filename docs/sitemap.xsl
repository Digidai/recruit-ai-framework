<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
                xmlns:html="http://www.w3.org/TR/REC-html40"
                xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" indent="yes"/>

  <xsl:template match="/">
    <html lang="zh-CN">
      <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title>站点地图 - Recruitment & AI Hiring Framework</title>
        <meta name="description" content="Recruitment & AI Hiring Framework 的 XML 站点地图"/>
        <style type="text/css">
          body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background: #0b0c10;
            color: #e6e6e6;
          }
          .container {
            max-width: 1200px;
            margin: 0 auto;
          }
          h1 {
            color: #78b7ff;
            border-bottom: 2px solid #2a2f3a;
            padding-bottom: 10px;
          }
          .intro {
            background: #1f2937;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            border-left: 4px solid #78b7ff;
          }
          table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background: #1f2937;
            border-radius: 8px;
            overflow: hidden;
          }
          th {
            background: #2a2f3a;
            color: #78b7ff;
            text-align: left;
            padding: 12px;
            font-weight: 600;
          }
          td {
            padding: 12px;
            border-bottom: 1px solid #2a2f3a;
          }
          tr:hover {
            background: #374151;
          }
          a {
            color: #78b7ff;
            text-decoration: none;
          }
          a:hover {
            text-decoration: underline;
          }
          .priority-high {
            color: #10b981;
            font-weight: 600;
          }
          .priority-medium {
            color: #f59e0b;
          }
          .priority-low {
            color: #ef4444;
          }
          .stats {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
          }
          .stat-box {
            background: #1f2937;
            padding: 15px;
            border-radius: 8px;
            flex: 1;
            text-align: center;
          }
          .stat-number {
            font-size: 32px;
            font-weight: bold;
            color: #78b7ff;
          }
          .stat-label {
            color: #a7a7a7;
            margin-top: 5px;
          }
          @media (max-width: 768px) {
            table {
              font-size: 14px;
            }
            .stats {
              flex-direction: column;
            }
          }
        </style>
      </head>
      <body>
        <div class="container">
          <h1>🗺️ 站点地图 - Sitemap</h1>

          <div class="intro">
            <p><strong>Recruitment & AI Hiring Framework</strong></p>
            <p>这是本网站的 XML 站点地图，包含所有需要被搜索引擎索引的页面。</p>
          </div>

          <div class="stats">
            <div class="stat-box">
              <div class="stat-number">
                <xsl:value-of select="count(//sitemap:url)"/>
              </div>
              <div class="stat-label">总页面数</div>
            </div>
            <div class="stat-box">
              <div class="stat-number">
                <xsl:value-of select="count(//sitemap:url[sitemap:priority &gt; 0.8])"/>
              </div>
              <div class="stat-label">高优先级页面</div>
            </div>
          </div>

          <table>
            <thead>
              <tr>
                <th>URL</th>
                <th>最后修改时间</th>
                <th>更新频率</th>
                <th>优先级</th>
              </tr>
            </thead>
            <tbody>
              <xsl:for-each select="//sitemap:url">
                <xsl:sort select="sitemap:priority" order="descending"/>
                <tr>
                  <td>
                    <a>
                      <xsl:attribute name="href">
                        <xsl:value-of select="sitemap:loc"/>
                      </xsl:attribute>
                      <xsl:value-of select="sitemap:loc"/>
                    </a>
                  </td>
                  <td>
                    <xsl:value-of select="sitemap:lastmod"/>
                  </td>
                  <td>
                    <xsl:choose>
                      <xsl:when test="sitemap:changefreq = 'always'">
                        <span style="color: #10b981;">总是</span>
                      </xsl:when>
                      <xsl:when test="sitemap:changefreq = 'hourly'">
                        <span style="color: #10b981;">每小时</span>
                      </xsl:when>
                      <xsl:when test="sitemap:changefreq = 'daily'">
                        <span style="color: #10b981;">每天</span>
                      </xsl:when>
                      <xsl:when test="sitemap:changefreq = 'weekly'">
                        <span style="color: #f59e0b;">每周</span>
                      </xsl:when>
                      <xsl:when test="sitemap:changefreq = 'monthly'">
                        <span style="color: #f59e0b;">每月</span>
                      </xsl:when>
                      <xsl:when test="sitemap:changefreq = 'yearly'">
                        <span style="color: #ef4444;">每年</span>
                      </xsl:when>
                      <xsl:otherwise>
                        <xsl:value-of select="sitemap:changefreq"/>
                      </xsl:otherwise>
                    </xsl:choose>
                  </td>
                  <td>
                    <xsl:attribute name="class">
                      <xsl:choose>
                        <xsl:when test="sitemap:priority &gt; 0.7">priority-high</xsl:when>
                        <xsl:when test="sitemap:priority &gt; 0.4">priority-medium</xsl:when>
                        <xsl:otherwise>priority-low</xsl:otherwise>
                      </xsl:choose>
                    </xsl:attribute>
                    <xsl:value-of select="sitemap:priority"/>
                  </td>
                </tr>
              </xsl:for-each>
            </tbody>
          </table>

          <div style="margin-top: 30px; padding: 15px; background: #1f2937; border-radius: 8px;">
            <p style="margin: 0; color: #a7a7a7;">
              <strong>提示：</strong>此站点地图旨在帮助搜索引擎更好地索引网站内容。
              <a href="https://recruit.genedai.me/">返回首页</a>
            </p>
          </div>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
