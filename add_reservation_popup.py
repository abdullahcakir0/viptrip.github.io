import os
import glob

html_code = """
<!-- Erken Rezervasyon Float Button -->
<div class="early-res-float" id="earlyResFloatBtn">
    <i class="fas fa-calendar-check"></i> <span>Erken Rezervasyon</span>
</div>

<!-- ERKEN REZERVASYON MODAL -->
<div class="reservation-modal-overlay" id="reservationModal">
    <div class="reservation-modal-content">
        <span class="reservation-modal-close" id="closeReservationModal">&times;</span>
        <h3 class="reservation-modal-title"><i class="fas fa-gift"></i> Gelin Arabası Erken Rezervasyon</h3>
        <p style="text-align: center; margin-bottom: 20px; font-size: 0.9rem; color: #ccc;">2024-2025 sezonu için %20'ye varan erken rezervasyon indirimlerinden yararlanın!</p>
        <form id="reservationForm">
            <div class="form-group">
                <label>Adınız Soyadınız</label>
                <input type="text" id="resName" required placeholder="Örn: Ahmet Yılmaz">
            </div>
            <div class="form-group">
                <label>Telefon Numaranız</label>
                <input type="tel" id="resPhone" required placeholder="05XX XXX XX XX">
            </div>
            <div class="form-group">
                <label>Düğün Tarihi</label>
                <input type="date" id="resDate" required>
            </div>
            <div class="form-group">
                <label>Araç Tercihi</label>
                <select id="resVehicle">
                    <option value="Mercedes Vito">Mercedes Vito</option>
                    <option value="Mercedes S-Class">Mercedes S-Class</option>
                </select>
            </div>
            <button type="submit" class="reservation-btn"><i class="fab fa-whatsapp"></i> WhatsApp ile Fiyat Al</button>
        </form>
    </div>
</div>
"""

def update_html_files():
    # Find all html files related to gelin arabasi
    files = glob.glob('*gelin-arabasi*.html')
    
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'id="reservationModal"' in content:
            print(f"Skipping {file}, modal already exists.")
            continue
            
        # Insert just before </body>
        if '</body>' in content:
            content = content.replace('</body>', f"{html_code}\n</body>")
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file}")

def update_css():
    css_code = """
/* =========================================
   ERKEN REZERVASYON MODAL (GELİN ARABASI)
   ========================================= */
.reservation-modal-overlay {
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
.reservation-modal-overlay.active {
    display: flex;
    animation: fadeInModal 0.4s ease forwards;
}
@keyframes fadeInModal {
    from { opacity: 0; }
    to { opacity: 1; }
}
.reservation-modal-content {
    background: #111;
    border: 1px solid #D4AF37;
    border-radius: 12px;
    padding: 30px;
    width: 90%;
    max-width: 450px;
    position: relative;
    box-shadow: 0 10px 40px rgba(212, 175, 55, 0.15);
    transform: translateY(20px);
    opacity: 0;
    animation: slideUpModal 0.4s ease 0.1s forwards;
}
@keyframes slideUpModal {
    to { transform: translateY(0); opacity: 1; }
}
.reservation-modal-close {
    position: absolute;
    top: 15px;
    right: 20px;
    color: #fff;
    font-size: 28px;
    cursor: pointer;
    transition: color 0.3s;
}
.reservation-modal-close:hover {
    color: #D4AF37;
}
.reservation-modal-title {
    color: #D4AF37;
    font-size: 1.4rem;
    margin-bottom: 10px;
    text-align: center;
    font-weight: 700;
}
.reservation-modal-content .form-group {
    margin-bottom: 15px;
}
.reservation-modal-content .form-group label {
    display: block;
    margin-bottom: 5px;
    color: #ddd;
    font-size: 0.9rem;
}
.reservation-modal-content .form-group input,
.reservation-modal-content .form-group select {
    width: 100%;
    padding: 12px;
    border: 1px solid #333;
    border-radius: 8px;
    background: #1a1a1a;
    color: #fff;
    font-family: inherit;
}
.reservation-modal-content .form-group input:focus,
.reservation-modal-content .form-group select:focus {
    border-color: #D4AF37;
    outline: none;
}
.reservation-btn {
    width: 100%;
    padding: 14px;
    background: #D4AF37;
    color: #000;
    border: none;
    border-radius: 8px;
    font-weight: 700;
    font-size: 1rem;
    cursor: pointer;
    margin-top: 10px;
    transition: all 0.3s;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
}
.reservation-btn:hover {
    background: #fff;
    color: #000;
    transform: translateY(-2px);
}

/* Erken Rezervasyon Floating Button (Bottom Left) */
.early-res-float {
    position: fixed;
    bottom: 30px;
    left: 30px;
    background: #D4AF37;
    color: #000;
    padding: 12px 20px;
    border-radius: 30px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 10px;
    z-index: 999;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4);
    transition: all 0.3s;
    animation: bounce 2s infinite;
}
.early-res-float:hover {
    background: #fff;
    transform: scale(1.05);
    animation: none;
}
.early-res-float i {
    font-size: 1.2rem;
}
@media (max-width: 768px) {
    .early-res-float {
        bottom: 85px;
        left: 20px;
        padding: 10px 15px;
        font-size: 0.9rem;
    }
    .early-res-float span {
        display: none; /* Hide text on mobile to save space */
    }
}
"""
    with open('style.css', 'r', encoding='utf-8') as f:
        content = f.read()
    if '.reservation-modal-overlay' not in content:
        with open('style.css', 'a', encoding='utf-8') as f:
            f.write(f"\n{css_code}\n")
        print("Updated style.css")
    else:
        print("style.css already has modal styles")

def update_js():
    js_code = """
/* =========================================
   ERKEN REZERVASYON MODAL (GELİN ARABASI)
   ========================================= */
document.addEventListener('DOMContentLoaded', () => {
    const resModal = document.getElementById('reservationModal');
    const closeResModal = document.getElementById('closeReservationModal');
    const resForm = document.getElementById('reservationForm');
    const resFloatBtn = document.getElementById('earlyResFloatBtn');

    if (resModal && closeResModal && resForm) {
        // Open modal on floating button click
        if (resFloatBtn) {
            resFloatBtn.addEventListener('click', () => {
                resModal.classList.add('active');
            });
        }

        // Close modal on 'X' click
        closeResModal.addEventListener('click', () => {
            resModal.classList.remove('active');
        });

        // Close modal when clicking outside
        resModal.addEventListener('click', (e) => {
            if (e.target === resModal) {
                resModal.classList.remove('active');
            }
        });

        // Automatically open modal after 10 seconds if not opened before
        if (!sessionStorage.getItem('resModalShown')) {
            setTimeout(() => {
                resModal.classList.add('active');
                sessionStorage.setItem('resModalShown', 'true');
            }, 10000);
        }

        // Form submit
        resForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('resName').value;
            const phone = document.getElementById('resPhone').value;
            const date = document.getElementById('resDate').value;
            const vehicle = document.getElementById('resVehicle').value;

            const text = `Merhaba, Gelin Arabası için erken rezervasyon formundan ulaşıyorum.\\n\\nİsim: ${name}\\nTelefon: ${phone}\\nTarih: ${date}\\nAraç: ${vehicle}\\n\\nMüsaitlik ve fiyat bilgisi alabilir miyim?`;
            
            const whatsappUrl = `https://wa.me/905453359706?text=${encodeURIComponent(text)}`;
            window.open(whatsappUrl, '_blank');
            resModal.classList.remove('active');
        });
    }
});
"""
    with open('script.js', 'r', encoding='utf-8') as f:
        content = f.read()
    if 'ERKEN REZERVASYON MODAL' not in content:
        with open('script.js', 'a', encoding='utf-8') as f:
            f.write(f"\n{js_code}\n")
        print("Updated script.js")
    else:
        print("script.js already has modal logic")

if __name__ == '__main__':
    update_html_files()
    update_css()
    update_js()
    print("Done!")
