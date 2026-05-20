/* ============================================================
   Orbit · form.js
   Renderização e validação de form de captura de lead
   Spec: TRACKING.md
   ------------------------------------------------------------
   - Renderiza em qualquer <div data-form="lead">
   - Atualiza window.__pbqphFormData a cada digitação
   - Máscara WhatsApp BR
   - Validação inline (email + whatsapp obrigatórios)
   - Submit → window.__pbqph.submitLead() → webhook → form_submit_success
   ============================================================ */

(function () {
  'use strict';

  // CSS mínimo — herda os tokens da LP. Pode ser overridado.
  var BASE_CSS = '\
.orbit-form{display:flex;flex-direction:column;gap:12px;width:100%}\
.orbit-form__row{display:grid;grid-template-columns:1fr 1fr;gap:10px}\
@media(max-width:560px){.orbit-form__row{grid-template-columns:1fr}}\
.orbit-form__field{display:flex;flex-direction:column;gap:4px}\
.orbit-form__label{font-family:inherit;font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:rgba(0,0,0,.6)}\
.orbit-form[data-theme="dark"] .orbit-form__label{color:rgba(255,255,255,.55)}\
.orbit-form__input,.orbit-form__select{font:inherit;width:100%;padding:12px 14px;border-radius:12px;border:1px solid rgba(0,0,0,.12);background:#fff;color:#18191B;font-size:14px;font-weight:500;outline:none;transition:border-color .2s,box-shadow .2s}\
.orbit-form[data-theme="dark"] .orbit-form__input,.orbit-form[data-theme="dark"] .orbit-form__select{background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);color:#fff}\
.orbit-form__input:focus,.orbit-form__select:focus{border-color:#ffba1a;box-shadow:0 0 0 3px rgba(255,186,26,.18)}\
.orbit-form__input::placeholder{color:rgba(0,0,0,.35)}\
.orbit-form[data-theme="dark"] .orbit-form__input::placeholder{color:rgba(255,255,255,.35)}\
.orbit-form__input.--invalid{border-color:#F85149;box-shadow:0 0 0 3px rgba(248,81,73,.15)}\
.orbit-form__hint{font-size:11px;color:#F85149;font-weight:600;min-height:14px}\
.orbit-form__submit{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:14px 22px;border-radius:9999px;border:0;cursor:pointer;background:#ffba1a;color:#0D1117;font:inherit;font-weight:800;font-size:15px;letter-spacing:-.01em;transition:transform .2s,box-shadow .2s,background .2s;margin-top:6px}\
.orbit-form__submit:hover{transform:translateY(-1px);box-shadow:0 12px 24px -8px rgba(255,186,26,.5)}\
.orbit-form__submit:disabled{opacity:.5;cursor:wait;transform:none}\
.orbit-form__micro{font-size:11px;color:rgba(0,0,0,.45);text-align:center;line-height:1.5}\
.orbit-form[data-theme="dark"] .orbit-form__micro{color:rgba(255,255,255,.45)}\
.orbit-form__ok{padding:18px 16px;border-radius:14px;background:rgba(63,185,80,.10);border:1px solid rgba(63,185,80,.30);color:#1f7c2f;display:flex;flex-direction:column;gap:6px}\
.orbit-form[data-theme="dark"] .orbit-form__ok{background:rgba(63,185,80,.10);border-color:rgba(63,185,80,.30);color:#3FB950}\
.orbit-form__ok strong{font-size:15px;font-weight:800}\
.orbit-form__ok span{font-size:13px;font-weight:500;opacity:.85}';

  function injectStyle() {
    if (document.getElementById('orbit-form-style')) return;
    var s = document.createElement('style');
    s.id = 'orbit-form-style';
    s.textContent = BASE_CSS;
    document.head.appendChild(s);
  }

  function maskWhatsapp(v) {
    v = (v || '').replace(/\D/g, '').slice(0, 11);
    if (v.length === 0) return '';
    if (v.length <= 2) return '(' + v;
    if (v.length <= 7) return '(' + v.slice(0, 2) + ') ' + v.slice(2);
    return '(' + v.slice(0, 2) + ') ' + v.slice(2, 7) + '-' + v.slice(7);
  }

  function isValidEmail(e) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e || '');
  }
  function isValidWhatsapp(v) {
    var d = (v || '').replace(/\D/g, '');
    return d.length === 10 || d.length === 11;
  }

  function renderForm(container) {
    var submitLabel = container.getAttribute('data-submit-label') || 'Falar com a Olívia';
    var empresaLabel = container.getAttribute('data-empresa-label') || 'Empresa';
    var theme = container.getAttribute('data-theme') || 'light';
    var formId = container.getAttribute('data-form-id') || 'waitlist-form';
    var microcopy = container.getAttribute('data-microcopy') || 'Sem cadastro complicado. Sem cartão. Você decide se quer agendar.';

    container.innerHTML = '' +
      '<form class="orbit-form" id="' + formId + '" data-theme="' + theme + '" novalidate>' +
      '<div class="orbit-form__row">' +
        '<div class="orbit-form__field">' +
          '<label class="orbit-form__label" for="' + formId + '-nome">Nome</label>' +
          '<input class="orbit-form__input" id="' + formId + '-nome" name="nome" placeholder="Seu primeiro nome" autocomplete="given-name" />' +
          '<span class="orbit-form__hint" data-hint="nome"></span>' +
        '</div>' +
        '<div class="orbit-form__field">' +
          '<label class="orbit-form__label" for="' + formId + '-sobrenome">Sobrenome</label>' +
          '<input class="orbit-form__input" id="' + formId + '-sobrenome" name="sobrenome" placeholder="Seu sobrenome" autocomplete="family-name" />' +
        '</div>' +
      '</div>' +
      '<div class="orbit-form__row">' +
        '<div class="orbit-form__field">' +
          '<label class="orbit-form__label" for="' + formId + '-email">E-mail corporativo</label>' +
          '<input class="orbit-form__input" id="' + formId + '-email" name="email" type="email" placeholder="voce@empresa.com.br" autocomplete="email" />' +
          '<span class="orbit-form__hint" data-hint="email"></span>' +
        '</div>' +
        '<div class="orbit-form__field">' +
          '<label class="orbit-form__label" for="' + formId + '-whatsapp">WhatsApp</label>' +
          '<input class="orbit-form__input" id="' + formId + '-whatsapp" name="whatsapp" inputmode="tel" placeholder="(11) 99999-9999" autocomplete="tel" />' +
          '<span class="orbit-form__hint" data-hint="whatsapp"></span>' +
        '</div>' +
      '</div>' +
      '<div class="orbit-form__field">' +
        '<label class="orbit-form__label" for="' + formId + '-empresa">' + empresaLabel + '</label>' +
        '<input class="orbit-form__input" id="' + formId + '-empresa" name="empresa" placeholder="Nome da empresa" autocomplete="organization" />' +
      '</div>' +
      '<div class="orbit-form__row">' +
        '<div class="orbit-form__field">' +
          '<label class="orbit-form__label" for="' + formId + '-funcionarios">Nº de funcionários</label>' +
          '<select class="orbit-form__select" id="' + formId + '-funcionarios" name="funcionarios">' +
            '<option value="">Selecione</option>' +
            '<option value="ate_10">Até 10</option>' +
            '<option value="11_30">11 – 30</option>' +
            '<option value="31_100">31 – 100</option>' +
            '<option value="101_300">101 – 300</option>' +
            '<option value="301_1000">301 – 1.000</option>' +
            '<option value="1000_mais">Mais de 1.000</option>' +
          '</select>' +
        '</div>' +
        '<div class="orbit-form__field">' +
          '<label class="orbit-form__label" for="' + formId + '-faturamento">Faturamento mensal</label>' +
          '<select class="orbit-form__select" id="' + formId + '-faturamento" name="faturamento">' +
            '<option value="">Selecione</option>' +
            '<option value="ate_100k">Até R$ 100k</option>' +
            '<option value="100_500k">R$ 100k – R$ 500k</option>' +
            '<option value="500k_1mi">R$ 500k – R$ 1mi</option>' +
            '<option value="1_5mi">R$ 1mi – R$ 5mi</option>' +
            '<option value="5mi_mais">Mais de R$ 5mi</option>' +
          '</select>' +
        '</div>' +
      '</div>' +
      '<button type="submit" class="orbit-form__submit">' + submitLabel +
        ' <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>' +
      '</button>' +
      '<p class="orbit-form__micro">' + microcopy + '</p>' +
      '</form>';

    return container.querySelector('form');
  }

  function syncGlobalFormData(form) {
    var fd = new FormData(form);
    var data = {};
    fd.forEach(function (v, k) { data[k] = v; });
    // aliases conforme TRACKING.md
    data.name = (data.nome || '') + (data.sobrenome ? ' ' + data.sobrenome : '');
    data.firstname = data.nome || '';
    data.lastname = data.sobrenome || '';
    data.phone = (data.whatsapp || '').replace(/\D/g, '');
    data.phoneNumber = data.phone;
    data.telefone = data.whatsapp || '';
    window.__pbqphFormData = data;
  }

  function bindForm(form, container) {
    var wa = form.querySelector('input[name="whatsapp"]');
    var email = form.querySelector('input[name="email"]');
    var submit = form.querySelector('button[type="submit"]');

    form.addEventListener('input', function () { syncGlobalFormData(form); });
    form.addEventListener('change', function () { syncGlobalFormData(form); });
    syncGlobalFormData(form);

    wa.addEventListener('input', function (e) {
      var pos = e.target.selectionStart;
      e.target.value = maskWhatsapp(e.target.value);
      try { e.target.setSelectionRange(pos + 1, pos + 1); } catch (err) {}
    });

    function setHint(name, msg) {
      var input = form.querySelector('[name="' + name + '"]');
      var hint = form.querySelector('[data-hint="' + name + '"]');
      if (input) input.classList.toggle('--invalid', !!msg);
      if (hint) hint.textContent = msg || '';
    }

    function validate() {
      var ok = true;
      setHint('email', ''); setHint('whatsapp', ''); setHint('nome', '');
      if (!form.nome.value.trim()) { setHint('nome', 'Como podemos te chamar?'); ok = false; }
      if (!isValidEmail(email.value)) { setHint('email', 'Confere o e-mail.'); ok = false; }
      if (!isValidWhatsapp(wa.value)) { setHint('whatsapp', 'WhatsApp com DDD.'); ok = false; }
      return ok;
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validate()) return;
      submit.disabled = true;
      submit.dataset.original = submit.dataset.original || submit.innerHTML;
      submit.innerHTML = 'Enviando…';

      var data = Object.assign({}, window.__pbqphFormData);
      if (!window.__pbqph || !window.__pbqph.submitLead) {
        console.warn('[orbit:form] __pbqph.submitLead não disponível — analytics.js não carregou?');
        submit.disabled = false;
        submit.innerHTML = submit.dataset.original;
        return;
      }

      window.__pbqph.submitLead(data, { source: container.getAttribute('data-source') || 'inline' })
        .then(function (res) {
          if (res && res.ok) {
            // sucesso
            container.innerHTML =
              '<div class="orbit-form__ok">' +
              '<strong>Recebemos seu contato' + (data.firstname ? ', ' + data.firstname : '') + '! ✦</strong>' +
              '<span>Olívia vai te chamar no WhatsApp em até 1 minuto. Se preferir, abra o chat agora.</span>' +
              '</div>';
            // opcional: redirect pra thank-you se page declarar
            var thanks = container.getAttribute('data-thanks');
            if (thanks) setTimeout(function () { location.href = thanks; }, 1200);
            // event lead_thanks_view
            window.dataLayer && window.dataLayer.push({ event: 'lead_thanks_view', session_id: (window.__pbqph && window.__pbqph.session && window.__pbqph.session()) || '' });
          } else {
            submit.disabled = false;
            submit.innerHTML = submit.dataset.original;
            setHint('email', 'Algo deu errado. Tente outra vez ou fale com a Olívia direto.');
          }
        });
    });
  }

  function init() {
    injectStyle();
    var containers = document.querySelectorAll('[data-form="lead"]');
    Array.prototype.forEach.call(containers, function (c) {
      var form = renderForm(c);
      bindForm(form, c);
    });
  }

  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
})();
