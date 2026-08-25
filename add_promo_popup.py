import os

cwd = "/Users/abdullahcakir/Desktop/viptrip"

html_code = """
<!-- AVANTAJLI PAKET PROMO MODAL -->
<div class="promo-modal-overlay" id="promoModal">
    <div class="promo-modal-content">
        <span class="promo-modal-close" id="closePromoModal">&times;</span>
        <div class="promo-modal-image">
            <img src="assets/img/vito-dis-yan.jpg" alt="VIP Gelin Arabası">
            <div class="promo-badge">%20 İndirim</div>
        </div>
        <div class="promo-modal-text">
            <h3>Avantajlı Gelin Arabası Paketi!</h3>
            <p>2026 sezonuna özel; Mercedes Vito, profesyonel süsleme ve gün boyu VIP şoför hizmetiyle en mutlu gününüzü taçlandırın.</p>
            <ul class="promo-features">
                <li><i class="fas fa-check-circle"></i> Süsleme Dahil</li>
                <li><i class="fas fa-check-circle"></i> Sınırsız İkram</li>
                <li><i class="fas fa-check-circle"></i> Özel VIP Şoför</li>
            </ul>
            <div class="promo-price">9.000₺<span>'den başlayan fiyatlarla</span></div>
            <a href="vip-gelin-arabasi.html" class="promo-btn">Hemen İncele & Rezervasyon Yap</a>
        </div>
    </div>
</div>
"""

css_code = """
/* =========================================
   PROMO MODAL (ANA SAYFA GELİN ARABASI)
   ========================================= */
.promo-modal-overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.85);
    z-index: 10000;
    justify-content: center;
    align-items: center;
    backdrop-filter: blur(5px);
}
.promo-modal-overlay.active {
    display: flex;
    animation: fadeInModal 0.4s ease forwards;
}
.promo-modal-content {
    background: #111;
    border: 1px solid #D4AF37;
    border-radius: 12px;
    width: 90%;
    max-width: 600px;
    position: relative;
    box-shadow: 0 10px 40px rgba(212, 175, 55, 0.15);
    transform: translateY(20px);
    opacity: 0;
    animation: slideUpModal 0.4s ease 0.1s forwards;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}
@media (min-width: 600px) {
    .promo-modal-content {
        flex-direction: row;
        max-width: 800px;
    }
}
.promo-modal-image {
    position: relative;
    flex: 1;
}
.promo-modal-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    min-height: 200px;
}
.promo-badge {
    position: absolute;
    top: 15px;
    left: 15px;
    background: #e74c3c;
    color: #fff;
    padding: 5px 10px;
    border-radius: 5px;
    font-weight: 700;
    font-size: 0.9rem;
    box-shadow: 0 2px 5px rgba(0,0,0,0.5);
}
.promo-modal-close {
    position: absolute;
    top: 10px;
    right: 15px;
    color: #fff;
    font-size: 28px;
    cursor: pointer;
    transition: color 0.3s;
    z-index: 2;
    text-shadow: 0 2px 4px rgba(0,0,0,0.5);
}
.promo-modal-close:hover {
    color: #D4AF37;
}
.promo-modal-text {
    flex: 1.5;
    padding: 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.promo-modal-text h3 {
    color: #D4AF37;
    font-size: 1.5rem;
    margin-bottom: 15px;
}
.promo-modal-text p {
    color: #ccc;
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: 15px;
}
.promo-features {
    list-style: none;
    margin-bottom: 20px;
    padding: 0;
}
.promo-features li {
    margin-bottom: 8px;
    color: #fff;
    font-size: 0.9rem;
}
.promo-features li i {
    color: #D4AF37;
    margin-right: 10px;
}
.promo-price {
    font-size: 1.6rem;
    color: #fff;
    font-weight: 700;
    margin-bottom: 20px;
}
.promo-price span {
    font-size: 0.9rem;
    color: #aaa;
    font-weight: 400;
}
.promo-btn {
    display: inline-block;
    padding: 12px 25px;
    background: #D4AF37;
    color: #000;
    text-decoration: none;
    font-weight: 700;
    border-radius: 5px;
    text-align: center;
    transition: background 0.3s;
}
.promo-btn:hover {
    background: #fff;
    color: #000;
}
"""

js_code = """
/* =========================================
   PROMO MODAL (ANA SAYFA GELİN ARABASI)
   ========================================= */
document.addEventListener('DOMContentLoaded', () => {
    const promoModal = document.getElementById('promoModal');
    const closePromoModal = document.getElementById('closePromoModal');

    if (promoModal && closePromoModal) {
        // Close modal on 'X' click
        closePromoModal.addEventListener('click', () => {
            promoModal.classList.remove('active');
        });

        // Close modal when clicking outside
        promoModal.addEventListener('click', (e) => {
            if (e.target === promoModal) {
                promoModal.classList.remove('active');
            }
        });

        // Automatically open modal after 5 seconds if not opened in this session
        if (!sessionStorage.getItem('promoModalShown')) {
            setTimeout(() => {
                promoModal.classList.add('active');
                sessionStorage.setItem('promoModalShown', 'true');
            }, 5000);
        }
    }
});
"""

def update_index_html():
    filepath = os.path.join(cwd, "index.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="promoModal"' not in content:
        if '</body>' in content:
            content = content.replace('</body>', f"{html_code}\n</body>")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Updated index.html")

def update_css():
    filepath = os.path.join(cwd, "style.css")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if '.promo-modal-overlay' not in content:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(f"\n{css_code}\n")
        print("Updated style.css")

def update_js():
    filepath = os.path.join(cwd, "script.js")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'PROMO MODAL' not in content:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(f"\n{js_code}\n")
        print("Updated script.js")

if __name__ == '__main__':
    update_index_html()
    update_css()
    update_js()
    print("Done!")
