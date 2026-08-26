import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"

# 1. Clean HTML files
html_files = [f for f in os.listdir(cwd) if f.endswith('.html')]

for file in html_files:
    filepath = os.path.join(cwd, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remove modals.js script tag
    content = content.replace('<script src="modals.js"></script>\n', '')
    content = content.replace('<script src="modals.js"></script>', '')
    
    # Remove PROMO MODAL
    content = re.sub(r'<!-- AVANTAJLI PAKET PROMO MODAL -->[\s\S]*?</div>\n</div>\n', '', content)
    # Just in case the trailing newline is different
    content = re.sub(r'<!-- AVANTAJLI PAKET PROMO MODAL -->[\s\S]*?</div>\s*</div>', '', content)
    
    # Remove ERKEN REZERVASYON MODAL and Float Button
    content = re.sub(r'<!-- Erken Rezervasyon Float Button -->[\s\S]*?</form>\s*</div>\s*</div>', '', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content.strip() + '\n')
        print(f"Cleaned {file}")

# 2. Clean style.css
css_path = os.path.join(cwd, "style.css")
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

idx = css_content.find("/* =========================================\n   ERKEN REZERVASYON MODAL (GELİN ARABASI)")
if idx != -1:
    css_content = css_content[:idx].strip() + '\n'
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Cleaned style.css")

# 3. Delete modals.js
modals_path = os.path.join(cwd, "modals.js")
if os.path.exists(modals_path):
    os.remove(modals_path)
    print("Deleted modals.js")

print("Popups removed successfully.")
