#!/usr/bin/env python3
"""
提交 sitemap 到多个搜索引擎
支持 Google, Bing, Yandex 等主流搜索引擎
"""

import requests
import argparse
from datetime import datetime


# 搜索引擎 ping 端点
SEARCH_ENGINES = {
    'google': 'https://www.google.com/ping?sitemap={sitemap_url}',
    'bing': 'https://www.bing.com/ping?sitemap={sitemap_url}',
    'yandex': 'https://webmaster.yandex.com/ping?sitemap={sitemap_url}',
}


def submit_sitemap(sitemap_url, engines='all'):
    """
    提交 sitemap 到搜索引擎

    Args:
        sitemap_url: sitemap 的完整 URL
        engines: 要提交的搜索引擎，'all' 或逗号分隔的列表
    """
    print(f"🚀 Starting sitemap submission...")
    print(f"📄 Sitemap URL: {sitemap_url}")
    print(f"⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")

    # 确定要提交的搜索引擎
    if engines == 'all':
        target_engines = SEARCH_ENGINES.keys()
    else:
        target_engines = [e.strip().lower() for e in engines.split(',')]
        target_engines = [e for e in target_engines if e in SEARCH_ENGINES]

    results = {}

    for engine in target_engines:
        ping_url = SEARCH_ENGINES[engine].format(sitemap_url=sitemap_url)

        try:
            print(f"📡 Submitting to {engine.upper()}...")
            response = requests.get(ping_url, timeout=10)

            if response.status_code == 200:
                print(f"✅ {engine.upper()}: Success (200)")
                results[engine] = 'success'
            else:
                print(f"⚠️ {engine.upper()}: HTTP {response.status_code}")
                results[engine] = f'failed_{response.status_code}'

        except requests.exceptions.Timeout:
            print(f"⏱️ {engine.upper()}: Timeout")
            results[engine] = 'timeout'
        except Exception as e:
            print(f"❌ {engine.upper()}: Error - {str(e)}")
            results[engine] = 'error'

    # 打印总结
    print("\n" + "="*50)
    print("📊 Submission Summary:")
    print("="*50)

    success_count = sum(1 for v in results.values() if v == 'success')
    total_count = len(results)

    for engine, status in results.items():
        status_icon = "✅" if status == "success" else "❌"
        print(f"{status_icon} {engine.upper()}: {status}")

    print(f"\n🎯 Success rate: {success_count}/{total_count}")

    return results


def main():
    parser = argparse.ArgumentParser(
        description='Submit sitemap to search engines'
    )
    parser.add_argument(
        '--sitemap-url',
        default='https://digidai.github.io/recruit-ai-framework/sitemap.xml',
        help='Full URL to your sitemap.xml'
    )
    parser.add_argument(
        '--engines',
        default='all',
        help='Comma-separated list of engines (google,bing,yandex) or "all"'
    )

    args = parser.parse_args()

    submit_sitemap(args.sitemap_url, args.engines)


if __name__ == "__main__":
    main()
