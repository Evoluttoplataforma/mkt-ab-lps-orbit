"""
Hero mockups específicos por módulo.
Cada módulo tem layout LIVRE (não preso ao sidebar+stats+chart do Financeiro).
- LP A (dark theme · Tailwind CDN)
- LP B (light theme · vanilla CSS com vars --gold-mid/--text/--surface/--border)

Wrapper externo padronizado (mantém unidade visual da marca):
  <div class="hidden md:flex ... h-[720px] max-w-[1440px]">
    <div class="... rounded-2xl ... shadow-2xl">
      [CONTEÚDO LIVRE POR MÓDULO]
    </div>
  </div>
"""

# ─────────────────────────────────────────────────────────────────
# CRM · Kanban board · 4 colunas com cards de leads
# ─────────────────────────────────────────────────────────────────

CRM_A = '''
  <!-- HERO MOCKUP DESKTOP · Kanban CRM -->
  <div class="hidden md:flex scroll-item scroll-blur-in d-500 w-full h-[720px] max-w-[1440px] mt-20 mr-auto ml-auto relative items-center justify-center" data-swap="screenshot-painel">
    <div class="flex flex-col overflow-hidden z-30 bg-[#0A0A0C] w-full h-full max-w-6xl border-white/10 border ring-white/5 ring-1 rounded-2xl mr-2 ml-2 md:mr-6 md:ml-6 relative shadow-2xl text-gray-400 select-none">
      <!-- Topbar -->
      <header class="h-14 border-b border-white/5 flex items-center justify-between px-6 shrink-0">
        <div class="flex items-center gap-3">
          <div class="w-7 h-7 rounded-full bg-gradient-to-br from-primary to-primary-600 flex items-center justify-center text-orbit-black font-extrabold text-[11px]">OR</div>
          <span class="text-white font-bold text-sm tracking-tight">Orbit</span>
          <span class="text-primary font-bold text-xs uppercase tracking-wider">CRM</span>
        </div>
        <div class="flex items-center gap-3">
          <div class="flex items-center gap-1.5 bg-success/10 border border-success/30 rounded-full px-2.5 py-1">
            <div class="w-1.5 h-1.5 rounded-full bg-success animate-pulse"></div>
            <span class="text-[11px] font-medium text-success">12 leads novos hoje</span>
          </div>
          <button class="bg-primary text-orbit-black px-3 py-1.5 rounded-lg text-[11px] font-bold flex items-center gap-1.5">+ Novo lead</button>
        </div>
      </header>
      <!-- Kanban -->
      <div class="flex-1 flex overflow-x-auto px-6 py-5 gap-4">
        <!-- Coluna 1 · Novo Lead -->
        <div class="flex-shrink-0 w-64 flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-[11px] uppercase tracking-wider text-gray-500 font-bold">Novo Lead</span>
            <span class="text-[10px] font-bold bg-white/5 rounded px-1.5 py-0.5">8</span>
          </div>
          <div class="space-y-2">
            <div class="bg-[#0E0E11] border border-white/10 rounded-xl p-3 hover:border-primary/40 transition-colors">
              <p class="text-[12px] font-bold text-white mb-1">Confiteria Andrade</p>
              <p class="text-[10px] text-gray-500 mb-2">CNPJ · R$ 880k/mês</p>
              <div class="flex items-center justify-between"><span class="text-[10px] font-bold text-success">R$ 24K</span><span class="text-[9px] bg-white/5 rounded px-1.5 py-0.5">há 2h</span></div>
            </div>
            <div class="bg-[#0E0E11] border border-white/10 rounded-xl p-3 hover:border-primary/40 transition-colors">
              <p class="text-[12px] font-bold text-white mb-1">Veridian Tech</p>
              <p class="text-[10px] text-gray-500 mb-2">SaaS · R$ 1,2M/mês</p>
              <div class="flex items-center justify-between"><span class="text-[10px] font-bold text-success">R$ 48K</span><span class="text-[9px] bg-white/5 rounded px-1.5 py-0.5">há 5h</span></div>
            </div>
            <div class="bg-[#0E0E11] border border-white/10 rounded-xl p-3">
              <p class="text-[12px] font-bold text-white/60 mb-1">Lumina Indústria</p>
              <p class="text-[10px] text-gray-600">+5 cards…</p>
            </div>
          </div>
        </div>
        <!-- Coluna 2 · Qualificação -->
        <div class="flex-shrink-0 w-64 flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-[11px] uppercase tracking-wider text-gray-500 font-bold">Qualificação</span>
            <span class="text-[10px] font-bold bg-white/5 rounded px-1.5 py-0.5">5</span>
          </div>
          <div class="space-y-2">
            <div class="bg-[#0E0E11] border border-primary/30 rounded-xl p-3 ring-1 ring-primary/20">
              <div class="flex items-center gap-1.5 mb-1"><span class="text-[9px] bg-primary/20 text-primary rounded px-1.5 py-0.5 font-bold uppercase">SCORE 87</span></div>
              <p class="text-[12px] font-bold text-white mb-1">ACME Corp</p>
              <p class="text-[10px] text-gray-500 mb-2">Logística · R$ 3,4M/mês</p>
              <div class="flex items-center justify-between"><span class="text-[10px] font-bold text-primary">R$ 180K</span><span class="text-[9px] bg-primary/15 text-primary rounded px-1.5 py-0.5">em 2 dias</span></div>
            </div>
            <div class="bg-[#0E0E11] border border-white/10 rounded-xl p-3">
              <p class="text-[12px] font-bold text-white mb-1">Constru Forte</p>
              <p class="text-[10px] text-gray-500">Obra · R$ 2M/mês</p>
            </div>
          </div>
        </div>
        <!-- Coluna 3 · Proposta -->
        <div class="flex-shrink-0 w-64 flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-[11px] uppercase tracking-wider text-gray-500 font-bold">Proposta enviada</span>
            <span class="text-[10px] font-bold bg-white/5 rounded px-1.5 py-0.5">3</span>
          </div>
          <div class="space-y-2">
            <div class="bg-gradient-to-br from-primary/15 to-transparent border border-primary/40 rounded-xl p-3">
              <div class="flex items-center gap-1.5 mb-1.5"><span class="text-[9px] bg-success/20 text-success rounded px-1.5 py-0.5 font-bold uppercase">⚡ 76% fechar</span></div>
              <p class="text-[12px] font-bold text-white mb-1">Page Sistemas</p>
              <p class="text-[10px] text-gray-500 mb-2">Split pagamento</p>
              <div class="flex items-center justify-between"><span class="text-[11px] font-extrabold text-primary">R$ 612K</span><span class="text-[9px] text-success font-bold">5° contato</span></div>
            </div>
            <div class="bg-[#0E0E11] border border-white/10 rounded-xl p-3">
              <p class="text-[12px] font-bold text-white mb-1">Grupo Carla Séd</p>
              <p class="text-[10px] text-gray-500">Dermato · 40 colab</p>
            </div>
          </div>
        </div>
        <!-- Coluna 4 · Negociação -->
        <div class="flex-shrink-0 w-64 flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-[11px] uppercase tracking-wider text-gray-500 font-bold">Negociação</span>
            <span class="text-[10px] font-bold bg-primary/15 text-primary rounded px-1.5 py-0.5">2</span>
          </div>
          <div class="space-y-2">
            <div class="bg-[#0E0E11] border border-white/10 rounded-xl p-3">
              <p class="text-[12px] font-bold text-white mb-1">F12 Publicidade</p>
              <p class="text-[10px] text-gray-500 mb-2">Agência · BR todo</p>
              <div class="flex items-center justify-between"><span class="text-[10px] font-bold text-primary">R$ 96K</span></div>
            </div>
          </div>
        </div>
      </div>
      <!-- Footer · Olívia floating -->
      <div class="absolute bottom-5 right-5 bg-[#0A0A0C] border border-primary/30 rounded-2xl p-3 max-w-xs shadow-2xl ring-1 ring-primary/15">
        <div class="flex items-start gap-2.5">
          <div class="w-8 h-8 rounded-full bg-gradient-to-br from-primary to-primary-600 flex items-center justify-center text-orbit-black font-extrabold text-[11px] shrink-0">OL</div>
          <div class="flex-1">
            <p class="text-[11px] font-bold text-white">Olívia · IA comercial</p>
            <p class="text-[10px] text-gray-400 mt-1 leading-snug">Mova ACME pra Proposta — score 87 e 5° contato indica timing.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
'''

# ─────────────────────────────────────────────────────────────────
# INDICADORES · Grid 3×2 de KPI cards com sparklines diversas
# ─────────────────────────────────────────────────────────────────

INDICADORES_A = '''
  <!-- HERO MOCKUP DESKTOP · Grid de KPIs Orbit -->
  <div class="hidden md:flex scroll-item scroll-blur-in d-500 w-full h-[720px] max-w-[1440px] mt-20 mr-auto ml-auto relative items-center justify-center" data-swap="screenshot-painel">
    <div class="flex flex-col overflow-hidden z-30 bg-[#0A0A0C] w-full h-full max-w-6xl border-white/10 border ring-white/5 ring-1 rounded-2xl mr-2 ml-2 md:mr-6 md:ml-6 relative shadow-2xl text-gray-400 select-none">
      <!-- Topbar -->
      <header class="h-14 border-b border-white/5 flex items-center justify-between px-6 shrink-0">
        <div class="flex items-center gap-3">
          <div class="w-7 h-7 rounded-full bg-gradient-to-br from-primary to-primary-600 flex items-center justify-center text-orbit-black font-extrabold text-[11px]">OR</div>
          <span class="text-white font-bold text-sm tracking-tight">Orbit</span>
          <span class="text-primary font-bold text-xs uppercase tracking-wider">Indicadores</span>
        </div>
        <div class="flex items-center gap-3">
          <span class="text-[11px] text-gray-500">Atualizado há 2 min</span>
          <button class="bg-white/5 border border-white/10 text-white px-3 py-1.5 rounded-lg text-[11px] font-bold">+ Dashboard</button>
        </div>
      </header>
      <!-- Grid 3x2 -->
      <div class="flex-1 grid grid-cols-3 gap-4 p-6">
        <!-- KPI 1 · CPL · Sparkline area -->
        <div class="bg-[#0E0E11] border border-white/10 rounded-2xl p-4 flex flex-col">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] uppercase tracking-wider text-gray-500 font-bold">CPL</span>
            <span class="text-[9px] bg-success/15 text-success rounded px-1.5 py-0.5 font-bold">−18%</span>
          </div>
          <p class="text-2xl font-extrabold text-white mb-1">R$ 187</p>
          <p class="text-[10px] text-gray-500 mb-3">vs R$ 228 mês anterior</p>
          <svg class="w-full h-12" viewBox="0 0 120 40" preserveAspectRatio="none">
            <defs><linearGradient id="g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3FB950" stop-opacity="0.4"/><stop offset="100%" stop-color="#3FB950" stop-opacity="0"/></linearGradient></defs>
            <path d="M0,30 L20,28 L40,22 L60,18 L80,12 L100,15 L120,8 L120,40 L0,40 Z" fill="url(#g1)"/>
            <path d="M0,30 L20,28 L40,22 L60,18 L80,12 L100,15 L120,8" stroke="#3FB950" stroke-width="1.5" fill="none"/>
          </svg>
        </div>
        <!-- KPI 2 · Conversão · Donut -->
        <div class="bg-[#0E0E11] border border-white/10 rounded-2xl p-4 flex flex-col">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] uppercase tracking-wider text-gray-500 font-bold">Taxa Conversão</span>
            <span class="text-[9px] bg-success/15 text-success rounded px-1.5 py-0.5 font-bold">+2,4pp</span>
          </div>
          <div class="flex items-center gap-3 mt-2">
            <svg class="w-16 h-16" viewBox="0 0 36 36">
              <circle cx="18" cy="18" r="15" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="3"/>
              <circle cx="18" cy="18" r="15" fill="none" stroke="#ffba1a" stroke-width="3" stroke-dasharray="14.3 100" transform="rotate(-90 18 18)" stroke-linecap="round"/>
            </svg>
            <div>
              <p class="text-2xl font-extrabold text-white">14,3%</p>
              <p class="text-[10px] text-gray-500">meta · 12%</p>
            </div>
          </div>
        </div>
        <!-- KPI 3 · MRR · Sparkline line -->
        <div class="bg-gradient-to-br from-primary/15 to-transparent border border-primary/40 rounded-2xl p-4 flex flex-col ring-1 ring-primary/20">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] uppercase tracking-wider text-primary font-bold">MRR · destaque</span>
            <span class="text-[9px] bg-primary/30 text-primary rounded px-1.5 py-0.5 font-bold">+22%</span>
          </div>
          <p class="text-2xl font-extrabold text-white mb-1">R$ 4,2M</p>
          <p class="text-[10px] text-gray-400 mb-3">12 meses crescendo</p>
          <svg class="w-full h-12" viewBox="0 0 120 40" preserveAspectRatio="none">
            <path d="M0,35 L15,30 L30,28 L45,22 L60,20 L75,14 L90,10 L105,8 L120,4" stroke="#ffba1a" stroke-width="2" fill="none" stroke-linecap="round"/>
            <circle cx="120" cy="4" r="2.5" fill="#ffba1a"/>
          </svg>
        </div>
        <!-- KPI 4 · NPS · Barras -->
        <div class="bg-[#0E0E11] border border-white/10 rounded-2xl p-4 flex flex-col">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] uppercase tracking-wider text-gray-500 font-bold">NPS</span>
            <span class="text-[9px] bg-success/15 text-success rounded px-1.5 py-0.5 font-bold">Excelente</span>
          </div>
          <p class="text-2xl font-extrabold text-white mb-1">72</p>
          <p class="text-[10px] text-gray-500 mb-3">↑ de 64 em 90 dias</p>
          <div class="flex items-end gap-1 h-12">
            <div class="flex-1 bg-white/5 rounded-t" style="height:30%"></div>
            <div class="flex-1 bg-white/10 rounded-t" style="height:45%"></div>
            <div class="flex-1 bg-success/40 rounded-t" style="height:60%"></div>
            <div class="flex-1 bg-success/60 rounded-t" style="height:75%"></div>
            <div class="flex-1 bg-success rounded-t" style="height:95%"></div>
          </div>
        </div>
        <!-- KPI 5 · Churn · Sparkline desc -->
        <div class="bg-[#0E0E11] border border-white/10 rounded-2xl p-4 flex flex-col">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[10px] uppercase tracking-wider text-gray-500 font-bold">Churn mensal</span>
            <span class="text-[9px] bg-error/15 text-error rounded px-1.5 py-0.5 font-bold">⚠ acima</span>
          </div>
          <p class="text-2xl font-extrabold text-white mb-1">2,4%</p>
          <p class="text-[10px] text-error mb-3">meta · 1,8%</p>
          <svg class="w-full h-12" viewBox="0 0 120 40" preserveAspectRatio="none">
            <path d="M0,8 L20,10 L40,12 L60,18 L80,22 L100,28 L120,32" stroke="#F85149" stroke-width="2" fill="none" stroke-linecap="round"/>
          </svg>
        </div>
        <!-- KPI 6 · Olívia insight card -->
        <div class="bg-[#0E0E11] border border-primary/30 rounded-2xl p-4 flex flex-col">
          <div class="flex items-center gap-2 mb-3">
            <div class="w-7 h-7 rounded-full bg-gradient-to-br from-primary to-primary-600 flex items-center justify-center text-orbit-black font-extrabold text-[10px]">OL</div>
            <span class="text-[11px] font-bold text-white">Insight da Olívia</span>
          </div>
          <p class="text-[12px] text-gray-300 leading-relaxed">Churn subiu 3 meses seguidos. Clientes que cancelaram tiveram <strong class="text-primary">NPS &lt; 30</strong>. Sugiro PDI no CS.</p>
          <button class="mt-auto text-[10px] text-primary font-bold flex items-center gap-1">Criar tarefa →</button>
        </div>
      </div>
    </div>
  </div>
'''

# ─────────────────────────────────────────────────────────────────
# ESTRATÉGICO · Mapa BSC 4 quadrantes com objetivos linkados
# ─────────────────────────────────────────────────────────────────

ESTRATEGICO_A = '''
  <!-- HERO MOCKUP DESKTOP · BSC Map -->
  <div class="hidden md:flex scroll-item scroll-blur-in d-500 w-full h-[720px] max-w-[1440px] mt-20 mr-auto ml-auto relative items-center justify-center" data-swap="screenshot-painel">
    <div class="flex flex-col overflow-hidden z-30 bg-[#0A0A0C] w-full h-full max-w-6xl border-white/10 border ring-white/5 ring-1 rounded-2xl mr-2 ml-2 md:mr-6 md:ml-6 relative shadow-2xl text-gray-400 select-none">
      <header class="h-14 border-b border-white/5 flex items-center justify-between px-6 shrink-0">
        <div class="flex items-center gap-3">
          <div class="w-7 h-7 rounded-full bg-gradient-to-br from-primary to-primary-600 flex items-center justify-center text-orbit-black font-extrabold text-[11px]">OR</div>
          <span class="text-white font-bold text-sm tracking-tight">Orbit</span>
          <span class="text-primary font-bold text-xs uppercase tracking-wider">Estratégico</span>
        </div>
        <div class="flex items-center gap-3">
          <span class="text-[11px] text-gray-500">Mapa estratégico · Q2 2026</span>
          <button class="bg-primary text-orbit-black px-3 py-1.5 rounded-lg text-[11px] font-bold">+ Iniciativa</button>
        </div>
      </header>
      <!-- BSC 4 quadrantes -->
      <div class="flex-1 p-6 grid grid-cols-2 grid-rows-2 gap-4 relative">
        <!-- Quadrante FINANCEIRO -->
        <div class="bg-gradient-to-br from-primary/20 to-transparent border border-primary/40 rounded-2xl p-4 flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <div><span class="text-[10px] uppercase tracking-wider text-primary font-bold">Financeiro</span><p class="text-2xl font-extrabold text-white">92%</p></div>
            <span class="text-[9px] bg-success/20 text-success rounded px-1.5 py-0.5 font-bold">+6pp</span>
          </div>
          <div class="space-y-1.5">
            <div class="bg-[#0A0A0C] border border-white/10 rounded-lg p-2 text-[11px] text-white flex justify-between"><span>Aumentar EBITDA 20%</span><span class="text-success font-bold">95%</span></div>
            <div class="bg-[#0A0A0C] border border-white/10 rounded-lg p-2 text-[11px] text-white flex justify-between"><span>Reduzir burn 30%</span><span class="text-success font-bold">88%</span></div>
          </div>
        </div>
        <!-- Quadrante CLIENTE -->
        <div class="bg-[#0E0E11] border border-white/10 rounded-2xl p-4 flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <div><span class="text-[10px] uppercase tracking-wider text-gray-500 font-bold">Cliente</span><p class="text-2xl font-extrabold text-white">78%</p></div>
            <span class="text-[9px] bg-success/20 text-success rounded px-1.5 py-0.5 font-bold">+12pp</span>
          </div>
          <div class="space-y-1.5">
            <div class="bg-[#0A0A0C] border border-white/10 rounded-lg p-2 text-[11px] text-white flex justify-between"><span>NPS &gt; 70</span><span class="text-success font-bold">72</span></div>
            <div class="bg-[#0A0A0C] border border-white/10 rounded-lg p-2 text-[11px] text-white flex justify-between"><span>Churn &lt; 2%</span><span class="text-error font-bold">2,4%</span></div>
          </div>
        </div>
        <!-- Quadrante PROCESSOS -->
        <div class="bg-[#0E0E11] border border-white/10 rounded-2xl p-4 flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <div><span class="text-[10px] uppercase tracking-wider text-gray-500 font-bold">Processos</span><p class="text-2xl font-extrabold text-white">65%</p></div>
            <span class="text-[9px] bg-error/15 text-error rounded px-1.5 py-0.5 font-bold">⚠ atraso</span>
          </div>
          <div class="space-y-1.5">
            <div class="bg-[#0A0A0C] border border-white/10 rounded-lg p-2 text-[11px] text-white flex justify-between"><span>47 processos mapeados</span><span class="text-success font-bold">100%</span></div>
            <div class="bg-[#0A0A0C] border border-error/30 rounded-lg p-2 text-[11px] text-white flex justify-between"><span>Tempo médio ciclo −20%</span><span class="text-error font-bold">−8%</span></div>
          </div>
        </div>
        <!-- Quadrante APRENDIZADO -->
        <div class="bg-[#0E0E11] border border-white/10 rounded-2xl p-4 flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <div><span class="text-[10px] uppercase tracking-wider text-gray-500 font-bold">Aprendizado</span><p class="text-2xl font-extrabold text-white">70%</p></div>
            <span class="text-[9px] bg-white/5 text-gray-300 rounded px-1.5 py-0.5 font-bold">+3pp</span>
          </div>
          <div class="space-y-1.5">
            <div class="bg-[#0A0A0C] border border-white/10 rounded-lg p-2 text-[11px] text-white flex justify-between"><span>PDI executado · 47/56</span><span class="text-success font-bold">84%</span></div>
            <div class="bg-[#0A0A0C] border border-white/10 rounded-lg p-2 text-[11px] text-white flex justify-between"><span>Treinamentos · meta 12</span><span class="font-bold">9</span></div>
          </div>
        </div>
        <!-- Olívia floating -->
        <div class="absolute bottom-4 right-4 bg-[#0A0A0C] border border-primary/30 rounded-2xl p-3 max-w-[260px] shadow-2xl ring-1 ring-primary/15">
          <div class="flex items-start gap-2"><div class="w-7 h-7 rounded-full bg-gradient-to-br from-primary to-primary-600 flex items-center justify-center text-orbit-black font-extrabold text-[10px] shrink-0">OL</div><p class="text-[11px] text-gray-300 leading-snug">Processos abaixo da meta há 2 meses. Tempo médio ciclo é o gargalo.</p></div>
        </div>
      </div>
    </div>
  </div>
'''

# ─────────────────────────────────────────────────────────────────
# PROCESSOS · Fluxograma BPMN horizontal com caixas + setas
# ─────────────────────────────────────────────────────────────────

PROCESSOS_A = '''
  <!-- HERO MOCKUP DESKTOP · BPMN flowchart -->
  <div class="hidden md:flex scroll-item scroll-blur-in d-500 w-full h-[720px] max-w-[1440px] mt-20 mr-auto ml-auto relative items-center justify-center" data-swap="screenshot-painel">
    <div class="flex flex-col overflow-hidden z-30 bg-[#0A0A0C] w-full h-full max-w-6xl border-white/10 border ring-white/5 ring-1 rounded-2xl mr-2 ml-2 md:mr-6 md:ml-6 relative shadow-2xl text-gray-400 select-none">
      <header class="h-14 border-b border-white/5 flex items-center justify-between px-6 shrink-0">
        <div class="flex items-center gap-3">
          <div class="w-7 h-7 rounded-full bg-gradient-to-br from-primary to-primary-600 flex items-center justify-center text-orbit-black font-extrabold text-[11px]">OR</div>
          <span class="text-white font-bold text-sm tracking-tight">Orbit</span>
          <span class="text-primary font-bold text-xs uppercase tracking-wider">Processos</span>
        </div>
        <div class="flex items-center gap-3">
          <span class="text-[11px] text-gray-500">Pedido de compra · v2.1 · ISO 9001</span>
          <button class="bg-primary text-orbit-black px-3 py-1.5 rounded-lg text-[11px] font-bold">Exportar BPMN</button>
        </div>
      </header>
      <!-- Flowchart canvas -->
      <div class="flex-1 p-8 relative overflow-hidden">
        <div class="absolute inset-0 opacity-[0.04]" style="background-image:linear-gradient(rgba(255,255,255,0.5) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.5) 1px, transparent 1px); background-size: 24px 24px;"></div>
        <!-- SVG canvas with BPMN nodes -->
        <svg class="w-full h-full relative z-10" viewBox="0 0 1200 500" preserveAspectRatio="xMidYMid meet">
          <!-- Linhas conectoras -->
          <line x1="160" y1="120" x2="220" y2="120" stroke="rgba(255,255,255,0.3)" stroke-width="2" marker-end="url(#arrow)"/>
          <line x1="370" y1="120" x2="430" y2="120" stroke="rgba(255,255,255,0.3)" stroke-width="2" marker-end="url(#arrow)"/>
          <line x1="540" y1="120" x2="600" y2="120" stroke="rgba(255,255,255,0.3)" stroke-width="2" marker-end="url(#arrow)"/>
          <line x1="670" y1="155" x2="670" y2="240" stroke="#ffba1a" stroke-width="2" marker-end="url(#arrow-gold)"/>
          <line x1="730" y1="120" x2="800" y2="120" stroke="rgba(255,255,255,0.3)" stroke-width="2" marker-end="url(#arrow)"/>
          <line x1="950" y1="120" x2="1010" y2="120" stroke="rgba(255,255,255,0.3)" stroke-width="2" marker-end="url(#arrow)"/>
          <line x1="730" y1="295" x2="800" y2="120" stroke="rgba(255,255,255,0.15)" stroke-width="1.5" stroke-dasharray="4 4"/>

          <defs>
            <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><polygon points="0 0, 10 5, 0 10" fill="rgba(255,255,255,0.3)"/></marker>
            <marker id="arrow-gold" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><polygon points="0 0, 10 5, 0 10" fill="#ffba1a"/></marker>
          </defs>

          <!-- Start · Recebe pedido -->
          <circle cx="100" cy="120" r="28" fill="#1A1A1F" stroke="rgba(255,255,255,0.25)" stroke-width="2"/>
          <text x="100" y="125" text-anchor="middle" fill="white" font-size="11" font-weight="700">Receber</text>

          <!-- Atividade 1 -->
          <rect x="220" y="90" width="150" height="60" rx="10" fill="#0E0E11" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
          <text x="295" y="115" text-anchor="middle" fill="white" font-size="11" font-weight="700">Validar dados</text>
          <text x="295" y="130" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="9">Compras · 15min</text>

          <!-- Atividade 2 -->
          <rect x="430" y="90" width="110" height="60" rx="10" fill="#0E0E11" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
          <text x="485" y="115" text-anchor="middle" fill="white" font-size="11" font-weight="700">Cotar</text>
          <text x="485" y="130" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="9">3 fornecedores</text>

          <!-- Decisão · losango -->
          <polygon points="670,90 730,120 670,150 610,120" fill="#0E0E11" stroke="#ffba1a" stroke-width="2"/>
          <text x="670" y="118" text-anchor="middle" fill="#ffba1a" font-size="11" font-weight="700">Valor</text>
          <text x="670" y="132" text-anchor="middle" fill="#ffba1a" font-size="10" font-weight="700">&gt; 10k?</text>

          <!-- Path NÃO · direto pra aprovar -->
          <rect x="800" y="90" width="150" height="60" rx="10" fill="#0E0E11" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
          <text x="875" y="115" text-anchor="middle" fill="white" font-size="11" font-weight="700">Aprovar líder</text>
          <text x="875" y="130" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="9">SLA · 4h</text>

          <!-- Path SIM · aprovação diretor -->
          <rect x="600" y="240" width="160" height="60" rx="10" fill="#0E0E11" stroke="#ffba1a" stroke-width="1.5"/>
          <text x="680" y="265" text-anchor="middle" fill="white" font-size="11" font-weight="700">Aprovar diretor</text>
          <text x="680" y="280" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="9">SLA · 24h · 2-vias</text>

          <!-- End · concluído -->
          <circle cx="1080" cy="120" r="28" fill="#1A1A1F" stroke="#3FB950" stroke-width="3"/>
          <text x="1080" y="120" text-anchor="middle" fill="#3FB950" font-size="11" font-weight="700">Concluído</text>

          <!-- Indicadores nas atividades -->
          <text x="295" y="170" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="9">KPI · 100% no SLA</text>
          <text x="485" y="170" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="9">KPI · 95% no SLA</text>
        </svg>

        <!-- Tags inferiores -->
        <div class="absolute bottom-4 left-6 flex gap-2 z-10">
          <span class="text-[10px] bg-success/15 text-success border border-success/30 rounded-full px-2.5 py-1 font-bold">✓ ISO 9001 ready</span>
          <span class="text-[10px] bg-white/5 border border-white/10 rounded-full px-2.5 py-1 font-bold text-gray-300">5 etapas · 2 responsáveis · 4 KPIs</span>
        </div>

        <!-- Olívia agent -->
        <div class="absolute bottom-4 right-4 bg-[#0A0A0C] border border-primary/30 rounded-2xl p-3 max-w-[260px] shadow-2xl ring-1 ring-primary/15 z-10">
          <div class="flex items-start gap-2"><div class="w-7 h-7 rounded-full bg-gradient-to-br from-primary to-primary-600 flex items-center justify-center text-orbit-black font-extrabold text-[10px] shrink-0">OL</div><div><p class="text-[11px] font-bold text-white">Agente IA · processo gerado</p><p class="text-[10px] text-gray-400 mt-0.5">A partir da descrição em texto. Edite ou aprove.</p></div></div>
        </div>
      </div>
    </div>
  </div>
'''

# ─────────────────────────────────────────────────────────────────
# PESSOAS · Organograma + tabela de candidatos com score
# ─────────────────────────────────────────────────────────────────

PESSOAS_A = '''
  <!-- HERO MOCKUP DESKTOP · Organograma + Candidatos -->
  <div class="hidden md:flex scroll-item scroll-blur-in d-500 w-full h-[720px] max-w-[1440px] mt-20 mr-auto ml-auto relative items-center justify-center" data-swap="screenshot-painel">
    <div class="flex flex-col overflow-hidden z-30 bg-[#0A0A0C] w-full h-full max-w-6xl border-white/10 border ring-white/5 ring-1 rounded-2xl mr-2 ml-2 md:mr-6 md:ml-6 relative shadow-2xl text-gray-400 select-none">
      <header class="h-14 border-b border-white/5 flex items-center justify-between px-6 shrink-0">
        <div class="flex items-center gap-3">
          <div class="w-7 h-7 rounded-full bg-gradient-to-br from-primary to-primary-600 flex items-center justify-center text-orbit-black font-extrabold text-[11px]">OR</div>
          <span class="text-white font-bold text-sm tracking-tight">Orbit</span>
          <span class="text-primary font-bold text-xs uppercase tracking-wider">Pessoas</span>
        </div>
        <div class="flex items-center gap-3">
          <span class="text-[11px] text-gray-500">Eng Sr React · 120 candidatos avaliados</span>
          <button class="bg-primary text-orbit-black px-3 py-1.5 rounded-lg text-[11px] font-bold">+ Nova vaga</button>
        </div>
      </header>
      <div class="flex-1 grid grid-cols-5 gap-4 p-6">
        <!-- Organograma · ocupa 2 colunas -->
        <div class="col-span-2 bg-[#0E0E11] border border-white/10 rounded-2xl p-4 flex flex-col">
          <div class="flex items-center justify-between mb-4"><span class="text-[11px] uppercase tracking-wider text-gray-500 font-bold">Organograma</span><span class="text-[10px] bg-white/5 rounded px-1.5 py-0.5 font-bold">28 pessoas</span></div>
          <!-- CEO topo -->
          <div class="flex justify-center mb-6 relative">
            <div class="bg-gradient-to-br from-primary/20 to-transparent border border-primary/40 rounded-xl px-3 py-2 text-center"><div class="w-7 h-7 rounded-full bg-primary mx-auto mb-1.5 flex items-center justify-center text-[10px] font-extrabold text-orbit-black">CE</div><p class="text-[11px] font-bold text-white">CEO</p><p class="text-[9px] text-gray-500">Mateus R.</p></div>
          </div>
          <!-- Linhas conectoras simbólicas -->
          <div class="h-4 relative mb-2"><div class="absolute top-0 left-1/2 w-0.5 h-2 bg-white/10"></div><div class="absolute top-2 left-[25%] right-[25%] h-0.5 bg-white/10"></div><div class="absolute top-2 left-[25%] w-0.5 h-2 bg-white/10"></div><div class="absolute top-2 left-1/2 w-0.5 h-2 bg-white/10"></div><div class="absolute top-2 right-[25%] w-0.5 h-2 bg-white/10"></div></div>
          <!-- 3 cards de diretoria -->
          <div class="grid grid-cols-3 gap-1.5 mb-4">
            <div class="bg-[#0A0A0C] border border-white/10 rounded-lg p-1.5 text-center"><div class="w-6 h-6 rounded-full bg-white/10 mx-auto mb-1 text-[9px] font-bold flex items-center justify-center text-white">DC</div><p class="text-[9px] font-bold text-white">Dir Com</p></div>
            <div class="bg-[#0A0A0C] border border-white/10 rounded-lg p-1.5 text-center"><div class="w-6 h-6 rounded-full bg-white/10 mx-auto mb-1 text-[9px] font-bold flex items-center justify-center text-white">CT</div><p class="text-[9px] font-bold text-white">CTO</p></div>
            <div class="bg-[#0A0A0C] border border-white/10 rounded-lg p-1.5 text-center"><div class="w-6 h-6 rounded-full bg-white/10 mx-auto mb-1 text-[9px] font-bold flex items-center justify-center text-white">CF</div><p class="text-[9px] font-bold text-white">CFO</p></div>
          </div>
          <!-- vagas em aberto -->
          <div class="mt-auto bg-primary/5 border border-primary/20 rounded-lg p-2.5"><div class="flex items-center justify-between"><span class="text-[10px] text-primary font-bold">Vagas abertas · time tech</span><span class="text-xs font-extrabold text-primary">3</span></div></div>
        </div>
        <!-- Candidatos · ocupa 3 colunas -->
        <div class="col-span-3 bg-[#0E0E11] border border-white/10 rounded-2xl flex flex-col overflow-hidden">
          <div class="flex items-center justify-between px-4 py-3 border-b border-white/10">
            <span class="text-[11px] uppercase tracking-wider text-gray-500 font-bold">Candidatos · Eng Sr React</span>
            <span class="text-[10px] bg-success/15 text-success rounded px-1.5 py-0.5 font-bold">Olívia avaliou 120/120</span>
          </div>
          <div class="flex-1 px-4 py-2 space-y-1.5 overflow-y-auto">
            <div class="flex items-center gap-3 p-2 rounded-lg bg-primary/5 border border-primary/30">
              <span class="text-[9px] bg-primary/20 text-primary rounded px-1.5 py-0.5 font-bold w-8 text-center">#3</span>
              <div class="flex-1"><p class="text-[12px] font-bold text-white">Maria Lima</p><p class="text-[10px] text-gray-500">DISC · D-Alto · 8 anos React</p></div>
              <div class="flex gap-1.5">
                <div class="text-center"><p class="text-[9px] text-gray-500">CV</p><p class="text-[11px] font-bold text-success">92</p></div>
                <div class="text-center"><p class="text-[9px] text-gray-500">DISC</p><p class="text-[11px] font-bold text-success">88</p></div>
                <div class="text-center"><p class="text-[9px] text-gray-500">Entr</p><p class="text-[11px] font-bold text-primary">94</p></div>
              </div>
              <span class="text-[10px] bg-success/15 text-success rounded px-1.5 py-0.5 font-bold">Aderente</span>
            </div>
            <div class="flex items-center gap-3 p-2 rounded-lg bg-white/[0.02] border border-white/5">
              <span class="text-[9px] bg-white/5 text-gray-300 rounded px-1.5 py-0.5 font-bold w-8 text-center">#7</span>
              <div class="flex-1"><p class="text-[12px] font-bold text-white">João Albuquerque</p><p class="text-[10px] text-gray-500">DISC · D-S · 6 anos</p></div>
              <div class="flex gap-1.5">
                <div class="text-center"><p class="text-[9px] text-gray-500">CV</p><p class="text-[11px] font-bold text-success">85</p></div>
                <div class="text-center"><p class="text-[9px] text-gray-500">DISC</p><p class="text-[11px] font-bold">76</p></div>
                <div class="text-center"><p class="text-[9px] text-gray-500">Entr</p><p class="text-[11px] font-bold">79</p></div>
              </div>
              <span class="text-[10px] bg-white/5 text-gray-300 rounded px-1.5 py-0.5 font-bold">Aderente</span>
            </div>
            <div class="flex items-center gap-3 p-2 rounded-lg bg-white/[0.02] border border-white/5">
              <span class="text-[9px] bg-white/5 text-gray-300 rounded px-1.5 py-0.5 font-bold w-8 text-center">#12</span>
              <div class="flex-1"><p class="text-[12px] font-bold text-white">Camila Ortiz</p><p class="text-[10px] text-gray-500">DISC · I-S · 5 anos</p></div>
              <div class="flex gap-1.5">
                <div class="text-center"><p class="text-[9px] text-gray-500">CV</p><p class="text-[11px] font-bold">78</p></div>
                <div class="text-center"><p class="text-[9px] text-gray-500">DISC</p><p class="text-[11px] font-bold">72</p></div>
                <div class="text-center"><p class="text-[9px] text-gray-500">Entr</p><p class="text-[11px] font-bold">81</p></div>
              </div>
              <span class="text-[10px] bg-white/5 text-gray-300 rounded px-1.5 py-0.5 font-bold">Avaliar</span>
            </div>
            <div class="flex items-center gap-3 p-2 rounded-lg bg-white/[0.02] border border-white/5">
              <span class="text-[9px] bg-white/5 text-gray-500 rounded px-1.5 py-0.5 font-bold w-8 text-center">#98</span>
              <div class="flex-1"><p class="text-[12px] font-bold text-white">Vinícius P. ⭐</p><p class="text-[10px] text-primary">Olívia: similar ao #3 · mesma confiança</p></div>
              <div class="flex gap-1.5">
                <div class="text-center"><p class="text-[9px] text-gray-500">CV</p><p class="text-[11px] font-bold text-success">90</p></div>
                <div class="text-center"><p class="text-[9px] text-gray-500">DISC</p><p class="text-[11px] font-bold text-success">87</p></div>
                <div class="text-center"><p class="text-[9px] text-gray-500">Entr</p><p class="text-[11px] font-bold text-success">91</p></div>
              </div>
              <span class="text-[10px] bg-success/15 text-success rounded px-1.5 py-0.5 font-bold">Aderente</span>
            </div>
            <p class="text-center text-[10px] text-gray-600 pt-2">+ 116 candidatos · todos avaliados pela Olívia</p>
          </div>
        </div>
      </div>
    </div>
  </div>
'''

# ─────────────────────────────────────────────────────────────────
# PROJETOS · Gantt simplificado
# ─────────────────────────────────────────────────────────────────

PROJETOS_A = '''
  <!-- HERO MOCKUP DESKTOP · Gantt -->
  <div class="hidden md:flex scroll-item scroll-blur-in d-500 w-full h-[720px] max-w-[1440px] mt-20 mr-auto ml-auto relative items-center justify-center" data-swap="screenshot-painel">
    <div class="flex flex-col overflow-hidden z-30 bg-[#0A0A0C] w-full h-full max-w-6xl border-white/10 border ring-white/5 ring-1 rounded-2xl mr-2 ml-2 md:mr-6 md:ml-6 relative shadow-2xl text-gray-400 select-none">
      <header class="h-14 border-b border-white/5 flex items-center justify-between px-6 shrink-0">
        <div class="flex items-center gap-3">
          <div class="w-7 h-7 rounded-full bg-gradient-to-br from-primary to-primary-600 flex items-center justify-center text-orbit-black font-extrabold text-[11px]">OR</div>
          <span class="text-white font-bold text-sm tracking-tight">Orbit</span>
          <span class="text-primary font-bold text-xs uppercase tracking-wider">Projetos</span>
        </div>
        <div class="flex items-center gap-3">
          <div class="flex bg-white/5 rounded-lg p-0.5"><span class="px-2.5 py-1 text-[10px] font-bold text-gray-400">Kanban</span><span class="px-2.5 py-1 text-[10px] font-bold bg-primary/20 text-primary rounded">Gantt</span><span class="px-2.5 py-1 text-[10px] font-bold text-gray-400">Lista</span></div>
          <button class="bg-primary text-orbit-black px-3 py-1.5 rounded-lg text-[11px] font-bold">+ Projeto</button>
        </div>
      </header>
      <div class="flex-1 p-6 flex flex-col">
        <!-- Eixo tempo -->
        <div class="grid grid-cols-12 gap-2 mb-3 border-b border-white/10 pb-2">
          <div class="col-span-3"></div>
          <div class="col-span-9 grid grid-cols-6 text-[10px] uppercase tracking-wider text-gray-500 font-bold">
            <div>Mai</div><div>Jun</div><div class="text-primary">Jul</div><div>Ago</div><div>Set</div><div>Out</div>
          </div>
        </div>
        <!-- Projetos · 6 linhas -->
        <div class="flex-1 space-y-2.5">
          <!-- Projeto 1 · CRM rollout -->
          <div class="grid grid-cols-12 gap-2 items-center">
            <div class="col-span-3">
              <p class="text-[12px] font-bold text-white">CRM rollout · Vendas</p>
              <p class="text-[10px] text-gray-500">PMO · Lia · 4/8 tarefas</p>
            </div>
            <div class="col-span-9 grid grid-cols-6 relative h-7 items-center">
              <div class="absolute left-[2%] w-[40%] h-6 bg-gradient-to-r from-primary to-primary-600 rounded-md flex items-center px-2"><span class="text-[10px] font-bold text-orbit-black">50%</span></div>
            </div>
          </div>
          <!-- Projeto 2 · ISO 9001 -->
          <div class="grid grid-cols-12 gap-2 items-center">
            <div class="col-span-3">
              <p class="text-[12px] font-bold text-white">Certificação ISO 9001</p>
              <p class="text-[10px] text-gray-500">PMO · Carlos · 12/24</p>
            </div>
            <div class="col-span-9 grid grid-cols-6 relative h-7 items-center">
              <div class="absolute left-[12%] w-[75%] h-6 bg-white/10 border border-white/20 rounded-md flex items-center px-2"><span class="text-[10px] font-bold text-white">50% · risco</span></div>
            </div>
          </div>
          <!-- Projeto 3 · com risco -->
          <div class="grid grid-cols-12 gap-2 items-center">
            <div class="col-span-3">
              <p class="text-[12px] font-bold text-white">Reforma operação SP <span class="text-error">⚠</span></p>
              <p class="text-[10px] text-error">5 dias atrasado · cliente notificado</p>
            </div>
            <div class="col-span-9 grid grid-cols-6 relative h-7 items-center">
              <div class="absolute left-[5%] w-[55%] h-6 bg-error/20 border border-error/50 rounded-md flex items-center px-2"><span class="text-[10px] font-bold text-error">38% · atrasado</span></div>
            </div>
          </div>
          <!-- Projeto 4 -->
          <div class="grid grid-cols-12 gap-2 items-center">
            <div class="col-span-3">
              <p class="text-[12px] font-bold text-white">Migração de servidor</p>
              <p class="text-[10px] text-gray-500">CTO · André · 8/10</p>
            </div>
            <div class="col-span-9 grid grid-cols-6 relative h-7 items-center">
              <div class="absolute left-[18%] w-[28%] h-6 bg-success/20 border border-success/50 rounded-md flex items-center px-2"><span class="text-[10px] font-bold text-success">80% · no prazo</span></div>
            </div>
          </div>
          <!-- Projeto 5 -->
          <div class="grid grid-cols-12 gap-2 items-center">
            <div class="col-span-3">
              <p class="text-[12px] font-bold text-white">Onboarding · Cliente Mega</p>
              <p class="text-[10px] text-gray-500">CS · Paula · 3/12</p>
            </div>
            <div class="col-span-9 grid grid-cols-6 relative h-7 items-center">
              <div class="absolute left-[40%] w-[35%] h-6 bg-white/10 border border-white/20 rounded-md flex items-center px-2"><span class="text-[10px] font-bold text-white">25%</span></div>
            </div>
          </div>
          <!-- Projeto 6 -->
          <div class="grid grid-cols-12 gap-2 items-center">
            <div class="col-span-3">
              <p class="text-[12px] font-bold text-white">Estudo de mercado SE</p>
              <p class="text-[10px] text-gray-500">Strategy · 0/6</p>
            </div>
            <div class="col-span-9 grid grid-cols-6 relative h-7 items-center">
              <div class="absolute left-[58%] w-[32%] h-6 bg-white/[0.04] border border-white/10 rounded-md flex items-center px-2"><span class="text-[10px] font-bold text-gray-400">planejado</span></div>
            </div>
          </div>
        </div>
        <!-- Olivia -->
        <div class="bg-primary/5 border border-primary/30 rounded-xl p-3 mt-4 flex items-center gap-3">
          <div class="w-9 h-9 rounded-full bg-gradient-to-br from-primary to-primary-600 flex items-center justify-center text-orbit-black font-extrabold text-xs shrink-0">OL</div>
          <p class="text-[12px] text-gray-300 flex-1"><strong class="text-primary">Risco preditivo:</strong> Reforma SP precisa de mais 2 pessoas até quinta. Mover do projeto Mega?</p>
          <button class="text-[10px] bg-primary text-orbit-black px-3 py-1.5 rounded-lg font-bold">Realocar</button>
        </div>
      </div>
    </div>
  </div>
'''

# ─────────────────────────────────────────────────────────────────
# CANAL ORBIT · Dashboard de clientes da consultoria
# ─────────────────────────────────────────────────────────────────

CANAL_ORBIT_A = '''
  <!-- HERO MOCKUP DESKTOP · Dashboard Canal Orbit -->
  <div class="hidden md:flex scroll-item scroll-blur-in d-500 w-full h-[720px] max-w-[1440px] mt-20 mr-auto ml-auto relative items-center justify-center" data-swap="screenshot-painel">
    <div class="flex flex-col overflow-hidden z-30 bg-[#0A0A0C] w-full h-full max-w-6xl border-white/10 border ring-white/5 ring-1 rounded-2xl mr-2 ml-2 md:mr-6 md:ml-6 relative shadow-2xl text-gray-400 select-none">
      <header class="h-14 border-b border-white/5 flex items-center justify-between px-6 shrink-0">
        <div class="flex items-center gap-3">
          <div class="w-7 h-7 rounded-full bg-gradient-to-br from-primary to-primary-600 flex items-center justify-center text-orbit-black font-extrabold text-[11px]">CN</div>
          <span class="text-white font-bold text-sm tracking-tight">Sua Consultoria</span>
          <span class="text-primary font-bold text-xs uppercase tracking-wider">· White-label</span>
        </div>
        <div class="flex items-center gap-3">
          <span class="text-[11px] text-gray-500">clientes.suaconsultoria.com.br</span>
          <button class="bg-primary text-orbit-black px-3 py-1.5 rounded-lg text-[11px] font-bold">+ Novo cliente</button>
        </div>
      </header>
      <!-- Stats row -->
      <div class="grid grid-cols-4 gap-3 p-5 border-b border-white/5">
        <div class="bg-gradient-to-br from-primary/15 to-transparent border border-primary/40 rounded-xl p-3"><p class="text-[10px] uppercase tracking-wider text-primary font-bold">MRR</p><p class="text-xl font-extrabold text-white">R$ 87,4K</p><p class="text-[10px] text-success font-bold">+22% / 90d</p></div>
        <div class="bg-[#0E0E11] border border-white/10 rounded-xl p-3"><p class="text-[10px] uppercase tracking-wider text-gray-500 font-bold">Clientes ativos</p><p class="text-xl font-extrabold text-white">24</p><p class="text-[10px] text-success font-bold">+3 no mês</p></div>
        <div class="bg-[#0E0E11] border border-white/10 rounded-xl p-3"><p class="text-[10px] uppercase tracking-wider text-gray-500 font-bold">Custo atendimento</p><p class="text-xl font-extrabold text-white">5,2%</p><p class="text-[10px] text-success font-bold">mercado · 20-30%</p></div>
        <div class="bg-[#0E0E11] border border-white/10 rounded-xl p-3"><p class="text-[10px] uppercase tracking-wider text-gray-500 font-bold">Equipe</p><p class="text-xl font-extrabold text-white">3</p><p class="text-[10px] text-gray-500">consultores · 24 clientes</p></div>
      </div>
      <!-- Lista de clientes -->
      <div class="flex-1 p-5 overflow-y-auto">
        <div class="flex items-center justify-between mb-3">
          <span class="text-[11px] uppercase tracking-wider text-gray-500 font-bold">Carteira · 24 clientes</span>
          <div class="flex gap-2">
            <span class="text-[10px] bg-success/15 text-success rounded-full px-2 py-0.5 font-bold">22 saudáveis</span>
            <span class="text-[10px] bg-error/15 text-error rounded-full px-2 py-0.5 font-bold">2 em risco</span>
          </div>
        </div>
        <div class="space-y-2">
          <!-- Cliente 1 -->
          <div class="bg-[#0E0E11] border border-white/10 rounded-xl p-3 flex items-center gap-4 hover:border-primary/30 transition-colors">
            <div class="w-9 h-9 rounded-full bg-gradient-to-br from-primary/30 to-primary/10 flex items-center justify-center text-[11px] font-extrabold text-primary">CA</div>
            <div class="flex-1"><p class="text-[12px] font-bold text-white">Construtora ACME · Plano Pro</p><p class="text-[10px] text-gray-500">desde set/2025 · próx revisão: 5/jun</p></div>
            <div class="text-right"><p class="text-[11px] font-bold text-primary">R$ 4.498/mês</p><span class="text-[9px] text-success font-bold">NPS 82</span></div>
            <span class="text-[10px] bg-success/15 text-success rounded px-2 py-1 font-bold">saudável</span>
          </div>
          <!-- Cliente 2 com risco -->
          <div class="bg-[#0E0E11] border border-error/30 rounded-xl p-3 flex items-center gap-4">
            <div class="w-9 h-9 rounded-full bg-gradient-to-br from-error/30 to-error/10 flex items-center justify-center text-[11px] font-extrabold text-error">CM</div>
            <div class="flex-1"><p class="text-[12px] font-bold text-white">Clínica MedSol · Plano Smart</p><p class="text-[10px] text-error">⚠ Olívia detectou · acesso caiu 70% nas últimas 3 semanas</p></div>
            <div class="text-right"><p class="text-[11px] font-bold text-primary">R$ 2.200/mês</p><span class="text-[9px] text-error font-bold">churn 64%</span></div>
            <button class="text-[10px] bg-error/15 text-error rounded px-2 py-1 font-bold">Ligar</button>
          </div>
          <!-- Cliente 3 -->
          <div class="bg-[#0E0E11] border border-white/10 rounded-xl p-3 flex items-center gap-4">
            <div class="w-9 h-9 rounded-full bg-gradient-to-br from-primary/30 to-primary/10 flex items-center justify-center text-[11px] font-extrabold text-primary">F1</div>
            <div class="flex-1"><p class="text-[12px] font-bold text-white">F12 Publicidade · Plano Ultra</p><p class="text-[10px] text-gray-500">desde mar/2025 · 8 colaboradores ativos</p></div>
            <div class="text-right"><p class="text-[11px] font-bold text-primary">R$ 4.498/mês</p><span class="text-[9px] text-success font-bold">NPS 89</span></div>
            <span class="text-[10px] bg-success/15 text-success rounded px-2 py-1 font-bold">saudável</span>
          </div>
          <!-- Cliente 4 -->
          <div class="bg-[#0E0E11] border border-white/10 rounded-xl p-3 flex items-center gap-4">
            <div class="w-9 h-9 rounded-full bg-gradient-to-br from-primary/30 to-primary/10 flex items-center justify-center text-[11px] font-extrabold text-primary">GC</div>
            <div class="flex-1"><p class="text-[12px] font-bold text-white">Grupo Connect · Frota</p><p class="text-[10px] text-gray-500">140 veículos · acessou ontem</p></div>
            <div class="text-right"><p class="text-[11px] font-bold text-primary">R$ 4.498/mês</p><span class="text-[9px] text-success font-bold">NPS 91</span></div>
            <span class="text-[10px] bg-success/15 text-success rounded px-2 py-1 font-bold">saudável</span>
          </div>
          <p class="text-center text-[10px] text-gray-600 pt-2">+ 20 clientes ativos · 100% white-label</p>
        </div>
      </div>
    </div>
  </div>
'''


# ─────────────────────────────────────────────────────────────────
# REGISTRY · slug → mockup A
# ─────────────────────────────────────────────────────────────────

HERO_MOCKUPS_A = {
    'crm': CRM_A,
    'estrategico': ESTRATEGICO_A,
    'indicadores': INDICADORES_A,
    'processos': PROCESSOS_A,
    'pessoas': PESSOAS_A,
    'projetos': PROJETOS_A,
    'canal-orbit': CANAL_ORBIT_A,
}
