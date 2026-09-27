import os
import re
import json

cwd = "/Users/abdullahcakir/Desktop/viptrip"

blogs_data = [
    {"slug": "blog-esenboga-havalimani-vip-transfer-fiyatlari", "title": "Esenboğa Havalimanı VIP Transfer Fiyatları 2026", "kw": "esenboğa vip transfer", "img": "esenboga_vip.png"},
    {"slug": "blog-esenboga-cankaya-vip-transfer", "title": "Esenboğa'dan Çankaya'ya Lüks VIP Transfer", "kw": "ankara vip transfer", "img": "ankara_city.png"},
    {"slug": "blog-esenboga-incek-vip-transfer", "title": "Esenboğa - İncek Arası Şoförlü VIP Araç Kiralama", "kw": "şoförlü araç kiralama", "img": "luxury_interior.png"},
    {"slug": "blog-esenboga-golbasi-vip-transfer", "title": "Esenboğa Havalimanı Gölbaşı VIP Transfer Hizmeti", "kw": "ankara transfer", "img": "esenboga_vip.png"},
    {"slug": "blog-esenboga-havalimani-luks-ulasim", "title": "Esenboğa Havalimanı Lüks Ulaşım Çözümleri", "kw": "esenboğa vip transfer", "img": "ankara_city.png"},
    {"slug": "blog-esenboga-havalimani-karsilama-hizmeti", "title": "Esenboğa CIP ve VIP İsimle Karşılama Hizmeti", "kw": "ankara vip transfer", "img": "luxury_interior.png"},
    {"slug": "blog-esenboga-transfer-mercedes-vito", "title": "Esenboğa Transferinde Mercedes Vito Ayrıcalığı", "kw": "mercedes vito kiralama", "img": "esenboga_vip.png"},
    {"slug": "blog-ankara-esenboga-7-24-transfer", "title": "Ankara Esenboğa 7/24 Kesintisiz VIP Transfer", "kw": "ankara transfer", "img": "ankara_city.png"},
    {"slug": "blog-esenboga-vip-taksi-alternatifi", "title": "Esenboğa Taksi Yerine VIP Transfer Neden Seçilmeli?", "kw": "esenboğa vip transfer", "img": "luxury_interior.png"},
    {"slug": "blog-esenboga-havalimani-soforlu-arac", "title": "Esenboğa Havalimanı Şoförlü Araç Kiralama Rehberi", "kw": "şoförlü araç kiralama", "img": "esenboga_vip.png"},
    
    {"slug": "blog-ankara-istanbul-vip-transfer", "title": "Ankara İstanbul Arası VIP Transfer Konforu", "kw": "şehirler arası vip transfer", "img": "highway_vip.png"},
    {"slug": "blog-ankara-kapadokya-vip-transfer-rehberi", "title": "Ankara'dan Kapadokya'ya VIP Transfer Rehberi", "kw": "şehirler arası vip transfer", "img": "highway_vip.png"},
    {"slug": "blog-ankara-bursa-vip-transfer", "title": "Ankara Bursa Şoförlü VIP Transfer Hizmeti", "kw": "şehirler arası transfer", "img": "luxury_interior.png"},
    {"slug": "blog-ankara-antalya-vip-transfer", "title": "Ankara Antalya Lüks VIP Araçla Tatil Ulaşımı", "kw": "şehirler arası vip transfer", "img": "highway_vip.png"},
    {"slug": "blog-ankara-izmir-vip-transfer", "title": "Ankara İzmir Şoförlü Araç Kiralama ve VIP Transfer", "kw": "şoförlü araç kiralama", "img": "luxury_interior.png"},
    {"slug": "blog-sehirlerarasi-vip-transfer-fiyatlari", "title": "2026 Şehirler Arası VIP Transfer Fiyatları", "kw": "şehirler arası vip transfer", "img": "highway_vip.png"},
    {"slug": "blog-ankara-bodrum-vip-transfer", "title": "Ankara Bodrum Kesintisiz Lüks VIP Ulaşım", "kw": "şehirler arası transfer", "img": "ankara_city.png"},
    {"slug": "blog-ankara-eskisehir-vip-transfer", "title": "Ankara Eskişehir Günübirlik VIP Transfer", "kw": "ankara vip transfer", "img": "highway_vip.png"},
    {"slug": "blog-ankara-konya-vip-transfer", "title": "Ankara Konya Şoförlü VIP Araç Hizmeti", "kw": "mercedes vito kiralama", "img": "luxury_interior.png"},
    {"slug": "blog-sehirlerarasi-soforlu-arac-kiralama", "title": "Şehirler Arası Şoförlü Araç Kiralama Avantajları", "kw": "şoförlü araç kiralama", "img": "highway_vip.png"}
]

template_path = os.path.join(cwd, "blog-sehirlerarasi-transferde-vip.html")
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

def generate_seo_content(title, kw):
    kws = [
        "ankara vip transfer", "esenboğa vip transfer", "şehirler arası vip transfer", 
        "ankara transfer", "şoförlü araç kiralama ankara", "mercedes vito kiralama", 
        "ankara havalimanı transfer", "şehirler arası transfer", "lüks ulaşım ankara"
    ]
    # Heavy keyword stuffing wrapped in readable HTML
    content = f"""
    <h2>{title} ile Lüks ve Konfor</h2>
    <p>Sonbahar ve kış aylarının gelmesiyle birlikte, <strong>{kw}</strong> ihtiyaçları her zamankinden daha fazla önem kazanmaktadır. 
    Siz değerli misafirlerimize sunduğumuz <strong>ankara vip transfer</strong> ve <strong>esenboğa vip transfer</strong> hizmetlerimizle, seyahatlerinizi 
    bir eziyet olmaktan çıkarıp keyifli bir yolculuğa dönüştürüyoruz. İster iş seyahati, ister tatil planı olsun; <strong>şoförlü araç kiralama ankara</strong> 
    arayışınızda VipTrip olarak daima yanınızdayız.</p>
    
    <h3>Neden <strong>{kw.title()}</strong> Tercih Etmelisiniz?</h3>
    <p>Özellikle <strong>şehirler arası vip transfer</strong> ve <strong>ankara havalimanı transfer</strong> konularında profesyonel şoförlerimiz ve 
    en yeni model araçlarımızla hizmet veriyoruz. Filomuzdaki araçlar, <strong>mercedes vito kiralama</strong> standartlarının çok üzerindedir. 
    İçi tamamen VIP tasarıma sahip olan bu araçlarla <strong>ankara transfer</strong> işlemlerinizi güvenle gerçekleştirebilirsiniz. 
    Zamanınızın değerli olduğunu biliyor ve <strong>lüks ulaşım ankara</strong> denilince akla gelen ilk marka olmanın gururunu yaşıyoruz.</p>
    
    <h3>Premium Deneyim ve Ayrıcalıklar</h3>
    <p>Sıradan taksi veya toplu taşıma seçeneklerinin aksine, <strong>esenboğa vip transfer</strong> veya <strong>şehirler arası transfer</strong> 
    tercihlerinizde size özel bir yaşam alanı sunuyoruz. Araçlarımızda ücretsiz Wi-Fi, ara bölme, televizyon ve mini buzdolabı gibi ekstra donanımlar bulunmaktadır. 
    Gerek <strong>ankara vip transfer</strong>, gerekse <strong>şoförlü araç kiralama ankara</strong> hizmetlerimizde hijyen ve güvenlik en üst düzeyde tutulmaktadır.</p>
    
    <p>Erken rezervasyon fırsatlarından yararlanarak <strong>{kw}</strong> hizmetini en uygun fiyat garantisiyle almak için iletişim sayfamızdan 
    veya WhatsApp hattımızdan bize 7/24 ulaşabilirsiniz. <strong>Ankara havalimanı transfer</strong> ve <strong>şehirler arası vip transfer</strong> 
    çözümlerimizle her anınızda VIP konforu yaşayın!</p>
    """
    return content

new_blogs_for_index = []

for b in blogs_data:
    slug = b['slug']
    title = b['title']
    desc = f"{title}. Ankara vip transfer, esenboğa vip transfer, şehirler arası vip transfer ve şoförlü araç kiralama hizmetleri hakkında detaylı bilgi."
    content_html = generate_seo_content(title, b['kw'])
    
    new_html = template
    new_html = re.sub(r'<title>.*?</title>', f'<title>{title} | VipTrip Ankara</title>', new_html)
    new_html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', new_html)
    new_html = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://viptrip.com.tr/{slug}">', new_html)
    new_html = re.sub(r'<h1>.*?</h1>', f'<h1>{title}</h1>', new_html)
    new_html = re.sub(r'<span class="blog-category">.*?</span>', f'<span class="blog-category">VIP Transfer Rehberi</span>', new_html)
    new_html = re.sub(r'"datePublished": ".*?"', f'"datePublished": "2026-09-27"', new_html)
    
    # Replace cover image
    new_html = re.sub(r'<img src="https://images.unsplash.com/.*?" alt=".*?" class="hero-bg">', 
                      f'<img src="assets/img/{b["img"]}" alt="{title}" class="hero-bg">', new_html)
                      
    # Replace the actual article body. It is inside <div class="blog-content">
    body_pattern = r'<div class="blog-content">.*?</div>\s*<!-- CTA BOX -->'
    replacement = f'<div class="blog-content">\n{content_html}\n</div>\n            <!-- CTA BOX -->'
    new_html = re.sub(body_pattern, replacement, new_html, flags=re.DOTALL)
    
    with open(os.path.join(cwd, f"{slug}.html"), 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    new_blogs_for_index.append(f'{{"slug": "{slug}", "title": "{title}", "desc": "{desc[:120]}..."}}')
    print(f"Created {slug}.html")

# Update create_blog_index.py
index_py_path = os.path.join(cwd, "create_blog_index.py")
with open(index_py_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Insert new blogs into the list
blogs_insert_str = ",\n    ".join(new_blogs_for_index)

# Find the end of the blogs array.
# It usually looks like:
#     {"slug": "blog-ankara-transfer-rehberi-2026", "title": "Ankara Transfer Rehberi 2026: En Çok Tercih Edilen Rotalar", "desc": "Esenboğa, Çankaya, İncek ve daha fazlası... Ankara içi transferlerde popüler rotalar ve ulaşım tüyoları."}
# ]
# Let's replace '}\n]' with '},\n    ' + blogs_insert_str + '\n]'
index_content = re.sub(r'}\n]', '},\n    ' + blogs_insert_str + '\n]', index_content)

with open(index_py_path, 'w', encoding='utf-8') as f:
    f.write(index_content)
    
print("Updated create_blog_index.py")
print("Done.")
