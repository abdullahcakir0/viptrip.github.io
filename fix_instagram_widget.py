import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"
index_path = os.path.join(cwd, "index.html")
style_path = os.path.join(cwd, "style.css")
script_path = os.path.join(cwd, "script.js")

# 1. Update style.css to dark background
with open(style_path, "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("background: #fdfdfd;", "background: #000000;")
css = css.replace("color: #333;", "color: #fff;") # If info card was white, user might want it to match or stand out. Wait, info card can stay white for contrast, but let's change section background.
# Wait, if info card is white, it looks like a real Instagram card. Let's keep it white.
# Just changing .insta-section background:
css = re.sub(r'(\.insta-section\s*\{[^}]*background:\s*)#[a-fA-F0-9]+', r'\g<1>#0a0a0a', css)

with open(style_path, "w", encoding="utf-8") as f:
    f.write(css)

# 2. Update script.js for video play/pause
with open(script_path, "r", encoding="utf-8") as f:
    js = f.read()

# Replace the existing Swiper initialization for insta-swiper
old_swiper = """        const swiper = new Swiper('.insta-swiper', {
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
        });"""

new_swiper = """        const swiper = new Swiper('.insta-swiper', {
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
            /* autoplay: { delay: 3000, disableOnInteraction: false, }, */
            on: {
                init: function () {
                    const activeSlide = this.slides[this.activeIndex];
                    const video = activeSlide.querySelector('video');
                    if(video) {
                        video.play().catch(e=>console.log(e));
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
                        video.play().catch(e=>console.log(e));
                    }
                }
            }
        });"""

js = js.replace(old_swiper, new_swiper)

with open(script_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Updated background and JS logic.")
