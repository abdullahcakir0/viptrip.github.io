import os

cwd = "/Users/abdullahcakir/Desktop/viptrip"
index_path = os.path.join(cwd, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Find the 5th slide to duplicate
slide_5_marker = '<!-- Slide 5 -->'
end_of_slide_5 = '</div>\n                    </div>\n                    <!-- Navigation -->'
slide_6_marker = '<!-- Slide 6 -->'

if slide_6_marker not in html:
    new_slide = """
                        <!-- Slide 6 -->
                        <div class="swiper-slide insta-slide">
                            <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-card">
                                <div class="insta-img">
                                    <video src="assets/video/video6.mp4" loop muted playsinline preload="auto" style="width:100%; height:100%; object-fit:cover;"></video>
                                </div>
                                <div class="insta-info">
                                    <p class="insta-title">Özel Transfer</p>
                                    <p class="insta-sub">Size Özel Çözümler</p>
                                    <div class="insta-user">
                                        <i class="fab fa-instagram"></i> @viptrip.tr
                                    </div>
                                </div>
                            </a>
                        </div>
"""
    html = html.replace('<!-- Slide 5 -->', '<!-- Slide 5 -->') # just to check
    # Let's just insert it right before <!-- Navigation -->
    html = html.replace('                    <!-- Navigation -->', new_slide + '                    <!-- Navigation -->')

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Added Slide 6.")
