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
        price_start: "По гороdu",
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
   3. POPÜLER VIP LOKASYON VERİ TABANI
   ========================================= */
const ANKARA_LOCATIONS = [
    // Havalimanı & Ulaşım Merkezleri
    {
        name: "Esenboğa Havalimanı (ESB)",
        sub: "VIP Karşılama & Terminal",
        aliases: ["esenboga", "esenboğa", "havalimani", "havalimanı", "airport", "esb"],
        coords: "32.9950,40.1281",
        icon: "fa-plane"
    },
    {
        name: "Ankara YHT Garı (Merkez)",
        sub: "Merkez Hızlı Tren Garı",
        aliases: ["yht", "yht garı", "ankara garı", "tren garı", "gar", "hızlı tren"],
        coords: "32.8447,39.9362",
        icon: "fa-train"
    },
    {
        name: "AŞTİ Otobüs Terminali",
        sub: "Şehirlerarası Otogar",
        aliases: ["asti", "aşti", "otogar", "terminal"],
        coords: "32.8128,39.9172",
        icon: "fa-bus"
    },
    {
        name: "Eryaman YHT Garı",
        sub: "Batı Ankara Tren Garı",
        aliases: ["eryaman yht", "eryaman gar"],
        coords: "32.6517,39.9675",
        icon: "fa-train"
    },

    // Çankaya & Protokol & Merkez
    {
        name: "Çankaya / Tunalı Hilmi",
        sub: "Merkez & Protokol Rotaları",
        aliases: ["cankaya", "çankaya", "tunali", "tunalı", "tunalı hilmi", "kavaklıdere", "kavaklidere"],
        coords: "32.8597,39.8974",
        icon: "fa-map-pin"
    },
    {
        name: "Kızılay / Bakanlıklar / TBMM",
        sub: "Şehir Merkezi & Bakanlıklar",
        aliases: ["kizilay", "kızılay", "bakanliklar", "bakanlıklar", "tbmm", "meclis", "sıhhiye", "sihhiye"],
        coords: "32.8543,39.9208",
        icon: "fa-landmark"
    },
    {
        name: "Gaziosmanpaşa (GOP) / Filistin Cad.",
        sub: "Elçilikler & Rezidans Bölgesi",
        aliases: ["gop", "gaziosmanpasa", "gaziosmanpaşa", "filistin", "ugur mumcu", "uğur mumcu"],
        coords: "32.8710,39.8965",
        icon: "fa-map-pin"
    },
    {
        name: "Çukurambar / Söğütözü (İş Merkezleri)",
        sub: "Armada, Next Level, Finans",
        aliases: ["cukurambar", "çukurambar", "sogutozu", "söğütözü", "armada", "next level", "the paragon"],
        coords: "32.8122,39.9075",
        icon: "fa-briefcase"
    },
    {
        name: "İncek / Beytepe / Alacaatlı",
        sub: "Lüks Konut & Villalar",
        aliases: ["incek", "i̇ncek", "beytepe", "alacaatli", "alacaatlı", "incek loft"],
        coords: "32.7214,39.8452",
        icon: "fa-home"
    },
    {
        name: "Çayyolu / Ümitköy / Yaşamkent",
        sub: "Batı Ankara Konut Bölgesi",
        aliases: ["cayyolu", "çayyolu", "umitkoy", "ümitköy", "yasamkent", "yaşamkent", "mesa koru"],
        coords: "32.7058,39.8872",
        icon: "fa-map-pin"
    },
    {
        name: "Bilkent / ODTÜ / Hacettepe",
        sub: "Üniversite & Teknokentler",
        aliases: ["bilkent", "odtu", "odtü", "hacettepe", "angora"],
        coords: "32.7533,39.8732",
        icon: "fa-graduation-cap"
    },
    {
        name: "Gölbaşı / Mogan Gölü",
        sub: "Göl Kenarı & Etkinlik Alanları",
        aliases: ["golbasi", "gölbaşı", "mogan", "eymir"],
        coords: "32.8083,39.7915",
        icon: "fa-water"
    },
    {
        name: "Yenimahalle / Batıkent / Eryaman",
        sub: "Göksu Parkı & Konut Alanları",
        aliases: ["yenimahalle", "batikent", "batıkent", "eryaman", "göksu", "goksu"],
        coords: "32.7314,39.9647",
        icon: "fa-map-pin"
    },
    {
        name: "Ostim / İvedik OSB",
        sub: "Sanayi & Ticaret Merkezleri",
        aliases: ["ostim", "ivedik", "osb", "sanayi"],
        coords: "32.7505,39.9722",
        icon: "fa-industry"
    },
    {
        name: "Bilkent & Etlik Şehir Hastaneleri",
        sub: "Sağlık Turizmi & Hastaneler",
        aliases: ["sehir hastanesi", "şehir hastanesi", "bilkent sehir hastanesi", "etlik sehir hastanesi"],
        coords: "32.7745,39.8970",
        icon: "fa-hospital"
    },

    // 5 Yıldızlı Lüks Oteller
    {
        name: "Sheraton Hotel Ankara (GOP)",
        sub: "5 Yıldızlı VIP Otel - GOP",
        aliases: ["sheraton", "sheraton ankara", "sheraton otel"],
        coords: "32.8660,39.8943",
        icon: "fa-hotel"
    },
    {
        name: "JW Marriott Hotel Ankara (Söğütözü)",
        sub: "5 Yıldızlı VIP Otel - Söğütözü",
        aliases: ["jw marriott", "marriott", "jw marriott ankara"],
        coords: "32.8142,39.9114",
        icon: "fa-hotel"
    },
    {
        name: "Hilton SA Ankara (Kavaklıdere)",
        sub: "5 Yıldızlı Otel - Kavaklıdere",
        aliases: ["hilton", "hilton ankara", "hilton sa"],
        coords: "32.8621,39.8988",
        icon: "fa-hotel"
    },
    {
        name: "Swissôtel Ankara (Çankaya)",
        sub: "5 Yıldızlı Otel - Çankaya/Yıldız",
        aliases: ["swissotel", "swiss otel", "swissotel ankara"],
        coords: "32.8653,39.8753",
        icon: "fa-hotel"
    },
    {
        name: "Divan Ankara (Çankaya)",
        sub: "Tunalı Hilmi Caddesi",
        aliases: ["divan", "divan otel", "divan ankara"],
        coords: "32.8606,39.9015",
        icon: "fa-hotel"
    },
    {
        name: "Mövenpick Hotel Ankara (Söğütözü)",
        sub: "Söğütözü İş Bölgesi",
        aliases: ["movenpick", "mövenpick"],
        coords: "32.8116,39.9103",
        icon: "fa-hotel"
    },

    // Şehirlerarası VIP Rotalar
    {
        name: "Bolu / Abant Gölü",
        sub: "Şehirlerarası Özel VIP Tur",
        aliases: ["bolu", "abant", "abant golu", "yedigoller", "yedigöller", "kartalkaya"],
        coords: "31.2818,40.6053",
        icon: "fa-mountain"
    },
    {
        name: "Kapadokya / Nevşehir / Göreme",
        sub: "Kapadokya VIP Tur & Transfer",
        aliases: ["kapadokya", "nevsehir", "nevşehir", "urgup", "ürgüp", "goreme", "göreme", "uchisar"],
        coords: "34.8290,38.6431",
        icon: "fa-map-signs"
    },
    {
        name: "İstanbul (Sabiha Gökçen - SAW)",
        sub: "Şehirlerarası VIP Havalimanı",
        aliases: ["istanbul", "sabiha", "sabiha gokcen", "sabiha gökçen", "saw", "anadolu yakasi"],
        coords: "29.3092,40.8986",
        icon: "fa-city"
    },
    {
        name: "İstanbul (İstanbul Havalimanı - İGA)",
        sub: "Şehirlerarası VIP Havalimanı",
        aliases: ["iga", "istanbul havalimani", "istanbul havalimanı", "avrupa yakasi"],
        coords: "28.7279,41.2608",
        icon: "fa-city"
    },
    {
        name: "Eskişehir Merkez",
        sub: "Şehirlerarası VIP Transfer",
        aliases: ["eskisehir", "eskişehir", "odunpazarı", "odunpazari"],
        coords: "30.5256,39.7767",
        icon: "fa-road"
    },
    {
        name: "Konya Merkez",
        sub: "Şehirlerarası VIP Transfer",
        aliases: ["konya", "mevlana", "selcuklu"],
        coords: "32.4846,37.8746",
        icon: "fa-road"
    },
    {
        name: "Kayseri / Erciyes",
        sub: "Şehirlerarası VIP Kayak & Tur",
        aliases: ["kayseri", "erciyes"],
        coords: "35.4853,38.7205",
        icon: "fa-mountain"
    },
    {
        name: "Bursa Merkez",
        sub: "Şehirlerarası VIP Transfer",
        aliases: ["bursa", "uludag", "uludağ"],
        coords: "29.0610,40.1885",
        icon: "fa-road"
    },
    {
        name: "Antalya / Alanya",
        sub: "Akdeniz VIP Transfer",
        aliases: ["antalya", "alanya", "kemer", "belek", "side"],
        coords: "30.7133,36.8969",
        icon: "fa-umbrella-beach"
    }
];

function normalizeText(text) {
    if (!text) return "";
    return text.toString()
        .toLowerCase()
        .trim()
        .replace(/ğ/g, "g")
        .replace(/ü/g, "u")
        .replace(/ş/g, "s")
        .replace(/ı/g, "i")
        .replace(/ö/g, "o")
        .replace(/ç/g, "c");
}

function findLocationInDb(query) {
    const q = normalizeText(query);
    if (!q) return null;

    for (const loc of ANKARA_LOCATIONS) {
        if (normalizeText(loc.name) === q) return loc;
        for (const alias of loc.aliases) {
            if (normalizeText(alias) === q) return loc;
        }
    }

    for (const loc of ANKARA_LOCATIONS) {
        if (normalizeText(loc.name).includes(q)) return loc;
        for (const alias of loc.aliases) {
            if (normalizeText(alias).includes(q) || q.includes(normalizeText(alias))) return loc;
        }
    }

    return null;
}

/* =========================================
   4. DIŞA AÇILAN HIZLI ROTA & LOKASYON PANELİ
   ========================================= */
let activeField = null;
let searchDebounceTimer = null;

function openSuggestionsPanel(field) {
    activeField = field;
    const panel = document.getElementById('route-suggestions-panel');
    const titleEl = document.getElementById('sugg-panel-title-text');
    const input = document.getElementById(`${field}-input`);
    if (!panel) return;

    if (titleEl) {
        if (field === 'pickup') {
            titleEl.innerHTML = `<i class="fas fa-map-marker-alt"></i> Nereden? - Popüler Başlangıç Noktaları`;
        } else {
            titleEl.innerHTML = `<i class="fas fa-location-arrow"></i> Nereye? - Popüler Varış Rotaları`;
        }
    }

    const currentVal = input ? input.value.trim() : "";
    filterSuggestionsCards(currentVal);
    panel.style.display = 'block';
}

function closeSuggestionsPanel() {
    const panel = document.getElementById('route-suggestions-panel');
    if (panel) panel.style.display = 'none';
    activeField = null;
}

function selectCardLocation(place) {
    if (!activeField) activeField = 'pickup';

    const input = document.getElementById(`${activeField}-input`);
    const coordsEl = document.getElementById(`${activeField}-coords`);

    if (input) input.value = place.name;
    if (coordsEl) coordsEl.value = place.coords;

    const chosenField = activeField;
    closeSuggestionsPanel();

    // Auto-advance: If pickup was filled and dropoff is empty, focus dropoff
    if (chosenField === 'pickup') {
        const dropoffInput = document.getElementById('dropoff-input');
        if (dropoffInput && !dropoffInput.value.trim()) {
            setTimeout(() => {
                dropoffInput.focus();
            }, 200);
        }
    }
}

function renderCardsInPanel(places) {
    const container = document.getElementById('sugg-cards-container');
    if (!container) return;

    container.innerHTML = "";

    if (!places || places.length === 0) {
        container.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; color: #888; padding: 25px 0;">
                <i class="fas fa-search" style="font-size: 1.6rem; color: #D4AF37; margin-bottom: 8px; display:block;"></i>
                <span style="font-size: 0.9rem; color: #ccc;">Sonuç bulunamadı.</span><br>
                <small style="color: #777;">Yazdığınız konumu doğrudan hesaplamak için <strong>HESAPLA</strong> butonuna basabilirsiniz.</small>
            </div>
        `;
        return;
    }

    places.forEach(place => {
        const card = document.createElement("div");
        card.className = "sugg-card";
        const iconClass = place.icon || "fa-map-marker-alt";
        const subText = place.sub || "Ankara VIP Transfer";

        card.innerHTML = `
            <div class="sugg-card-icon">
                <i class="fas ${iconClass}"></i>
            </div>
            <div class="sugg-card-info">
                <span class="sugg-card-name">${place.name}</span>
                <span class="sugg-card-sub">${subText}</span>
            </div>
        `;

        card.addEventListener("click", () => {
            selectCardLocation(place);
        });

        container.appendChild(card);
    });
}

async function filterSuggestionsCards(query) {
    const trimmed = query ? query.trim() : "";

    // If query is empty or 1 char, show top popular choices
    if (trimmed.length < 2) {
        let popularSlice;
        if (activeField === 'pickup') {
            // Airport, train, main hotels first
            popularSlice = ANKARA_LOCATIONS.slice(0, 8);
        } else {
            // Hotels, Çankaya, intercity destinations
            popularSlice = [
                ANKARA_LOCATIONS[4], // Çankaya
                ANKARA_LOCATIONS[14], // Sheraton
                ANKARA_LOCATIONS[15], // JW Marriott
                ANKARA_LOCATIONS[0], // Esenboğa Havalimanı
                ANKARA_LOCATIONS[5], // Kızılay
                ANKARA_LOCATIONS[7], // Çukurambar
                ANKARA_LOCATIONS[20], // Bolu / Abant
                ANKARA_LOCATIONS[21], // Kapadokya
            ];
        }
        renderCardsInPanel(popularSlice);
        return;
    }

    const qNorm = normalizeText(trimmed);
    const localMatches = ANKARA_LOCATIONS.filter(loc => {
        if (normalizeText(loc.name).includes(qNorm)) return true;
        return loc.aliases.some(alias => normalizeText(alias).includes(qNorm));
    });

    renderCardsInPanel(localMatches);

    // Online photon lookup if local matches < 4
    if (localMatches.length < 4 && trimmed.length >= 3) {
        try {
            const url = `https://photon.komoot.io/api/?q=${encodeURIComponent(trimmed)}&limit=4&lat=39.93&lon=32.85`;
            const res = await fetch(url);
            if (res.ok) {
                const data = await res.json();
                if (data && data.features && data.features.length > 0) {
                    const extraPlaces = [];
                    data.features.forEach(f => {
                        const name = [f.properties.name, f.properties.district, f.properties.city || f.properties.state]
                            .filter(Boolean).join(", ");
                        const coords = `${f.geometry.coordinates[0]},${f.geometry.coordinates[1]}`;
                        if (!localMatches.some(m => m.name === name)) {
                            extraPlaces.push({
                                name: name,
                                sub: f.properties.district || "Ankara",
                                coords: coords,
                                icon: "fa-map-pin"
                            });
                        }
                    });
                    const combined = [...localMatches, ...extraPlaces].slice(0, 8);
                    const currentInput = document.getElementById(`${activeField}-input`);
                    if (currentInput && currentInput.value.trim() === trimmed) {
                        renderCardsInPanel(combined);
                    }
                }
            }
        } catch (e) {}
    }
}

// Input Event Listeners
['pickup', 'dropoff'].forEach(field => {
    const input = document.getElementById(`${field}-input`);
    const coordsEl = document.getElementById(`${field}-coords`);

    if (input) {
        input.addEventListener('focus', function () {
            openSuggestionsPanel(field);
        });

        input.addEventListener('input', function () {
            if (coordsEl) coordsEl.value = "";
            clearTimeout(searchDebounceTimer);
            const val = this.value;
            searchDebounceTimer = setTimeout(() => {
                filterSuggestionsCards(val);
            }, 200);
        });
    }
});

// Close panel when clicking outside booking widget and suggestions panel
document.addEventListener('click', function (e) {
    const widget = document.getElementById('transfer');
    const panel = document.getElementById('route-suggestions-panel');

    if (widget && panel && panel.style.display !== 'none') {
        if (!widget.contains(e.target) && !panel.contains(e.target)) {
            closeSuggestionsPanel();
        }
    }
});

// Close on Escape key
document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
        closeSuggestionsPanel();
    }
});

/* =========================================
   5. GÜZERGÂH & FİYAT HESAPLAMA (GARANTİLİ MOTOR)
   ========================================= */
function calculateHaversineDistance(lon1, lat1, lon2, lat2) {
    const R = 6371; // km
    const dLat = (lat2 - lat1) * Math.PI / 180;
    const dLon = (lon2 - lon1) * Math.PI / 180;
    const a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    const straightKm = R * c;
    // Türkiye karayolu kıvrım katsayısı: 1.28
    return Math.max(5, straightKm * 1.28);
}

async function resolveCoords(inputEl, coordsEl) {
    if (coordsEl.value && coordsEl.value.includes(",")) {
        return coordsEl.value;
    }

    const val = inputEl.value.trim();
    if (!val) return null;

    // 1. Try local DB match
    const matched = findLocationInDb(val);
    if (matched) {
        coordsEl.value = matched.coords;
        inputEl.value = matched.name;
        return matched.coords;
    }

    // 2. Try online geocoding
    try {
        const url = `https://photon.komoot.io/api/?q=${encodeURIComponent(val)}&limit=1&lat=39.93&lon=32.85`;
        const res = await fetch(url);
        if (res.ok) {
            const data = await res.json();
            if (data && data.features && data.features.length > 0) {
                const f = data.features[0];
                const c = `${f.geometry.coordinates[0]},${f.geometry.coordinates[1]}`;
                coordsEl.value = c;
                return c;
            }
        }
    } catch (e) {}

    return null;
}

async function calculateDistancePrice() {
    closeSuggestionsPanel();

    const pickupInput = document.getElementById('pickup-input');
    const dropoffInput = document.getElementById('dropoff-input');
    const pickupCoordsEl = document.getElementById('pickup-coords');
    const dropoffCoordsEl = document.getElementById('dropoff-coords');
    const vehicleType = document.getElementById('vehicle-type').value;
    const btn = document.querySelector('button[onclick="calculateDistancePrice()"]');
    const btnSpan = btn ? btn.querySelector('span') : null;
    const t = translations[currentLang];

    if (!pickupInput.value.trim() || !dropoffInput.value.trim()) {
        alert(t.error_fill);
        return;
    }

    const originalText = btnSpan ? btnSpan.innerText : "HESAPLA";
    if (btnSpan) btnSpan.innerText = t.loading;

    // Resolve coordinates automatically if needed
    const pickupCoords = await resolveCoords(pickupInput, pickupCoordsEl);
    const dropoffCoords = await resolveCoords(dropoffInput, dropoffCoordsEl);

    if (!pickupCoords || !dropoffCoords) {
        alert(t.error_route);
        if (btnSpan) btnSpan.innerText = originalText;
        return;
    }

    let distanceKm = 0;
    let durationMin = 0;

    // 1. OSRM API with 3.5-second timeout
    try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 3500);

        const url = `https://router.project-osrm.org/route/v1/driving/${pickupCoords};${dropoffCoords}?overview=false`;
        const response = await fetch(url, { signal: controller.signal });
        clearTimeout(timeoutId);

        if (response.ok) {
            const data = await response.json();
            if (data && data.code === "Ok" && data.routes && data.routes[0]) {
                const route = data.routes[0];
                distanceKm = parseFloat((route.distance / 1000).toFixed(1));
                durationMin = Math.round(route.duration / 60);
            }
        }
    } catch (e) {
        // Fallback to Haversine calculation below
    }

    // 2. Reliable Fallback if OSRM failed or returned 0
    if (!distanceKm || distanceKm <= 0) {
        const [lon1, lat1] = pickupCoords.split(',').map(Number);
        const [lon2, lat2] = dropoffCoords.split(',').map(Number);
        const estDist = calculateHaversineDistance(lon1, lat1, lon2, lat2);
        distanceKm = parseFloat(estDist.toFixed(1));
        const avgSpeed = distanceKm > 60 ? 85 : 48;
        durationMin = Math.max(15, Math.round((distanceKm / avgSpeed) * 60));
    }

    // 3. Price calculation based on vehicle type
    const isSprinter = vehicleType === 'sprinter';
    const rate = isSprinter ? CONFIG.pricePerKmSprinter : CONFIG.pricePerKm;
    const minPrice = isSprinter ? CONFIG.minPriceSprinter : CONFIG.minPriceVito;

    let rawPrice = distanceKm * rate;
    let finalPrice = Math.max(minPrice, rawPrice);
    finalPrice = Math.ceil(finalPrice / 50) * 50; // Round to nearest 50₺

    const vehicleTitle = isSprinter ? "Mercedes Sprinter VIP (7-13 Kişi)" : "Mercedes Vito VIP (1-6 Kişi)";

    calculationData = {
        price: finalPrice,
        distance: distanceKm,
        duration: durationMin,
        pickup: pickupInput.value,
        dropoff: dropoffInput.value,
        vehicle: vehicleTitle
    };

    updateResultUI();
    if (btnSpan) btnSpan.innerText = t.btn_calc;
}

function updateResultUI() {
    const resultBox = document.getElementById('price-result');
    const t = translations[currentLang];
    if (!resultBox) return;

    resultBox.style.display = 'flex';

    document.getElementById('show-price').innerText = calculationData.price.toLocaleString('tr-TR') + "₺";

    const distVal = document.getElementById('dist-val');
    const durVal = document.getElementById('dur-val');
    const vehVal = document.getElementById('vehicle-val');

    if (distVal) distVal.innerText = `${calculationData.distance} km`;
    if (durVal) {
        if (calculationData.duration >= 60) {
            const h = Math.floor(calculationData.duration / 60);
            const m = calculationData.duration % 60;
            durVal.innerText = `${h} sa ${m > 0 ? m + ' dk' : ''}`;
        } else {
            durVal.innerText = `${calculationData.duration} dk`;
        }
    }
    if (vehVal) vehVal.innerText = calculationData.vehicle;

    const routeInfo = document.getElementById('show-route');
    if (routeInfo) {
        routeInfo.innerHTML = `<strong>${calculationData.pickup}</strong> <i class="fas fa-arrow-right" style="color:#D4AF37; margin:0 6px;"></i> <strong>${calculationData.dropoff}</strong>`;
    }

    const bookBtn = document.querySelector('.whatsapp-book-btn');
    if (bookBtn) {
        bookBtn.innerHTML = `<i class="fab fa-whatsapp"></i> <span>${t.btn_book}</span>`;
    }

    // Smooth scroll to result
    resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function selectQuickRoute(pickupName, dropoffName) {
    closeSuggestionsPanel();

    const pickupInput = document.getElementById('pickup-input');
    const dropoffInput = document.getElementById('dropoff-input');
    const pickupCoords = document.getElementById('pickup-coords');
    const dropoffCoords = document.getElementById('dropoff-coords');

    const pLoc = findLocationInDb(pickupName);
    const dLoc = findLocationInDb(dropoffName);

    if (pickupInput && pLoc) {
        pickupInput.value = pLoc.name;
        pickupCoords.value = pLoc.coords;
    }
    if (dropoffInput && dLoc) {
        dropoffInput.value = dLoc.name;
        dropoffCoords.value = dLoc.coords;
    }

    calculateDistancePrice();
}

function bookNow() {
    const t = translations[currentLang];
    const message = `
*VIPTRIP REZERVASYON TALEBİ* 🌟
---------------------------
📍 *${t.wa_route}:* ${calculationData.pickup} ➔ ${calculationData.dropoff}
📏 *${t.res_dist}:* ${calculationData.distance} km (~${calculationData.duration} dk)
🚐 *${t.wa_vehicle}:* ${calculationData.vehicle}
💰 *${t.wa_price}:* ${calculationData.price}₺
---------------------------
❓ *${t.wa_ask}*`.trim();

    window.open(`https://wa.me/${CONFIG.whatsappPhone}?text=${encodeURIComponent(message)}`, '_blank');
}

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
                // Mute all other videos first
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
