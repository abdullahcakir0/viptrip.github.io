/* =========================================================
   VIPTRIP · GÜZERGÂH PLANLAYICI
   - Anında yerel öneriler + Photon (iptal edilebilir, önbellekli)
   - İki OSRM sunucusuna paralel istek, ilk yanıt kazanır
   - Seçim yapılır yapılmaz rota arka planda hesaplanır
   - Leaflet haritası (işaretler anında, rota çizgisi gelince)
   - Fiyatlandırma: script.js içindeki CONFIG ile birebir aynı
   ========================================================= */
(function () {
    'use strict';

    /* ---------- 1. POPÜLER LOKASYONLAR ---------- */
    const ANKARA_LOCATIONS = [
        { name: "Esenboğa Havalimanı (ESB)", aliases: ["esenboga", "havalimani", "airport", "esb", "havaalani"], coords: [32.9950, 40.1281], icon: "fa-plane" },
        { name: "Ankara YHT Garı (Merkez)", aliases: ["yht", "ankara gari", "tren gari", "gar", "hizli tren"], coords: [32.8447, 39.9362], icon: "fa-train" },
        { name: "AŞTİ Otobüs Terminali", aliases: ["asti", "otogar", "terminal"], coords: [32.8128, 39.9172], icon: "fa-bus" },
        { name: "Eryaman YHT Garı", aliases: ["eryaman yht", "eryaman gar"], coords: [32.6517, 39.9675], icon: "fa-train" },
        { name: "Çankaya / Tunalı Hilmi", aliases: ["cankaya", "tunali", "tunali hilmi", "kavaklidere"], coords: [32.8597, 39.8974], icon: "fa-map-pin" },
        { name: "Kızılay / Bakanlıklar / TBMM", aliases: ["kizilay", "bakanliklar", "tbmm", "meclis", "sihhiye"], coords: [32.8543, 39.9208], icon: "fa-landmark" },
        { name: "Gaziosmanpaşa (GOP) / Filistin Cad.", aliases: ["gop", "gaziosmanpasa", "filistin", "ugur mumcu"], coords: [32.8710, 39.8965], icon: "fa-map-pin" },
        { name: "Çukurambar / Söğütözü (İş Merkezleri)", aliases: ["cukurambar", "sogutozu", "armada", "next level", "the paragon"], coords: [32.8122, 39.9075], icon: "fa-briefcase" },
        { name: "İncek / Beytepe / Alacaatlı", aliases: ["incek", "beytepe", "alacaatli", "incek loft"], coords: [32.7214, 39.8452], icon: "fa-home" },
        { name: "Çayyolu / Ümitköy / Yaşamkent", aliases: ["cayyolu", "umitkoy", "yasamkent", "mesa koru"], coords: [32.7058, 39.8872], icon: "fa-map-pin" },
        { name: "Bilkent / ODTÜ / Hacettepe", aliases: ["bilkent", "odtu", "hacettepe", "angora"], coords: [32.7533, 39.8732], icon: "fa-graduation-cap" },
        { name: "Gölbaşı / Mogan Gölü", aliases: ["golbasi", "mogan", "eymir"], coords: [32.8083, 39.7915], icon: "fa-water" },
        { name: "Yenimahalle / Batıkent / Eryaman", aliases: ["yenimahalle", "batikent", "eryaman", "goksu"], coords: [32.7314, 39.9647], icon: "fa-map-pin" },
        { name: "Keçiören / Etlik", aliases: ["kecioren", "etlik", "kuscagiz"], coords: [32.8636, 39.9790], icon: "fa-map-pin" },
        { name: "Ostim / İvedik OSB", aliases: ["ostim", "ivedik", "osb", "sanayi"], coords: [32.7505, 39.9722], icon: "fa-industry" },
        { name: "Bilkent Şehir Hastanesi", aliases: ["sehir hastanesi", "bilkent sehir hastanesi", "hastane"], coords: [32.7745, 39.8970], icon: "fa-hospital" },
        { name: "Etlik Şehir Hastanesi", aliases: ["etlik sehir hastanesi", "etlik hastane"], coords: [32.8340, 39.9790], icon: "fa-hospital" },
        { name: "Anıtkabir", aliases: ["anitkabir", "tandogan"], coords: [32.8369, 39.9254], icon: "fa-landmark" },
        { name: "Sheraton Hotel Ankara (GOP)", aliases: ["sheraton", "sheraton ankara", "sheraton otel"], coords: [32.8660, 39.8943], icon: "fa-hotel" },
        { name: "JW Marriott Hotel Ankara (Söğütözü)", aliases: ["jw marriott", "marriott"], coords: [32.8142, 39.9114], icon: "fa-hotel" },
        { name: "Hilton SA Ankara (Kavaklıdere)", aliases: ["hilton", "hilton ankara", "hilton sa"], coords: [32.8621, 39.8988], icon: "fa-hotel" },
        { name: "Swissôtel Ankara (Çankaya)", aliases: ["swissotel", "swiss otel"], coords: [32.8653, 39.8753], icon: "fa-hotel" },
        { name: "Divan Ankara (Çankaya)", aliases: ["divan", "divan otel"], coords: [32.8606, 39.9015], icon: "fa-hotel" },
        { name: "Bolu / Abant Gölü", aliases: ["bolu", "abant", "abant golu", "yedigoller", "kartalkaya"], coords: [31.2818, 40.6053], icon: "fa-mountain" },
        { name: "Kapadokya / Nevşehir / Göreme", aliases: ["kapadokya", "nevsehir", "urgup", "goreme", "uchisar"], coords: [34.8290, 38.6431], icon: "fa-map-signs" },
        { name: "İstanbul (Sabiha Gökçen - SAW)", aliases: ["istanbul", "sabiha", "sabiha gokcen", "saw", "anadolu yakasi"], coords: [29.3092, 40.8986], icon: "fa-city" },
        { name: "İstanbul (İstanbul Havalimanı - İGA)", aliases: ["iga", "istanbul havalimani", "avrupa yakasi"], coords: [28.7279, 41.2608], icon: "fa-city" },
        { name: "Eskişehir Merkez", aliases: ["eskisehir", "odunpazari"], coords: [30.5256, 39.7767], icon: "fa-road" },
        { name: "Konya Merkez", aliases: ["konya", "mevlana", "selcuklu"], coords: [32.4846, 37.8746], icon: "fa-road" }
    ];

    const ANKARA_CENTER = [39.93, 32.85];
    const TR_BBOX = "25.6,35.8,44.9,42.2";
    const PHOTON = "https://photon.komoot.io";
    const OSRM_SERVERS = [
        "https://router.project-osrm.org/route/v1/driving/",
        "https://routing.openstreetmap.de/routed-car/route/v1/driving/"
    ];
    const ROUTE_TIMEOUT = 4000;

    /* ---------- 2. YARDIMCILAR ---------- */
    const I18N = {
        tr: { searching: "Aranıyor…", no_result: "Sonuç bulunamadı", my_location: "Mevcut Konumum", locating: "Konum alınıyor…", loc_denied: "Konum izni verilmedi.", calc_wait: "Rota hesaplanıyor…", estimate_note: "Tahmini sabit fiyat · Otoyol, köprü ve bekleme dahil değildir.", vehicle: "Araç", vito: "Mercedes Vito VIP (1-6 Kişi)", sprinter: "Mercedes Sprinter VIP (7-13 Kişi)", approx: "yaklaşık", min: "dk", hour: "sa", same_place: "Nereden ve nereye aynı olamaz." },
        en: { searching: "Searching…", no_result: "No results", my_location: "My Current Location", locating: "Getting location…", loc_denied: "Location permission denied.", calc_wait: "Calculating route…", estimate_note: "Estimated fixed price · Tolls and waiting not included.", vehicle: "Vehicle", vito: "Mercedes Vito VIP (1-6 Pax)", sprinter: "Mercedes Sprinter VIP (7-13 Pax)", approx: "approx.", min: "min", hour: "h", same_place: "Pick-up and drop-off cannot be the same." },
        de: { searching: "Suche…", no_result: "Keine Ergebnisse", my_location: "Mein Standort", locating: "Standort wird ermittelt…", loc_denied: "Standortzugriff verweigert.", calc_wait: "Route wird berechnet…", estimate_note: "Geschätzter Festpreis · Maut und Wartezeit nicht inbegriffen.", vehicle: "Fahrzeug", vito: "Mercedes Vito VIP (1-6 Pers.)", sprinter: "Mercedes Sprinter VIP (7-13 Pers.)", approx: "ca.", min: "Min.", hour: "Std.", same_place: "Start und Ziel dürfen nicht gleich sein." },
        ru: { searching: "Поиск…", no_result: "Ничего не найдено", my_location: "Моё местоположение", locating: "Определяем местоположение…", loc_denied: "Доступ к геолокации запрещён.", calc_wait: "Расчёт маршрута…", estimate_note: "Ориентировочная фиксированная цена · Платные дороги не включены.", vehicle: "Авто", vito: "Mercedes Vito VIP (1-6 чел.)", sprinter: "Mercedes Sprinter VIP (7-13 чел.)", approx: "≈", min: "мин", hour: "ч", same_place: "Пункты отправления и назначения совпадают." }
    };

    const lang = () => (typeof currentLang !== 'undefined' && I18N[currentLang]) ? currentLang : 'tr';
    const t = (key) => {
        const all = (typeof translations !== 'undefined' && translations) || {};
        const base = all[lang()] || {};
        return I18N[lang()][key] || base[key] || I18N.tr[key] || (all.tr && all.tr[key]) || key;
    };

    const norm = (s) => (s || "").toString().toLocaleLowerCase('tr-TR')
        .replace(/ğ/g, "g").replace(/ü/g, "u").replace(/ş/g, "s").replace(/ı/g, "i")
        .replace(/i̇/g, "i").replace(/ö/g, "o").replace(/ç/g, "c").replace(/â/g, "a").replace(/ô/g, "o")
        .replace(/[^a-z0-9 ]+/g, " ").replace(/\s+/g, " ").trim();

    const esc = (s) => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

    function highlight(label, query) {
        const q = norm(query);
        if (!q) return esc(label);
        const n = norm(label);
        // norm() aynı uzunlukta kalmayabilir; basit ve güvenli: kelime başı eşleşmesini vurgula
        const idx = n.indexOf(q);
        if (idx < 0 || n.length !== label.length) return esc(label);
        return esc(label.slice(0, idx)) + '<mark>' + esc(label.slice(idx, idx + q.length)) + '</mark>' + esc(label.slice(idx + q.length));
    }

    function haversineKm(a, b) {
        const R = 6371, toRad = d => d * Math.PI / 180;
        const dLat = toRad(b[1] - a[1]), dLon = toRad(b[0] - a[0]);
        const h = Math.sin(dLat / 2) ** 2 + Math.cos(toRad(a[1])) * Math.cos(toRad(b[1])) * Math.sin(dLon / 2) ** 2;
        return 2 * R * Math.atan2(Math.sqrt(h), Math.sqrt(1 - h));
    }

    function fetchJSON(url, { signal, timeout } = {}) {
        const ctrl = new AbortController();
        const onAbort = () => ctrl.abort();
        if (signal) signal.addEventListener('abort', onAbort, { once: true });
        const timer = timeout ? setTimeout(() => ctrl.abort(), timeout) : null;
        return fetch(url, { signal: ctrl.signal })
            .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
            .finally(() => { if (timer) clearTimeout(timer); if (signal) signal.removeEventListener('abort', onAbort); });
    }

    /* ---------- 3. ARAMA (YEREL + PHOTON) ---------- */
    function searchLocal(query, limit = 5) {
        const q = norm(query);
        if (!q) return [];
        const scored = [];
        for (const loc of ANKARA_LOCATIONS) {
            const keys = [norm(loc.name), ...loc.aliases.map(norm)];
            let best = 0;
            for (const k of keys) {
                if (k === q) best = Math.max(best, 100);
                else if (k.startsWith(q)) best = Math.max(best, 80);
                else if (k.split(' ').some(w => w.startsWith(q))) best = Math.max(best, 60);
                else if (q.length >= 3 && k.includes(q)) best = Math.max(best, 40);
            }
            if (best) scored.push({ loc, best });
        }
        return scored.sort((a, b) => b.best - a.best).slice(0, limit)
            .map(({ loc }) => ({ label: loc.name, sub: "VipTrip · Popüler", coords: loc.coords, icon: loc.icon, local: true }));
    }

    function bestLocalMatch(query) {
        const q = norm(query);
        if (!q) return null;
        const exact = ANKARA_LOCATIONS.find(l => norm(l.name) === q || l.aliases.some(a => norm(a) === q));
        if (exact) return { label: exact.name, coords: exact.coords };
        const r = searchLocal(query, 1)[0];
        return r ? { label: r.label, coords: r.coords } : null;
    }

    const PHOTON_ICONS = {
        aerodrome: "fa-plane", airport: "fa-plane", station: "fa-train", bus_station: "fa-bus",
        hotel: "fa-hotel", motel: "fa-hotel", hostel: "fa-hotel", guest_house: "fa-hotel",
        hospital: "fa-hospital", clinic: "fa-hospital", university: "fa-graduation-cap", school: "fa-graduation-cap",
        restaurant: "fa-utensils", cafe: "fa-coffee", mall: "fa-shopping-bag", embassy: "fa-flag",
        city: "fa-city", town: "fa-city", village: "fa-home", suburb: "fa-map-pin", residential: "fa-home"
    };

    function photonToPlace(f) {
        const p = f.properties || {};
        const street = [p.street, p.housenumber].filter(Boolean).join(' ');
        const main = p.name || street || p.district || p.city || p.county;
        const subParts = [p.name ? street : null, p.district || p.locality, p.city || p.county, p.state !== (p.city || p.county) ? p.state : null]
            .filter(Boolean).filter((v, i, arr) => arr.indexOf(v) === i && v !== main);
        return {
            label: main,
            sub: subParts.slice(0, 3).join(', '),
            coords: f.geometry.coordinates,
            icon: PHOTON_ICONS[p.osm_value] || PHOTON_ICONS[p.type] || "fa-map-marker-alt"
        };
    }

    const photonCache = new Map();
    function searchRemote(query, signal) {
        const key = norm(query);
        if (photonCache.has(key)) return Promise.resolve(photonCache.get(key));
        const url = `${PHOTON}/api/?q=${encodeURIComponent(query)}&limit=7&lat=${ANKARA_CENTER[0]}&lon=${ANKARA_CENTER[1]}&bbox=${TR_BBOX}`;
        return fetchJSON(url, { signal, timeout: 5000 }).then(data => {
            const seen = new Set();
            const places = (data.features || []).map(photonToPlace).filter(p => {
                if (!p.label) return false;
                const k = norm(p.label + '|' + p.sub);
                if (seen.has(k)) return false;
                seen.add(k);
                return true;
            });
            photonCache.set(key, places);
            return places;
        });
    }

    /* ---------- 4. ROTA (PARALEL OSRM + ÖNBELLEK) ---------- */
    const routeCache = new Map();

    function fallbackRoute(a, b) {
        const km = Math.max(5, haversineKm(a, b) * 1.28);
        const speed = km > 60 ? 85 : 48;
        return { distanceKm: +km.toFixed(1), durationMin: Math.max(15, Math.round(km / speed * 60)), geometry: null, approximate: true };
    }

    function requestRoute(a, b) {
        const key = `${a.join(',')};${b.join(',')}`;
        if (routeCache.has(key)) return routeCache.get(key);

        const shared = new AbortController();
        const attempts = OSRM_SERVERS.map(base =>
            fetchJSON(`${base}${key}?overview=simplified&geometries=geojson`, { signal: shared.signal, timeout: ROUTE_TIMEOUT })
                .then(data => {
                    const r = data && data.code === "Ok" && data.routes && data.routes[0];
                    if (!r || !r.distance) throw new Error('no-route');
                    return {
                        distanceKm: +(r.distance / 1000).toFixed(1),
                        durationMin: Math.round(r.duration / 60),
                        geometry: r.geometry ? r.geometry.coordinates.map(([lon, lat]) => [lat, lon]) : null,
                        approximate: false
                    };
                })
        );

        const promise = Promise.any(attempts)
            .then(res => { shared.abort(); return res; })
            .catch(() => fallbackRoute(a, b));

        routeCache.set(key, promise);
        // Yedek sonuçlar önbellekte kalmasın, bir sonraki denemede tekrar sorulsun
        promise.then(r => { if (r.approximate) routeCache.delete(key); });
        return promise;
    }

    /* ---------- 5. FİYAT (ÖNCEKİ İLE BİREBİR AYNI) ---------- */
    function calculatePrice(distanceKm, vehicle) {
        const isSprinter = vehicle === 'sprinter';
        const rate = isSprinter ? CONFIG.pricePerKmSprinter : CONFIG.pricePerKm;
        const minPrice = isSprinter ? CONFIG.minPriceSprinter : CONFIG.minPriceVito;
        return Math.ceil(Math.max(minPrice, distanceKm * rate) / 50) * 50;
    }

    function formatDuration(min) {
        if (min < 60) return `${min} ${t('min')}`;
        const h = Math.floor(min / 60), m = min % 60;
        return m ? `${h} ${t('hour')} ${m} ${t('min')}` : `${h} ${t('hour')}`;
    }

    /* ---------- 6. HARİTA ---------- */
    const mapState = { map: null, layer: null };

    function markerIcon(letter, cls) {
        return L.divIcon({ className: '', html: `<div class="rp-pin ${cls}">${letter}</div>`, iconSize: [30, 30], iconAnchor: [15, 15] });
    }

    function ensureMap() {
        if (typeof L === 'undefined') return null;
        if (mapState.map) return mapState.map;
        const el = document.getElementById('rp-map');
        if (!el) return null;
        const map = L.map(el, { zoomControl: false, attributionControl: true, scrollWheelZoom: false, tap: false })
            .setView(ANKARA_CENTER, 11);
        L.control.zoom({ position: 'bottomright' }).addTo(map);
        L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
            subdomains: 'abcd', maxZoom: 19, detectRetina: true,
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OSM</a> &copy; <a href="https://carto.com/" target="_blank" rel="noopener">CARTO</a>'
        }).addTo(map);
        mapState.map = map;
        mapState.layer = L.layerGroup().addTo(map);
        return map;
    }

    function drawMap(a, b, geometry) {
        const map = ensureMap();
        if (!map) { document.getElementById('rp-map')?.classList.add('rp-map--off'); return; }
        map.invalidateSize();
        const A = [a[1], a[0]], B = [b[1], b[0]];
        mapState.layer.clearLayers();
        const line = geometry && geometry.length > 1
            ? L.polyline(geometry, { color: '#D4AF37', weight: 5, opacity: 0.95, lineCap: 'round' })
            : L.polyline([A, B], { color: '#D4AF37', weight: 3, opacity: 0.7, dashArray: '6 10' });
        if (geometry) L.polyline(geometry, { color: '#000', weight: 9, opacity: 0.35 }).addTo(mapState.layer);
        line.addTo(mapState.layer);
        L.marker(A, { icon: markerIcon('A', 'rp-pin--a'), keyboard: false }).addTo(mapState.layer);
        L.marker(B, { icon: markerIcon('B', 'rp-pin--b'), keyboard: false }).addTo(mapState.layer);
        map.fitBounds(line.getBounds(), { padding: [36, 36], maxZoom: 14, animate: !!geometry });
    }

    /* ---------- 7. DURUM & DOM ---------- */
    const state = {
        pickup: null,   // { label, coords:[lon,lat] }
        dropoff: null,
        result: null,
        calcSeq: 0
    };

    const $ = (id) => document.getElementById(id);
    let els = {};

    function getVehicle() {
        const checked = document.querySelector('input[name="rp-vehicle"]:checked');
        return checked ? checked.value : 'vito';
    }

    function showError(msg) {
        els.error.textContent = msg;
        els.error.hidden = !msg;
    }

    /* ----- Öneri listesi (combobox) ----- */
    function createCombobox(field) {
        const input = $(`${field}-input`);
        const list = $(`${field}-suggestions`);
        const wrap = input.closest('.rp-field');
        let items = [];
        let active = -1;
        let ctrl = null;
        let timer = null;

        function open() { list.hidden = false; input.setAttribute('aria-expanded', 'true'); wrap.classList.add('is-open'); }
        function close() { list.hidden = true; input.setAttribute('aria-expanded', 'false'); wrap.classList.remove('is-open'); active = -1; }

        function render(query, places, loading) {
            items = places;
            active = places.length ? 0 : -1;
            let html = places.map((p, i) => `
                <li role="option" id="${field}-opt-${i}" class="${i === active ? 'is-active' : ''}" data-i="${i}">
                    <i class="fas ${p.icon}"></i>
                    <span class="rp-s-text"><span class="rp-s-main">${highlight(p.label, query)}</span>${p.sub ? `<span class="rp-s-sub">${esc(p.sub)}</span>` : ''}</span>
                </li>`).join('');
            if (loading) html += `<li class="rp-s-status"><i class="fas fa-circle-notch fa-spin"></i> ${t('searching')}</li>`;
            else if (!places.length) html += `<li class="rp-s-status">${t('no_result')}</li>`;
            list.innerHTML = html;
            input.setAttribute('aria-activedescendant', active >= 0 ? `${field}-opt-${active}` : '');
            open();
        }

        function setActive(i) {
            if (!items.length) return;
            active = (i + items.length) % items.length;
            list.querySelectorAll('li[role="option"]').forEach((li, idx) => li.classList.toggle('is-active', idx === active));
            const li = list.querySelector(`#${field}-opt-${active}`);
            if (li) li.scrollIntoView({ block: 'nearest' });
            input.setAttribute('aria-activedescendant', `${field}-opt-${active}`);
        }

        function choose(place) {
            input.value = place.label;
            state[field] = { label: place.label, coords: place.coords };
            wrap.classList.add('is-set');
            close();
            showError('');
            onPlaceChange();
            if (field === 'pickup' && !state.dropoff) $('dropoff-input').focus();
        }

        function query(val) {
            const q = val.trim();
            if (ctrl) ctrl.abort();
            clearTimeout(timer);
            if (q.length < 2) { close(); return; } // liste sadece yazınca açılır
            const local = searchLocal(q, 4);
            const key = norm(q);
            if (photonCache.has(key)) {
                render(q, merge(local, photonCache.get(key)), false);
                return;
            }
            render(q, local, true); // anında yerel sonuç + yükleniyor satırı
            timer = setTimeout(() => {
                ctrl = new AbortController();
                const mySignal = ctrl.signal;
                searchRemote(q, mySignal)
                    .then(remote => { if (!mySignal.aborted && input.value.trim() === q) render(q, merge(local, remote), false); })
                    .catch(() => { if (!mySignal.aborted && input.value.trim() === q) render(q, local, false); });
            }, 140);
        }

        function merge(local, remote) {
            const seen = new Set(local.map(p => norm(p.label)));
            return [...local, ...remote.filter(p => !seen.has(norm(p.label)))].slice(0, 7);
        }

        input.addEventListener('input', () => {
            state[field] = null;
            wrap.classList.remove('is-set');
            query(input.value);
        });
        input.addEventListener('focus', () => { if (!state[field] && input.value.trim().length >= 2) query(input.value); });
        input.addEventListener('keydown', (e) => {
            if (list.hidden && (e.key === 'ArrowDown' || e.key === 'ArrowUp')) { query(input.value); return; }
            if (e.key === 'ArrowDown') { e.preventDefault(); setActive(active + 1); }
            else if (e.key === 'ArrowUp') { e.preventDefault(); setActive(active - 1); }
            else if (e.key === 'Enter') {
                if (!list.hidden && active >= 0 && items[active]) { e.preventDefault(); choose(items[active]); }
            } else if (e.key === 'Escape') close();
            else if (e.key === 'Tab' && !list.hidden && active >= 0 && items[active] && !state[field] && input.value.trim().length >= 2) choose(items[active]);
        });
        input.addEventListener('blur', () => setTimeout(close, 120));
        list.addEventListener('mousedown', (e) => {
            const li = e.target.closest('li[role="option"]');
            e.preventDefault();
            if (li) choose(items[+li.dataset.i]);
        });

        return {
            set(place) {
                input.value = place ? place.label : '';
                state[field] = place;
                wrap.classList.toggle('is-set', !!place);
            },
            close,
            async resolve() {
                if (state[field]) return state[field];
                const q = input.value.trim();
                if (!q) return null;
                const local = bestLocalMatch(q);
                if (local) { this.set(local); return local; }
                try {
                    const remote = await searchRemote(q);
                    if (remote[0]) { const p = { label: remote[0].label, coords: remote[0].coords }; this.set(p); return p; }
                } catch (e) { /* yoksay */ }
                return null;
            }
        };
    }

    /* ----- Seçim değişince rotayı arka planda hazırla ----- */
    function onPlaceChange() {
        if (state.pickup && state.dropoff) {
            requestRoute(state.pickup.coords, state.dropoff.coords); // ön yükleme
            calculate();
        }
    }

    /* ----- Hesaplama ----- */
    async function calculate() {
        els.combos.pickup.close();
        els.combos.dropoff.close();

        if (!els.pickupInput.value.trim() || !els.dropoffInput.value.trim()) {
            showError(t('error_fill'));
            return;
        }

        const seq = ++state.calcSeq;
        setLoading(true);

        const [p, d] = await Promise.all([els.combos.pickup.resolve(), els.combos.dropoff.resolve()]);
        if (seq !== state.calcSeq) return;
        if (!p || !d) { setLoading(false); showError(t('error_route')); return; }
        if (p.coords[0] === d.coords[0] && p.coords[1] === d.coords[1]) { setLoading(false); showError(t('same_place')); return; }

        showError('');
        openResult(p, d); // harita + işaretler anında
        const route = await requestRoute(p.coords, d.coords);
        if (seq !== state.calcSeq) return;

        state.result = { pickup: p, dropoff: d, route };
        renderResult();
        drawMap(p.coords, d.coords, route.geometry);
        setLoading(false);
    }

    function setLoading(on) {
        els.root.classList.toggle('is-loading', on);
        els.submit.disabled = on;
        els.submitLabel.textContent = on ? t('loading') : t('btn_calc');
    }

    function openResult(p, d) {
        const wasHidden = els.result.hidden;
        els.result.hidden = false;
        els.result.classList.add('is-pending');
        els.routeFrom.textContent = p.label;
        els.routeTo.textContent = d.label;
        els.price.textContent = '—';
        els.dist.textContent = '…';
        els.dur.textContent = '…';
        els.status.textContent = t('calc_wait');
        drawMap(p.coords, d.coords, null);
        if (wasHidden) {
            requestAnimationFrame(() => {
                const r = els.result.getBoundingClientRect();
                if (r.bottom > window.innerHeight) els.result.scrollIntoView({ behavior: 'smooth', block: 'center' });
            });
        }
    }

    function renderResult() {
        const r = state.result;
        if (!r) return;
        const vehicle = getVehicle();
        const price = calculatePrice(r.route.distanceKm, vehicle);
        const vehicleTitle = t(vehicle);

        els.result.classList.remove('is-pending');
        els.routeFrom.textContent = r.pickup.label;
        els.routeTo.textContent = r.dropoff.label;
        els.dist.textContent = `${r.route.approximate ? '~' : ''}${r.route.distanceKm.toLocaleString('tr-TR')} km`;
        els.dur.textContent = formatDuration(r.route.durationMin);
        els.veh.textContent = vehicleTitle;
        els.price.textContent = price.toLocaleString('tr-TR') + '₺';
        els.status.textContent = t('estimate_note');

        // WhatsApp mesajı için global veri (script.js ile uyumlu)
        window.calculationData = {
            price, distance: r.route.distanceKm, duration: r.route.durationMin,
            pickup: r.pickup.label, dropoff: r.dropoff.label, vehicle: vehicleTitle
        };
    }

    /* ----- Konumumu kullan ----- */
    function useMyLocation() {
        if (!navigator.geolocation) { showError(t('loc_denied')); return; }
        const input = els.pickupInput;
        const prev = input.value;
        input.value = t('locating');
        navigator.geolocation.getCurrentPosition(async (pos) => {
            const coords = [+pos.coords.longitude.toFixed(6), +pos.coords.latitude.toFixed(6)];
            let label = t('my_location');
            try {
                const data = await fetchJSON(`${PHOTON}/reverse?lon=${coords[0]}&lat=${coords[1]}&limit=1`, { timeout: 3000 });
                if (data.features && data.features[0]) {
                    const pl = photonToPlace(data.features[0]);
                    label = [pl.label, pl.sub.split(',')[0]].filter(Boolean).join(', ');
                }
            } catch (e) { /* etiket varsayılan kalır */ }
            els.combos.pickup.set({ label, coords });
            showError('');
            onPlaceChange();
            if (!state.dropoff) els.dropoffInput.focus();
        }, () => { input.value = prev; showError(t('loc_denied')); }, { enableHighAccuracy: true, timeout: 8000, maximumAge: 60000 });
    }

    /* ---------- 8. GLOBAL API (HTML onclick'ler için) ---------- */
    window.calculateDistancePrice = calculate;

    window.selectQuickRoute = function (pickupName, dropoffName) {
        const p = bestLocalMatch(pickupName), d = bestLocalMatch(dropoffName);
        if (p) els.combos.pickup.set(p);
        if (d) els.combos.dropoff.set(d);
        calculate();
        els.root.scrollIntoView({ behavior: 'smooth', block: 'start' });
    };

    window.bookNow = function () {
        const c = window.calculationData;
        if (!c || !c.price) return;
        const tr = (typeof translations !== 'undefined' && translations[lang()]) || {};
        const message = `
*VIPTRIP REZERVASYON TALEBİ* 🌟
---------------------------
📍 *${tr.wa_route || 'Güzergah'}:* ${c.pickup} ➔ ${c.dropoff}
📏 *${tr.res_dist || 'Mesafe'}:* ${c.distance} km (~${c.duration} dk)
🚐 *${tr.wa_vehicle || 'Araç'}:* ${c.vehicle}
💰 *${tr.wa_price || 'Fiyat'}:* ${c.price.toLocaleString('tr-TR')}₺
---------------------------
❓ *${tr.wa_ask || 'Müsaitlik durumunuz nedir?'}*`.trim();
        window.open(`https://wa.me/${CONFIG.whatsappPhone}?text=${encodeURIComponent(message)}`, '_blank', 'noopener');
    };

    // Dil değişince sonuç metinlerini tazele
    const origChangeLanguage = window.changeLanguage;
    if (typeof origChangeLanguage === 'function') {
        window.changeLanguage = function (l) {
            origChangeLanguage(l);
            if (state.result) renderResult();
        };
    }

    /* ---------- 9. BAŞLAT ---------- */
    function init() {
        els = {
            root: $('transfer'),
            form: $('rp-form'),
            pickupInput: $('pickup-input'),
            dropoffInput: $('dropoff-input'),
            submit: $('rp-submit'),
            submitLabel: document.querySelector('#rp-submit [data-lang="btn_calc"]'),
            error: $('rp-error'),
            result: $('price-result'),
            routeFrom: $('rp-route-from'),
            routeTo: $('rp-route-to'),
            dist: $('dist-val'),
            dur: $('dur-val'),
            veh: $('vehicle-val'),
            price: $('show-price'),
            status: $('rp-note')
        };
        if (!els.root || !els.form) return;

        els.combos = { pickup: createCombobox('pickup'), dropoff: createCombobox('dropoff') };

        els.form.addEventListener('submit', (e) => { e.preventDefault(); calculate(); });

        $('rp-swap').addEventListener('click', () => {
            const p = state.pickup, d = state.dropoff;
            const pv = els.pickupInput.value, dv = els.dropoffInput.value;
            els.combos.pickup.set(d); els.combos.dropoff.set(p);
            if (!d) els.pickupInput.value = dv;
            if (!p) els.dropoffInput.value = pv;
            if (state.pickup && state.dropoff) calculate();
        });

        $('rp-locate').addEventListener('click', useMyLocation);

        document.querySelectorAll('input[name="rp-vehicle"]').forEach(r =>
            r.addEventListener('change', () => { if (state.result) renderResult(); }));
    }

    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
    else init();
})();
