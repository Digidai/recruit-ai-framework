#!/usr/bin/env python3
"""
Fix data quality issues in tarf.json:
1. Add missing 'type' field to nodes
2. Remove duplicate URLs
"""

import json
import re

def fix_missing_type(node, path=''):
    """Add missing type field based on node structure."""
    current_path = path + '/' + node.get('name', '') if path else node.get('name', '')

    if 'type' not in node:
        # Determine type based on structure
        if 'children' in node:
            node['type'] = 'folder'
            print(f"Fixed: Added type='folder' to {node.get('name', 'unknown')[:50]}")
        elif 'url' in node:
            url = node.get('url', '')
            if '{query}' in url:
                node['type'] = 'template'
            else:
                node['type'] = 'url'
            print(f"Fixed: Added type='{node['type']}' to {node.get('name', 'unknown')[:50]}")

    # Recurse
    for child in node.get('children', []):
        fix_missing_type(child, current_path)


def remove_duplicate_urls(node, seen_urls=None, parent=None, is_root=False):
    """Remove duplicate URLs, keeping the first occurrence."""
    if seen_urls is None:
        seen_urls = {}

    url = node.get('url')
    if url and url in seen_urls:
        # This is a duplicate
        return True  # Mark for removal
    elif url:
        seen_urls[url] = node.get('name', 'unknown')

    # Process children and remove duplicates
    if 'children' in node:
        children_to_keep = []
        for child in node['children']:
            should_remove = remove_duplicate_urls(child, seen_urls, node)
            if not should_remove:
                children_to_keep.append(child)
            else:
                print(f"Removed duplicate: {child.get('name', 'unknown')[:50]} (URL: {child.get('url', '')[:50]})")
        node['children'] = children_to_keep

    return False  # Don't remove this node


def add_missing_name_en(node):
    """Add name_en if missing by using the name field."""
    if not node.get('name_en') and node.get('name'):
        # Try to extract English part from name
        name = node.get('name', '')
        # If name contains both Chinese and English, try to extract English
        # Pattern: Chinese（English）or Chinese (English)
        match = re.search(r'[（(]([^）)]+)[）)]', name)
        if match:
            english_part = match.group(1)
            # Check if it's actually English (no Chinese characters)
            if not re.search(r'[\u4e00-\u9fff]', english_part):
                node['name_en'] = name  # Keep the full name for now

    for child in node.get('children', []):
        add_missing_name_en(child)


def main():
    print("Loading tarf.json...")
    with open('docs/tarf.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("\n" + "="*60)
    print("Step 1: Fixing missing 'type' fields...")
    print("="*60)
    fix_missing_type(data)

    print("\n" + "="*60)
    print("Step 2: Removing duplicate URLs...")
    print("="*60)
    remove_duplicate_urls(data, is_root=True)

    print("\n" + "="*60)
    print("Step 3: Adding missing name_en fields...")
    print("="*60)
    add_missing_name_en(data)

    print("\nSaving fixed data...")
    with open('docs/tarf.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\n" + "="*60)
    print("Data quality fixes complete!")
    print("="*60)


if __name__ == "__main__":
    main()
