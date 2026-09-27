import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"
index_path = os.path.join(cwd, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Remove the insta-info div entirely from index.html
html = re.sub(r'<div class="insta-info">.*?</div>\s*</div>\s*</a>', '</a>', html, flags=re.DOTALL)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Removed insta-info from index.html")
