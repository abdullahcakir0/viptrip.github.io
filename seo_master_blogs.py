import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"

# The 20 existing blogs
existing_blogs = [
    "blog-esenboga-havalimani-vip-transfer-fiyatlari", "blog-esenboga-cankaya-vip-transfer",
    "blog-esenboga-incek-vip-transfer", "blog-esenboga-golbasi-vip-transfer",
    "blog-esenboga-havalimani-luks-ulasim", "blog-esenboga-havalimani-karsilama-hizmeti",
    "blog-esenboga-transfer-mercedes-vito", "blog-ankara-esenboga-7-24-transfer",
    "blog-esenboga-vip-taksi-alternatifi", "blog-esenboga-havalimani-soforlu-arac",
    "blog-ankara-istanbul-vip-transfer", "blog-ankara-kapadokya-vip-transfer-rehberi",
    "blog-ankara-bursa-vip-transfer", "blog-ankara-antalya-vip-transfer",
    "blog-ankara-izmir-vip-transfer", "blog-sehirlerarasi-vip-transfer-fiyatlari",
    "blog-ankara-bodrum-vip-transfer", "blog-ankara-eskisehir-vip-transfer",
    "blog-ankara-konya-vip-transfer", "blog-sehirlerarasi-soforlu-arac-kiralama"
]

# The 15 new blogs
new_blogs_data = [
    {"slug": "blog-ankara-kartalkaya-vip-transfer", "title": "Ankara Kartalkaya Kayak Merkezi VIP Transfer", "img": "highway_vip.png", "desc": "Kartalkaya kayak tatiliniz için VIP ulaşım çözümleri."},
    {"slug": "blog-ankara-erciyes-vip-transfer", "title": "Ankara Erciyes Şoförlü Araç Kiralama ve Transfer", "img": "highway_vip.png", "desc": "Erciyes kış turizmi için konforlu şoförlü VIP araç kiralama."},
    {"slug": "blog-ankara-fethiye-vip-transfer", "title": "Ankara Fethiye Lüks Transfer Hizmetleri", "img": "highway_vip.png", "desc": "Ankara'dan Fethiye ve Ölüdeniz'e direkt lüks transfer."},
    {"slug": "blog-ankara-marmaris-vip-transfer", "title": "Ankara Marmaris VIP Vito Kiralama", "img": "luxury_interior.png", "desc": "Marmaris tatiliniz için geniş ve lüks Mercedes Vito kiralama."},
    {"slug": "blog-ankara-kongre-fuar-transfer", "title": "Ankara Kongre ve Fuar VIP Transfer Organizasyonu", "img": "ankara_city.png", "desc": "Kurumsal kongre ve fuar etkinlikleri için VIP transfer ve taşıma."},
    {"slug": "blog-ankara-saglik-turizmi-transfer", "title": "Ankara Sağlık Turizmi Hastane VIP Transfer", "img": "esenboga_vip.png", "desc": "Sağlık turizmi kapsamında hastane ve kliniklere özel VIP ulaşım."},
    {"slug": "blog-ankara-uluslararasi-heyet-transfer", "title": "Uluslararası Heyet ve Protokol VIP Transfer Ankara", "img": "luxury_interior.png", "desc": "Protokol kurallarına uygun, yabancı heyetler için VIP transfer."},
    {"slug": "blog-ankara-elcilik-konsolosluk-transfer", "title": "Ankara Büyükelçilik ve Konsolosluk VIP Ulaşım", "img": "ankara_city.png", "desc": "Diplomatik misyonlar ve konsolosluklar için güvenli lüks transfer."},
    {"slug": "blog-ankara-sanatci-oyuncu-transfer", "title": "Sanatçı, Oyuncu ve VİP Konuk Transfer Hizmetleri", "img": "luxury_interior.png", "desc": "Sanat dünyası ve VIP konuklar için gizlilik odaklı lüks transfer."},
    {"slug": "blog-ankara-spor-kafilesi-transfer", "title": "Spor Kulüpleri ve Kafile VIP Transfer Ankara", "img": "esenboga_vip.png", "desc": "Sporcular ve yönetim kadrosu için lüks VIP minibüs ve araçlar."},
    {"slug": "blog-ankara-gunubirlik-turlar-transfer", "title": "Ankara Çıkışlı Günübirlik VIP Tur Transferleri", "img": "highway_vip.png", "desc": "Ailenizle veya grubunuzla özel günübirlik lüks tur ulaşımı."},
    {"slug": "blog-ankara-yht-gar-vip-transfer", "title": "Ankara YHT Gar VIP Karşılama ve Transfer", "img": "ankara_city.png", "desc": "Yüksek Hızlı Tren garında isimle karşılama ve VIP transfer."},
    {"slug": "blog-esenboga-otel-vip-transfer", "title": "Esenboğa Havalimanı Lüks Otel Transferleri", "img": "esenboga_vip.png", "desc": "Esenboğa'dan Ankara'nın 5 yıldızlı otellerine direkt lüks transfer."},
    {"slug": "blog-ankara-vip-minibus-kiralama", "title": "Ankara VIP Minibüs Kiralama Şoförlü", "img": "luxury_interior.png", "desc": "Geniş gruplar için şoförlü VIP minibüs kiralama hizmeti."},
    {"slug": "blog-ankara-uzun-donem-soforlu-arac", "title": "Ankara Uzun Dönem Şoförlü VIP Araç Kiralama", "img": "ankara_city.png", "desc": "Kurumlar ve yöneticiler için aylık ve uzun dönem şoförlü VIP araç."}
]

# Extremely heavy SEO block (25 keyword insertions) tailored for an SEO expert
# K1: ankara vip transfer
# K2: esenboğa vip transfer
# K3: şehirler arası vip transfer
# K4: şoförlü araç kiralama ankara
# K5: mercedes vito kiralama
seo_heavy_block = """
    <h2>VipTrip ile 360 Derece Ulaşım Çözümleri ve Acenta Kalitesi</h2>
    <p>Yılların getirdiği turizm ve acenta tecrübesiyle, <strong>ankara vip transfer</strong> sektöründe lider konumumuzu koruyoruz. Müşterilerimiz <strong>ankara vip transfer</strong> ihtiyaçlarında daima kaliteyi ararken, biz <strong>ankara vip transfer</strong> hizmetini <strong>şoförlü araç kiralama ankara</strong> konseptiyle birleştiriyoruz. Havalimanı yolculuklarında <strong>esenboğa vip transfer</strong> operasyonlarımızla fark yaratıyor, <strong>esenboğa vip transfer</strong> arayan misafirlerimize en hızlı çözümleri üretiyoruz. Özel misafir karşılama ve <strong>esenboğa vip transfer</strong> organizasyonlarımızda <strong>mercedes vito kiralama</strong> seçeneklerimiz en çok tercih edilenler arasındadır. Lüks ve konforlu bir <strong>mercedes vito kiralama</strong> arıyorsanız, <strong>mercedes vito kiralama</strong> filomuz beklentilerinizi fazlasıyla karşılayacaktır.</p>

    <p>Sadece şehir içi değil, <strong>şehirler arası vip transfer</strong> taleplerinizde de Türkiye'nin her noktasına <strong>şehirler arası vip transfer</strong> kalitesiyle ulaşıyoruz. Uzun yolda <strong>şehirler arası vip transfer</strong> konforunu yaşamak isteyenler için <strong>şoförlü araç kiralama ankara</strong> departmanımız 7/24 çalışmaktadır. <strong>Şoförlü araç kiralama ankara</strong> hizmetlerimiz sayesinde yorgunluk hissetmeden, tam donanımlı <strong>mercedes vito kiralama</strong> araçlarımızda seyahat edersiniz. Yeni nesil <strong>mercedes vito kiralama</strong> filomuz, <strong>ankara vip transfer</strong> pazarında standartları belirleyen bir <strong>ankara vip transfer</strong> kalitesine sahiptir. Turizm ve transfer dünyasında <strong>esenboğa vip transfer</strong> denilince akla ilk gelen firma olmamız, <strong>esenboğa vip transfer</strong> hizmetine verdiğimiz değerden kaynaklanır.</p>

    <p>Güvenilir bir <strong>şoförlü araç kiralama ankara</strong> partnerine ihtiyacınız olduğunda, <strong>şoförlü araç kiralama ankara</strong> uzmanlarımız anında devreye girer. Şirketlerin ve bireysel misafirlerin <strong>şehirler arası vip transfer</strong> aramalarında bizi bulmaları tesadüf değildir. Zira <strong>şehirler arası vip transfer</strong> operasyonlarımızda her zaman en üst segment araçlar kullanılır. Kurumsal bir acenta olarak misyonumuz; ulaşım alanında her daim en iyi hizmeti kusursuz bir deneyimle taçlandırmaktır.</p>
"""

# Part 1: Update the existing 20 blogs to append the SEO Heavy Block
for slug in existing_blogs:
    filepath = os.path.join(cwd, f"{slug}.html")
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already added to avoid duplication during testing
        if "360 Derece Ulaşım Çözümleri" not in content:
            # Append before the CTA box
            body_pattern = r'(<div class="cta-box">)'
            replacement = f'{seo_heavy_block}\n            \\1'
            new_content = re.sub(body_pattern, replacement, content, count=1)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Boosted SEO for {slug}.html")

# Part 2: Generate 15 New Blogs
template_path = os.path.join(cwd, "blog-sehirlerarasi-transferde-vip.html")
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

new_blogs_for_index = []

for b in new_blogs_data:
    slug = b['slug']
    title = b['title']
    desc = b['desc']
    
    unique_intro = f"""
    <h2>{title} Hakkında</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Acenta düzeyinde sunduğumuz lüks taşıma hizmetleriyle, {title.lower()} rotalarında en yüksek standartları sağlıyoruz. Bireysel ve kurumsal tüm seyahatleriniz, uzman ekibimiz tarafından titizlikle planlanmaktadır.</p>
    <p>Modern araçlarımız ve eğitimli sürücü kadromuzla, seyahatinizin başından sonuna kadar kusursuz bir deneyim yaşamanız bizim en büyük önceliğimizdir. Vakit kaybetmeden lüks yolculuğun tadını çıkarın.</p>
    """
    
    full_content = unique_intro + "\n" + seo_heavy_block
    
    new_html = template
    new_html = re.sub(r'<title>.*?</title>', f'<title>{title} | VipTrip Acenta Blog</title>', new_html)
    new_html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc} {title}.">', new_html)
    new_html = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://viptrip.com.tr/{slug}">', new_html)
    new_html = re.sub(r'<h1>.*?</h1>', f'<h1>{title}</h1>', new_html)
    new_html = re.sub(r'<span class="blog-category">.*?</span>', f'<span class="blog-category">VIP Transfer Rehberi</span>', new_html)
    new_html = re.sub(r'"datePublished": ".*?"', f'"datePublished": "2026-09-27"', new_html)
    
    # Image replace
    new_html = re.sub(r'<img src="https://images.unsplash.com/.*?" alt=".*?" class="hero-bg">', 
                      f'<img src="assets/img/{b["img"]}" alt="{title}" class="hero-bg">', new_html)
                      
    # Replace body
    body_pattern = r'(<section class="blog-body">\s*<div class="container">).*?(<div class="cta-box">)'
    replacement = f'\\1\n{full_content}\n\\2'
    new_html = re.sub(body_pattern, replacement, new_html, flags=re.DOTALL)
    
    with open(os.path.join(cwd, f"{slug}.html"), 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    new_blogs_for_index.append(f'{{"slug": "{slug}", "title": "{title}", "desc": "{desc[:120]}"}}')
    print(f"Created new blog {slug}.html")

# Update create_blog_index.py
index_py_path = os.path.join(cwd, "create_blog_index.py")
with open(index_py_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

blogs_insert_str = ",\n    ".join(new_blogs_for_index)

# Regex to append to the end of the JSON array
index_content = re.sub(r'}\n]', '},\n    ' + blogs_insert_str + '\n]', index_content)

with open(index_py_path, 'w', encoding='utf-8') as f:
    f.write(index_content)
    
print("Updated create_blog_index.py with 15 new blogs.")
print("Done executing SEO Master tasks.")
