
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

            const text = `Merhaba, Gelin Arabası için erken rezervasyon formundan ulaşıyorum.\n\nİsim: ${name}\nTelefon: ${phone}\nTarih: ${date}\nAraç: ${vehicle}\n\nMüsaitlik ve fiyat bilgisi alabilir miyim?`;
            
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
