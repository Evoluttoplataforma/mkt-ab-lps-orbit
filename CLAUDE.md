# CLAUDE.md

Contexto persistente para sessões do Claude Code neste repositório.

## O que é este projeto

Estratégia de marketing + Google Ads + landing pages da **Orbit Gestão** — SaaS BR all-in-one (BPMS + IA) com 20 módulos, 3.045+ clientes e Olívia como agente IA central.

A ação atual: rodar a Fase 1 do playbook (R$ 15k/mês Google Ads, 7 módulos prioritários) e construir LPs por produto antes de subir as campanhas.

## ICP (corte HARD, não negociável)

- **B2B (funil principal)**: empresas R$ 500k+/mês E 30+ funcionários.
- **Canal Orbit (funil paralelo)**: consultorias R$ 100k+/mês — plataforma white-label.

Detalhes de decisor, dor e mensagem por módulo em `Orbit_Playbook_Estrategico.docx`.

## Documentos-fonte (não alterar sem aprovar com Rodrigo)

| Arquivo | Conteúdo |
|---|---|
| `Orbit_Playbook_Estrategico.docx` | Estratégia completa (diagnóstico, 7 módulos, plano operacional, roadmap 90 dias) |
| `Orbit_Workbook_Operacional_GoogleAds.xlsx` | 11 abas operacionais: plano de mídia, 35 ad groups, 190 keywords, 194 negativadas, 9 RSAs, etc. |
| `Orbit_Deck_Executivo.pptx` | Deck consolidado para diretoria |
| `Orbit_Copy_LPs.docx` | Copy completa das 8 LPs (7 módulos B2B + Canal Orbit) |
| `TRACKING.md` | Sistema de tracking portável (analytics.js + form.js) |
| `Extract HTML Design System.md` | Instruções para gerar `design-system.html` por produto |
| `analise + sobre/idntidade visual orbit.pdf` | Tokens visuais (cores, tipografia, espaçamento) |

## Convenções de design

- **Tema**: escuro default (`#0D1117`), claro disponível para seções "light".
- **Cor de marca**: dourado `#ffba1a` (CTA, destaques). Variantes: dark `#e6a200`, light `#ffca4a`.
- **Tipografia**: Plus Jakarta Sans (400–800), Google Fonts.
- **Ícones**: Lucide (SVG inline) + Font Awesome 6 quando precisar de variedade vetorial.
- **Layout**: max-w-7xl, padding 6, gap responsivo, bordas `rgba(255,255,255,0.10)`.

## Convenções de pasta

- `public/` = root de deploy Cloudflare Pages.
- `public/<produto>/design-system.html` = vocabulário visual reutilizável do produto.
- `public/<produto>/index.html` = LP final (a construir).
- `public/shared/js/` = `analytics.js`, `form.js` (ver `TRACKING.md`).

Referência visual por produto: `referencias templates sites /referencias para <produto>/`.

## Convenções de campanha Google Ads

Nomenclatura: `ORB-[FUNIL]-[TIPO]-[MÓDULO]`. Ex: `ORB-B2B-Search-Financeiro`.

5 eventos de conversão (GA4 + Google Ads):

| Nível | Evento | Valor |
|---|---|---|
| Macro 1 | `demo_agendada` | R$ 800 — PRIMÁRIA |
| Macro 2 | `chat_qualificou_pci` | R$ 500 — PRIMÁRIA secundária |
| Micro 3 | `form_lead_enviado` | R$ 300 |
| Micro 4 | `chat_abriu` | R$ 100 |
| Micro 5 | `video_demo_60s` | R$ 100 |

## Princípios de execução

- **Não alterar** os documentos-fonte (DOCX/PPTX/XLSX/PDF) — só consultar e extrair.
- **Não apagar** pastas existentes sem aviso explícito do Rodrigo.
- **Cloudflare Pages**: zero build step — HTML estático autossuficiente (Tailwind via CDN no DS; LPs finais podem ter CSS dedicado depois).
- **Antes de subir campanha**: LPs por módulo + 5 eventos no GA4 + lista de negativadas + Customer Match.
