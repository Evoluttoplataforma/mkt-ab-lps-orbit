/* ============================================================
   Orbit · analytics.js
   Sistema portável de tracking + atribuição
   Spec: TRACKING.md (raiz do projeto)
   ------------------------------------------------------------
   - First-touch UTMs em cookie root domain (2 anos)
   - Pageview customizado no dataLayer
   - Geo IP (com cache em sessionStorage)
   - Scroll depth (25/50/75/90%)
   - Time on page (30s, 60s, ..., 600s)
   - FAQ open / nav drawer / sticky CTA
   - Helper window.__orbit.goChat(opts) — abre chat com UTMs
   - Expõe submitLead() para o form.js
   ============================================================ */

(function () {
  'use strict';

  // ---------- CONFIG (sobrescrever na página se necessário) ----------
  var DEFAULT_CONFIG = {
    webhookUrl: '',           // URL do webhook (Make/Zapier/n8n) — sobrescrever no HTML
    chatUrl: 'https://demonstracao.orbitgestao.com.br/chat',
    rootDomain: '.orbitgestao.com.br',
    cookieDays: 730,           // first-touch dura 2 anos
    geoEndpoint: 'https://ipapi.co/json/',
    debug: false
  };

  window.__pbqph = window.__pbqph || {};
  window.__pbqph.config = Object.assign({}, DEFAULT_CONFIG, window.__pbqph.config || {});
  var cfg = window.__pbqph.config;

  window.dataLayer = window.dataLayer || [];
  function push(obj) {
    window.dataLayer.push(obj);
    if (cfg.debug) console.log('[orbit:dataLayer]', obj);
  }

  // ---------- COOKIE / STORAGE HELPERS ----------
  function setCookie(name, value, days) {
    var maxAge = days * 24 * 60 * 60;
    var domain = '';
    try {
      if (location.hostname.indexOf(cfg.rootDomain.replace(/^\./, '')) !== -1) {
        domain = '; domain=' + cfg.rootDomain;
      }
    } catch (e) {}
    document.cookie = name + '=' + encodeURIComponent(value) +
      '; max-age=' + maxAge +
      '; path=/' + domain + '; SameSite=Lax';
  }
  function getCookie(name) {
    var match = document.cookie.match(new RegExp('(?:^|;\\s*)' + name + '=([^;]*)'));
    return match ? decodeURIComponent(match[1]) : '';
  }
  function ssGet(k) { try { return sessionStorage.getItem(k) || ''; } catch (e) { return ''; } }
  function ssSet(k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} }

  // ---------- IDS ----------
  function uuid() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
      var r = Math.random() * 16 | 0; return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
  }
  function getOrCreateSession() {
    var sid = ssGet('apex_session_id');
    if (!sid) { sid = 'sess_' + uuid(); ssSet('apex_session_id', sid); }
    return sid;
  }
  function newEventId() { return 'ev_' + uuid(); }

  // ---------- URL PARAMS ----------
  var TRACKED_PARAMS = [
    'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content',
    'fbclid', 'gclid', 'ttclid', 'msclkid',
    'gad_source', 'gad_campaignid', 'gbraid', 'wbraid', 'li_fat_id',
    'referrer_source'
  ];
  function getUrlParams() {
    var q = new URLSearchParams(location.search);
    var out = {};
    TRACKED_PARAMS.forEach(function (k) { if (q.get(k)) out[k] = q.get(k); });
    return out;
  }

  // ---------- FIRST-TOUCH (grava se não existe) ----------
  function captureFirstTouch() {
    var params = getUrlParams();
    var hasAny = false;
    Object.keys(params).forEach(function (k) {
      var ftKey = 'ft_' + k;
      if (!getCookie(ftKey) && params[k]) {
        setCookie(ftKey, params[k], cfg.cookieDays);
        hasAny = true;
      }
    });
    // first_visit / landing_page (uma vez)
    if (!getCookie('first_visit')) {
      setCookie('first_visit', new Date().toISOString(), cfg.cookieDays);
      setCookie('landing_page', location.pathname + location.search, cfg.cookieDays);
    }
    // _fbc para CAPI (formato fb.1.<ts>.<fbclid>)
    if (params.fbclid && !getCookie('_fbc')) {
      setCookie('_fbc', 'fb.1.' + Date.now() + '.' + params.fbclid, cfg.cookieDays);
    }
    if (hasAny && cfg.debug) console.log('[orbit] first-touch saved');
  }

  function readFirstTouch() {
    var out = {};
    TRACKED_PARAMS.forEach(function (k) {
      var v = getCookie('ft_' + k);
      if (v) out['ft_' + k] = v;
    });
    var fv = getCookie('first_visit');
    if (fv) out.first_visit = fv;
    var lp = getCookie('landing_page');
    if (lp) out.landing_page = lp;
    return out;
  }

  // ---------- VARIANT / NORM detection ----------
  function detectVariant() {
    var b = document.body;
    if (b && b.dataset && b.dataset.variant) return b.dataset.variant;
    // fallback: detect from URL path (financeiro-variant-a → "a")
    var m = location.pathname.match(/variant-([a-z])/i);
    return m ? m[1].toLowerCase() : 'a';
  }
  function detectNormSlug() {
    var parts = location.pathname.split('/').filter(Boolean);
    return parts[0] || 'home';
  }

  // ---------- GEO IP (cache em sessionStorage) ----------
  function loadGeo() {
    var cached = ssGet('__pbqph_geo');
    if (cached) {
      try {
        window.__pbqphGeo = JSON.parse(cached);
        push(Object.assign({ event: 'geo_loaded' }, window.__pbqphGeo));
        return;
      } catch (e) {}
    }
    if (!cfg.geoEndpoint) return;
    fetch(cfg.geoEndpoint, { cache: 'no-store' })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (j) {
        if (!j) return;
        var geo = {
          geo_country: j.country_code || '',
          geo_country_name: j.country_name || '',
          geo_state: j.region_code || '',
          geo_state_name: j.region || '',
          geo_city: j.city || '',
          geo_zip: j.postal || '',
          geo_ip: j.ip || ''
        };
        window.__pbqphGeo = geo;
        ssSet('__pbqph_geo', JSON.stringify(geo));
        push(Object.assign({ event: 'geo_loaded' }, geo));
      })
      .catch(function () {});
  }

  // ---------- PAGEVIEW ENRIQUECIDO ----------
  function pushPageView() {
    var payload = Object.assign(
      {
        event: 'custom_page_view',
        event_id: newEventId(),
        session_id: getOrCreateSession(),
        variant: detectVariant(),
        norm_slug: detectNormSlug(),
        page_path: location.pathname,
        page_url: location.href,
        page_title: document.title,
        referrer: document.referrer,
        ts: Date.now()
      },
      readFirstTouch(),
      getUrlParams()
    );
    push(payload);
  }

  // ---------- SCROLL DEPTH ----------
  function initScrollDepth() {
    var marks = [25, 50, 75, 90];
    var fired = {};
    function onScroll() {
      var st = window.pageYOffset || document.documentElement.scrollTop;
      var dh = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight) - window.innerHeight;
      if (dh <= 0) return;
      var pct = Math.round((st / dh) * 100);
      marks.forEach(function (m) {
        if (!fired[m] && pct >= m) {
          fired[m] = true;
          push({ event: 'scroll_depth', percent: m, session_id: getOrCreateSession() });
        }
      });
    }
    var t;
    window.addEventListener('scroll', function () {
      clearTimeout(t); t = setTimeout(onScroll, 80);
    }, { passive: true });
  }

  // ---------- TIME ON PAGE ----------
  function initTimeOnPage() {
    var ticks = [30, 60, 120, 180, 300, 600];
    var fired = {};
    var start = Date.now();
    setInterval(function () {
      var sec = Math.round((Date.now() - start) / 1000);
      ticks.forEach(function (t) {
        if (!fired[t] && sec >= t) {
          fired[t] = true;
          push({ event: 'time_on_page', seconds: t, session_id: getOrCreateSession() });
        }
      });
    }, 5000);
    window.__pbqphStartTime = start;
  }

  // ---------- FAQ TRACKING (auto: <details> ou clique em [data-faq-q]) ----------
  function initFaqTracking() {
    document.addEventListener('toggle', function (e) {
      var el = e.target;
      if (el && el.tagName === 'DETAILS') {
        if (el.open) {
          push({
            event: 'faq_open',
            question: (el.querySelector('summary') || {}).innerText || '',
            session_id: getOrCreateSession()
          });
        }
      }
    }, true);
  }

  // ---------- CHAT CTA HELPER ----------
  // URL do chat carrega APENAS UTMs + click IDs.
  // Prioridade: last-touch (URL atual) → fallback first-touch (cookie ft_*).
  // Variant, session, etc. continuam no dataLayer (uso interno GTM/GA4) — não vão na URL.
  function buildChatUrl(extra) {
    var u = new URL(cfg.chatUrl);
    var urlParams = new URLSearchParams(location.search);
    TRACKED_PARAMS.forEach(function (k) {
      var val = urlParams.get(k) || getCookie('ft_' + k);
      if (val) u.searchParams.set(k, val);
    });
    if (extra && typeof extra === 'object') {
      Object.keys(extra).forEach(function (k) { u.searchParams.set(k, extra[k]); });
    }
    return u.toString();
  }
  function goChat(opts) {
    opts = opts || {};
    var url = buildChatUrl(opts.params);
    var origin = opts.origin || 'cta';
    push({
      event: 'chat_abriu',
      event_id: newEventId(),
      session_id: getOrCreateSession(),
      variant: detectVariant(),
      norm_slug: detectNormSlug(),
      origin: origin,
      destination: url,
      ts: Date.now()
    });
    // sendBeacon não bloqueia navegação; o push acima já é síncrono
    // pequeno delay garante o pixel client-side se atrelado a tag
    setTimeout(function () {
      if (opts.target === '_blank') {
        window.open(url, '_blank', 'noopener');
      } else {
        location.href = url;
      }
    }, 60);
  }
  function bindChatLinks() {
    var els = document.querySelectorAll('[data-cta="olivia"], [data-cta="chat"], a[href*="demonstracao.orbitgestao.com.br/chat"]');
    Array.prototype.forEach.call(els, function (el) {
      el.addEventListener('click', function (e) {
        if (el.tagName === 'A' && (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1)) return; // open in new tab natural
        e.preventDefault();
        goChat({ origin: el.getAttribute('data-cta-origin') || 'cta', target: el.target });
      });
    });
  }

  // ---------- VIDEO (auto-track <video[data-track]>) ----------
  function initVideoTracking() {
    var vids = document.querySelectorAll('video[data-track]');
    Array.prototype.forEach.call(vids, function (v) {
      var fired60 = false, fired30 = false;
      v.addEventListener('play', function () {
        push({ event: 'video_play', session_id: getOrCreateSession() });
      });
      v.addEventListener('timeupdate', function () {
        if (!fired30 && v.currentTime >= 30) {
          fired30 = true;
          push({ event: 'video_demo_30s', session_id: getOrCreateSession() });
        }
        if (!fired60 && v.currentTime >= 60) {
          fired60 = true;
          push({ event: 'video_demo_60s', session_id: getOrCreateSession() });
        }
      });
      v.addEventListener('ended', function () {
        push({ event: 'video_complete', session_id: getOrCreateSession() });
      });
    });
  }

  // ---------- SUBMIT LEAD (chamado pelo form.js) ----------
  // Posta no webhook com payload completo (form + ft + lt + geo + contexto)
  function submitLead(formData, opts) {
    opts = opts || {};
    var eventId = newEventId();
    var ft = readFirstTouch();
    var lt = getUrlParams();
    var geo = window.__pbqphGeo || {};
    var session = getOrCreateSession();
    var timeOn = Math.round((Date.now() - (window.__pbqphStartTime || Date.now())) / 1000);

    var payload = Object.assign(
      {
        event: 'form_submit_success',
        event_id: eventId,
        source: opts.source || 'inline',
        variant: detectVariant(),
        norm_slug: detectNormSlug(),
        ts: Date.now(),
        time_on_page_at_submit: timeOn,
        session_id: session,
        referrer: document.referrer,
        page_url: location.href,
        user_agent: navigator.userAgent
      },
      formData || {},
      ft,
      lt,
      geo
    );

    if (!cfg.webhookUrl) {
      // demo mode
      push(Object.assign({}, payload, { simulated: true }));
      // cookie de email/nome pra remarketing
      if (formData && formData.email) setCookie('cookie_em', formData.email, cfg.cookieDays);
      if (formData && formData.nome) setCookie('cookie_nm', formData.nome, cfg.cookieDays);
      // snapshot pra thank-you
      ssSet('__pbqph_lastlead', JSON.stringify(payload));
      return Promise.resolve({ ok: true, simulated: true });
    }

    return fetch(cfg.webhookUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
      keepalive: true
    })
      .then(function (r) {
        if (!r.ok) throw new Error('webhook ' + r.status);
        push(payload); // só dispara form_submit_success quando webhook = 200
        if (formData && formData.email) setCookie('cookie_em', formData.email, cfg.cookieDays);
        if (formData && formData.nome) setCookie('cookie_nm', formData.nome, cfg.cookieDays);
        ssSet('__pbqph_lastlead', JSON.stringify(payload));
        // Microsoft Clarity (se presente): identifica o lead com o email
        if (window.clarity && formData && formData.email) {
          try { window.clarity('identify', formData.email); } catch (e) {}
        }
        return { ok: true, event_id: eventId };
      })
      .catch(function (err) {
        if (cfg.debug) console.warn('[orbit] webhook fail', err);
        push({ event: 'form_submit_error', error: String(err), session_id: session });
        return { ok: false, error: err };
      });
  }

  // ---------- API PÚBLICA ----------
  window.__orbit = window.__orbit || {};
  window.__orbit.goChat = goChat;
  window.__orbit.buildChatUrl = buildChatUrl;
  window.__orbit.config = cfg;
  window.__pbqph.submitLead = submitLead;
  window.__pbqph.readFirstTouch = readFirstTouch;
  window.__pbqph.getUrlParams = getUrlParams;
  window.__pbqph.session = getOrCreateSession;

  // ---------- INIT ----------
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }
  ready(function () {
    captureFirstTouch();
    pushPageView();
    loadGeo();
    initScrollDepth();
    initTimeOnPage();
    initFaqTracking();
    initVideoTracking();
    bindChatLinks();
    if (cfg.debug) console.log('[orbit] analytics ready', { variant: detectVariant(), session: getOrCreateSession() });
  });
})();
