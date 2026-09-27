import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"
index_path = os.path.join(cwd, "index.html")
script_path = os.path.join(cwd, "script.js")

# 1. Update HTML
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

mute_btn_html = """
                    <!-- Mute Toggle -->
                    <div class="insta-mute-btn" style="position: absolute; bottom: 30px; right: 30px; z-index: 100; background: rgba(0,0,0,0.7); color: white; width: 45px; height: 45px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; backdrop-filter: blur(5px); box-shadow: 0 4px 10px rgba(0,0,0,0.3);">
                        <i class="fas fa-volume-up"></i>
                    </div>
"""
if "insta-mute-btn" not in html:
    html = html.replace('<!-- Navigation -->', mute_btn_html + '                    <!-- Navigation -->')
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)

# 2. Update JS
with open(script_path, "r", encoding="utf-8") as f:
    js = f.read()

# I need to update the Swiper initialization again to respect the mute state, and add event listener for the button
old_swiper_pattern = r"const swiper = new Swiper\('\.insta-swiper', \{.*?\n        \}\);"

new_swiper = """
        window.instaGlobalMuted = false;
        
        const muteBtn = document.querySelector('.insta-mute-btn');
        const muteIcon = document.querySelector('.insta-mute-btn i');
        
        muteBtn.addEventListener('click', () => {
            window.instaGlobalMuted = !window.instaGlobalMuted;
            if (window.instaGlobalMuted) {
                muteIcon.classList.remove('fa-volume-up');
                muteIcon.classList.add('fa-volume-mute');
            } else {
                muteIcon.classList.remove('fa-volume-mute');
                muteIcon.classList.add('fa-volume-up');
            }
            
            // Apply to active video immediately
            if (swiper && swiper.slides) {
                const activeSlide = swiper.slides[swiper.activeIndex];
                if (activeSlide) {
                    const video = activeSlide.querySelector('video');
                    if (video) video.muted = window.instaGlobalMuted;
                }
            }
        });

        const swiper = new Swiper('.insta-swiper', {
            grabCursor: true,
            centeredSlides: true,
            slidesPerView: 'auto',
            spaceBetween: 20,
            loop: true,
            loopedSlides: 6,
            navigation: {
                nextEl: '.insta-next',
                prevEl: '.insta-prev',
            },
            on: {
                init: function () {
                    const activeSlide = this.slides[this.activeIndex];
                    const video = activeSlide.querySelector('video');
                    if(video) {
                        video.muted = window.instaGlobalMuted;
                        video.play().catch(e => {
                            video.muted = true;
                            video.play();
                        });
                    }
                },
                slideChangeTransitionEnd: function () {
                    this.slides.forEach(slide => {
                        const video = slide.querySelector('video');
                        if (video) video.pause();
                    });
                    const activeSlide = this.slides[this.activeIndex];
                    const video = activeSlide.querySelector('video');
                    if(video) {
                        video.currentTime = 0;
                        video.muted = window.instaGlobalMuted;
                        const playPromise = video.play();
                        if (playPromise !== undefined) {
                            playPromise.catch(e => {
                                video.muted = true;
                                video.play();
                            });
                        }
                    }
                }
            }
        });"""

js = re.sub(old_swiper_pattern, new_swiper, js, flags=re.DOTALL)

with open(script_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Added mute button and updated JS logic.")
