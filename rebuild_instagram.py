import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"
index_path = os.path.join(cwd, "index.html")
style_path = os.path.join(cwd, "style.css")
script_path = os.path.join(cwd, "script.js")

# --- 1. REBUILD INDEX.HTML ---
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

new_html_block = """<section class="insta-section">
        <div class="container">
            <div class="section-title" data-aos="fade-up">
                <h2>INSTAGRAM'DA <span class="gold-text">BİZ</span></h2>
                <p>Referanslarımız ve araçlarımız: <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-link">@viptrip.tr</a></p>
            </div>
        </div>
        
        <div class="insta-slider-container" data-aos="fade-up">
            <div class="swiper insta-swiper">
                <div class="swiper-wrapper">
                    <!-- Slide 1 -->
                    <div class="swiper-slide insta-slide">
                        <video src="assets/video/video1.mp4" loop playsinline preload="auto" muted></video>
                        <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-overlay"><i class="fab fa-instagram"></i></a>
                    </div>
                    <!-- Slide 2 -->
                    <div class="swiper-slide insta-slide">
                        <video src="assets/video/video2.mp4" loop playsinline preload="auto" muted></video>
                        <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-overlay"><i class="fab fa-instagram"></i></a>
                    </div>
                    <!-- Slide 3 -->
                    <div class="swiper-slide insta-slide">
                        <video src="assets/video/video3.mp4" loop playsinline preload="auto" muted></video>
                        <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-overlay"><i class="fab fa-instagram"></i></a>
                    </div>
                    <!-- Slide 4 -->
                    <div class="swiper-slide insta-slide">
                        <video src="assets/video/video4.mp4" loop playsinline preload="auto" muted></video>
                        <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-overlay"><i class="fab fa-instagram"></i></a>
                    </div>
                    <!-- Slide 5 -->
                    <div class="swiper-slide insta-slide">
                        <video src="assets/video/video5.mp4" loop playsinline preload="auto" muted></video>
                        <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-overlay"><i class="fab fa-instagram"></i></a>
                    </div>
                    <!-- Slide 6 -->
                    <div class="swiper-slide insta-slide">
                        <video src="assets/video/video6.mp4" loop playsinline preload="auto" muted></video>
                        <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-overlay"><i class="fab fa-instagram"></i></a>
                    </div>
                </div>
                
                <div class="insta-controls">
                    <div class="swiper-button-prev insta-btn-prev"></div>
                    <div class="insta-mute-btn" id="instaMuteToggle" title="Sesi Aç/Kapat">
                        <i class="fas fa-volume-mute"></i>
                    </div>
                    <div class="swiper-button-next insta-btn-next"></div>
                </div>
            </div>
        </div>
    </section>"""

# Replace the whole section
html = re.sub(r'<section class="insta-section">.*?</section>', new_html_block, html, flags=re.DOTALL)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)


# --- 2. REBUILD STYLE.CSS ---
with open(style_path, "r", encoding="utf-8") as f:
    css = f.read()

# Strip all old insta related css
css = re.sub(r'/\* Instagram Widget Styles \*/.*', '', css, flags=re.DOTALL)
css = re.sub(r'\.insta-section\s*\{[^}]*\}', '', css)
css = re.sub(r'\.instagram-feed-wrapper\s*\{[^}]*\}', '', css)

new_css = """/* Instagram Widget Styles REBUILT */
.insta-section {
    padding: 80px 0;
    background: #0a0a0a;
    overflow: hidden;
    position: relative;
}
.insta-slider-container {
    width: 100%;
    position: relative;
    padding: 40px 0;
}
.insta-swiper {
    width: 100%;
    padding-top: 30px;
    padding-bottom: 30px;
}
.insta-slide {
    width: 300px;
    height: 520px;
    border-radius: 25px;
    overflow: hidden;
    transform: scale(0.85);
    transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.6s ease;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    position: relative;
    background: #111;
}
.swiper-slide-active.insta-slide {
    transform: scale(1.15);
    box-shadow: 0 20px 60px rgba(0,0,0,0.9);
    z-index: 10;
}
.insta-slide video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    border-radius: 25px;
}
.insta-overlay {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 50px;
    height: 50px;
    background: rgba(255,255,255,0.2);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    font-size: 24px;
    text-decoration: none;
    opacity: 0;
    transition: opacity 0.3s;
}
.swiper-slide-active:hover .insta-overlay {
    opacity: 1;
}
.insta-controls {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 25px;
    margin-top: 40px;
    position: relative;
    z-index: 20;
}
.insta-btn-prev, .insta-btn-next {
    position: static !important;
    width: 45px !important;
    height: 45px !important;
    background: rgba(255,255,255,0.1) !important;
    border-radius: 50%;
    color: #fff !important;
    margin: 0 !important;
    transition: background 0.3s;
}
.insta-btn-prev:hover, .insta-btn-next:hover {
    background: rgba(255,255,255,0.2) !important;
}
.insta-btn-prev::after, .insta-btn-next::after {
    font-size: 16px !important;
    font-weight: bold;
}
.insta-mute-btn {
    width: 55px;
    height: 55px;
    background: rgba(212, 175, 55, 0.15);
    border: 1px solid rgba(212, 175, 55, 0.5);
    border-radius: 50%;
    color: #d4af37;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    cursor: pointer;
    transition: all 0.3s;
}
.insta-mute-btn:hover {
    background: rgba(212, 175, 55, 0.3);
    transform: scale(1.05);
}
@media (max-width: 768px) {
    .insta-slide {
        width: 240px;
        height: 420px;
    }
}
"""
with open(style_path, "w", encoding="utf-8") as f:
    f.write(css + "\n" + new_css)


# --- 3. REBUILD SCRIPT.JS ---
with open(script_path, "r", encoding="utf-8") as f:
    js = f.read()

# Strip all old insta swiper logic
js = re.sub(r'window\.instaGlobalMuted.*?\n        \n        const muteBtn = .*?\n.*?\n        \}\);', '', js, flags=re.DOTALL)
js = re.sub(r'const swiper = new Swiper\(\'\.insta-swiper\'.*?\}\);', '', js, flags=re.DOTALL)
# One more sweep for any leftovers
js = re.sub(r'// Apply to active video immediately.*?\}\);', '', js, flags=re.DOTALL)

new_js = """
    let instaMuted = true;
    if(document.querySelector('.insta-swiper')) {
        const instaSwiper = new Swiper('.insta-swiper', {
            grabCursor: true,
            centeredSlides: true,
            slidesPerView: 'auto',
            spaceBetween: 0,
            loop: true,
            loopedSlides: 6,
            speed: 600,
            navigation: {
                nextEl: '.insta-btn-next',
                prevEl: '.insta-btn-prev',
            },
            on: {
                init: function () {
                    const activeSlide = this.slides[this.activeIndex];
                    if(activeSlide) {
                        const video = activeSlide.querySelector('video');
                        if (video) {
                            video.muted = instaMuted;
                            video.play().catch(e => console.log("Autoplay block on init"));
                        }
                    }
                },
                slideChangeTransitionStart: function () {
                    this.slides.forEach(slide => {
                        const video = slide.querySelector('video');
                        if (video) {
                            video.pause();
                            video.currentTime = 0;
                        }
                    });
                },
                slideChangeTransitionEnd: function () {
                    const activeSlide = this.slides[this.activeIndex];
                    if(activeSlide) {
                        const video = activeSlide.querySelector('video');
                        if (video) {
                            video.muted = instaMuted;
                            video.play().catch(e => console.log("Autoplay block on change"));
                        }
                    }
                }
            }
        });

        const muteToggle = document.getElementById('instaMuteToggle');
        if(muteToggle) {
            muteToggle.addEventListener('click', function() {
                instaMuted = !instaMuted;
                const icon = this.querySelector('i');
                if(instaMuted) {
                    icon.className = 'fas fa-volume-mute';
                } else {
                    icon.className = 'fas fa-volume-up';
                }
                const activeVideo = document.querySelector('.swiper-slide-active video');
                if(activeVideo) {
                    activeVideo.muted = instaMuted;
                }
            });
        }
    }
"""

js = js.replace("document.addEventListener('DOMContentLoaded', () => {", "document.addEventListener('DOMContentLoaded', () => {\n" + new_js)

with open(script_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Completely rebuilt instagram section with pristine clean code.")
