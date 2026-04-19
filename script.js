/* =========================================
   1. AYARLAR VE SABİTLER
   ========================================= */
const CONFIG = {
    pricePerKm: 75,           // Km başına 75₺ sabit fiyat
    whatsappPhone: "905453359706"
};

let currentLang = 'tr';
let calculationData = {
    price: 0,
    distance: 0,
    duration: 0,
    pickup: "",
    dropoff: "",
    vehicle: ""
};

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

        blog_title: `ANKARA <span class="gold-text">REHBERİ</span>`,
        blog_desc: "Başkentte iş, yaşam ve tarih rehberi.",
        btn_read: "Devamını Oku",

        footer_desc: "Ankara'nın lider protokol ve VIP transfer firması. Operasyonlarımız Ayka Travel güvencesiyle yürütülmektedir.",
        footer_quick: "Hızlı Erişim",
        footer_routes: "Popüler Rotalar",
        footer_contact: "İletişim & Ofis",
        footer_rights: "Tüm hakları saklıdır.",

        placeholder_pickup: "Örn: Esenboğa Havalimanı...",
        placeholder_dropoff: "Örn: Sheraton Ankara...",
        loading: "Hesaplanıyor...",
        error_route: "Rota hesaplanamadı. Lütfen listeden seçiniz.",
        error_fill: "Lütfen tüm alanları doldurunuz.",
        res_dist: "Mesafe",
        res_dur: "Süre",
        res_total: "Tahmini Tutar",
        wa_msg: "Merhaba, Ankara transfer hizmeti için rezervasyon yapmak istiyorum.",
        wa_route: "Rota",
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

        blog_title: `ANKARA <span class="gold-text">GUIDE</span>`,
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
        error_fill: "Please fill in all fields.",
        res_dist: "Distance",
        res_dur: "Duration",
        res_total: "Estimated Price",
        wa_msg: "Hello, I would like to book a transfer in Ankara.",
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

        blog_title: `ANKARA <span class="gold-text">FÜHRER</span>`,
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
        error_fill: "Bitte füllen Sie alle Felder aus.",
        res_dist: "Entfernung",
        res_dur: "Dauer",
        res_total: "Geschätzter Preis",
        wa_msg: "Hallo, ich möchte einen Transfer in Ankara buchen.",
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

        blog_title: `ГИД ПО <span class="gold-text">АНКАРЕ</span>`,
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
        error_fill: "Пожалуйста, заполните все поля.",
        res_dist: "Расстояние",
        res_dur: "Время",
        res_total: "Цена",
        wa_msg: "Здравствуйте, я хочу забронировать трансфер в Анкаре.",
        wa_route: "Маршрут",
        wa_vehicle: "Авто",
        wa_price: "Цена",
        wa_ask: "Есть ли свободные места?"
    }
};

/* =========================================
   3. GARANTİ ADRES ARAMA (IŞINLAMA YÖNTEMİ)
   ========================================= */
let typingTimer;

// Listeyi Input'un altına ışınlayan fonksiyon
function positionList(input, list) {
    // 1. Listeyi "body" etiketine taşı (Hapisten kurtar)
    if (list.parentNode !== document.body) {
        document.body.appendChild(list);
    }

    // 2. Input kutusunun sayfadaki yerini ölç
    const rect = input.getBoundingClientRect();
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const scrollLeft = window.scrollX || document.documentElement.scrollLeft;

    // 3. Listeyi tam oraya yapıştır
    list.style.position = "absolute";
    list.style.top = (rect.bottom + scrollTop) + "px"; // Kutunun altı
    list.style.left = (rect.left + scrollLeft) + "px"; // Kutunun solu
    list.style.width = rect.width + "px"; // Genişliği kutuyla aynı olsun
    list.style.zIndex = "9999999"; // En üste çıksın
}

async function searchAddress(query, listId, inputId, coordsId) {
    if (query.length < 3) return;

    const input = document.getElementById(inputId);
    const list = document.getElementById(listId);

    // --> KRİTİK HAMLE: Listeyi konumlandır ve göster <--
    positionList(input, list);
    list.style.display = "block";

    list.innerHTML = '<li style="color:#888; padding:15px; background:#fff;"><i class="fas fa-circle-notch fa-spin"></i> Aranıyor...</li>';

    // HTTPS ve TR Filtreli Arama
    const url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}&limit=7&countrycodes=tr&addressdetails=1&email=info@viptrip.com.tr`;

    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error("Hata");
        const data = await response.json();

        list.innerHTML = "";

        if (data.length === 0) {
            list.innerHTML = `<li style="cursor:default; color:#999; padding:15px; background:#fff;">Sonuç bulunamadı</li>`;
            return;
        }

        data.forEach(place => {
            const item = document.createElement("li");
            let displayName = place.display_name.split(',').slice(0, 4).join(', ');

            let icon = 'fa-map-marker-alt';
            if (displayName.toLowerCase().includes('havalimanı') || displayName.toLowerCase().includes('airport')) icon = 'fa-plane';
            else if (displayName.toLowerCase().includes('otel')) icon = 'fa-hotel';

            item.innerHTML = `<i class="fas ${icon}" style="color:#D4AF37; margin-right:10px;"></i> ${displayName}`;

            // Tıklama Olayı
            item.onclick = function () {
                document.getElementById(inputId).value = displayName;
                document.getElementById(coordsId).value = place.lon + "," + place.lat;
                list.style.display = "none"; // Seçince gizle
            };
            list.appendChild(item);
        });

    } catch (error) {
        list.innerHTML = `<li style="color:red; padding:15px; background:#fff;">Bağlantı hatası.</li>`;
    }
}

// Olay Dinleyicileri
['pickup', 'dropoff'].forEach(type => {
    const input = document.getElementById(`${type}-input`);
    const list = document.getElementById(`${type}-suggestions`);

    if (input) {
        input.addEventListener('input', function () {
            clearTimeout(typingTimer);
            const val = this.value;
            typingTimer = setTimeout(() => {
                searchAddress(val, `${type}-suggestions`, `${type}-input`, `${type}-coords`);
            }, 800);
        });

        // Sayfa kaydırılırsa veya pencere boyutu değişirse listeyi kapat (Kayma olmasın diye)
        window.addEventListener('resize', () => { if (list) list.style.display = 'none'; });
        window.addEventListener('scroll', () => { if (list) list.style.display = 'none'; });

        // Dışarı tıklayınca kapat
        document.addEventListener('click', function (e) {
            if (e.target !== input && e.target !== list) {
                if (list) list.style.display = 'none';
            }
        });
    }
});

/* =========================================
   4. HESAPLAMA (OSRM API)
   ========================================= */
async function calculateDistancePrice() {
    const pickupCoords = document.getElementById('pickup-coords').value;
    const dropoffCoords = document.getElementById('dropoff-coords').value;
    const vehicleType = document.getElementById('vehicle-type').value;
    const btnSpan = document.querySelector('button[onclick="calculateDistancePrice()"] span');

    if (!pickupCoords || !dropoffCoords) {
        alert(translations[currentLang].error_fill);
        return;
    }

    const originalText = btnSpan.innerText;
    btnSpan.innerText = translations[currentLang].loading;

    const url = `https://router.project-osrm.org/route/v1/driving/${pickupCoords};${dropoffCoords}?overview=false`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.code !== "Ok") {
            alert(translations[currentLang].error_route);
            btnSpan.innerText = originalText;
            return;
        }

        const distanceMeters = data.routes[0].distance;
        const distanceKm = (distanceMeters / 1000).toFixed(1);
        const durationMin = Math.round(data.routes[0].duration / 60);

        let price = distanceKm * CONFIG.pricePerKm;
        price = Math.ceil(price / 10) * 10; // 10'un katına yuvarla

        calculationData = {
            price: price,
            distance: distanceKm,
            duration: durationMin,
            pickup: document.getElementById('pickup-input').value,
            dropoff: document.getElementById('dropoff-input').value,
            vehicle: (vehicleType === 'sprinter') ? "Mercedes Sprinter (VIP)" : "Mercedes Vito (VIP)"
        };

        updateResultUI();
        btnSpan.innerText = translations[currentLang].btn_calc;

    } catch (error) {
        console.error("Hesaplama Hatası:", error);
        alert("Bağlantı hatası");
        btnSpan.innerText = originalText;
    }
}

function updateResultUI() {
    const resultBox = document.getElementById('price-result');
    const t = translations[currentLang];

    resultBox.style.display = 'flex';
    document.getElementById('show-price').innerText = calculationData.price + "₺";

    const infoHTML = `
        ${t.res_dist}: <b>${calculationData.distance} km</b> | 
        ${t.res_dur}: <b>${calculationData.duration} dk/min</b>
    `;

    document.querySelector('.result-content p').innerHTML = infoHTML;
    document.getElementById('show-route').innerText = `${calculationData.pickup} -> ${calculationData.dropoff}`;
    document.querySelector('.whatsapp-book-btn').innerHTML = `<i class="fab fa-whatsapp"></i> ${t.btn_book}`;
}

function bookNow() {
    const t = translations[currentLang];
    const message = `
*${t.wa_msg}*
---------------------------
📍 *${t.wa_route}:* ${calculationData.pickup} -> ${calculationData.dropoff}
📏 *${t.res_dist}:* ${calculationData.distance} km
🚐 *${t.wa_vehicle}:* ${calculationData.vehicle}
💰 *${t.wa_price}:* ${calculationData.price}₺
---------------------------
❓ *${t.wa_ask}*`.trim();

    window.open(`https://wa.me/${CONFIG.whatsappPhone}?text=${encodeURIComponent(message)}`, '_blank');
}

/* =========================================
   5. DİL & ARAYÜZ MANTIĞI
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

    const pInput = document.getElementById('pickup-input');
    const dInput = document.getElementById('dropoff-input');
    if (pInput) pInput.placeholder = t.placeholder_pickup;
    if (dInput) dInput.placeholder = t.placeholder_dropoff;

    if (document.getElementById('price-result').style.display === 'flex') updateResultUI();
}

function toggleMobileMenu() {
    document.querySelector('.nav-menu').classList.toggle('active');
}

function closeMenu() {
    document.querySelector('.nav-menu').classList.remove('active');
}

document.addEventListener('DOMContentLoaded', () => {
    const userLang = navigator.language || navigator.userLanguage;
    if (userLang.includes('en')) changeLanguage('en');
    else if (userLang.includes('de')) changeLanguage('de');
    else if (userLang.includes('ru')) changeLanguage('ru');
    else changeLanguage('tr');

    AOS.init({ once: true, offset: 100 });

    window.addEventListener('scroll', function () {
        const header = document.querySelector('header');
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
});

/* --- FAQ AKORDİYON ÇALIŞTIRMA --- */
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

/* =========================================
   6. HIZLI ROTA KARTLARI (Quick Book)
   ========================================= */
function quickBook(packageName) {
    // 1. Mesajı Hazırla
    const message = `*MERHABA VIPTRIP* 🔔%0A%0A` +
        `Aşağıdaki hızlı paketiniz için fiyat ve müsaitlik öğrenmek istiyorum:%0A` +
        `🚀 *Seçilen Paket:* ${packageName}%0A%0A` +
        `Müsait misiniz?`;

    // 2. WhatsApp'ı Aç
    const url = `https://wa.me/${CONFIG.whatsappPhone}?text=${message}`;
    window.open(url, '_blank').focus();
}