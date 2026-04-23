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
            
        # The template has:
        # <title>Anıtkabir Ziyaret Rehberi ve VIP Ulaşım - VipTrip Ankara</title>
        # <meta name="description" content="Ankara Anıtkabir ziyaret rehberi. Ziyaret saatleri, giriş kuralları ve VIP şoförlü araçla konforlu ulaşım hizmeti. Park sorunu olmadan Ata'nın huzuruna.">
        
        # We need to replace the entire title tag content
        start_title = html.find('<title>')
        end_title = html.find('</title>') + 8
        if start_title != -1:
            html = html[:start_title] + f'<title>{blog["title"]} | VipTrip Ankara</title>' + html[end_title:]
            
        # We need to replace the description meta tag
        start_desc = html.find('<meta name="description"')
        end_desc = html.find('>', start_desc) + 1
        if start_desc != -1:
            html = html[:start_desc] + f'<meta name="description" content="{blog["desc"]}">' + html[end_desc:]
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Fixed Meta for: {slug}")
    else:
        print(f"File not found: {slug}.html")

print("All Meta tags updated successfully!")
