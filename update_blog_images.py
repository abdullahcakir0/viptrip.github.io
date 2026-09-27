import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"

blog_image_map = {
    # Airport & General
    "blog-esenboga-havalimani-vip-transfer-fiyatlari": "esenboga_havalimani_transfer.png",
    "blog-esenboga-havalimani-luks-ulasim": "esenboga_vip.png",
    "blog-esenboga-havalimani-karsilama-hizmeti": "esenboga_havalimani_transfer.png",
    "blog-esenboga-transfer-mercedes-vito": "mercedes_vito_kiralama.png",
    "blog-ankara-esenboga-7-24-transfer": "vip_transfer_ankara.png",
    "blog-esenboga-vip-taksi-alternatifi": "soforlu_arac_kiralama.png",
    "blog-esenboga-havalimani-soforlu-arac": "soforlu_arac_kiralama.png",
    "blog-esenboga-otel-vip-transfer": "ankara_city.png",

    # Intercity General
    "blog-sehirlerarasi-vip-transfer-fiyatlari": "sehirler_arasi_transfer.png",
    "blog-sehirlerarasi-soforlu-arac-kiralama": "sehirler_arasi_transfer.png",
    
    # Specific Cities
    "blog-ankara-istanbul-vip-transfer": "highway_vip.png",
    "blog-ankara-bursa-vip-transfer": "highway_vip.png",
    "blog-ankara-izmir-vip-transfer": "sehirler_arasi_transfer.png",
    "blog-ankara-eskisehir-vip-transfer": "highway_vip.png",
    "blog-ankara-konya-vip-transfer": "highway_vip.png",
    
    # Summer/Resort
    "blog-ankara-antalya-vip-transfer": "luks_tatil_transferi.png",
    "blog-ankara-bodrum-vip-transfer": "luks_tatil_transferi.png",
    "blog-ankara-fethiye-vip-transfer": "luks_tatil_transferi.png",
    "blog-ankara-marmaris-vip-transfer": "luks_tatil_transferi.png",
    
    # Winter/Snow
    "blog-ankara-kartalkaya-vip-transfer": "kayak_merkezi_vip_transfer.png",
    "blog-ankara-erciyes-vip-transfer": "kayak_merkezi_vip_transfer.png",
    "blog-ankara-kapadokya-vip-transfer-rehberi": "kayak_merkezi_vip_transfer.png", 
    
    # City / Local
    "blog-esenboga-cankaya-vip-transfer": "ankara_city.png",
    "blog-esenboga-incek-vip-transfer": "vip_transfer_ankara.png",
    "blog-esenboga-golbasi-vip-transfer": "ankara_city.png",
    
    # Special Events / Protocols
    "blog-ankara-kongre-fuar-transfer": "kongre_fuar_vip.png",
    "blog-ankara-saglik-turizmi-transfer": "soforlu_arac_kiralama.png",
    "blog-ankara-uluslararasi-heyet-transfer": "kongre_fuar_vip.png",
    "blog-ankara-elcilik-konsolosluk-transfer": "vip_transfer_ankara.png",
    "blog-ankara-sanatci-oyuncu-transfer": "luxury_interior.png",
    "blog-ankara-spor-kafilesi-transfer": "mercedes_vito_kiralama.png",
    "blog-ankara-yht-gar-vip-transfer": "ankara_city.png",
    "blog-ankara-gunubirlik-turlar-transfer": "highway_vip.png",
    
    # Corporate / Minibus
    "blog-ankara-vip-minibus-kiralama": "luxury_interior.png",
    "blog-ankara-uzun-donem-soforlu-arac": "mercedes_vito_kiralama.png"
}

for slug, img_name in blog_image_map.items():
    filepath = os.path.join(cwd, f"{slug}.html")
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        title_match = re.search(r'<title>(.*?)</title>', content)
        if title_match:
            title = title_match.group(1).split('|')[0].strip()
        else:
            title = slug.replace("-", " ").title()
            
        seo_alt = f"{title} - Ankara VIP Transfer, Esenboğa Transfer, Mercedes Vito Kiralama"
        
        img_pattern = r'<img src="assets/img/.*?" alt=".*?" class="hero-bg">'
        new_img_tag = f'<img src="assets/img/{img_name}" alt="{seo_alt}" class="hero-bg">'
        
        new_content = re.sub(img_pattern, new_img_tag, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated image and SEO alt for {slug}")
        
print("Successfully distributed 12 unique images and updated alt tags for 35 blogs.")
