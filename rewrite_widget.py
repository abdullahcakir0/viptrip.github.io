import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"
index_path = os.path.join(cwd, "index.html")

# Restore index.html to the state before the bad video conversion
os.system("git checkout 02379e3 -- index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Build the flawless 6-slide video widget without info cards
widget = """<div class="instagram-feed-wrapper" data-aos="fade-up">
                <div class="swiper insta-swiper">
                    <div class="swiper-wrapper">
                        <!-- Slide 1 -->
                        <div class="swiper-slide insta-slide">
                            <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-card">
                                <div class="insta-img">
                                    <video src="assets/video/video1.mp4" loop muted playsinline preload="auto" style="width:100%; height:100%; object-fit:cover;"></video>
                                </div>
                            </a>
                        </div>
                        <!-- Slide 2 -->
                        <div class="swiper-slide insta-slide">
                            <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-card">
                                <div class="insta-img">
                                    <video src="assets/video/video2.mp4" loop muted playsinline preload="auto" style="width:100%; height:100%; object-fit:cover;"></video>
                                </div>
                            </a>
                        </div>
                        <!-- Slide 3 -->
                        <div class="swiper-slide insta-slide">
                            <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-card">
                                <div class="insta-img">
                                    <video src="assets/video/video3.mp4" loop muted playsinline preload="auto" style="width:100%; height:100%; object-fit:cover;"></video>
                                </div>
                            </a>
                        </div>
                        <!-- Slide 4 -->
                        <div class="swiper-slide insta-slide">
                            <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-card">
                                <div class="insta-img">
                                    <video src="assets/video/video4.mp4" loop muted playsinline preload="auto" style="width:100%; height:100%; object-fit:cover;"></video>
                                </div>
                            </a>
                        </div>
                        <!-- Slide 5 -->
                        <div class="swiper-slide insta-slide">
                            <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-card">
                                <div class="insta-img">
                                    <video src="assets/video/video5.mp4" loop muted playsinline preload="auto" style="width:100%; height:100%; object-fit:cover;"></video>
                                </div>
                            </a>
                        </div>
                        <!-- Slide 6 -->
                        <div class="swiper-slide insta-slide">
                            <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-card">
                                <div class="insta-img">
                                    <video src="assets/video/video6.mp4" loop muted playsinline preload="auto" style="width:100%; height:100%; object-fit:cover;"></video>
                                </div>
                            </a>
                        </div>
                    </div>
                    <!-- Navigation -->
                    <div class="swiper-button-next insta-next"></div>
                    <div class="swiper-button-prev insta-prev"></div>
                </div>
            </div>"""

html = re.sub(r'<div class="instagram-feed-wrapper" data-aos="fade-up">.*?</section>', widget + '\n        </div>\n    </section>', html, flags=re.DOTALL)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Rewrote instagram section.")
