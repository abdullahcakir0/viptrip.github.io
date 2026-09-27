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
            
            <div class="insta-grid" data-aos="fade-up">
                <!-- Video 1 -->
                <div class="insta-grid-item">
                    <video src="assets/video/video1.mp4" autoplay loop muted playsinline></video>
                    <div class="insta-grid-overlay">
                        <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-btn"><i class="fab fa-instagram"></i> İncele</a>
                        <button class="mute-btn" title="Sesi Aç/Kapat"><i class="fas fa-volume-mute"></i></button>
                    </div>
                </div>
                <!-- Video 2 -->
                <div class="insta-grid-item">
                    <video src="assets/video/video2.mp4" autoplay loop muted playsinline></video>
                    <div class="insta-grid-overlay">
                        <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-btn"><i class="fab fa-instagram"></i> İncele</a>
                        <button class="mute-btn" title="Sesi Aç/Kapat"><i class="fas fa-volume-mute"></i></button>
                    </div>
                </div>
                <!-- Video 3 -->
                <div class="insta-grid-item">
                    <video src="assets/video/video3.mp4" autoplay loop muted playsinline></video>
                    <div class="insta-grid-overlay">
                        <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-btn"><i class="fab fa-instagram"></i> İncele</a>
                        <button class="mute-btn" title="Sesi Aç/Kapat"><i class="fas fa-volume-mute"></i></button>
                    </div>
                </div>
                <!-- Video 4 -->
                <div class="insta-grid-item">
                    <video src="assets/video/video4.mp4" autoplay loop muted playsinline></video>
                    <div class="insta-grid-overlay">
                        <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-btn"><i class="fab fa-instagram"></i> İncele</a>
                        <button class="mute-btn" title="Sesi Aç/Kapat"><i class="fas fa-volume-mute"></i></button>
                    </div>
                </div>
                <!-- Video 5 -->
                <div class="insta-grid-item">
                    <video src="assets/video/video5.mp4" autoplay loop muted playsinline></video>
                    <div class="insta-grid-overlay">
                        <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-btn"><i class="fab fa-instagram"></i> İncele</a>
                        <button class="mute-btn" title="Sesi Aç/Kapat"><i class="fas fa-volume-mute"></i></button>
                    </div>
                </div>
                <!-- Video 6 -->
                <div class="insta-grid-item">
                    <video src="assets/video/video6.mp4" autoplay loop muted playsinline></video>
                    <div class="insta-grid-overlay">
                        <a href="https://www.instagram.com/viptrip.tr" target="_blank" class="insta-btn"><i class="fab fa-instagram"></i> İncele</a>
                        <button class="mute-btn" title="Sesi Aç/Kapat"><i class="fas fa-volume-mute"></i></button>
                    </div>
                </div>
            </div>
        </div>
    </section>"""

html = re.sub(r'<section class="insta-section">.*?</section>', new_html_block, html, flags=re.DOTALL)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)


# --- 2. REBUILD STYLE.CSS ---
with open(style_path, "r", encoding="utf-8") as f:
    css = f.read()

css = re.sub(r'/\* Instagram Widget Styles REBUILT \*/.*', '', css, flags=re.DOTALL)

new_css = """/* Instagram Static Grid Styles */
.insta-section {
    padding: 80px 0;
    background: #0a0a0a;
}
.insta-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    margin-top: 40px;
}
.insta-grid-item {
    position: relative;
    border-radius: 20px;
    overflow: hidden;
    aspect-ratio: 9/16;
    background: #111;
    box-shadow: 0 5px 15px rgba(0,0,0,0.5);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.insta-grid-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(212, 175, 55, 0.2);
}
.insta-grid-item video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}
.insta-grid-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 25px 20px;
    background: linear-gradient(to top, rgba(0,0,0,0.95), rgba(0,0,0,0.4) 50%, transparent);
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    opacity: 0;
    transition: opacity 0.3s ease;
}
.insta-grid-item:hover .insta-grid-overlay {
    opacity: 1;
}
.insta-btn {
    background: #D4AF37;
    color: #000;
    padding: 10px 18px;
    border-radius: 25px;
    text-decoration: none;
    font-weight: 700;
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: background 0.3s;
}
.insta-btn:hover {
    background: #fff;
    color: #000;
}
.mute-btn {
    background: rgba(255,255,255,0.2);
    border: 1px solid rgba(255,255,255,0.4);
    color: #fff;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    backdrop-filter: blur(5px);
    transition: background 0.3s;
}
.mute-btn:hover {
    background: rgba(255,255,255,0.5);
}
@media (max-width: 992px) {
    .insta-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
    }
    .insta-grid-overlay {
        opacity: 1; /* Always show buttons on tablet */
    }
}
@media (max-width: 576px) {
    .insta-grid {
        grid-template-columns: 1fr;
        gap: 30px;
        max-width: 350px;
        margin-left: auto;
        margin-right: auto;
    }
    .insta-grid-overlay {
        opacity: 1; /* Always show buttons on mobile */
    }
}
"""

with open(style_path, "w", encoding="utf-8") as f:
    f.write(css + "\n" + new_css)

# --- 3. REBUILD SCRIPT.JS ---
with open(script_path, "r", encoding="utf-8") as f:
    js = f.read()

# Strip any old insta JS (which we did last time, but just in case we didn't get all of it or if we are building fresh)
# Actually, the previous commit removed all the old stuff. 
new_js = """
    // Instagram Static Grid Video Mute Toggles
    document.querySelectorAll('.mute-btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const video = this.closest('.insta-grid-item').querySelector('video');
            const icon = this.querySelector('i');
            
            if(video.muted) {
                video.muted = false;
                icon.className = 'fas fa-volume-up';
            } else {
                video.muted = true;
                icon.className = 'fas fa-volume-mute';
            }
        });
    });
"""

# Append to DOMContentLoaded
js = js.replace("document.addEventListener('DOMContentLoaded', () => {", "document.addEventListener('DOMContentLoaded', () => {\n" + new_js)

with open(script_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Swapped to Static Grid successfully.")
