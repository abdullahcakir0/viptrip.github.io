import os
import re
import shutil

cwd = "/Users/abdullahcakir/Desktop/viptrip"

# 1. Copy Favicon
src_favicon = "/Users/abdullahcakir/.gemini/antigravity/brain/42ee8c64-c234-4316-8c13-cede42acc644/favicon_1787686328971.png"
dst_favicon = os.path.join(cwd, "assets/img/favicon.png")
if os.path.exists(src_favicon):
    shutil.copy(src_favicon, dst_favicon)
    print("Copied favicon.")

# 2. Add New Blogs to create_blog_index.py
index_py_path = os.path.join(cwd, "create_blog_index.py")
new_blogs = [
    '{"slug": "blog-vip-gelin-arabasi-kiralama", "title": "VIP Gelin Arabası Kiralama: Özel Gününüzde Zirve Konfor", "desc": "Hayatınızın en mutlu gününde sıradanlığın dışına çıkın. VIP gelin arabası kiralama hizmetinin benzersiz avantajları ve detayları."},',
    '{"slug": "blog-ankara-vip-transfer-farklari", "title": "Ankara VIP Transfer ile Standart Ulaşım Arasındaki Farklar", "desc": "Ankara VIP transfer hizmetinin özellikleri, iş seyahatlerindeki yeri ve neden gitgide daha çok tercih edildiği hakkında detaylar."},',
    '{"slug": "blog-ankara-transfer-rehberi-2026", "title": "Ankara Transfer Rehberi 2026: En Çok Tercih Edilen Rotalar", "desc": "Esenboğa, Çankaya, İncek ve daha fazlası... Ankara içi transferlerde popüler rotalar ve ulaşım tüyoları."}'
]

with open(index_py_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before closing bracket of blogs list
if "blog-vip-gelin-arabasi-kiralama" not in content:
    content = content.replace("]\n\n# Create HTML content", f"    {new_blogs[0]}\n    {new_blogs[1]}\n    {new_blogs[2]}\n]\n\n# Create HTML content")
    with open(index_py_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated create_blog_index.py with new blogs.")

# 3. Create the 3 Blog HTML files
template_path = os.path.join(cwd, "blog-sehirlerarasi-transferde-vip.html")
with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

blogs_data = [
    {
        "slug": "blog-vip-gelin-arabasi-kiralama.html",
        "title": "VIP Gelin Arabası Kiralama: Özel Gününüzde Zirve Konfor | VipTrip Ankara",
        "desc": "Hayatınızın en mutlu gününde sıradanlığın dışına çıkın. VIP gelin arabası kiralama hizmetinin benzersiz avantajları.",
        "h1": "VIP Gelin Arabası Kiralama: Özel Gününüzde Zirve Konfor",
        "category": "Gelin Arabası",
        "date": "2026-08-25"
    },
    {
        "slug": "blog-ankara-vip-transfer-farklari.html",
        "title": "Ankara VIP Transfer ile Standart Ulaşım Arasındaki Farklar | VipTrip",
        "desc": "Ankara VIP transfer hizmetinin özellikleri, iş seyahatlerindeki yeri ve neden gitgide daha çok tercih edildiği.",
        "h1": "Ankara VIP Transfer ile Standart Ulaşım Arasındaki Farklar",
        "category": "VIP Transfer",
        "date": "2026-08-25"
    },
    {
        "slug": "blog-ankara-transfer-rehberi-2026.html",
        "title": "Ankara Transfer Rehberi 2026: Popüler Rotalar | VipTrip",
        "desc": "Esenboğa, Çankaya, İncek ve daha fazlası... Ankara içi transferlerde popüler rotalar ve ulaşım tüyoları.",
        "h1": "Ankara Transfer Rehberi 2026: En Çok Tercih Edilen Rotalar",
        "category": "Rehber",
        "date": "2026-08-25"
    }
]

for bd in blogs_data:
    new_html = template_content
    # Simple regex replacements
    new_html = re.sub(r'<title>.*?</title>', f'<title>{bd["title"]}</title>', new_html)
    new_html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{bd["desc"]}">', new_html)
    new_html = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://viptrip.com.tr/{bd["slug"].replace(".html", "")}">', new_html)
    new_html = re.sub(r'<h1>.*?</h1>', f'<h1>{bd["h1"]}</h1>', new_html)
    new_html = re.sub(r'<span class="blog-category">.*?</span>', f'<span class="blog-category">{bd["category"]}</span>', new_html)
    new_html = re.sub(r'"datePublished": ".*?"', f'"datePublished": "{bd["date"]}"', new_html)
    
    with open(os.path.join(cwd, bd["slug"]), 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Created {bd['slug']}")

# 4. Update Favicon in all HTML files
html_files = [f for f in os.listdir(cwd) if f.endswith('.html')]
for file in html_files:
    filepath = os.path.join(cwd, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # Replace the existing favicon link with the new one
    new_content = re.sub(r'<link rel="icon".*?>', '<link rel="icon" type="image/png" href="assets/img/favicon.png">', file_content)
    
    if file_content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated favicon in {file}")

print("Update completed.")
