import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"
index_path = os.path.join(cwd, "index.html")
style_path = os.path.join(cwd, "style.css")
script_path = os.path.join(cwd, "script.js")

# 1. Update index.html
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add Swiper CSS if not exists
if "swiper-bundle.min.css" not in html:
    html = html.replace('</title>', '</title>\n    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css" />')

# Build the Swiper HTML
swiper_html = """
                <div class="swiper insta-swiper">
                    <div class="swiper-wrapper">
                        <!-- Slide 1 -->
                        <div class="swiper-slide insta-slide">
                            <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-card">
                                <div class="insta-img">
                                    <img src="assets/img/vip_transfer_ankara.png" alt="Ankara VIP Transfer Instagram">
                                </div>
                                <div class="insta-info">
                                    <p class="insta-title">Ankara VIP Transfer</p>
                                    <p class="insta-sub">Lüks & Prestij</p>
                                    <div class="insta-user">
                                        <i class="fab fa-instagram"></i> @viptrip.tr
                                    </div>
                                </div>
                            </a>
                        </div>
                        <!-- Slide 2 -->
                        <div class="swiper-slide insta-slide">
                            <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-card">
                                <div class="insta-img">
                                    <img src="assets/img/esenboga_havalimani_transfer.png" alt="Esenboğa VIP Transfer Instagram">
                                </div>
                                <div class="insta-info">
                                    <p class="insta-title">Esenboğa Karşılama</p>
                                    <p class="insta-sub">7/24 Kesintisiz</p>
                                    <div class="insta-user">
                                        <i class="fab fa-instagram"></i> @viptrip.tr
                                    </div>
                                </div>
                            </a>
                        </div>
                        <!-- Slide 3 -->
                        <div class="swiper-slide insta-slide">
                            <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-card">
                                <div class="insta-img">
                                    <img src="assets/img/sehirler_arasi_transfer.png" alt="Şehirler Arası VIP Transfer Instagram">
                                </div>
                                <div class="insta-info">
                                    <p class="insta-title">Şehirler Arası VIP</p>
                                    <p class="insta-sub">Konforlu Seyahat</p>
                                    <div class="insta-user">
                                        <i class="fab fa-instagram"></i> @viptrip.tr
                                    </div>
                                </div>
                            </a>
                        </div>
                        <!-- Slide 4 -->
                        <div class="swiper-slide insta-slide">
                            <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-card">
                                <div class="insta-img">
                                    <img src="assets/img/mercedes_vito_kiralama.png" alt="Mercedes Vito Kiralama Instagram">
                                </div>
                                <div class="insta-info">
                                    <p class="insta-title">Vito & Sprinter</p>
                                    <p class="insta-sub">Geniş Filo</p>
                                    <div class="insta-user">
                                        <i class="fab fa-instagram"></i> @viptrip.tr
                                    </div>
                                </div>
                            </a>
                        </div>
                        <!-- Slide 5 -->
                        <div class="swiper-slide insta-slide">
                            <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-card">
                                <div class="insta-img">
                                    <img src="assets/img/soforlu_arac_kiralama.png" alt="Şoförlü Araç Kiralama Instagram">
                                </div>
                                <div class="insta-info">
                                    <p class="insta-title">Şoförlü Kiralama</p>
                                    <p class="insta-sub">VIP Asistanlık</p>
                                    <div class="insta-user">
                                        <i class="fab fa-instagram"></i> @viptrip.tr
                                    </div>
                                </div>
                            </a>
                        </div>
                    </div>
                    <!-- Navigation -->
                    <div class="swiper-button-next insta-next"></div>
                    <div class="swiper-button-prev insta-prev"></div>
                </div>
"""

# Replace the old feed wrapper content
body_pattern = r'(<div class="instagram-feed-wrapper" data-aos="fade-up">).*?(</div>\s*</div>\s*</section>)'
html = re.sub(body_pattern, f'\\1\n{swiper_html}\n\\2', html, flags=re.DOTALL)

# Add Swiper JS if not exists
if "swiper-bundle.min.js" not in html:
    html = html.replace('</body>', '<script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>\n</body>')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

# 2. Add Swiper Initialization to script.js
with open(script_path, "r", encoding="utf-8") as f:
    js = f.read()

if "Swiper('.insta-swiper'" not in js:
    swiper_init = """
document.addEventListener('DOMContentLoaded', () => {
    if(document.querySelector('.insta-swiper')) {
        const swiper = new Swiper('.insta-swiper', {
            effect: 'coverflow',
            grabCursor: true,
            centeredSlides: true,
            slidesPerView: 'auto',
            loop: true,
            coverflowEffect: {
                rotate: 0,
                stretch: 0,
                depth: 100,
                modifier: 2,
                slideShadows: true,
            },
            navigation: {
                nextEl: '.insta-next',
                prevEl: '.insta-prev',
            },
            autoplay: {
                delay: 3000,
                disableOnInteraction: false,
            }
        });
    }
});
"""
    with open(script_path, "a", encoding="utf-8") as f:
        f.write(swiper_init)

# 3. Add CSS for Instagram Widget
with open(style_path, "r", encoding="utf-8") as f:
    css = f.read()

if ".insta-swiper" not in css:
    custom_css = """
/* Instagram Widget Styles */
.insta-section {
    padding: 60px 0;
    background: #fdfdfd;
    overflow: hidden;
}

.insta-swiper {
    width: 100%;
    padding: 50px 0 !important;
}

.insta-slide {
    width: 280px;
    height: 480px;
    transition: all 0.3s ease;
}

.insta-card {
    display: block;
    width: 100%;
    height: 100%;
    position: relative;
    border-radius: 20px;
    text-decoration: none;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    transform: scale(0.9);
    transition: transform 0.3s ease;
}

.swiper-slide-active .insta-card {
    transform: scale(1.05);
    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
}

.insta-img {
    width: 100%;
    height: 100%;
    border-radius: 20px;
    overflow: hidden;
}

.insta-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.insta-info {
    position: absolute;
    bottom: -20px;
    left: 50%;
    transform: translateX(-50%);
    width: 85%;
    background: #fff;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    text-align: center;
    color: #333;
}

.insta-info .insta-title {
    font-size: 0.95rem;
    font-weight: 700;
    margin: 0 0 5px 0;
    color: #111;
}

.insta-info .insta-sub {
    font-size: 0.8rem;
    color: #777;
    margin: 0 0 10px 0;
}

.insta-user {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-size: 0.85rem;
    color: #C13584; /* Instagram Brand Color */
    font-weight: 600;
}

.insta-prev, .insta-next {
    color: #fff !important;
    background: rgba(0,0,0,0.6);
    width: 45px !important;
    height: 45px !important;
    border-radius: 50%;
    backdrop-filter: blur(5px);
}
.insta-prev:after, .insta-next:after {
    font-size: 1.2rem !important;
    font-weight: bold;
}
.insta-prev { left: 20px !important; }
.insta-next { right: 20px !important; }

@media (max-width: 768px) {
    .insta-slide {
        width: 240px;
        height: 420px;
    }
    .insta-prev, .insta-next { display: none !important; }
}
"""
    with open(style_path, "a", encoding="utf-8") as f:
        f.write(custom_css)

print("Instagram widget successfully injected!")
