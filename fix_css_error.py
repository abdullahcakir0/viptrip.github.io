import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"
style_path = os.path.join(cwd, "style.css")

with open(style_path, "r", encoding="utf-8") as f:
    css = f.read()

# Fix the dangling comma and missing block
broken_css = """/* --- FİLO & BLOG ORTAK --- */
.fleet-section,
.blog-section,"""

fixed_css = """/* --- FİLO & BLOG ORTAK --- */
.fleet-section,
.blog-section {
    background-color: #0a0a0a;
    padding: 100px 50px;
}"""

css = css.replace(broken_css, fixed_css)

with open(style_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed CSS syntax error.")
