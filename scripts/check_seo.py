#!/usr/bin/env python3
"""
SEO 本地验证脚本
用于检查网站的基本 SEO 配置
"""

import requests
import json
import sys
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from datetime import datetime

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

def check_url(url, description):
    """检查 URL 是否可访问"""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print_status(f"{description}: 可访问 (状态码: {response.status_code})", 'pass')
            return True, response
        else:
            print_status(f"{description}: 返回状态码 {response.status_code}", 'fail')
            return False, None
    except Exception as e:
        print_status(f"{description}: 无法访问 - {str(e)}", 'fail')
        return False, None

def check_seo_base(url):
    """检查基础 SEO 元素"""
    print(f"\n{Colors.BOLD}=== 基础 SEO 检查 ==={Colors.END}")

    success, response = check_url(url, "主页")

    if not success:
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # 检查 title
    title = soup.find('title')
    if title:
        title_text = title.get_text().strip()
        title_length = len(title_text)
        if 50 <= title_length <= 60:
            print_status(f"Title 标签存在且长度适中 ({title_length} 字符): '{title_text}'", 'pass')
        elif title_length < 50:
            print_status(f"Title 标签存在但偏短 ({title_length} 字符): '{title_text}'", 'warn')
        else:
            print_status(f"Title 标签存在但偏长 ({title_length} 字符): '{title_text}'", 'warn')
    else:
        print_status("Title 标签缺失", 'fail')

    # 检查 meta description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc and meta_desc.get('content'):
        desc_length = len(meta_desc['content'])
        if 150 <= desc_length <= 160:
            print_status(f"Meta Description 存在且长度适中 ({desc_length} 字符)", 'pass')
        else:
            print_status(f"Meta Description 存在但长度为 {desc_length} 字符", 'warn')
    else:
        print_status("Meta Description 缺失", 'fail')

    # 检查 canonical URL
    canonical = soup.find('link', attrs={'rel': 'canonical'})
    if canonical and canonical.get('href'):
        print_status(f"Canonical URL 存在: {canonical['href']}", 'pass')
    else:
        print_status("Canonical URL 缺失", 'fail')

    # 检查 robots meta
    robots_meta = soup.find('meta', attrs={'name': 'robots'})
    if robots_meta and robots_meta.get('content'):
        print_status(f"Robots meta 标签存在: {robots_meta['content']}", 'pass')
    else:
        print_status("Robots meta 标签缺失", 'warn')

    # 检查 viewport
    viewport = soup.find('meta', attrs={'name': 'viewport'})
    if viewport and viewport.get('content'):
        print_status("Viewport meta 标签存在", 'pass')
    else:
        print_status("Viewport meta 标签缺失", 'fail')

def check_structured_data(url):
    """检查结构化数据"""
    print(f"\n{Colors.BOLD}=== 结构化数据检查 ==={Colors.END}")

    success, response = check_url(url, "主页")

    if not success:
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    json_ld_scripts = soup.find_all('script', type='application/ld+json')

    if not json_ld_scripts:
        print_status("未找到 JSON-LD 结构化数据", 'fail')
        return

    print_status(f"找到 {len(json_ld_scripts)} 个 JSON-LD 块", 'pass')

    found_types = []
    for i, script in enumerate(json_ld_scripts, 1):
        try:
            data = json.loads(script.string)
            schema_type = data.get('@type', 'Unknown')
            found_types.append(schema_type)
            print_status(f"  块 {i}: {schema_type}", 'info')
        except json.JSONDecodeError:
            print_status(f"  块 {i}: JSON 解析失败", 'fail')

    expected_types = ['WebSite', 'ItemList', 'FAQPage', 'BreadcrumbList', 'SoftwareApplication']
    for expected_type in expected_types:
        if expected_type in found_types:
            print_status(f"包含 {expected_type} 结构化数据", 'pass')
        else:
            print_status(f"缺少 {expected_type} 结构化数据", 'fail')

def check_open_graph(url):
    """检查 Open Graph 标签"""
    print(f"\n{Colors.BOLD}=== Open Graph 检查 ==={Colors.END}")

    success, response = check_url(url, "主页")

    if not success:
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    og_tags = {
        'og:type': '类型',
        'og:url': 'URL',
        'og:title': '标题',
        'og:description': '描述',
        'og:site_name': '站点名称',
        'og:locale': '语言',
    }

    for tag_name, description in og_tags.items():
        tag = soup.find('meta', property=tag_name)
        if tag and tag.get('content'):
            print_status(f"OG {description} ({tag_name}): 存在", 'pass')
        else:
            print_status(f"OG {description} ({tag_name}): 缺失", 'warn')

def check_twitter_cards(url):
    """检查 Twitter Card 标签"""
    print(f"\n{Colors.BOLD}=== Twitter Card 检查 ==={Colors.END}")

    success, response = check_url(url, "主页")

    if not success:
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    twitter_tags = {
        'twitter:card': '卡片类型',
        'twitter:title': '标题',
        'twitter:description': '描述',
    }

    for tag_name, description in twitter_tags.items():
        tag = soup.find('meta', attrs={'name': tag_name})
        if tag and tag.get('content'):
            print_status(f"Twitter {description} ({tag_name}): 存在", 'pass')
        else:
            print_status(f"Twitter {description} ({tag_name}): 缺失", 'warn')

def check_technical_files(base_url):
    """检查技术文件"""
    print(f"\n{Colors.BOLD}=== 技术文件检查 ==={Colors.END}")

    parsed = urlparse(base_url)
    base = f"{parsed.scheme}://{parsed.netloc}"

    files_to_check = [
        ('/robots.txt', 'Robots.txt'),
        ('/sitemap.xml', 'Sitemap.xml'),
        ('/manifest.json', 'Web App Manifest'),
        ('/favicon.ico', 'Favicon'),
    ]

    for path, description in files_to_check:
        url = base + path
        success, response = check_url(url, description)
        if success:
            # 检查内容类型
            if response and response.headers.get('content-type'):
                content_type = response.headers['content-type']
                print_status(f"  Content-Type: {content_type}", 'info')

def check_performance(url):
    """检查性能相关"""
    print(f"\n{Colors.BOLD}=== 性能检查 ==={Colors.END}")

    success, response = check_url(url, "主页")

    if not success:
        return

    # 检查 preload
    soup = BeautifulSoup(response.text, 'html.parser')
    preloads = soup.find_all('link', rel='preload')

    if preloads:
        print_status(f"找到 {len(preloads)} 个 preload 资源", 'pass')
        for preload in preloads:
            href = preload.get('href', 'Unknown')
            as_type = preload.get('as', 'Unknown')
            print_status(f"  预加载: {href} (as: {as_type})", 'info')
    else:
        print_status("未找到 preload 资源", 'warn')

    # 检查 preconnect
    preconnects = soup.find_all('link', rel='preconnect')
    if preconnects:
        print_status(f"找到 {len(preconnects)} 个 preconnect 链接", 'pass')
    else:
        print_status("未找到 preconnect 链接", 'warn')

def main():
    # 主 URL
    base_url = "https://digidai.github.io/recruit-ai-framework/"

    print(f"{Colors.BOLD}{Colors.BLUE}")
    print("=" * 60)
    print("SEO 本地验证工具")
    print("=" * 60)
    print(f"{Colors.END}")

    print(f"{Colors.BOLD}目标网站:{Colors.END} {base_url}")
    print(f"{Colors.BOLD}检查时间:{Colors.END} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # 运行检查
    check_seo_base(base_url)
    check_structured_data(base_url)
    check_open_graph(base_url)
    check_twitter_cards(base_url)
    check_technical_files(base_url)
    check_performance(base_url)

    print(f"\n{Colors.BOLD}{Colors.BLUE}")
    print("=" * 60)
    print("检查完成！")
    print("=" * 60)
    print(f"{Colors.END}")

    print(f"\n{Colors.BOLD}下一步操作:{Colors.END}")
    print("1. 访问 https://search.google.com/test/rich-results 测试结构化数据")
    print("2. 访问 https://pagespeed.web.dev/ 测试性能")
    print("3. 访问 https://search.google.com/search-console 设置 Search Console")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}检查已取消{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n{Colors.RED}错误: {str(e)}{Colors.END}")
        sys.exit(1)
