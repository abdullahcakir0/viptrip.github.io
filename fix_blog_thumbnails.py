import os
import re

directory = "/Users/abdullahcakir/Desktop/viptrip"
filepath = os.path.join(directory, "blog.html")

image_map = {
    "blog-ankarada-soforlu-arac-kiralama-rehberi": "assets/img/vito-dis-on.jpg",
    "blog-vip-transfer-ve-taksi-farklari": "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?q=80&w=1200&auto=format&fit=crop",
    "blog-protokol-tasimaciligi-kurallari": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=1200&auto=format&fit=crop",
    "blog-esenboga-havalimani-vip-karsilama": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?q=80&w=1200&auto=format&fit=crop",
    "blog-ankaradan-kapadokyaya-vip-ulasim": "https://images.unsplash.com/photo-1604085461230-07e0344d2d46?q=80&w=1200&auto=format&fit=crop",
    "blog-gelin-arabasi-secerken-vip-arac": "assets/img/gelin-arabasi-hero.png",
    "blog-is-seyahatleri-mercedes-vito": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=1200&auto=format&fit=crop",
    "blog-ankara-kis-turizmi-transfer": "https://images.unsplash.com/photo-1478265409131-1f65c88f965c?q=80&w=1200&auto=format&fit=crop",
    "blog-yabanci-misafirler-icin-karsilama": "https://images.unsplash.com/photo-1521791136064-7986c2920216?q=80&w=1200&auto=format&fit=crop",
    "blog-mercedes-s-class-makam-araci": "assets/img/sclass.jpeg",
    "blog-guvenli-transfer-hijyen": "https://images.unsplash.com/photo-1584483766114-2cea6facdf57?q=80&w=1200&auto=format&fit=crop",
    "blog-ankara-sehir-ici-rotalar": "assets/img/atakule.jpg",
    "blog-sehirlerarasi-transferde-vip": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=1200&auto=format&fit=crop",
    "blog-buyukelcilik-arac-kiralama": "https://images.unsplash.com/photo-1525186402429-b4ff38a3014f?q=80&w=1200&auto=format&fit=crop",
    "blog-bolu-abant-tatili-ulasim": "https://images.unsplash.com/photo-1542224566-6e85f2e6772f?q=80&w=1200&auto=format&fit=crop",
    "blog-ankarada-luks-otel-transferleri": "https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=1200&auto=format&fit=crop",
    "blog-vip-araclarda-hangi-donanimlar-var": "assets/img/vito-ic-yildizli.jpg",
    "blog-kurumsal-transfer-anlasmasi": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=1200&auto=format&fit=crop",
    "blog-ankara-vip-aracla-gezilecek-yerler": "assets/img/atakule.jpg",
    "blog-havalimani-transfer-erken-rezervasyon": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?q=80&w=1200&auto=format&fit=crop"
}

if os.path.exists(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
        
    for slug, img_url in image_map.items():
        # Match href="slug" ... <img src="old_src"
        pattern = r'(href="' + re.escape(slug) + r'"[^>]*>.*?<img\s+src=")[^"]+(")'
        # Replace the src content with the new img_url
        html = re.sub(pattern, r'\g<1>' + img_url + r'\g<2>', html, flags=re.DOTALL)
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated blog.html thumbnails.")
else:
    print("blog.html not found.")
