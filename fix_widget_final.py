import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"
index_path = os.path.join(cwd, "index.html")
script_path = os.path.join(cwd, "script.js")
style_path = os.path.join(cwd, "style.css")

# 1. Update index.html to remove 'muted' attribute from videos
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace muted with empty string in all video tags in the widget
html = re.sub(r'<video (.*?) muted (.*?)>', r'<video \1 \2>', html)
# Just in case they are different order:
html = html.replace(' muted ', ' ')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)


# 2. Update script.js to change Swiper effect to flat centered (no coverflow) and fix sound logic
with open(script_path, "r", encoding="utf-8") as f:
    js = f.read()

# We need to replace the entire Swiper('.insta-swiper' block
old_swiper_pattern = r"const swiper = new Swiper\('\.insta-swiper', \{.*?\n        \}\);"

new_swiper = """const swiper = new Swiper('.insta-swiper', {
            grabCursor: true,
            centeredSlides: true,
            slidesPerView: 'auto',
            spaceBetween: 20,
            loop: true,
            navigation: {
                nextEl: '.insta-next',
                prevEl: '.insta-prev',
            },
            on: {
                init: function () {
                    const activeSlide = this.slides[this.activeIndex];
                    const video = activeSlide.querySelector('video');
                    if(video) {
                        video.muted = false;
                        video.play().catch(e => {
                            console.log("Autoplay blocked, muting...", e);
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
                        video.muted = false; // Try with sound on slide change
                        const playPromise = video.play();
                        if (playPromise !== undefined) {
                            playPromise.catch(e => {
                                console.log("Play failed, retrying muted...", e);
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

# 3. Enhance CSS so it looks like the reference image (larger center, spacing)
with open(style_path, "r", encoding="utf-8") as f:
    css = f.read()

# We can make the non-active cards slightly transparent or just smaller.
# Already have:
# .insta-card { transform: scale(0.9); transition: transform 0.3s ease; }
# .swiper-slide-active .insta-card { transform: scale(1.05); }

with open(style_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed Swiper layout and Sound.")
