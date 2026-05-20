# gap mkt orbit

Landing pages, design system e tracking da **Orbit Gestão** — para a campanha do novo ICP B2B (R$ 500k+/mês · 30+ funcionários) e funil paralelo Canal Orbit.

Deploy: **Cloudflare Pages** (estático, sem build step).

---

## Estrutura

```
.
├── public/                       ← raiz de deploy do Cloudflare Pages
│   ├── financeiro/
│   │   ├── design-system.html    ← DS do produto Financeiro (Olívia)
│   │   └── index.html            (LP — em construção)
│   ├── shared/
│   │   └── js/                   (analytics.js + form.js — ver TRACKING.md)
│   └── _headers                  (CSP / cache control)
│
├── analise + sobre/              ← briefings, PDFs, Clarity, Google Ads CSVs
├── referencias templates sites / ← templates visuais de referência (finex, futureui)
├── fotos orbit/                  ← logos e ativos visuais
├── olivia nossa coordenadora /   ← componente Olívia + agentes (Orbital Hub)
│
├── Extract HTML Design System.md ← instruções para gerar design-system.html
├── Orbit_Playbook_Estrategico.docx
├── Orbit_Deck_Executivo.pptx
├── Orbit_Workbook_Operacional_GoogleAds.xlsx
├── Orbit_Copy_LPs.docx
├── TRACKING.md                   ← sistema de tracking portável
├── CLAUDE.md                     ← contexto para sessões de Claude Code
└── .claude/                      ← settings do Claude Code
```

## Identidade visual

Tokens em `analise + sobre/idntidade visual orbit.pdf`. Resumo:

| Token | Hex | Uso |
|---|---|---|
| `--primary` | `#ffba1a` | Dourado Orbit — CTA, destaques |
| `--primary-dark` | `#e6a200` | Hover do dourado |
| `--primary-light` | `#ffca4a` | Variação clara |
| `--black` | `#0D1117` | Background principal (tema escuro default) |
| `--black-soft` | `#161B22` | Background de seções |
| `--black-card` | `#1C2333` | Cards, inputs |
| `--success` | `#3FB950` | Verde de confirmação |
| `--error` | `#F85149` | Vermelho de erro |

Fonte única: **Plus Jakarta Sans** (Google Fonts, weights 400 · 500 · 600 · 700 · 800).
Ícones: **Lucide** (SVG inline) + **Font Awesome 6** (Orbit-branded).

## Design System por produto

Cada produto da Orbit (Financeiro, CRM, Estratégico, Indicadores, Processos, Pessoas, Projetos, Canal Orbit) tem seu próprio `design-system.html` em `public/<produto>/` documentando o vocabulário visual reutilizável na LP.

A referência visual por produto fica em `referencias templates sites /referencias para <produto>/`.

| Produto | Referência visual |
|---|---|
| Financeiro | finex-finance-saas.aura.build |
| Demais | futureui.aura.build |

## Tracking

Sistema portável documentado em `TRACKING.md`: `analytics.js` + `form.js`, dataLayer com 8 eventos, first/last-touch, geo, webhook único, dedupe `event_id` pixel ↔ CAPI.

## Deploy

Cloudflare Pages com pasta de saída `public/`. Sem build step — HTML estático com Tailwind via CDN no design system e CSS dedicado nas LPs finais.

```bash
# preview local rápido
npx http-server public -p 4173
```
