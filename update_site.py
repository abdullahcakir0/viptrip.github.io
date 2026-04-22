import os
import re

directory = "/Users/abdullahcakir/Desktop/viptrip"

# Regex for internal HTML links
# Matches href="page.html" or href="page.html#anchor" or href="./page.html"
link_pattern = re.compile(r'href=["\'](?!http|https|mailto|tel|javascript)([^"\'#]+)\.html(#.*)?["\']')

def replace_link(match):
    page = match.group(1)
    fragment = match.group(2) if match.group(2) else ""
    if page == "index":
        return f'href="/{fragment}"'
    return f'href="{page}{fragment}"'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update blog header if present
    if 'class="header-nav"' in content and '<a href="vip-gelin-arabasi.html">Gelin Arabası</a>' in content:
        content = content.replace(
            '<a href="vip-gelin-arabasi.html">Gelin Arabası</a>',
            '<a href="vip-gelin-arabasi.html">Gelin Arabası</a>\n            <a href="ankara-bolu-transfer.html">Bölgeler</a>\n            <a href="blog.html">Blog</a>'
        )

    # Replace .html in internal links
    new_content = link_pattern.sub(replace_link, content)
    
    # Also replace in window.location or similar in script.js if any, but script.js might be processed separately

    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            print(f"Updated: {filepath}")

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if filename.endswith(".html") or filename == "sitemap.xml":
        process_file(filepath)
    elif filename == "script.js":
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = re.sub(r'["\'](?!http|https)([a-zA-Z0-9_-]+)\.html["\']', r'"\1"', content)
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                print(f"Updated: {filepath}")

print("Done.")
