import os
import re
import ast

directory = "/Users/abdullahcakir/Desktop/viptrip"

# Read the original create_pages.py to extract the blogs array
with open(os.path.join(directory, "create_pages.py"), "r", encoding="utf-8") as f:
    text = f.read()

start = text.find('blogs = [')
end = text.find(']', start) + 1
blogs_str = text[start:end]
blogs = ast.literal_eval(blogs_str.split('blogs = ')[1])

for blog in blogs:
    slug = blog["slug"]
    filepath = os.path.join(directory, f"{slug}.html")
    
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
        
    # We want to replace everything between <section class="blog-body"> and <section class="related-section">
    start_marker = '<section class="blog-body">'
    end_marker = '<section class="related-section">'
    
    start_idx = html.find(start_marker)
    end_idx = html.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        # Create rich content for the blog body
        new_body = f"""<section class="blog-body">
        <div class="container">
            <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">{blog['content']}</p>

            <h2>{blog['title']} Detayları</h2>
            <p>VipTrip olarak amacımız, sadece A noktasından B noktasına ulaşım sağlamak değil, aynı zamanda yolculuğunuzun her anını lüks, güvenli ve konforlu bir deneyime dönüştürmektir. Alanında uzman şoförlerimiz ve son model Mercedes-Benz araçlarımızla her zaman yanınızdayız.</p>

            <div class="highlight-box">
                <h3><i class="fas fa-star"></i> Neden Bizi Tercih Etmelisiniz?</h3>
                <ul class="checklist">
                    <li><i class="fas fa-check-circle"></i> <strong>7/24 Hizmet:</strong> İhtiyaç duyduğunuz her an VIP araçlarımız hizmetinizde.</li>
                    <li><i class="fas fa-check-circle"></i> <strong>Profesyonel Şoförler:</strong> Yabancı dil bilen, deneyimli ve güler yüzlü ekip.</li>
                    <li><i class="fas fa-check-circle"></i> <strong>Üst Düzey Güvenlik:</strong> Araçlarımız düzenli bakımdan geçer ve tam donanımlıdır.</li>
                    <li><i class="fas fa-check-circle"></i> <strong>Şeffaf Fiyatlandırma:</strong> Sürpriz ücretler olmadan, sabit ve güvenilir fiyatlar.</li>
                </ul>
            </div>

            <h2>VIP Transferin Avantajları</h2>
            <p>Standart ulaşım yöntemleri stresli ve yorucu olabilir. Özellikle iş seyahatlerinde, özel günlerde veya yabancı misafir ağırlamalarında VIP transfer hizmeti, zaman kazandırır ve prestij sağlar. İster şehir içi yoğun trafikte, ister şehirlerarası uzun yolculuklarda olun, aracınızın içinde kendinizi evinizde veya ofisinizde hissedeceksiniz.</p>

            <div class="cta-box">
                <h3><i class="fas fa-car"></i> Yerinizi Hemen Ayırtın</h3>
                <p>Mercedes Vito, Sprinter veya S-Class araçlarımızla VIP konforunu yaşamak için bizimle iletişime geçin.</p>
                <div class="cta-buttons">
                    <a href="/#transfer" class="btn-gold"><i class="fas fa-calculator"></i> Fiyat Hesapla</a>
                    <a href="https://wa.me/905453359706?text=Merhaba,%20VIP%20transfer%20için%20bilgi%20almak%20istiyorum." class="btn-whatsapp" target="_blank"><i class="fab fa-whatsapp"></i> WhatsApp</a>
                </div>
            </div>
        </div>
    </section>

    """
        
        # Replace the old body with the new body
        html = html[:start_idx] + new_body + html[end_idx:]
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Updated content for: {slug}.html")
    else:
        print(f"Could not find body section in {slug}.html")

print("All blog posts have been successfully rewritten with unique content!")
