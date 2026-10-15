/* =========================================
   1. AYARLAR VE SABİTLER
   ========================================= */
const CONFIG = {
    pricePerKm: 75,           // Km başına 75₺ sabit fiyat (Mercedes Vito)
    pricePerKmSprinter: 105,  // Km başına 105₺ (Mercedes Sprinter)
    minPriceVito: 1250,       // Şehir içi taban VIP açılış fiyatı
    minPriceSprinter: 1750,   // Sprinter taban açılış fiyatı
    whatsappPhone: "905453359706"
};

let currentLang = 'tr';

/* =========================================
   2. DİL SÖZLÜĞÜ (ANKARA & PROTOKOL ODAKLI)
   ========================================= */
const translations = {
    tr: {
        menu_fleet: "Filo",
        menu_transfer: "Transfer",
        menu_blog: "Rehber",
        menu_contact: "İletişim",
        hero_title: `ANKARA'DA <span class="gold-text">PROTOKOL</span> KONFORU`,
        hero_subtitle: "Esenboğa Havalimanı'ndan iş toplantılarınıza ve evinize prestijli ulaşım.",
        label_pickup: "Nereden",
        label_dropoff: "Nereye",
        label_vehicle: "Araç Tipi",
        btn_calc: "HESAPLA",
        btn_book: "REZERVASYON YAP",

        step_1_title: "Rotanı Seç",
        step_1_desc: "Esenboğa veya şehir içi rotanı belirle.",
        step_2_title: "Rezervasyon Yap",
        step_2_desc: "Kurumsal veya bireysel rezervasyonunu onayla.",
        step_3_title: "CIP Karşılama",
        step_3_desc: "Havalimanı çıkışında isminizle karşılıyor, valizlerinize yardımcı oluyoruz.",

        fleet_title: `MAKAM <span class="gold-text">STANDARDI</span>`,
        fleet_desc: "Ankara'nın resmiyetine uygun, siyah, cam filmli ve protokol donanımlı araçlar.",
        price_start: "Şehir İçi",
        btn_examine: "Fiyat Al",
        vito_desc: "Maybach dizayn, gizlilik camı, toplantı düzeni.",
        sprinter_desc: "Heyetler ve geniş aileler için protokol aracı.",
        sclass_desc: "Yabancı misafirler ve özel günler için zirve nokta.",

        blog_title: `HİZMETLER & <span class="gold-text">REHBER</span>`,
        blog_desc: "VIP transfer, gelin arabası ve Ankara rehberi.",
        btn_read: "Devamını Oku",

        footer_desc: "Ankara'nın lider protokol ve VIP transfer firması. Operasyonlarımız Ayka Travel güvencesiyle yürütülmektedir.",
        footer_quick: "Hızlı Erişim",
        footer_routes: "Popüler Rotalar",
        footer_contact: "İletişim & Ofis",
        footer_rights: "Tüm hakları saklıdır.",

        placeholder_pickup: "Örn: Esenboğa Havalimanı...",
        placeholder_dropoff: "Örn: Sheraton Ankara, Çankaya...",
        loading: "Hesaplanıyor...",
        error_route: "Rota hesaplanamadı. Lütfen kontrol ediniz.",
        error_fill: "Lütfen nereden ve nereye gideceğinizi belirtiniz.",
        res_dist: "Mesafe",
        res_dur: "Tahmini Süre",
        res_total: "Tahmini Tutar",
        wa_msg: "Merhaba, VIP transfer rezervasyonu yapmak istiyorum.",
        wa_route: "Güzergah",
        wa_vehicle: "Araç",
        wa_price: "Fiyat",
        wa_ask: "Müsaitlik durumunuz nedir?"
    },
    en: {
        menu_fleet: "Fleet",
        menu_transfer: "Transfer",
        menu_blog: "Guide",
        menu_contact: "Contact",
        hero_title: `PROTOCOL <span class="gold-text">COMFORT</span> IN ANKARA`,
        hero_subtitle: "Prestigious transportation from Esenboğa Airport to your business meetings.",
        label_pickup: "Pick-up",
        label_dropoff: "Drop-off",
        label_vehicle: "Vehicle Type",
        btn_calc: "CALCULATE",
        btn_book: "BOOK NOW",

        step_1_title: "Choose Route",
        step_1_desc: "Select Esenboğa or city transfer route.",
        step_2_title: "Book via WhatsApp",
        step_2_desc: "Confirm your corporate or individual reservation.",
        step_3_title: "CIP Meet & Greet",
        step_3_desc: "We welcome you at the airport exit with a name sign.",

        fleet_title: `EXECUTIVE <span class="gold-text">STANDARD</span>`,
        fleet_desc: "Black, tinted, and protocol-equipped vehicles suitable for Ankara's formality.",
        price_start: "City Transfer",
        btn_examine: "Get Quote",
        vito_desc: "Maybach design, privacy glass, meeting layout.",
        sprinter_desc: "Protocol vehicle for delegations and large groups.",
        sclass_desc: "The peak point for foreign guests and special occasions.",

        blog_title: `SERVICES & <span class="gold-text">GUIDE</span>`,
        blog_desc: "Business, life, and history guide in the Capital.",
        btn_read: "Read More",

        footer_desc: "Ankara's leading protocol and VIP transfer company. Operations powered by Ayka Travel.",
        footer_quick: "Quick Links",
        footer_routes: "Popular Routes",
        footer_contact: "Contact & Office",
        footer_rights: "All rights reserved.",

        placeholder_pickup: "Ex: Esenboğa Airport...",
        placeholder_dropoff: "Ex: Sheraton Ankara...",
        loading: "Calculating...",
        error_route: "Route could not be calculated.",
        error_fill: "Please enter pick-up and drop-off locations.",
        res_dist: "Distance",
        res_dur: "Est. Duration",
        res_total: "Estimated Price",
        wa_msg: "Hello, I would like to book a VIP transfer in Ankara.",
        wa_route: "Route",
        wa_vehicle: "Vehicle",
        wa_price: "Price",
        wa_ask: "Is there availability?"
    },
    de: {
        menu_fleet: "Flotte",
        menu_transfer: "Transfer",
        menu_blog: "Reiseführer",
        menu_contact: "Kontakt",
        hero_title: `PROTOKOLL <span class="gold-text">KOMFORT</span> IN ANKARA`,
        hero_subtitle: "Prestigeträchtiger Transport vom Flughafen Esenboğa zu Ihren Geschäftsterminen.",
        label_pickup: "Abholung",
        label_dropoff: "Zielort",
        label_vehicle: "Fahrzeugtyp",
        btn_calc: "BERECHNEN",
        btn_book: "JETZT BUCHEN",

        step_1_title: "Route Wählen",
        step_1_desc: "Wählen Sie Esenboğa oder Stadttransfer.",
        step_2_title: "Buchen per WhatsApp",
        step_2_desc: "Bestätigen Sie Ihre geschäftliche oder private Reservierung.",
        step_3_title: "CIP Empfang",
        step_3_desc: "Wir erwarten Sie am Flughafenausgang mit einem Namensschild.",

        fleet_title: `EXECUTIVE <span class="gold-text">STANDARD</span>`,
        fleet_desc: "Schwarze, getönte und protokollgerechte Fahrzeuge.",
        price_start: "Stadttransfer",
        btn_examine: "Angebot",
        vito_desc: "Maybach-Design, Sichtschutzglas, Meeting-Layout.",
        sprinter_desc: "Protokollfahrzeug für Delegationen.",
        sclass_desc: "Der Höhepunkt für ausländische Gäste.",

        blog_title: `DIENSTE & <span class="gold-text">REISEFÜHRER</span>`,
        blog_desc: "Geschäfts-, Lebens- und Geschichtsführer in der Hauptstadt.",
        btn_read: "Weiterlesen",

        footer_desc: "Ankaras führendes Protokoll- und VIP-Transferunternehmen. Powered by Ayka Travel.",
        footer_quick: "Schnelllinks",
        footer_routes: "Beliebte Routen",
        footer_contact: "Kontakt & Büro",
        footer_rights: "Alle Rechte vorbehalten.",

        placeholder_pickup: "z.B. Flughafen Esenboğa...",
        placeholder_dropoff: "z.B. Sheraton Ankara...",
        loading: "Berechnung...",
        error_route: "Route konnte nicht berechnet werden.",
        error_fill: "Bitte geben Sie Start- und Zielort ein.",
        res_dist: "Entfernung",
        res_dur: "Geschätzte Dauer",
        res_total: "Geschätzter Preis",
        wa_msg: "Hallo, ich möchte einen VIP-Transfer in Ankara buchen.",
        wa_route: "Route",
        wa_vehicle: "Fahrzeug",
        wa_price: "Preis",
        wa_ask: "Ist Verfügbarkeit vorhanden?"
    },
    ru: {
        menu_fleet: "Автопарк",
        menu_transfer: "Трансфер",
        menu_blog: "Гид",
        menu_contact: "Контакт",
        hero_title: `ПРОТОКОЛЬНЫЙ <span class="gold-text">КОМФОРТ</span> В АНКАРЕ`,
        hero_subtitle: "Престижный трансфер из аэропорта Эсенбога на деловые встречи.",
        label_pickup: "Откуда",
        label_dropoff: "Куда",
        label_vehicle: "Тип авто",
        btn_calc: "РАССЧИТАТЬ",
        btn_book: "ЗАБРОНИРОВАТЬ",

        step_1_title: "Выберите Маршрут",
        step_1_desc: "Выберите маршрут: Эсенбога или по городу.",
        step_2_title: "Бронь через WhatsApp",
        step_2_desc: "Подтвердите корпоративное или частное бронирование.",
        step_3_title: "CIP Встреча",
        step_3_desc: "Встречаем на выходе из аэропорта с табличкой.",

        fleet_title: `ПРЕДСТАВИТЕЛЬСКИЙ <span class="gold-text">КЛАСС</span>`,
        fleet_desc: "Черные автомобили с тонировкой для протокольных встреч.",
        price_start: "По городу",
        btn_examine: "Узнать цену",
        vito_desc: "Дизайн Maybach, конфиденциальность, условия для встреч.",
        sprinter_desc: "Протокольный автомобиль для делегаций.",
        sclass_desc: "Пик комфорта для иностранных гостей.",

        blog_title: `УСЛУГИ И <span class="gold-text">ГАЙД</span>`,
        blog_desc: "Бизнес, жизнь и история столицы.",
        btn_read: "Читать далее",

        footer_desc: "Ведущая компания протокольного и VIP-трансфера в Анкаре. Powered by Ayka Travel.",
        footer_quick: "Ссылки",
        footer_routes: "Популярные маршруты",
        footer_contact: "Офис",
        footer_rights: "Все права защищены.",

        placeholder_pickup: "Напр: Аэропорт Эсенбога...",
        placeholder_dropoff: "Напр: Sheraton Ankara...",
        loading: "Вычисление...",
        error_route: "Маршрут не может быть рассчитан.",
        error_fill: "Пожалуйста, заполните пункты отправления и назначения.",
        res_dist: "Расстояние",
        res_dur: "Примерное время",
        res_total: "Цена",
        wa_msg: "Здравствуйте, я хочу забронировать VIP-трансфер в Анкаре.",
        wa_route: "Маршрут",
        wa_vehicle: "Авто",
        wa_price: "Цена",
        wa_ask: "Есть ли свободные места?"
    }
};

/* =========================================
   3-5. GÜZERGÂH ARAMA & FİYAT HESAPLAMA
   → route-planner.js dosyasına taşındı (fiyat kuralları yukarıdaki CONFIG'den okunur)
   ========================================= */

/* =========================================
   6. DİL & ARAYÜZ MANTIĞI
   ========================================= */
function changeLanguage(lang) {
    currentLang = lang;
    const t = translations[lang];
    const htmlKeys = ['hero_title', 'fleet_title', 'blog_title'];

    document.querySelectorAll('[data-lang]').forEach(el => {
        const key = el.getAttribute('data-lang');
        if (t[key]) {
            if (el.tagName === 'INPUT') el.placeholder = t[key];
            else if (htmlKeys.includes(key)) el.innerHTML = t[key];
            else el.innerText = t[key];
        }
    });

    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.innerText.toLowerCase() === lang) btn.classList.add('active');
    });

    const pickupInput = document.getElementById('pickup-input');
    const dropoffInput = document.getElementById('dropoff-input');
    if (pickupInput) pickupInput.placeholder = t.placeholder_pickup;
    if (dropoffInput) dropoffInput.placeholder = t.placeholder_dropoff;
}

function toggleMenu() {
    document.querySelector('.nav-menu').classList.toggle('active');
    const overlay = document.querySelector('.nav-overlay');
    if (overlay) overlay.classList.toggle('active');
}

function closeMenu() {
    document.querySelector('.nav-menu').classList.remove('active');
    const overlay = document.querySelector('.nav-overlay');
    if (overlay) overlay.classList.remove('active');
}

/* =========================================
   7. HIZLI ROTA KARTLARI (Quick Book)
   ========================================= */
function quickBook(packageName) {
    const message = `*MERHABA VIPTRIP* 🔔%0A%0A` +
        `Aşağıdaki hizmetiniz için bilgi ve müsaitlik öğrenmek istiyorum:%0A` +
        `🚀 *Seçilen Paket:* ${packageName}%0A%0A` +
        `Müsait misiniz?`;

    const url = `https://wa.me/${CONFIG.whatsappPhone}?text=${message}`;
    window.open(url, '_blank').focus();
}

/* =========================================
   8. SAYFA YÜKLENDİĞİNDE ÇALIŞACAKLAR
   ========================================= */
document.addEventListener('DOMContentLoaded', () => {
    // 1. Dil Tespiti
    const userLang = navigator.language || navigator.userLanguage;
    if (userLang.includes('en')) changeLanguage('en');
    else if (userLang.includes('de')) changeLanguage('de');
    else if (userLang.includes('ru')) changeLanguage('ru');
    else changeLanguage('tr');

    // 2. AOS Animasyonları
    if (typeof AOS !== 'undefined') {
        AOS.init({ once: true, offset: 100 });
    }

    // 3. Header Scroll Efekti
    window.addEventListener('scroll', function () {
        const header = document.querySelector('header');
        if (!header) return;
        const isMobile = window.innerWidth <= 768;
        if (window.scrollY > 50) {
            header.style.backgroundColor = 'rgba(0, 0, 0, 0.95)';
            header.style.backdropFilter = 'blur(10px)';
            header.style.padding = isMobile ? '12px 20px' : '15px 50px';
        } else {
            header.style.backgroundColor = 'transparent';
            header.style.backdropFilter = 'none';
            header.style.padding = isMobile ? '20px' : '30px 50px';
        }
    });

    // 4. FAQ Akordiyon
    document.querySelectorAll('.faq-question').forEach(button => {
        button.addEventListener('click', () => {
            button.classList.toggle('active');
            const answer = button.nextElementSibling;
            if (button.classList.contains('active')) {
                answer.style.maxHeight = answer.scrollHeight + "px";
            } else {
                answer.style.maxHeight = 0;
            }
        });
    });

    // 5. Instagram Statik Video Kartları Ses Kontrolü
    document.querySelectorAll('.mute-btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();

            const video = this.closest('.insta-grid-item').querySelector('video');
            const icon = this.querySelector('i');

            if (video.muted) {
                document.querySelectorAll('.insta-grid-item video').forEach(v => {
                    v.muted = true;
                });
                document.querySelectorAll('.mute-btn i').forEach(i => {
                    i.className = 'fas fa-volume-mute';
                });

                video.muted = false;
                video.play().catch(err => console.log("Play interrupted:", err));
                icon.className = 'fas fa-volume-up';
            } else {
                video.muted = true;
                icon.className = 'fas fa-volume-mute';
            }
        });
    });
});
