import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"

# 1. Update prices in all HTML files
html_files = [f for f in os.listdir(cwd) if f.endswith('.html')]

for file in html_files:
    filepath = os.path.join(cwd, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace("9.000₺", "10.000₺")
    new_content = new_content.replace("9.000", "10.000")
    
    if file == 'index.html':
        new_content = new_content.replace("%20 İndirim", "%30 İndirim")
        
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated price in {file}")

# 2. Extract modal logic to modals.js
modals_js_content = """
/* =========================================
   ERKEN REZERVASYON MODAL (GELİN ARABASI)
   ========================================= */
document.addEventListener('DOMContentLoaded', () => {
    const resModal = document.getElementById('reservationModal');
    const closeResModal = document.getElementById('closeReservationModal');
    const resForm = document.getElementById('reservationForm');
    const resFloatBtn = document.getElementById('earlyResFloatBtn');

    if (resModal && closeResModal && resForm) {
        if (resFloatBtn) {
            resFloatBtn.addEventListener('click', () => {
                resModal.classList.add('active');
            });
        }

        closeResModal.addEventListener('click', () => {
            resModal.classList.remove('active');
        });

        resModal.addEventListener('click', (e) => {
            if (e.target === resModal) {
                resModal.classList.remove('active');
            }
        });

        if (!sessionStorage.getItem('resModalShown')) {
            setTimeout(() => {
                resModal.classList.add('active');
                sessionStorage.setItem('resModalShown', 'true');
            }, 10000);
        }

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

/* =========================================
   PROMO MODAL (ANA SAYFA GELİN ARABASI)
   ========================================= */
document.addEventListener('DOMContentLoaded', () => {
    const promoModal = document.getElementById('promoModal');
    const closePromoModal = document.getElementById('closePromoModal');

    if (promoModal && closePromoModal) {
        closePromoModal.addEventListener('click', () => {
            promoModal.classList.remove('active');
        });

        promoModal.addEventListener('click', (e) => {
            if (e.target === promoModal) {
                promoModal.classList.remove('active');
            }
        });

        if (!sessionStorage.getItem('promoModalShown')) {
            setTimeout(() => {
                promoModal.classList.add('active');
                sessionStorage.setItem('promoModalShown', 'true');
            }, 5000);
        }
    }
});
"""

with open(os.path.join(cwd, 'modals.js'), 'w', encoding='utf-8') as f:
    f.write(modals_js_content)
print("Created modals.js")

# 3. Add modals.js to all HTML files
for file in html_files:
    filepath = os.path.join(cwd, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<script src="modals.js"></script>' not in content and '</body>' in content:
        new_content = content.replace('</body>', '<script src="modals.js"></script>\n</body>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added modals.js to {file}")

# 4. Remove modal logic from script.js
script_path = os.path.join(cwd, 'script.js')
with open(script_path, 'r', encoding='utf-8') as f:
    script_content = f.read()

# Just regex out everything from ERKEN REZERVASYON MODAL to the end, since I appended them at the end
if '/* =========================================' in script_content and 'ERKEN REZERVASYON MODAL' in script_content:
    idx = script_content.find('/* =========================================\n   ERKEN REZERVASYON MODAL')
    if idx != -1:
        script_content = script_content[:idx]
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(script_content)
        print("Cleaned up script.js")

print("Done!")
