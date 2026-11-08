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
        wa_ask: "Müsaitlik durumunuz nedir?",

        // --- Ana sayfa (2026-11) ---
        hero_title: "<span class=\"vip-eyebrow\">Ankara VIP Transfer &amp; Gelin Arabası</span>ANKARA'DA <span class=\"gold-text\">PROTOKOL</span> KONFORU",
        annc_aria: "Duyuru",
        annc_long: "2027 düğün sezonu için <strong>gelin arabası erken rezervasyonu</strong> başladı · Tarihinizi kapora ile ayırtın",
        annc_short: "<strong>2027 gelin arabası</strong> erken rezervasyon başladı",
        annc_cta: "Tarihimi Ayırt",
        annc_close: "Duyuruyu kapat",
        annc_wa: "Merhaba, 2027 düğünüm için gelin arabası erken rezervasyonu yapmak istiyorum. Düğün tarihi: ... Düğün salonu/bölge: ...",
        nav_home: "Ana Sayfa",
        nav_transfer: "VIP Transfer",
        nav_wedding: "Ankara VIP Gelin Arabası",
        nav_regions: "Bölgeler",
        nav_blog: "Blog",
        nav_cta: "Transfer Ayarla",
        rp_locate: "Konumumu kullan",
        rp_swap_short: "Yer değiştir",
        rp_swap: "Nereden ve nereye yer değiştir",
        pax: "kişi",
        rp_map: "Güzergah haritası",
        rp_badge: "VIP Transfer Teklifi",
        quick_title: "veya popüler rotalardan seçin:",
        q1_title: "Havalimanı ⇄ Çankaya",
        q1_sub: "Protokol Karşılama",
        q2_title: "Havalimanı ⇄ Otel",
        q2_sub: "Konforlu Ulaşım",
        q3_title: "Günlük Tahsis",
        q3_sub: "Şoförlü Araç Kiralama",
        season_title: "Kış Hizmetleri",
        s1_title: "Kayak Transferi",
        s2_title: "Yılbaşı Gecesi",
        s2_sub: "Şoförlü araç · Yıl sonu etkinlikleri",
        s3_title: "2027 Gelin Arabası",
        s3_sub: "Erken rezervasyon başladı",
        price_city: "Şehir İçi",
        price_group: "Heyet Transferi",
        price_exec: "Makam Aracı",
        price_quote: "Fiyat Alın",
        f_pax6: "6 Kişi",
        f_bag6: "6 Bavul",
        f_wifi: "WiFi & Priz",
        f_pax13: "13 Kişi",
        f_bag15: "15 Bavul",
        f_tv: "TV & Buzdolabı",
        f_pax3: "3 Kişi",
        f_bag2: "2 Bavul",
        f_protocol: "Protokol",
        cat_wedding: "Ankara VIP Gelin Arabası",
        cat_transfer: "Ankara VIP Transfer",
        cat_esb_cankaya: "Esenboğa Çankaya Transfer",
        cat_airport: "✈️ Havalimanı",
        cat_intercity: "🛣️ Şehirlerarası",
        cat_corporate: "🏛️ Kurumsal",
        cat_rental: "🔑 Kiralama",
        card1_tag: "Düğün",
        card1_title: "Ankara VIP Gelin Arabası",
        card1_desc: "Mercedes Vito Maybach ile şoför, yakıt ve süsleme dahil Ankara VIP gelin arabası paketleri.",
        card2_tag: "Transfer",
        card2_title: "Ankara VIP Transfer",
        card2_desc: "Esenboğa Havalimanı, Çankaya, otel ve şehirlerarası rotalarda 7/24 Ankara VIP transfer hizmeti.",
        card3_tag: "Havalimanı",
        card3_title: "Ankara Havalimanı Transfer",
        card3_desc: "Esenboğa Havalimanı'ndan CIP karşılama, uçuş takibi ve isim tabelası ile VIP havalimanı transferi.",
        faq_title: "MERAK <span class=\"gold-text\">EDİLENLER</span>",
        faq_desc: "Transfer sürecinizle ilgili sıkça sorulan sorular.",
        faq1_q: "Fatura kesiyor musunuz?",
        faq1_a: "Evet, tüm transferlerimiz faturalıdır. Şirketiniz adına %20 KDV dahil fatura kesilir.",
        faq2_q: "Rötar olursa ne olur?",
        faq2_a: "Uçağınızı takip ediyoruz. Rötar durumunda şoförümüz ek ücret almadan sizi bekler.",
        faq3_q: "Araçta sigara içiliyor mu?",
        faq3_a: "Hijyen kuralları gereği araçlarımızda sigara içilmemektedir. Ancak isteğiniz üzerine mola verilebilir.",
        loc_title: "Hizmetlerimiz & Güzergahlar",
        loc_prices: "Ankara VIP Transfer Fiyatları",
        loc_wedding: "VIP Gelin Arabası",
        loc_airport: "Ankara Havalimanı Transfer",
        loc_corp: "Kurumsal Transfer",
        loc_chauffeur: "Ankara Şoförlü Araç Kiralama",
        loc_ist: "İstanbul Transfer",
        loc_kap: "Kapadokya Transfer",
        loc_ant: "Antalya Transfer",
        loc_bod: "Bodrum Transfer",
        loc_bolu: "Bolu / Abant Transfer",
        insta_title: "INSTAGRAM'DA <span class=\"gold-text\">BİZ</span>",
        insta_desc: "Referanslarımız ve araçlarımız:",
        insta_btn: "İncele",
        insta_mute: "Sesi Aç/Kapat",
        fq_home: "Ana Sayfa",
        fq_fleet: "Araç Filosu",
        fq_calc: "Fiyat Hesapla",
        fq_w_cankaya: "Çankaya VIP Gelin Arabası",
        fq_w_incek: "İncek VIP Gelin Arabası",
        fq_w_golbasi: "Gölbaşı VIP Gelin Arabası",
        fq_esb_cankaya: "Esenboğa Çankaya VIP Transfer",
        fq_ski: "Ankara Kayak Transferi",
        fq_nye: "Yılbaşı Şoförlü Araç",
        fq_special: "Özel Gün Araç Kiralama",
        r1: "Esenboğa - Çankaya",
        r2: "Esenboğa - Kızılay",
        r3: "Esenboğa - Ümitköy",
        r4: "Ankara - Kapadokya",
        r5: "Ankara - Bolu/Abant",
        fb_terms: "Mesafeli Satış Sözleşmesi",
        bn_call: "ARA"
    },
    en: {
        menu_fleet: "Fleet",
        menu_transfer: "Transfer",
        menu_blog: "Guide",
        menu_contact: "Contact",
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
        wa_ask: "Is there availability?",

        // --- Ana sayfa (2026-11) ---
        hero_title: "<span class=\"vip-eyebrow\">Ankara VIP Transfer &amp; Wedding Cars</span>PROTOCOL <span class=\"gold-text\">COMFORT</span> IN ANKARA",
        annc_aria: "Announcement",
        annc_long: "Early booking for <strong>2027 wedding cars</strong> is now open · Reserve your date with a deposit",
        annc_short: "<strong>2027 wedding car</strong> early booking open",
        annc_cta: "Reserve My Date",
        annc_close: "Close announcement",
        annc_wa: "Hello, I would like to make an early booking for a wedding car for my 2027 wedding. Wedding date: ... Venue/area: ...",
        nav_home: "Home",
        nav_transfer: "VIP Transfer",
        nav_wedding: "VIP Wedding Car",
        nav_regions: "Service Areas",
        nav_blog: "Blog",
        nav_cta: "Book a Transfer",
        rp_locate: "Use my location",
        rp_swap_short: "Swap",
        rp_swap: "Swap pick-up and drop-off",
        pax: "pax",
        rp_map: "Route map",
        rp_badge: "VIP Transfer Quote",
        quick_title: "or choose a popular route:",
        q1_title: "Airport ⇄ Çankaya",
        q1_sub: "Protocol Meet & Greet",
        q2_title: "Airport ⇄ Hotel",
        q2_sub: "Comfortable Ride",
        q3_title: "Full-Day Hire",
        q3_sub: "Car with Chauffeur",
        season_title: "Winter Services",
        s1_title: "Ski Transfer",
        s2_title: "New Year's Eve",
        s2_sub: "Chauffeur car · Year-end events",
        s3_title: "2027 Wedding Car",
        s3_sub: "Early booking open",
        price_city: "City Transfer",
        price_group: "Delegations",
        price_exec: "Executive Car",
        price_quote: "Get a Quote",
        f_pax6: "6 Pax",
        f_bag6: "6 Bags",
        f_wifi: "Wi-Fi & Power",
        f_pax13: "13 Pax",
        f_bag15: "15 Bags",
        f_tv: "TV & Fridge",
        f_pax3: "3 Pax",
        f_bag2: "2 Bags",
        f_protocol: "Protocol",
        cat_wedding: "VIP Wedding Car",
        cat_transfer: "Ankara VIP Transfer",
        cat_esb_cankaya: "Esenboğa – Çankaya",
        cat_airport: "✈️ Airport",
        cat_intercity: "🛣️ Intercity",
        cat_corporate: "🏛️ Corporate",
        cat_rental: "🔑 Chauffeur Hire",
        card1_tag: "Wedding",
        card1_title: "VIP Wedding Car in Ankara",
        card1_desc: "Mercedes Vito Maybach wedding car packages in Ankara with chauffeur, fuel and decoration included.",
        card2_tag: "Transfer",
        card2_title: "Ankara VIP Transfer",
        card2_desc: "24/7 VIP transfers in Ankara: Esenboğa Airport, Çankaya, hotels and intercity routes.",
        card3_tag: "Airport",
        card3_title: "Ankara Airport Transfer",
        card3_desc: "VIP transfers from Esenboğa Airport with CIP meet & greet, flight tracking and a name sign.",
        faq_title: "FREQUENTLY <span class=\"gold-text\">ASKED</span>",
        faq_desc: "Common questions about your transfer.",
        faq1_q: "Do you issue invoices?",
        faq1_a: "Yes, every transfer is invoiced. We issue the invoice to your company, including 20% VAT.",
        faq2_q: "What if my flight is delayed?",
        faq2_a: "We track your flight. If it is delayed, your chauffeur waits for you at no extra charge.",
        faq3_q: "Is smoking allowed in the vehicle?",
        faq3_a: "Smoking is not permitted in our vehicles for hygiene reasons, but we can stop for a break on request.",
        loc_title: "Services & Routes",
        loc_prices: "Ankara VIP Transfer Prices",
        loc_wedding: "VIP Wedding Car",
        loc_airport: "Ankara Airport Transfer",
        loc_corp: "Corporate Transfer",
        loc_chauffeur: "Chauffeur Service Ankara",
        loc_ist: "Istanbul Transfer",
        loc_kap: "Cappadocia Transfer",
        loc_ant: "Antalya Transfer",
        loc_bod: "Bodrum Transfer",
        loc_bolu: "Bolu / Abant Transfer",
        insta_title: "FOLLOW US ON <span class=\"gold-text\">INSTAGRAM</span>",
        insta_desc: "Our references and vehicles:",
        insta_btn: "View",
        insta_mute: "Sound on/off",
        fq_home: "Home",
        fq_fleet: "Our Fleet",
        fq_calc: "Price Calculator",
        fq_w_cankaya: "Çankaya VIP Wedding Car",
        fq_w_incek: "İncek VIP Wedding Car",
        fq_w_golbasi: "Gölbaşı VIP Wedding Car",
        fq_esb_cankaya: "Esenboğa – Çankaya VIP Transfer",
        fq_ski: "Ski Transfer from Ankara",
        fq_nye: "New Year's Eve Chauffeur",
        fq_special: "Special Occasion Car",
        r1: "Esenboğa - Çankaya",
        r2: "Esenboğa - Kızılay",
        r3: "Esenboğa - Ümitköy",
        r4: "Ankara - Cappadocia",
        r5: "Ankara - Bolu/Abant",
        fb_terms: "Distance Sales Agreement",
        bn_call: "CALL"
    },
    de: {
        menu_fleet: "Flotte",
        menu_transfer: "Transfer",
        menu_blog: "Reiseführer",
        menu_contact: "Kontakt",
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
        wa_ask: "Ist Verfügbarkeit vorhanden?",

        // --- Ana sayfa (2026-11) ---
        hero_title: "<span class=\"vip-eyebrow\">VIP-Transfer &amp; Hochzeitsautos in Ankara</span>PROTOKOLL <span class=\"gold-text\">KOMFORT</span> IN ANKARA",
        annc_aria: "Ankündigung",
        annc_long: "Frühbuchung für <strong>Hochzeitsautos 2027</strong> gestartet · Sichern Sie Ihren Termin mit einer Anzahlung",
        annc_short: "<strong>Hochzeitsauto 2027</strong>: Frühbuchung offen",
        annc_cta: "Termin sichern",
        annc_close: "Ankündigung schließen",
        annc_wa: "Hallo, ich möchte ein Hochzeitsauto für meine Hochzeit 2027 frühbuchen. Hochzeitsdatum: ... Location/Gebiet: ...",
        nav_home: "Startseite",
        nav_transfer: "VIP-Transfer",
        nav_wedding: "VIP-Hochzeitsauto",
        nav_regions: "Einsatzgebiete",
        nav_blog: "Blog",
        nav_cta: "Transfer buchen",
        rp_locate: "Meinen Standort verwenden",
        rp_swap_short: "Tauschen",
        rp_swap: "Abholung und Ziel tauschen",
        pax: "Pers.",
        rp_map: "Routenkarte",
        rp_badge: "VIP-Transfer-Angebot",
        quick_title: "oder wählen Sie eine beliebte Route:",
        q1_title: "Flughafen ⇄ Çankaya",
        q1_sub: "Protokollempfang",
        q2_title: "Flughafen ⇄ Hotel",
        q2_sub: "Komfortable Fahrt",
        q3_title: "Tagesmiete",
        q3_sub: "Fahrzeug mit Chauffeur",
        season_title: "Winterangebote",
        s1_title: "Skitransfer",
        s2_title: "Silvesternacht",
        s2_sub: "Mit Chauffeur · Jahresabschlussfeiern",
        s3_title: "Hochzeitsauto 2027",
        s3_sub: "Frühbuchung offen",
        price_city: "Stadttransfer",
        price_group: "Delegationen",
        price_exec: "Repräsentationsfahrzeug",
        price_quote: "Preis anfragen",
        f_pax6: "6 Pers.",
        f_bag6: "6 Koffer",
        f_wifi: "WLAN & Steckdose",
        f_pax13: "13 Pers.",
        f_bag15: "15 Koffer",
        f_tv: "TV & Kühlschrank",
        f_pax3: "3 Pers.",
        f_bag2: "2 Koffer",
        f_protocol: "Protokoll",
        cat_wedding: "VIP-Hochzeitsauto",
        cat_transfer: "VIP-Transfer Ankara",
        cat_esb_cankaya: "Esenboğa – Çankaya",
        cat_airport: "✈️ Flughafen",
        cat_intercity: "🛣️ Fernstrecken",
        cat_corporate: "🏛️ Firmen",
        cat_rental: "🔑 Mit Chauffeur",
        card1_tag: "Hochzeit",
        card1_title: "VIP-Hochzeitsauto in Ankara",
        card1_desc: "Hochzeitsauto-Pakete mit dem Mercedes Vito Maybach in Ankara – inklusive Chauffeur, Kraftstoff und Dekoration.",
        card2_tag: "Transfer",
        card2_title: "VIP-Transfer in Ankara",
        card2_desc: "VIP-Transfers rund um die Uhr in Ankara: Flughafen Esenboğa, Çankaya, Hotels und Fernstrecken.",
        card3_tag: "Flughafen",
        card3_title: "Flughafentransfer Ankara",
        card3_desc: "VIP-Transfer ab Flughafen Esenboğa mit CIP-Empfang, Flugverfolgung und Namensschild.",
        faq_title: "HÄUFIGE <span class=\"gold-text\">FRAGEN</span>",
        faq_desc: "Häufige Fragen zu Ihrem Transfer.",
        faq1_q: "Stellen Sie Rechnungen aus?",
        faq1_a: "Ja, jeder Transfer wird in Rechnung gestellt. Die Rechnung wird auf Ihr Unternehmen ausgestellt, inkl. 20 % MwSt.",
        faq2_q: "Was passiert bei einer Flugverspätung?",
        faq2_a: "Wir verfolgen Ihren Flug. Bei einer Verspätung wartet Ihr Chauffeur ohne Aufpreis auf Sie.",
        faq3_q: "Darf im Fahrzeug geraucht werden?",
        faq3_a: "Aus Hygienegründen ist das Rauchen in unseren Fahrzeugen nicht gestattet. Auf Wunsch legen wir gerne eine Pause ein.",
        loc_title: "Leistungen & Routen",
        loc_prices: "VIP-Transfer-Preise Ankara",
        loc_wedding: "VIP-Hochzeitsauto",
        loc_airport: "Flughafentransfer Ankara",
        loc_corp: "Firmentransfer",
        loc_chauffeur: "Fahrzeug mit Chauffeur",
        loc_ist: "Transfer nach Istanbul",
        loc_kap: "Transfer nach Kappadokien",
        loc_ant: "Transfer nach Antalya",
        loc_bod: "Transfer nach Bodrum",
        loc_bolu: "Transfer nach Bolu / Abant",
        insta_title: "WIR AUF <span class=\"gold-text\">INSTAGRAM</span>",
        insta_desc: "Unsere Referenzen und Fahrzeuge:",
        insta_btn: "Ansehen",
        insta_mute: "Ton an/aus",
        fq_home: "Startseite",
        fq_fleet: "Fahrzeugflotte",
        fq_calc: "Preisrechner",
        fq_w_cankaya: "VIP-Hochzeitsauto Çankaya",
        fq_w_incek: "VIP-Hochzeitsauto İncek",
        fq_w_golbasi: "VIP-Hochzeitsauto Gölbaşı",
        fq_esb_cankaya: "VIP-Transfer Esenboğa – Çankaya",
        fq_ski: "Skitransfer ab Ankara",
        fq_nye: "Silvester mit Chauffeur",
        fq_special: "Auto für besondere Anlässe",
        r1: "Esenboğa - Çankaya",
        r2: "Esenboğa - Kızılay",
        r3: "Esenboğa - Ümitköy",
        r4: "Ankara - Kappadokien",
        r5: "Ankara - Bolu/Abant",
        fb_terms: "Fernabsatzvertrag",
        bn_call: "ANRUFEN"
    },
    ru: {
        menu_fleet: "Автопарк",
        menu_transfer: "Трансфер",
        menu_blog: "Гид",
        menu_contact: "Контакт",
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
        wa_ask: "Есть ли свободные места?",

        // --- Ana sayfa (2026-11) ---
        hero_title: "<span class=\"vip-eyebrow\">VIP-трансфер и свадебные авто в Анкаре</span>ПРОТОКОЛЬНЫЙ <span class=\"gold-text\">КОМФОРТ</span> В АНКАРЕ",
        annc_aria: "Объявление",
        annc_long: "Открыто раннее бронирование <strong>свадебных авто на 2027 год</strong> · Закрепите дату предоплатой",
        annc_short: "<strong>Свадебный авто 2027</strong>: раннее бронирование",
        annc_cta: "Забронировать",
        annc_close: "Закрыть объявление",
        annc_wa: "Здравствуйте, хочу заранее забронировать свадебный автомобиль на 2027 год. Дата свадьбы: ... Зал/район: ...",
        nav_home: "Главная",
        nav_transfer: "VIP-трансфер",
        nav_wedding: "Свадебный авто",
        nav_regions: "Районы",
        nav_blog: "Блог",
        nav_cta: "Заказать трансфер",
        rp_locate: "Моё местоположение",
        rp_swap_short: "Поменять",
        rp_swap: "Поменять местами откуда и куда",
        pax: "чел.",
        rp_map: "Карта маршрута",
        rp_badge: "Предложение VIP-трансфера",
        quick_title: "или выберите популярный маршрут:",
        q1_title: "Аэропорт ⇄ Чанкая",
        q1_sub: "Протокольная встреча",
        q2_title: "Аэропорт ⇄ Отель",
        q2_sub: "Комфортная поездка",
        q3_title: "Аренда на день",
        q3_sub: "Авто с водителем",
        season_title: "Зимние услуги",
        s1_title: "Горнолыжный трансфер",
        s2_title: "Новогодняя ночь",
        s2_sub: "Авто с водителем · Корпоративы",
        s3_title: "Свадебный авто 2027",
        s3_sub: "Раннее бронирование открыто",
        price_city: "По городу",
        price_group: "Делегации",
        price_exec: "Представительский авто",
        price_quote: "Узнать цену",
        f_pax6: "6 мест",
        f_bag6: "6 чемоданов",
        f_wifi: "Wi-Fi и розетки",
        f_pax13: "13 мест",
        f_bag15: "15 чемоданов",
        f_tv: "ТВ и холодильник",
        f_pax3: "3 места",
        f_bag2: "2 чемодана",
        f_protocol: "Протокол",
        cat_wedding: "Свадебный авто",
        cat_transfer: "VIP-трансфер",
        cat_esb_cankaya: "Эсенбога – Чанкая",
        cat_airport: "✈️ Аэропорт",
        cat_intercity: "🛣️ Междугородние",
        cat_corporate: "🏛️ Корпоративные",
        cat_rental: "🔑 Аренда",
        card1_tag: "Свадьба",
        card1_title: "VIP-свадебный авто в Анкаре",
        card1_desc: "Пакеты свадебного авто Mercedes Vito Maybach в Анкаре: водитель, топливо и украшение включены.",
        card2_tag: "Трансфер",
        card2_title: "VIP-трансфер в Анкаре",
        card2_desc: "VIP-трансфер в Анкаре 24/7: аэропорт Эсенбога, Чанкая, отели и междугородние маршруты.",
        card3_tag: "Аэропорт",
        card3_title: "Трансфер из аэропорта Анкары",
        card3_desc: "VIP-трансфер из аэропорта Эсенбога: CIP-встреча, отслеживание рейса и табличка с именем.",
        faq_title: "ЧАСТЫЕ <span class=\"gold-text\">ВОПРОСЫ</span>",
        faq_desc: "Частые вопросы о трансфере.",
        faq1_q: "Вы выставляете счёт?",
        faq1_a: "Да, на каждый трансфер выставляется счёт. Счёт оформляется на вашу компанию, НДС 20% включён.",
        faq2_q: "Что, если рейс задержится?",
        faq2_a: "Мы отслеживаем ваш рейс. При задержке водитель дождётся вас без доплаты.",
        faq3_q: "Можно ли курить в машине?",
        faq3_a: "В наших автомобилях не курят по гигиеническим соображениям, но по вашей просьбе мы сделаем остановку.",
        loc_title: "Услуги и маршруты",
        loc_prices: "Цены на VIP-трансфер",
        loc_wedding: "Свадебный авто",
        loc_airport: "Трансфер из аэропорта",
        loc_corp: "Корпоративный трансфер",
        loc_chauffeur: "Аренда авто с водителем",
        loc_ist: "Трансфер в Стамбул",
        loc_kap: "Трансфер в Каппадокию",
        loc_ant: "Трансфер в Анталью",
        loc_bod: "Трансфер в Бодрум",
        loc_bolu: "Трансфер в Болу / Абант",
        insta_title: "МЫ В <span class=\"gold-text\">INSTAGRAM</span>",
        insta_desc: "Наши отзывы и автомобили:",
        insta_btn: "Смотреть",
        insta_mute: "Вкл./выкл. звук",
        fq_home: "Главная",
        fq_fleet: "Автопарк",
        fq_calc: "Расчёт цены",
        fq_w_cankaya: "Свадебный авто Чанкая",
        fq_w_incek: "Свадебный авто Инджек",
        fq_w_golbasi: "Свадебный авто Гёльбашы",
        fq_esb_cankaya: "VIP-трансфер Эсенбога – Чанкая",
        fq_ski: "Горнолыжный трансфер",
        fq_nye: "Авто с водителем на Новый год",
        fq_special: "Авто для особых случаев",
        r1: "Эсенбога - Чанкая",
        r2: "Эсенбога - Кызылай",
        r3: "Эсенбога - Юмиткёй",
        r4: "Анкара - Каппадокия",
        r5: "Анкара - Болу/Абант",
        fb_terms: "Договор дистанционной продажи",
        bn_call: "ЗВОНОК"
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
    const t = translations[lang];
    if (!t) return;
    currentLang = lang;
    document.documentElement.lang = lang;

    // Metinler: HTML içeren değerler innerHTML, diğerleri textContent ile yazılır
    document.querySelectorAll('[data-lang]').forEach(el => {
        const value = t[el.getAttribute('data-lang')];
        if (value == null) return;
        if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') el.placeholder = value;
        else if (/<[a-z]/i.test(value)) el.innerHTML = value;
        else el.textContent = value;
    });

    // Öznitelikler: data-lang-attr="title:anahtar;aria-label:anahtar"
    document.querySelectorAll('[data-lang-attr]').forEach(el => {
        el.getAttribute('data-lang-attr').split(';').forEach(pair => {
            const [attr, key] = pair.split(':').map(x => x && x.trim());
            if (attr && key && t[key] != null) el.setAttribute(attr, t[key]);
        });
    });

    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.innerText.toLowerCase() === lang);
    });

    // WhatsApp mesajları ziyaretçinin dilinde
    const wa = (text) => `https://wa.me/${CONFIG.whatsappPhone}?text=${encodeURIComponent(text)}`;
    const annc = document.querySelector('.annc-link');
    if (annc && t.annc_wa) annc.href = wa(t.annc_wa);
    const float = document.querySelector('.whatsapp-float');
    if (float && t.wa_msg) float.href = wa(t.wa_msg);

    if (typeof window.onViptripLanguageChange === 'function') window.onViptripLanguageChange(lang);
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
    // Arama motoru tarayıcıları (Googlebot vb.) varsayılan Türkçe içeriği görür;
    // aksi halde Google sayfayı İngilizce tarayıcı ayarlarıyla işleyip İngilizce dizine ekleyebilir.
    const isCrawler = /googlebot|google-inspectiontool|adsbot-google|mediapartners-google|storebot-google|bingbot|yandexbot|yandex\.com\/bots|duckduckbot|baiduspider|slurp|applebot|petalbot/i.test(navigator.userAgent || '');
    const userLang = isCrawler ? 'tr' : (navigator.language || navigator.userLanguage || 'tr').toLowerCase();
    if (userLang.startsWith('en')) changeLanguage('en');
    else if (userLang.startsWith('de')) changeLanguage('de');
    else if (userLang.startsWith('ru')) changeLanguage('ru');
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
