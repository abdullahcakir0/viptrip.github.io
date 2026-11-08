/* =========================================================
   VIPTRIP · İLETİŞİM TIKLAMA ÖLÇÜMÜ
   WhatsApp ve telefon tıklamalarını Google Tag Manager'a bildirir.

   dataLayer olayları:
     whatsapp_click  → wa.me bağlantıları, WhatsApp butonları, teklif formu,
                       fiyat hesaplayıcının "Rezervasyon Yap" butonu
     phone_click     → tel: bağlantıları

   Her olayla gönderilen alanlar:
     click_location  → tıklamanın sitedeki yeri (header, float, bottom_nav,
                       route_planner, announcement, cta, form, content ...)
     click_text      → butonun yazısı (kısaltılmış)
     page_path       → sayfa yolu
   ========================================================= */
(function () {
    'use strict';

    window.dataLayer = window.dataLayer || [];

    var LOCATIONS = [
        ['.annc-bar', 'announcement'],
        ['.blog-header, header', 'header'],
        ['.whatsapp-float, .blog-whatsapp-float', 'float'],
        ['.mobile-bottom-nav, .blog-bottom-nav', 'bottom_nav'],
        ['.route-planner', 'route_planner'],
        ['.quick-card, .quick-cards-grid', 'quick_card'],
        ['.wa-form', 'form'],
        ['.promo-box', 'promo'],
        ['.cta-box', 'cta'],
        ['.price-card, .vehicle-card', 'vehicle_card'],
        ['footer', 'footer']
    ];

    function locationOf(el) {
        if (!el || !el.closest) return 'content';
        for (var i = 0; i < LOCATIONS.length; i++) {
            if (el.closest(LOCATIONS[i][0])) return LOCATIONS[i][1];
        }
        return 'content';
    }

    function textOf(el) {
        var t = (el && (el.innerText || el.textContent) || '').replace(/\s+/g, ' ').trim();
        return t.slice(0, 60);
    }

    // Aynı tıklama iki yoldan (bağlantı + window.open) gelirse bir kez say
    var last = { type: '', at: 0 };
    function push(type, el, extra) {
        var now = Date.now();
        if (last.type === type && now - last.at < 800) return;
        last = { type: type, at: now };
        var data = {
            event: type,
            click_location: locationOf(el),
            click_text: textOf(el),
            page_path: location.pathname
        };
        if (extra) for (var k in extra) data[k] = extra[k];
        window.dataLayer.push(data);
    }

    function isWhatsApp(url) {
        return /^https?:\/\/(wa\.me|api\.whatsapp\.com|web\.whatsapp\.com)\//i.test(url || '');
    }

    // 1) Bağlantı tıklamaları (yakalama aşamasında, sayfa değişmeden önce)
    document.addEventListener('click', function (e) {
        var a = e.target && e.target.closest && e.target.closest('a[href]');
        if (!a) return;
        var href = a.getAttribute('href') || '';
        if (isWhatsApp(href)) push('whatsapp_click', a);
        else if (/^tel:/i.test(href)) push('phone_click', a);
    }, true);

    // 2) JavaScript ile açılan WhatsApp pencereleri (rezervasyon butonu, hızlı kartlar, teklif formu)
    var lastClicked = null;
    document.addEventListener('click', function (e) { lastClicked = e.target; }, true);
    document.addEventListener('submit', function (e) { lastClicked = e.target; }, true);

    var originalOpen = window.open;
    window.open = function (url) {
        try {
            if (isWhatsApp(String(url))) push('whatsapp_click', lastClicked && lastClicked.closest ? (lastClicked.closest('button, a, form, .quick-card') || lastClicked) : null);
        } catch (err) { /* ölçüm hatası sayfayı etkilemesin */ }
        return originalOpen.apply(window, arguments);
    };
})();
