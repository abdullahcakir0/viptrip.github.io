import os
import ast

directory = "/Users/abdullahcakir/Desktop/viptrip"

# Extract the 'blogs' list from create_pages.py
with open(os.path.join(directory, "create_pages.py"), "r", encoding="utf-8") as f:
    text = f.read()

start = text.find('blogs = [')
end = text.find(']', start) + 1
blogs_str = text[start:end]
blogs = ast.literal_eval(blogs_str.split('blogs = ')[1])

for blog in blogs:
    slug = blog["slug"]
    filepath = os.path.join(directory, f"{slug}.html")
    
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()
            
        # Replace the hardcoded Anıtkabir H1 and current span
        html = html.replace("<h1>Anıtkabir Ziyareti: Protokol Yolundan Ata'nın Huzuruna</h1>", f"<h1>{blog['title']}</h1>")
        html = html.replace('<span class="current">Anıtkabir Ziyareti</span>', f'<span class="current">{blog["title"]}</span>')
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Fixed H1 for: {slug}")
    else:
        print(f"File not found: {slug}.html")

print("All H1 tags updated successfully!")
