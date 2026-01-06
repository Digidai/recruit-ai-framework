#!/usr/bin/env python3
"""
自动生成和更新 sitemap.xml
根据 tarf.json 中的资源自动生成完整的 sitemap
"""

import json
import os
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET
from xml.dom import minidom

# 配置
BASE_URL = "https://digidai.github.io/recruit-ai-framework"
# 获取项目根目录
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
DOCS_DIR = PROJECT_ROOT / "docs"
TARF_FILE = DOCS_DIR / "tarf.json"
SITEMAP_FILE = DOCS_DIR / "sitemap.xml"
SITEMAP_XSL = "https://digidai.github.io/recruit-ai-framework/sitemap.xsl"


def load_resources():
    """加载 tarf.json 中的所有资源"""
    try:
        with open(TARF_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error loading tarf.json: {e}")
        return {}


def extract_all_urls(data, path=''):
    """递归提取所有 URL 资源"""
    urls = []

    # 添加根页面
    urls.append({
        'name': data.get('name', ''),
        'url': f"{BASE_URL}/",
        'priority': 1.0
    })

    def traverse(node, depth=0):
        """递归遍历节点"""
        if node.get('type') == 'url':
            # 这是一个 URL 资源
            url = node.get('url', '')
            if url and not url.startswith(BASE_URL):
                # 如果是外部链接，创建一个内部资源页面
                resource_id = f"res-{len(urls)}"
                urls.append({
                    'name': node.get('name', ''),
                    'name_en': node.get('name_en', ''),
                    'url': f"{BASE_URL}/?resource={resource_id}",
                    'priority': max(0.6, 1.0 - depth * 0.1)
                })

        # 递归处理子节点
        for child in node.get('children', []):
            traverse(child, depth + 1)

    traverse(data)
    return urls


def create_url_element(url, lastmod, changefreq, priority):
    """创建一个 URL 元素"""
    url_elem = ET.Element('url')

    loc = ET.SubElement(url_elem, 'loc')
    loc.text = url

    lastmod_elem = ET.SubElement(url_elem, 'lastmod')
    lastmod_elem.text = lastmod

    changefreq_elem = ET.SubElement(url_elem, 'changefreq')
    changefreq_elem.text = changefreq

    priority_elem = ET.SubElement(url_elem, 'priority')
    priority_elem.text = str(priority)

    return url_elem


def generate_sitemap():
    """生成完整的 sitemap"""
    # 创建根元素
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    urlset.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    urlset.set('xsi:schemaLocation',
                'http://www.sitemaps.org/schemas/sitemap/0.9 '
                'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd')

    # 获取当前日期
    today = datetime.now().strftime('%Y-%m-%d')

    # 1. 添加主页（已经在 extract_all_urls 中添加，但为了确保优先级，再次添加）
    urlset.append(create_url_element(
        f"{BASE_URL}/",
        today,
        'weekly',
        1.0
    ))

    urlset.append(create_url_element(
        f"{BASE_URL}/index.html",
        today,
        'weekly',
        1.0
    ))

    # 2. 加载并添加所有资源页面
    data = load_resources()
    urls = extract_all_urls(data)

    # 过滤掉根主页（因为已经添加过了）
    urls = [u for u in urls if not u['url'] == f"{BASE_URL}/"]

    print(f"Found {len(urls)} resource URLs")

    for url_data in urls:
        urlset.append(create_url_element(
            url_data['url'],
            today,
            'monthly',
            url_data.get('priority', 0.8)
        ))

    # 3. 添加其他静态页面
    static_pages = [
        ('404.html', 0.3, 'monthly'),
        ('manifest.json', 0.3, 'monthly'),
    ]

    for page, priority, changefreq in static_pages:
        urlset.append(create_url_element(
            f"{BASE_URL}/{page}",
            today,
            changefreq,
            priority
        ))

    # 生成 XML 字符串
    xml_str = minidom.parseString(ET.tostring(urlset)).toprettyxml(indent="  ")

    # 添加 XSL 样式表
    xml_lines = xml_str.split('\n')
    xml_lines.insert(1, f'<?xml-stylesheet type="text/xsl" href="{SITEMAP_XSL}"?>')
    xml_str = '\n'.join(xml_lines)

    return xml_str


def main():
    """主函数"""
    print("🚀 Starting sitemap generation...")

    # 生成 sitemap
    sitemap_content = generate_sitemap()

    # 写入文件
    with open(SITEMAP_FILE, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    print(f"✅ Sitemap generated successfully: {SITEMAP_FILE}")
    print(f"📊 Total URLs in sitemap: {sitemap_content.count('<url>')}")


if __name__ == "__main__":
    main()
