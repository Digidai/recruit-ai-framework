#!/usr/bin/env python3
"""
SEO 本地文件验证脚本
用于检查本地 HTML 文件的 SEO 配置
"""

import json
import os
import sys
from pathlib import Path

# 颜色输出
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_status(message, status):
    if status == 'pass':
        print(f"{Colors.GREEN}✓{Colors.END} {message}")
    elif status == 'fail':
        print(f"{Colors.RED}✗{Colors.END} {message}")
    elif status == 'warn':
        print(f"{Colors.YELLOW}⚠{Colors.END} {message}")
    elif status == 'info':
        print(f"{Colors.BLUE}ℹ{Colors.END} {message}")

def check_html_file(filepath):
    """检查 HTML 文件的 SEO 元素"""
    print(f"\n{Colors.BOLD}=== 检查文件: {filepath} ==={Colors.END}")

    if not os.path.exists(filepath):
        print_status(f"文件不存在: {filepath}", 'fail')
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查基础 meta 标签
    checks = [
        ('<title>', 'Title 标签'),
        ('name="description"', 'Meta Description'),
        ('name="keywords"', 'Meta Keywords'),
        ('name="robots"', 'Robots Meta'),
        ('rel="canonical"', 'Canonical URL'),
        ('rel="manifest"', 'Web App Manifest'),
        ('property="og:title"', 'Open Graph Title'),
        ('property="og:description"', 'Open Graph Description'),
        ('name="twitter:card"', 'Twitter Card'),
        ('<script type="application/ld+json">', 'JSON-LD 结构化数据'),
        ('role="banner"', 'ARIA Banner'),
        ('role="main"', 'ARIA Main'),
        ('role="complementary"', 'ARIA Complementary'),
        ('role="contentinfo"', 'ARIA Contentinfo'),
        ('rel="preload"', 'Preload 资源'),
        ('rel="preconnect"', 'Preconnect 链接'),
        ('hreflang=', 'Hreflang 标签'),
    ]

    for pattern, description in checks:
        if pattern in content:
            print_status(f"{description}", 'pass')
        else:
            print_status(f"{description} 未找到", 'warn')

    # 检查 JSON-LD 数量
    json_ld_count = content.count('<script type="application/ld+json">')
    print_status(f"找到 {json_ld_count} 个 JSON-LD 块", 'info')

    # 验证 JSON-LD 语法
    import re
    json_ld_pattern = r'<script type="application/ld\+json">(.*?)</script>'
    json_ld_blocks = re.findall(json_ld_pattern, content, re.DOTALL)

    valid_count = 0
    for i, block in enumerate(json_ld_blocks, 1):
        try:
            data = json.loads(block)
            schema_type = data.get('@type', 'Unknown')
            print_status(f"  JSON-LD 块 {i}: {schema_type} (有效)", 'pass')
            valid_count += 1
        except json.JSONDecodeError as e:
            print_status(f"  JSON-LD 块 {i}: JSON 解析失败 - {str(e)[:50]}", 'fail')

    print_status(f"有效的 JSON-LD: {valid_count}/{len(json_ld_blocks)}", 'info')

def check_file_exists(filepath, description):
    """检查文件是否存在"""
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        print_status(f"{description} 存在 ({size} bytes)", 'pass')
        return True
    else:
        print_status(f"{description} 不存在", 'fail')
        return False

def main():
    # 项目路径
    docs_dir = Path(__file__).parent.parent / "docs"

    print(f"{Colors.BOLD}{Colors.BLUE}")
    print("=" * 60)
    print("SEO 本地文件验证工具")
    print("=" * 60)
    print(f"{Colors.END}")

    print(f"{Colors.BOLD}项目路径:{Colors.END} {docs_dir}")

    # 检查主要文件
    print(f"\n{Colors.BOLD}=== 检查必需文件 ==={Colors.END}")
    check_file_exists(docs_dir / "index.html", "index.html")
    check_file_exists(docs_dir / "404.html", "404.html")
    check_file_exists(docs_dir / "robots.txt", "robots.txt")
    check_file_exists(docs_dir / "sitemap.xml", "sitemap.xml")
    check_file_exists(docs_dir / "manifest.json", "manifest.json")
    check_file_exists(docs_dir / "sitemap.xsl", "sitemap.xsl")

    # 检查 index.html 的 SEO
    check_html_file(docs_dir / "index.html")

    # 检查 404.html
    print(f"\n{Colors.BOLD}=== 检查 404.html ==={Colors.END}")
    filepath_404 = docs_dir / "404.html"
    if os.path.exists(filepath_404):
        with open(filepath_404, 'r', encoding='utf-8') as f:
            content_404 = f.read()

        if 'name="robots" content="noindex' in content_404:
            print_status("404 页面包含 noindex 标签", 'pass')
        else:
            print_status("404 页面缺少 noindex 标签", 'warn')

        if 'rel="canonical"' in content_404:
            print_status("404 页面包含 canonical URL", 'pass')
        else:
            print_status("404 页面缺少 canonical URL", 'warn')

    print(f"\n{Colors.BOLD}{Colors.BLUE}")
    print("=" * 60)
    print("本地检查完成！")
    print("=" * 60)
    print(f"{Colors.END}")

    print(f"\n{Colors.BOLD}下一步操作:{Colors.END}")
    print("1. 运行 python scripts/check_seo.py 进行在线检查")
    print("2. 访问 https://search.google.com/test/rich-results 测试结构化数据")
    print("3. 访问 https://pagespeed.web.dev/ 测试性能")
    print("4. 参考 SEO_VALIDATION_CHECKLIST.md 进行完整验证")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}检查已取消{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n{Colors.RED}错误: {str(e)}{Colors.END}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
