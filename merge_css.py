import os
import glob

directory = "/Users/abdullahcakir/Desktop/viptrip"

style_css_path = os.path.join(directory, "style.css")
blog_css_path = os.path.join(directory, "blog.css")

# 1. Read both CSS files
with open(style_css_path, "r", encoding="utf-8") as f:
    style_content = f.read()

with open(blog_css_path, "r", encoding="utf-8") as f:
    blog_content = f.read()

# 2. Add Hardware Acceleration to fix blurry menu
# Find the exact class and add the properties
blog_content = blog_content.replace(
    ".blog-header .header-nav {",
    ".blog-header .header-nav {\n        -webkit-font-smoothing: antialiased;\n        -moz-osx-font-smoothing: grayscale;\n        transform: translateZ(0);\n        will-change: transform;"
)

# 3. Create the new merged CSS content
merged_css = f"""/* 
=========================================================
   VIPTRIP MAIN STYLESHEET (UNIFIED & GROUPED)
=========================================================
   1. CORE & RESET
   2. TYPOGRAPHY & BUTTONS
   3. LAYOUT & HERO
   4. SECTIONS (SERVICES, FLEET, CONTACT)
   5. BLOG & SUB-PAGES (Geo Pages, Articles)
=========================================================
*/

{style_content}

/* 
=========================================================
   5. BLOG & SUB-PAGES (Grouped Components)
=========================================================
*/
{blog_content}
"""

# Write the merged CSS back to style.css
with open(style_css_path, "w", encoding="utf-8") as f:
    f.write(merged_css)
print("CSS files merged successfully into style.css")

# 4. Remove blog.css link from all HTML files
html_files = glob.glob(os.path.join(directory, "*.html"))
for html_file in html_files:
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if blog.css is in the file
    if "blog.css" in content:
        # Remove the line containing blog.css
        lines = content.split('\n')
        new_lines = [line for line in lines if '<link rel="stylesheet" href="blog.css">' not in line]
        new_content = '\n'.join(new_lines)
        
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Removed blog.css link from {os.path.basename(html_file)}")

# 5. Delete blog.css
if os.path.exists(blog_css_path):
    os.remove(blog_css_path)
    print("Deleted blog.css")
