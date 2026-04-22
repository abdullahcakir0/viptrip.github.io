import os
import json

directory = "/Users/abdullahcakir/Desktop/viptrip"

# The blog list
blogs = [
    {"slug": "blog-ankarada-soforlu-arac-kiralama-rehberi", "title": "Ankara'da Şoförlü Araç Kiralama Rehberi", "desc": "Ankara'da şoförlü araç kiralarken nelere dikkat edilmeli? VIP hizmetin avantajları ve fiyatlandırma detayları."},
    {"slug": "blog-vip-transfer-ve-taksi-farklari", "title": "VIP Transfer ile Taksiler Arasındaki 5 Fark", "desc": "Neden VIP transfer tercih etmelisiniz? Standart taksi taşımacılığı ile şoförlü VIP transfer arasındaki temel farklar."},
    {"slug": "blog-protokol-tasimaciligi-kurallari", "title": "Protokol Taşımacılığında Dikkat Edilmesi Gerekenler", "desc": "Ankara'da diplomatik görevler ve protokol taşımacılığı için gerekli standartlar, araç özellikleri ve şoför protokol kuralları."},
    {"slug": "blog-esenboga-havalimani-vip-karsilama", "title": "Esenboğa Havalimanı CIP Salonu Ayrıcalıkları", "desc": "Ankara Esenboğa Havalimanı CIP ve VIP terminal hizmetleri, isim tabelalı karşılama ve hızlı transfer avantajları."},
    {"slug": "blog-ankaradan-kapadokyaya-vip-ulasim", "title": "Ankara'dan Kapadokya'ya VIP Ulaşım", "desc": "Hafta sonu tatili veya yabancı misafirleriniz için Ankara'dan Kapadokya'ya şoförlü VIP transfer detayları."},
    {"slug": "blog-gelin-arabasi-secerken-vip-arac", "title": "Gelin Arabası Seçerken Neden VIP Araç Tercih Edilmeli?", "desc": "Düğün gününüzde gelinlik rahatlığı ve şoför stresi yaşamamak için Mercedes Vito VIP gelin arabası kiralama rehberi."},
    {"slug": "blog-is-seyahatleri-mercedes-vito", "title": "İş Seyahatleri İçin Mercedes Vito'nun Avantajları", "desc": "Ankara'daki holdingler ve firmalar neden yöneticileri için VIP Vito kiralama hizmetini tercih ediyor?"},
    {"slug": "blog-ankara-kis-turizmi-transfer", "title": "Ankara Kış Turizmi: Ilgaz ve Kartalkaya Transferleri", "desc": "Kış tatiline çıkarken kar lastikli, güvenli ve lüks araçlarla Ankara'dan Ilgaz ve Kartalkaya'ya VIP transfer."},
    {"slug": "blog-yabanci-misafirler-icin-karsilama", "title": "Yabancı Misafirler İçin Ankara'da VIP Karşılama", "desc": "Yurtdışından gelen konuklarınız ve iş ortaklarınız için İngilizce bilen şoförlü araç tahsisinin önemi."},
    {"slug": "blog-mercedes-s-class-makam-araci", "title": "Mercedes S-Class ile Makam Aracı Deneyimi", "desc": "Zirvedeki yöneticiler, CEO'lar ve büyükelçiler için S-Class VIP transfer ayrıcalıkları."},
    {"slug": "blog-guvenli-transfer-hijyen", "title": "Güvenli Transfer: Pandemi Sonrası Hijyen Standartlarımız", "desc": "VipTrip olarak araçlarımızda uyguladığımız ozonla dezenfeksiyon ve hijyen politikalarımız."},
    {"slug": "blog-ankara-sehir-ici-rotalar", "title": "Ankara Şehir İçi VIP Transfer Rotaları", "desc": "Çankaya, Kızılay, Tunalı ve İncek gibi Ankara'nın popüler bölgeleri arası lüks ulaşım seçenekleri."},
    {"slug": "blog-sehirlerarasi-transferde-vip", "title": "Şehirlerarası Transferde VIP Konforu", "desc": "Uçak veya otobüs yerine neden şehirlerarası VIP araç transferi daha avantajlıdır?"},
    {"slug": "blog-buyukelcilik-arac-kiralama", "title": "Büyükelçilik ve Diplomatik Görevler İçin Araç Kiralama", "desc": "Ankara'daki büyükelçilikler ve uluslararası delegasyonlar için yüksek güvenlikli ve protokol kurallarına uygun transfer."},
    {"slug": "blog-bolu-abant-tatili-ulasim", "title": "Bolu Abant Tatili İçin VIP Ulaşım Çözümleri", "desc": "Doğa ile iç içe bir hafta sonu için Ankara'dan Bolu Yedi Göller ve Abant'a şoförlü transfer."},
    {"slug": "blog-ankarada-luks-otel-transferleri", "title": "Ankara'da Lüks Otel Transferleri", "desc": "Sheraton, JW Marriott, Lugal ve Ankara HiltonSA otellerine havalimanından VIP karşılama."},
    {"slug": "blog-vip-araclarda-hangi-donanimlar-var", "title": "VIP Araçlarda Hangi Donanımlar Bulunur?", "desc": "Gerçek bir VIP transfer aracının sahip olması gereken özellikler, teknoloji ve konfor donanımları."},
    {"slug": "blog-kurumsal-transfer-anlasmasi", "title": "Şirketler İçin Kurumsal Transfer Anlaşmasının Faydaları", "desc": "Firmalar için aylık faturalandırma ve kurumsal VIP taşımacılık anlaşmalarının avantajları."},
    {"slug": "blog-ankara-vip-aracla-gezilecek-yerler", "title": "Ankara'da VİP Araçla Gezilecek En İyi 5 Yer", "desc": "Şehri ilk kez ziyaret edenler için Anıtkabir, Ankara Kalesi, Atakule ve müzeleri kapsayan şoförlü tur rotası."},
    {"slug": "blog-havalimani-transfer-erken-rezervasyon", "title": "Havalimanı Transferinde Neden Erken Rezervasyon Yapılmalı?", "desc": "Son dakika stresi yaşamamak ve en uygun VIP aracı garantilemek için erken rezervasyonun önemi."}
]

# Create HTML content
html = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sektörel Blog ve Rehber | VipTrip Ankara</title>
    <meta name="description" content="Ankara VIP transfer sektörü hakkında en güncel yazılar, ulaşım rehberleri ve vip araç kiralama tüyoları.">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="blog.css">
    <link rel="icon" type="image/jpeg" href="assets/img/vito.jpeg">
</head>
<body>
    <header class="blog-header">
        <a href="/" class="logo">VIPTRIP<span class="dot">.</span></a>
        <div class="blog-menu-toggle" onclick="document.querySelector('.header-nav').classList.add('active'); document.querySelector('.blog-nav-overlay').classList.add('active');">
            <span></span><span></span><span></span>
        </div>
        <nav class="header-nav">
            <button class="blog-nav-close" onclick="document.querySelector('.header-nav').classList.remove('active'); document.querySelector('.blog-nav-overlay').classList.remove('active');"><i class="fas fa-times"></i></button>
            <a href="/">Ana Sayfa</a>
            <a href="ankara-vip-transfer">VIP Transfer</a>
            <a href="ankara-bolu-transfer">Bölgeler</a>
            <a href="blog" class="current">Blog</a>
            <a href="/#transfer" class="btn-header-cta">Transfer Ayarla</a>
        </nav>
    </header>
    <div class="blog-nav-overlay" onclick="document.querySelector('.header-nav').classList.remove('active'); this.classList.remove('active');"></div>

    <section class="blog-hero" style="height:40vh; min-height:300px;">
        <div class="hero-overlay" style="background: rgba(0,0,0,0.8);"></div>
        <div class="hero-text">
            <span class="blog-category">Blog</span>
            <h1>Sektörel Yazılar & Rehber</h1>
            <p class="hero-meta">VipTrip Ankara Transfer Bloğu</p>
        </div>
    </section>

    <div class="breadcrumb-bar">
        <div class="container"><nav>
            <a href="/"><i class="fas fa-home"></i> Ana Sayfa</a>
            <span class="separator"><i class="fas fa-chevron-right"></i></span>
            <span class="current">Blog</span>
        </nav></div>
    </div>

    <section class="related-section" style="background:#0a0a0a;">
        <div class="container">
            <div class="related-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
"""

for i, blog in enumerate(blogs):
    # Just a placeholder image logic based on index
    img_src = "assets/img/vito.jpeg" if i % 3 == 0 else ("assets/img/sprinter.jpeg" if i % 3 == 1 else "assets/img/sclass.jpeg")
    
    html += f"""
                <a href="{blog['slug']}" class="related-card" style="text-decoration:none;">
                    <div class="card-thumb">
                        <img src="{img_src}" alt="{blog['title']}">
                        <span class="tag">Makale</span>
                    </div>
                    <div class="card-body">
                        <h3>{blog['title']}</h3>
                        <p>{blog['desc']}</p>
                        <span class="card-link">Devamını Oku <i class="fas fa-arrow-right"></i></span>
                    </div>
                </a>
"""

html += """
            </div>
        </div>
    </section>

    <footer class="blog-footer"><p>&copy; 2025 VipTrip Ankara. Powered by <strong>Ayka Travel</strong> | <a href="/">Ana Sayfa</a></p></footer>
</body>
</html>
"""

with open(os.path.join(directory, "blog.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Created blog.html")
