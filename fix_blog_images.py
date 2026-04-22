import os
import re

directory = "/Users/abdullahcakir/Desktop/viptrip"

# Dictionary mapping slug to (image_url, alt_text)
image_map = {
    "blog-ankarada-soforlu-arac-kiralama-rehberi": ("assets/img/vito-dis-on.jpg", "Ankara Şoförlü Araç Kiralama"),
    "blog-vip-transfer-ve-taksi-farklari": ("https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?q=80&w=1200&auto=format&fit=crop", "VIP Transfer ve Taksi Kıyaslaması"),
    "blog-protokol-tasimaciligi-kurallari": ("https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=1200&auto=format&fit=crop", "Protokol ve Makam Taşımacılığı"),
    "blog-esenboga-havalimani-vip-karsilama": ("https://images.unsplash.com/photo-1436491865332-7a61a109cc05?q=80&w=1200&auto=format&fit=crop", "Esenboğa Havalimanı VIP Karşılama"),
    "blog-ankaradan-kapadokyaya-vip-ulasim": ("https://images.unsplash.com/photo-1604085461230-07e0344d2d46?q=80&w=1200&auto=format&fit=crop", "Ankara Kapadokya VIP Transfer"),
    "blog-gelin-arabasi-secerken-vip-arac": ("assets/img/gelin-arabasi-hero.png", "VIP Gelin Arabası Kiralama"),
    "blog-is-seyahatleri-mercedes-vito": ("https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=1200&auto=format&fit=crop", "İş Seyahatleri için Mercedes Vito"),
    "blog-ankara-kis-turizmi-transfer": ("https://images.unsplash.com/photo-1478265409131-1f65c88f965c?q=80&w=1200&auto=format&fit=crop", "Ilgaz ve Kartalkaya Kar Transferi"),
    "blog-yabanci-misafirler-icin-karsilama": ("https://images.unsplash.com/photo-1521791136064-7986c2920216?q=80&w=1200&auto=format&fit=crop", "Yabancı Misafir VIP Karşılama"),
    "blog-mercedes-s-class-makam-araci": ("assets/img/sclass.jpeg", "Mercedes S-Class Makam Aracı"),
    "blog-guvenli-transfer-hijyen": ("https://images.unsplash.com/photo-1584483766114-2cea6facdf57?q=80&w=1200&auto=format&fit=crop", "Hijyenik ve Güvenli Transfer"),
    "blog-ankara-sehir-ici-rotalar": ("assets/img/atakule.jpg", "Ankara Şehir İçi VIP Rotalar"),
    "blog-sehirlerarasi-transferde-vip": ("https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=1200&auto=format&fit=crop", "Şehirlerarası Lüks VIP Transfer"),
    "blog-buyukelcilik-arac-kiralama": ("https://images.unsplash.com/photo-1525186402429-b4ff38a3014f?q=80&w=1200&auto=format&fit=crop", "Büyükelçilik ve Diplomatik Transfer"),
    "blog-bolu-abant-tatili-ulasim": ("https://images.unsplash.com/photo-1542224566-6e85f2e6772f?q=80&w=1200&auto=format&fit=crop", "Bolu Abant Tatil Transferi"),
    "blog-ankarada-luks-otel-transferleri": ("https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=1200&auto=format&fit=crop", "Ankara Lüks Otel VIP Transferi"),
    "blog-vip-araclarda-hangi-donanimlar-var": ("assets/img/vito-ic-yildizli.jpg", "VIP Araç İç Donanım Özellikleri"),
    "blog-kurumsal-transfer-anlasmasi": ("https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=1200&auto=format&fit=crop", "Kurumsal VIP Transfer Anlaşması"),
    "blog-ankara-vip-aracla-gezilecek-yerler": ("assets/img/atakule.jpg", "Ankara'da VIP Araçla Gezilecek Yerler"),
    "blog-havalimani-transfer-erken-rezervasyon": ("https://images.unsplash.com/photo-1436491865332-7a61a109cc05?q=80&w=1200&auto=format&fit=crop", "Havalimanı Erken Rezervasyon")
}

for slug, (img_url, alt_text) in image_map.items():
    filepath = os.path.join(directory, f"{slug}.html")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()
            
        # Replace the <img ... class="hero-bg">
        new_tag = f'<img src="{img_url}" alt="{alt_text}" class="hero-bg">'
        
        # Regex to find the existing hero-bg img tag
        # It could be anitkabir.jpg or something else if we modified it
        html = re.sub(r'<img[^>]*class="hero-bg"[^>]*>', new_tag, html)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Updated image for: {slug}")
    else:
        print(f"File not found: {slug}.html")

print("All blog images updated successfully!")
