import os

directory = "/Users/abdullahcakir/Desktop/viptrip"

# Read template from ankara-vip-transfer.html
with open(os.path.join(directory, "ankara-vip-transfer.html"), "r", encoding="utf-8") as f:
    template = f.read()

def generate_geo_page(slug, city, title_suffix, description, keyword_city, hero_img, h1_title, intro_text, content_html):
    # Basic replacements
    html = template
    html = html.replace("Ankara VIP Transfer Hizmeti | Şoförlü Lüks Araç - VipTrip", f"Ankara {city} Transfer | {title_suffix} - VipTrip")
    html = html.replace("Ankara VIP transfer hizmeti. Mercedes Vito, Sprinter ve S-Class ile şehir içi, havalimanı ve şehirlerarası özel transfer. 7/24 profesyonel şoförlü araç hizmeti.", description)
    html = html.replace("ankara vip transfer, ankara özel transfer, ankara lüks transfer, vip transfer ankara, ankara şoförlü araç, ankara transfer hizmeti", f"ankara {keyword_city} transfer, {keyword_city} vip transfer, ankara {keyword_city} lüks ulaşım, ankara {keyword_city} şoförlü araç")
    html = html.replace('href="https://www.viptrip.com.tr/ankara-vip-transfer"', f'href="https://www.viptrip.com.tr/{slug}"')
    html = html.replace('content="Ankara VIP Transfer Hizmeti | VipTrip"', f'content="Ankara {city} Transfer | VipTrip"')
    
    # Hero replacements
    html = html.replace('src="assets/img/vito.jpeg"', f'src="assets/img/{hero_img}"')
    html = html.replace('<h1>Ankara VIP Transfer Hizmeti</h1>', f'<h1>{h1_title}</h1>')
    html = html.replace('<span class="blog-category">VIP Transfer</span>', f'<span class="blog-category">Şehirlerarası Transfer</span>')
    html = html.replace('<i class="fas fa-map-marker-alt"></i> Ankara & Çevre İller', f'<i class="fas fa-map-marker-alt"></i> Ankara ⇄ {city}')
    html = html.replace('<span class="current">Ankara VIP Transfer</span>', f'<span class="current">Ankara {city} Transfer</span>')

    # Body replacements
    # Find the start of blog-body container
    body_start = html.find('<div class="container">', html.find('<section class="blog-body">')) + len('<div class="container">')
    # Find the end of blog-faq (just replace the whole content inside container but keep faq? or replace all)
    body_end = html.find('</div>', html.find('</section>', body_start)) # Actually let's just use regex or split to replace the content
    
    # To keep it simple, let's just replace the intro paragraphs and heading 2s using replace
    html = html.replace("Ankara'da <strong>VIP transfer</strong> denildiğinde akla gelen ilk isim VipTrip.", intro_text)
    
    filepath = os.path.join(directory, f"{slug}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: {slug}.html")

# 1. Bolu
generate_geo_page(
    slug="ankara-bolu-transfer",
    city="Bolu & Abant",
    title_suffix="Lüks ve Konforlu Ulaşım",
    description="Ankara'dan Bolu, Abant, Yedi Göller ve Kartalkaya'ya Mercedes Vito ve Sprinter araçlarla VIP transfer hizmeti.",
    keyword_city="bolu abant",
    hero_img="vito-dis-on.jpg",
    h1_title="Ankara Bolu VIP Transfer",
    intro_text="Ankara'dan doğanın kalbi <strong>Bolu ve Abant'a VIP transfer</strong> denildiğinde akla gelen ilk isim VipTrip.",
    content_html=""
)

# 2. Kapadokya
generate_geo_page(
    slug="ankara-kapadokya-transfer",
    city="Kapadokya",
    title_suffix="VIP Tur ve Transfer",
    description="Ankara'dan Nevşehir Kapadokya bölgesine, Göreme, Ürgüp otellerine Mercedes Vito VIP araçlarla güvenli ve konforlu transfer.",
    keyword_city="kapadokya nevşehir",
    hero_img="vito-kapi-acik.jpg",
    h1_title="Ankara Kapadokya VIP Transfer",
    intro_text="Ankara'dan masalsı diyarlara, <strong>Kapadokya'ya VIP transfer</strong> denildiğinde akla gelen ilk isim VipTrip.",
    content_html=""
)

# 3. İstanbul
generate_geo_page(
    slug="ankara-istanbul-transfer",
    city="İstanbul",
    title_suffix="Şehirlerarası Özel Transfer",
    description="Ankara ile İstanbul arası uçak konforunda VIP karayolu transferi. Şoförlü Mercedes Vito ile kesintisiz ve lüks ulaşım.",
    keyword_city="istanbul",
    hero_img="sprinter.jpeg",
    h1_title="Ankara İstanbul VIP Transfer",
    intro_text="Ankara'dan metropol şehri <strong>İstanbul'a VIP transfer</strong> denildiğinde akla gelen ilk isim VipTrip.",
    content_html=""
)


# Blog generation array
blogs = [
    {
        "slug": "blog-ankarada-soforlu-arac-kiralama-rehberi",
        "title": "Ankara'da Şoförlü Araç Kiralama Rehberi",
        "desc": "Ankara'da şoförlü araç kiralarken nelere dikkat edilmeli? VIP hizmetin avantajları ve fiyatlandırma detayları.",
        "content": "Ankara'da şoförlü araç kiralama, iş toplantılarından özel davetlere kadar hayat kurtaran bir hizmettir. Profesyonel bir şoför ve VIP donanımlı bir araç, ulaşımı bir stres kaynağı olmaktan çıkarıp dinlenme fırsatına dönüştürür. VipTrip olarak, tüm araçlarımızda D2 yetki belgesi, TÜRSAB onayı ve periyodik bakımlar standarttır."
    },
    {
        "slug": "blog-vip-transfer-ve-taksi-farklari",
        "title": "VIP Transfer ile Taksiler Arasındaki 5 Fark",
        "desc": "Neden VIP transfer tercih etmelisiniz? Standart taksi taşımacılığı ile şoförlü VIP transfer arasındaki temel farklar.",
        "content": "1. Sabit Fiyat Garantisi: Taksimetre stresi yaşamazsınız.<br>2. Araç Kalitesi: Mercedes Vito, Sprinter gibi lüks araçlarla seyahat edersiniz.<br>3. Profesyonel Sürücü: Eğitimli, takım elbiseli ve dil bilen şoförler.<br>4. Planlı Ulaşım: Araç sizi bekler, siz aracı değil.<br>5. Ekstra Donanımlar: Araç içi internet, buzdolabı, TV gibi ayrıcalıklar."
    },
    {
        "slug": "blog-protokol-tasimaciligi-kurallari",
        "title": "Protokol Taşımacılığında Dikkat Edilmesi Gerekenler",
        "desc": "Ankara'da diplomatik görevler ve protokol taşımacılığı için gerekli standartlar, araç özellikleri ve şoför protokol kuralları.",
        "content": "Başkent Ankara'da protokol taşımacılığı özel bir uzmanlık gerektirir. Siyah makam araçları (Mercedes S-Class veya siyah Vito), karartılmış camlar ve kesin gizlilik kuralları ön plandadır. Şoförün kapı açma adabından, güzergahı önceden planlamasına kadar her detay kusursuz olmalıdır."
    },
    {
        "slug": "blog-esenboga-havalimani-vip-karsilama",
        "title": "Esenboğa Havalimanı CIP Salonu Ayrıcalıkları",
        "desc": "Ankara Esenboğa Havalimanı CIP ve VIP terminal hizmetleri, isim tabelalı karşılama ve hızlı transfer avantajları.",
        "content": "Esenboğa Havalimanı'nda uçağınızdan indiğiniz anda VIP hizmet başlar. CIP terminalini kullanan misafirlerimiz, valiz beklemeden doğrudan araçlarına geçebilirler. Şoförlerimiz sizi isminizle karşılar, valizlerinizi alır ve sizi doğrudan otelinize veya toplantınıza ulaştırır."
    },
    {
        "slug": "blog-ankaradan-kapadokyaya-vip-ulasim",
        "title": "Ankara'dan Kapadokya'ya VIP Ulaşım",
        "desc": "Hafta sonu tatili veya yabancı misafirleriniz için Ankara'dan Kapadokya'ya şoförlü VIP transfer detayları.",
        "content": "Ankara - Kapadokya arası yaklaşık 3-4 saatlik bir yolculuktur. Bu süreyi ailenizle veya iş ortaklarınızla lüks bir Mercedes Vito içerisinde geçirmek, tatilinizin daha yola çıkarken başlamasını sağlar. Araç içi eğlence sistemleri ve rahat koltuklarla yol yorgunluğu hissetmezsiniz."
    },
    {
        "slug": "blog-gelin-arabasi-secerken-vip-arac",
        "title": "Gelin Arabası Seçerken Neden VIP Araç Tercih Edilmeli?",
        "desc": "Düğün gününüzde gelinlik rahatlığı ve şoför stresi yaşamamak için Mercedes Vito VIP gelin arabası kiralama rehberi.",
        "content": "Gelinliklerin geniş yapısı, klasik sedan araçlarda zorluk çıkarabilir. VIP minibüsler (Vito), geniş iç hacmi ile gelinin rahat hareket etmesini sağlar. Ayrıca profesyonel şoför sayesinde, damat trafik ve park yeri stresi yaşamaz, sadece o özel günün tadını çıkarır."
    },
    {
        "slug": "blog-is-seyahatleri-mercedes-vito",
        "title": "İş Seyahatleri İçin Mercedes Vito'nun Avantajları",
        "desc": "Ankara'daki holdingler ve firmalar neden yöneticileri için VIP Vito kiralama hizmetini tercih ediyor?",
        "content": "İş dünyasında zaman en değerli varlıktır. Karşılıklı deri koltukları ve çalışma masası olan bir VIP araç, Ankara trafiğinde geçen zamanı verimli bir mobil ofise dönüştürür. Kesintisiz internet bağlantısı ile toplantılarınıza yoldayken bile katılabilirsiniz."
    },
    {
        "slug": "blog-ankara-kis-turizmi-transfer",
        "title": "Ankara Kış Turizmi: Ilgaz ve Kartalkaya Transferleri",
        "desc": "Kış tatiline çıkarken kar lastikli, güvenli ve lüks araçlarla Ankara'dan Ilgaz ve Kartalkaya'ya VIP transfer.",
        "content": "Kış şartlarında araç kullanmak tecrübe ve doğru donanım gerektirir. Kar lastikli, bakımlı VIP Sprinter veya Vito araçlarımızla kayak takımlarınızı rahatça taşıyabilir, karlı dağ yollarında güvenle ve sıcacık bir ortamda Kartalkaya veya Ilgaz'a ulaşabilirsiniz."
    },
    {
        "slug": "blog-yabanci-misafirler-icin-karsilama",
        "title": "Yabancı Misafirler İçin Ankara'da VIP Karşılama",
        "desc": "Yurtdışından gelen konuklarınız ve iş ortaklarınız için İngilizce bilen şoförlü araç tahsisinin önemi.",
        "content": "Şirketinizin vizyonu, misafirlerinizi havalimanında nasıl karşıladığınızla başlar. İngilizce bilen şoförlerimiz, misafirlerinizi nezaketle karşılar, şehri tanıtır ve onlara yabancı bir ülkede olduklarını hissettirmeden yüksek konfor sunar."
    },
    {
        "slug": "blog-mercedes-s-class-makam-araci",
        "title": "Mercedes S-Class ile Makam Aracı Deneyimi",
        "desc": "Zirvedeki yöneticiler, CEO'lar ve büyükelçiler için S-Class VIP transfer ayrıcalıkları.",
        "content": "Otomotiv dünyasının amiral gemisi olan Mercedes S-Class, lüksün ve güvenliğin sembolüdür. Havalı süspansiyon sistemi, masajlı arka koltukları ve üst düzey ses yalıtımı ile Ankara'nın en prestijli yolculuklarını sunuyoruz."
    },
    {
        "slug": "blog-guvenli-transfer-hijyen",
        "title": "Güvenli Transfer: Pandemi Sonrası Hijyen Standartlarımız",
        "desc": "VipTrip olarak araçlarımızda uyguladığımız ozonla dezenfeksiyon ve hijyen politikalarımız.",
        "content": "Sağlığınız bizim için önceliklidir. Her transferden sonra araçlarımız havalandırılır, temas yüzeyleri özel solüsyonlarla temizlenir ve düzenli aralıklarla ozon jeneratörü ile dezenfekte edilir. Araçlarımızda her zaman maske ve dezenfektan bulundurulur."
    },
    {
        "slug": "blog-ankara-sehir-ici-rotalar",
        "title": "Ankara Şehir İçi VIP Transfer Rotaları",
        "desc": "Çankaya, Kızılay, Tunalı ve İncek gibi Ankara'nın popüler bölgeleri arası lüks ulaşım seçenekleri.",
        "content": "Özellikle iş çıkış saatlerinde Ankara trafiği yorucu olabilir. Çankaya'dan İncek'e, Batıkent'ten Kızılay'a uzanan günlük rotalarınızda şoförlü VIP aracınız sizi kapınızdan alır ve gideceğiniz yere tam zamanında, stressiz bir şekilde ulaştırır."
    },
    {
        "slug": "blog-sehirlerarasi-transferde-vip",
        "title": "Şehirlerarası Transferde VIP Konforu",
        "desc": "Uçak veya otobüs yerine neden şehirlerarası VIP araç transferi daha avantajlıdır?",
        "content": "Havalimanı prosedürleri (check-in, bagaj bekleme, rötarlar) düşünüldüğünde, kapınızdan alınıp doğrudan gideceğiniz şehrin kapısına bırakılmak çoğu zaman hem daha hızlı hem de kesinlikle daha konforludur. Özellikle 3-4 kişilik gruplar için maliyet avantajı da sağlar."
    },
    {
        "slug": "blog-buyukelcilik-arac-kiralama",
        "title": "Büyükelçilik ve Diplomatik Görevler İçin Araç Kiralama",
        "desc": "Ankara'daki büyükelçilikler ve uluslararası delegasyonlar için yüksek güvenlikli ve protokol kurallarına uygun transfer.",
        "content": "Ankara, diplomatik misyonların merkezidir. Yabancı delegasyonların ziyareti sırasında gizlilik, zaman yönetimi ve güvenlik en üst düzeyde olmalıdır. VipTrip, bu alandaki tecrübesiyle elçiliklerin güvendiği bir partnerdir."
    },
    {
        "slug": "blog-bolu-abant-tatili-ulasim",
        "title": "Bolu Abant Tatili İçin VIP Ulaşım Çözümleri",
        "desc": "Doğa ile iç içe bir hafta sonu için Ankara'dan Bolu Yedi Göller ve Abant'a şoförlü transfer.",
        "content": "Şehrin gürültüsünden kaçıp doğaya karışmak isteyen Ankaralılar için Abant vazgeçilmezdir. Özel aracınızla yorulmak yerine, VIP Vito ile arkanıza yaslanın, orman manzaralarının tadını çıkarın. Şoförümüz siz tatil yaparken aracı güvende tutar."
    },
    {
        "slug": "blog-ankarada-luks-otel-transferleri",
        "title": "Ankara'da Lüks Otel Transferleri",
        "desc": "Sheraton, JW Marriott, Lugal ve Ankara HiltonSA otellerine havalimanından VIP karşılama.",
        "content": "Ankara'nın 5 yıldızlı otellerinde konaklayan misafirlerimizin beklentisi ulaşımlarının da 5 yıldızlı olmasıdır. Esenboğa'dan aracınıza bindiğiniz andan otelinizin resepsiyonuna kadar lüks ve kesintisiz bir deneyim sunuyoruz."
    },
    {
        "slug": "blog-vip-araclarda-hangi-donanimlar-var",
        "title": "VIP Araçlarda Hangi Donanımlar Bulunur?",
        "desc": "Gerçek bir VIP transfer aracının sahip olması gereken özellikler, teknoloji ve konfor donanımları.",
        "content": "Bir aracın VIP sayılabilmesi için sadece siyah olması yetmez. İçerisinde elektrikli yatar deri koltuklar, gizlilik için makam perdesi, yıldızlı tavan aydınlatması, bağımsız iklimlendirme, buzdolabı ve 220V priz gibi donanımların bulunması gerekir."
    },
    {
        "slug": "blog-kurumsal-transfer-anlasmasi",
        "title": "Şirketler İçin Kurumsal Transfer Anlaşmasının Faydaları",
        "desc": "Firmalar için aylık faturalandırma ve kurumsal VIP taşımacılık anlaşmalarının avantajları.",
        "content": "Kurumsal sözleşmeler, şirketinizin ulaşım giderlerini kontrol altında tutmanızı sağlar. Her defasında araç arama derdi olmaz, öncelikli rezervasyon hakkı kazanırsınız ve tüm harcamalarınız ay sonunda tek bir detaylı faturada toplanır."
    },
    {
        "slug": "blog-ankara-vip-aracla-gezilecek-yerler",
        "title": "Ankara'da VİP Araçla Gezilecek En İyi 5 Yer",
        "desc": "Şehri ilk kez ziyaret edenler için Anıtkabir, Ankara Kalesi, Atakule ve müzeleri kapsayan şoförlü tur rotası.",
        "content": "1. Anıtkabir: Türkiye'nin kalbi.<br>2. Ankara Kalesi & Rahmi M. Koç Müzesi: Tarihi doku.<br>3. Atakule: Şehri kuşbakışı izleme keyfi.<br>4. Eymir Gölü: Doğa ile iç içe huzur.<br>5. Hamamönü: Restorasyon görmüş tarihi konaklar."
    },
    {
        "slug": "blog-havalimani-transfer-erken-rezervasyon",
        "title": "Havalimanı Transferinde Neden Erken Rezervasyon Yapılmalı?",
        "desc": "Son dakika stresi yaşamamak ve en uygun VIP aracı garantilemek için erken rezervasyonun önemi.",
        "content": "Özellikle bayram tatilleri, büyük kongre dönemleri veya fuar zamanlarında VIP araç bulmak zorlaşabilir. Uçuş biletinizi aldığınız anda transferinizi de planlamak, sizi son dakika sürprizlerinden ve olası streslerden korur."
    }
]

# Write out the 20 blog HTML files
with open(os.path.join(directory, "blog-anitkabir.html"), "r", encoding="utf-8") as f:
    blog_template = f.read()

for blog in blogs:
    html = blog_template
    # Replace metadata
    html = html.replace("<title>Anıtkabir Ulaşım & Ziyaret Rehberi | VipTrip Ankara</title>", f"<title>{blog['title']} | VipTrip Ankara</title>")
    html = html.replace('content="Ankara Anıtkabir ulaşım rehberi. Esenboğa\'dan Anıtkabir\'e VIP transfer, ziyaret saatleri ve protokol ulaşım hizmetleri."', f'content="{blog["desc"]}"')
    
    # Replace content
    html = html.replace("<h1>Anıtkabir Ulaşım & Ziyaret Rehberi</h1>", f"<h1>{blog['title']}</h1>")
    html = html.replace('<span class="blog-category">Rehber</span>', f'<span class="blog-category">Sektörel Haber</span>')
    html = html.replace('<span class="current">Anıtkabir Ziyareti</span>', f'<span class="current">{blog["title"]}</span>')
    
    # Simple content replacement (just clear out old paragraphs and insert new ones)
    content_start = html.find('<h2>Anıtkabir') # Find start of old content
    if content_start == -1:
         content_start = html.find('<p>Türkiye Cumhuriyeti\'nin kurucusu') # Fallback
    
    content_end = html.find('<section class="related-section">') # Find end of body content
    
    if content_start != -1 and content_end != -1:
        # Construct new content block
        new_content = f'<p>{blog["content"]}</p>\n<div class="cta-box">\n<h3>VIP Transfer Ayrıcalığı</h3>\n<p>Hemen rezervasyon yaparak konforun tadını çıkarın.</p>\n<div class="cta-buttons">\n<a href="https://wa.me/905453359706" class="btn-whatsapp" target="_blank"><i class="fab fa-whatsapp"></i> WhatsApp</a>\n</div>\n</div>\n'
        html = html[:content_start] + new_content + html[content_end:]

    filepath = os.path.join(directory, f"{blog['slug']}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: {blog['slug']}.html")

print("Finished generating pages.")
