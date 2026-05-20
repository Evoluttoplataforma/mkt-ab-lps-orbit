#!/usr/bin/env python3
"""
Gerador de LPs Orbit por módulo · A (dark) + B (light)
Lê os templates de Financeiro e aplica configs por módulo via find-replace.
"""
import re, shutil, os
from pathlib import Path

ROOT = Path(__file__).parent.parent
TPL_A = (ROOT / 'public/financeiro-variant-a/index.html').read_text()
TPL_B = (ROOT / 'public/financeiro-variant-b/index.html').read_text()

# ─────────────────────────────────────────────────────────────────
# MÓDULOS · cada um define os swaps específicos
# Estrutura: cada chave é o texto literal do Financeiro a ser substituído
# ─────────────────────────────────────────────────────────────────

MODULES = {
    'crm': {
        'label': 'CRM',
        'image_available': True,
        'meta': {
            'title': 'CRM com IA para Empresas B2B | Orbit Gestão',
            'description': 'Pipeline visual, análise IA por lead e integração nativa com WhatsApp. Para empresas B2B com R$ 500k+/mês e 30+ funcionários.',
            'keywords': 'CRM com WhatsApp, alternativa Pipedrive, alternativa RD Station, pipeline de vendas software, IA para vendas, CRM para empresa média',
            'og_title': 'Orbit CRM — CRM com IA para empresas B2B',
            'og_description': 'Tire os leads do WhatsApp pessoal. Pipeline, análise IA e automação para empresas R$ 500k+/30+ funcionários.',
        },
        'hero_a_h1': 'CRM com <span class="text-primary">IA</span>. Pipeline real, integrado ao WhatsApp.',
        'hero_a_sub': 'Pipeline visual, automação, web forms, análise IA por oportunidade — e tudo conversa com Financeiro, RH e Processos da empresa.',
        'hero_b_h1': 'Tire o comercial do <em>WhatsApp pessoal</em> sem perder agilidade.',
        'hero_b_sub': 'Pipeline visual, automação, web forms, análise IA por oportunidade — e tudo conversa com Financeiro, RH e Processos da empresa.',
        'credibility_headline': '3.045+ empresas tiraram o comercial do WhatsApp pessoal',
        'stats': [
            ('65%', 'mais produtividade do time comercial'),
            ('40%', 'menos tempo em tarefas operacionais'),
            ('85%', 'menos leads perdidos por esquecimento'),
            ('2.204', 'leads médios gerenciados por cliente'),
        ],
        'pci_headline': 'Quem ganha mais com o <span class="text-primary">Orbit CRM</span>',
        'pci_headline_b': 'Quem ganha mais com o <em>Orbit CRM</em>',
        'pci_sub': 'Empresas B2B estruturadas que cansaram do WhatsApp pessoal e Pipedrive básico:',
        'pci_items': [
            ('solar:buildings-3-bold-duotone', 'Porte', '<strong>R$ 500.000+/mês de faturamento</strong> e <strong>30 ou mais funcionários</strong>.'),
            ('solar:users-group-rounded-bold-duotone', 'Time comercial', 'Time comercial tem <strong>5+ vendedores</strong> (ou está chegando lá).'),
            ('solar:chat-round-dots-bold-duotone', 'Leads no WhatsApp', 'Leads ainda chegam no <strong>WhatsApp pessoal</strong> do vendedor.'),
            ('solar:eye-closed-bold-duotone', 'Sem visibilidade', 'Direção comercial <strong>não vê pipeline</strong> em tempo real.'),
            ('solar:exit-bold-duotone', 'Stack limitado', 'Já tentou <strong>Pipedrive/RD Station</strong> mas não integra com fin/RH.'),
            ('solar:magic-stick-3-bold-duotone', 'Falta IA', 'Precisa de <strong>IA para qualificar</strong> e sugerir próxima ação.'),
        ],
        'anti_target': [
            ('solar:cart-large-2-linear', 'B2C de alto volume (e-commerce, varejo unitário).'),
            ('solar:user-linear', 'Empresa com 1 vendedor / SDR — não precisa de plataforma.'),
            ('solar:server-square-cloud-linear', 'Quem precisa de CRM enterprise tipo Salesforce Lightning.'),
        ],
        'benefits_headline': 'O CRM que <span class="text-primary">cresceu junto</span> com a empresa B2B',
        'benefits_headline_b': 'O CRM que <em>cresceu junto</em> com a empresa B2B',
        'benefits': [
            ('solar:magic-stick-3-bold-duotone', 'Análise IA por lead', 'Cada oportunidade recebe sugestão de próxima ação baseada em padrões.', 'A IA analisa histórico de interação, perfil da empresa e estágio do funil para sugerir o melhor próximo passo. Vendedor não fica adivinhando — segue insight com base em dado.'),
            ('solar:chat-round-dots-bold-duotone', 'WhatsApp integrado · sem extensão paga', 'Mensagens do WhatsApp registradas no pipeline automaticamente.', 'Conversa do vendedor com lead vira histórico do CRM em tempo real. Direção comercial vê tudo. Vendedor não perde tempo registrando manualmente.'),
            ('solar:document-add-bold-duotone', 'Web Forms e automações', 'Formulário do site cria lead na etapa certa.', 'Cada formulário do seu site (ou LP de Google Ads) cria lead no pipeline correto, atribui vendedor por regra e dispara mensagem automática. Zero retrabalho.'),
            ('solar:branching-paths-up-bold-duotone', 'Conectado com Financeiro, RH e Processos', 'Closer vê histórico financeiro do cliente em tela única.', 'Lead virou cliente? Já aparece no financeiro com proposta. Cliente reclamou? Closer vê o problema no módulo Problemas. Tudo conversa nativamente.'),
        ],
        'steps_headline': 'Migrar para um CRM <span class="text-primary">de verdade</span> em 3 passos',
        'steps_headline_b': 'Migrar para um CRM <em>de verdade</em> em 3 passos',
        'steps_sub': 'Implantação guiada pela equipe Orbit, sem perder histórico.',
        'steps': [
            ('01', 'Semana 1', 'Diagnóstico', 'Mapeamos seu funil atual, importamos leads do CRM antigo (Pipedrive/RD/HubSpot/planilha) e configuramos seus estágios.'),
            ('02', 'Semana 2', 'Configuração', 'Web Forms, automações, atribuição de leads e integração com WhatsApp do time.'),
            ('03', 'Semana 3', 'Go-live', 'Time comercial treinado. Diretoria começa a ver pipeline em tempo real no mesmo dia.'),
        ],
        'compare_headline': 'Por que sair de <span class="text-primary">Pipedrive + WhatsApp</span> + planilha',
        'compare_headline_b': 'Por que sair de <em>Pipedrive + WhatsApp</em> + planilha',
        'compare_sub': 'Sua stack comercial está cara e desconectada.',
        'compare_rows': [
            ('solar:branching-paths-up-bold-duotone', 'Pipedrive/RD + Zapier', 'Stack desconectada · export/import constante', 'CRM nativamente integrado', 'Sem Zapier, sem export/import'),
            ('solar:chat-round-dots-bold-duotone', 'WhatsApp pessoal do vendedor', 'Sem histórico · dependência da pessoa', 'WhatsApp integrado ao pipeline', 'Histórico pra diretoria + sem dependência'),
            ('solar:calculator-minimalistic-bold-duotone', 'Planilha de comissão batendo manual', 'Briga de número mês após mês', 'Comissão calculada do mesmo dado', 'Sem briga de número'),
            ('solar:magic-stick-3-bold-duotone', 'Vendedor adivinhando próxima ação', 'Achismo vs dado', 'IA sugere próxima ação', 'Mais conversão, menos achismo'),
            ('solar:database-bold-duotone', 'CRM separado do financeiro', 'Closer não vê histórico de pagamento', 'Tudo conectado nativamente', 'Margem por cliente em 1 clique'),
        ],
        'compare_foot': 'Soma Pipedrive + Zapier + Trello + planilha de comissão <strong class="text-primary font-extrabold">&gt; Orbit</strong>. E o Orbit conversa com o resto da empresa.',
        'faqs': [
            ('Importa o histórico do Pipedrive/RD Station?', 'Sim. A migração é guiada pela equipe Orbit. Todos os contatos, deals, etapas e histórico de interação são preservados.'),
            ('Funciona com WhatsApp Business?', 'Sim. Integração nativa com WhatsApp Business API. Mensagens entram e saem do CRM com histórico vinculado ao lead.'),
            ('Quanto custa por usuário?', 'O Orbit precifica por porte de empresa, não por usuário do CRM. Isso significa que escala sem "pegadinha" por seat. Faixa típica do ICP: <strong>R$ 1.500 a R$ 4.500/mês</strong> para a plataforma toda.'),
            ('Tem mobile?', 'Sim. App iOS e Android para vendedores em campo, com todas as funcionalidades do pipeline.'),
            ('Posso testar antes?', 'Conversa com a Olívia → SDR agenda demonstração guiada → você vê com seus dados antes de decidir.'),
            ('Funciona se meu produto tem ciclo de venda longo (3-6 meses)?', 'Sim — é exatamente o perfil de B2B 500k+/30+ que melhor se beneficia. Pipeline configurável por etapa, automações de follow-up e análise IA mantêm o lead vivo.'),
        ],
        'cta_final_h': 'Pronto para tirar o comercial do <span class="text-primary">WhatsApp pessoal?</span>',
        'cta_final_h_b': 'Pronto para tirar o comercial do <em>WhatsApp pessoal?</em>',
        'cta_final_sub': 'Fale com a Olívia agora — ela entende seu funil em 2 minutos e agenda uma demonstração com nosso especialista comercial.',
        'cta_final_micro': 'Sem cartão. Sem instalação. Só uma conversa de 2 minutos.',
    },

    'estrategico': {
        'label': 'Estratégico',
        'image_available': False,
        'placeholder_icon': 'solar:compass-big-bold-duotone',
        'meta': {
            'title': 'Software de Planejamento Estratégico com BSC | Orbit Gestão',
            'description': 'BSC, OKRs, SWOT e inteligência de mercado conectados à execução. Para empresas R$ 500k+/mês e 30+ funcionários.',
            'keywords': 'software BSC, balanced scorecard, software OKR, planejamento estratégico, software de estratégia, BSC online',
            'og_title': 'Orbit Estratégico — BSC, OKR e SWOT que saem do papel',
            'og_description': 'Estratégia auditável conectada à execução. SWOT, BSC, OKR e inteligência de mercado em uma plataforma.',
        },
        'hero_a_h1': 'Estratégia que <span class="text-primary">sai do papel</span> e chega na execução.',
        'hero_a_sub': 'BSC, OKR, SWOT e inteligência de mercado conectados ao operacional — sem PowerPoint empoeirado, sem planilha que ninguém atualiza.',
        'hero_b_h1': 'Seu plano estratégico está <em>empoeirado?</em>',
        'hero_b_sub': 'BSC, OKR, SWOT e inteligência de mercado conectados ao operacional — sem PowerPoint empoeirado, sem planilha que ninguém atualiza.',
        'credibility_headline': '3.045+ empresas tiraram a estratégia do PowerPoint',
        'stats': [
            ('92%', 'mais alinhamento entre estratégia e execução'),
            ('70%', 'menos tempo em reuniões de revisão'),
            ('100%', 'das metas auditáveis em tempo real'),
            ('3x', 'velocidade de tomada de decisão'),
        ],
        'pci_headline': 'Quem ganha mais com o <span class="text-primary">Orbit Estratégico</span>',
        'pci_headline_b': 'Quem ganha mais com o <em>Orbit Estratégico</em>',
        'pci_sub': 'CEOs, sócios e diretores que querem estratégia conectada à operação:',
        'pci_items': [
            ('solar:buildings-3-bold-duotone', 'Porte', '<strong>R$ 500k+/mês</strong> e <strong>30+ funcionários</strong>.'),
            ('solar:document-text-bold-duotone', 'Plano no PowerPoint', 'Planejamento de <strong>80 páginas</strong> que ninguém abre.'),
            ('solar:archive-minimalistic-bold-duotone', 'SWOT arquivado', 'SWOT feito <strong>uma vez por ano</strong> e esquecido.'),
            ('solar:calculator-minimalistic-bold-duotone', 'BSC em planilha', 'BSC vira <strong>Excel quebrado</strong> que ninguém atualiza.'),
            ('solar:routing-bold-duotone', 'Plano sem execução', 'Estratégia não <strong>chega na tarefa</strong> do colaborador.'),
            ('solar:graph-up-bold-duotone', 'Sem visão competitiva', 'Não conhece <strong>concorrência</strong> em profundidade.'),
        ],
        'anti_target': [
            ('solar:user-linear', 'Microempresa, MEI — Orbit é overkill.'),
            ('solar:server-square-cloud-linear', 'Empresa que já tem consultoria estratégica fixa rodando.'),
            ('solar:document-text-linear', 'Quem só quer SWOT para sócios — não é o foco.'),
        ],
        'benefits_headline': 'O que muda quando a estratégia <span class="text-primary">é viva</span>',
        'benefits_headline_b': 'O que muda quando a estratégia <em>é viva</em>',
        'benefits': [
            ('solar:routing-bold-duotone', 'BSC conectado à tarefa', 'Cada meta do BSC liga a um projeto e uma tarefa real.', 'O Balanced Scorecard sai do PowerPoint e vive na plataforma. Cada objetivo financeiro, cliente, processo ou aprendizado puxa projetos e tarefas que aparecem no dia-a-dia do time.'),
            ('solar:target-bold-duotone', 'OKR trimestral auditável', 'Defina, acompanhe e ajuste OKRs com histórico completo.', 'Reunião trimestral deixa de ser "estamos bem?" e vira "atingimos 87% do KR1 com essas 3 iniciativas". Tudo gravado, tudo auditável.'),
            ('solar:magnifer-zoom-in-bold-duotone', 'Inteligência de mercado com IA', 'Olívia analisa concorrência e oportunidades automaticamente.', 'Aponte um concorrente e a IA traz posicionamento, preços, principais movimentos e oportunidades para você. Sem precisar contratar consultoria de mercado.'),
            ('solar:branching-paths-up-bold-duotone', 'Conectado com Financeiro, CRM, RH', 'Estratégia conversa com receita, pipeline e headcount.', 'Meta de crescer 30%? O sistema mostra se o pipeline (CRM), o caixa (Financeiro) e a estrutura (RH) sustentam. Sem planilhas paralelas.'),
        ],
        'steps_headline': 'Estratégia <span class="text-primary">viva</span> em 3 passos',
        'steps_headline_b': 'Estratégia <em>viva</em> em 3 passos',
        'steps_sub': 'Estruturação guiada pela equipe Orbit + agente IA Estrategista.',
        'steps': [
            ('01', 'Semana 1', 'Diagnóstico', 'Mapeamos missão, visão, SWOT atual e contextualizamos o cenário competitivo da sua empresa.'),
            ('02', 'Semana 2', 'Setup BSC + OKR', 'Configuramos os 4 quadrantes do BSC, conectamos objetivos a projetos e definimos OKRs do trimestre.'),
            ('03', 'Semanas 3-4', 'Go-live', 'Time treinado, diretoria começa a usar nas reuniões mensais. Olívia gera relatórios automáticos.'),
        ],
        'compare_headline': 'Por que sair de <span class="text-primary">PowerPoint + Excel</span> de BSC',
        'compare_headline_b': 'Por que sair de <em>PowerPoint + Excel</em> de BSC',
        'compare_sub': 'Estratégia em arquivos mortos não muda o resultado da empresa.',
        'compare_rows': [
            ('solar:document-text-bold-duotone', 'Plano estratégico em PowerPoint', '80 páginas · ninguém abre · empoeirado', 'BSC vivo conectado a projetos', 'Estratégia chega na tarefa do colab'),
            ('solar:calculator-minimalistic-bold-duotone', 'BSC em planilha Excel', 'Fórmula quebra · ninguém atualiza', 'BSC nativo com indicadores vivos', 'Sem briga de fórmula'),
            ('solar:archive-minimalistic-bold-duotone', 'SWOT feito 1x por ano', 'Arquivado · ninguém revisita', 'SWOT acompanhado trimestralmente', 'Cenário sempre atualizado'),
            ('solar:user-id-bold-duotone', 'Consultoria estratégica externa', 'Cara · termina e tudo volta', 'Olívia + agente IA Estrategista', 'Capacidade interna permanente'),
            ('solar:eye-closed-bold-duotone', 'Análise de concorrência manual', 'Subjetiva · desatualizada', 'IA analisa mercado automaticamente', 'Decisão competitiva com dado'),
        ],
        'compare_foot': '<strong class="text-primary font-extrabold">Estratégia auditável conectada à operação</strong> = velocidade de decisão multiplicada por 3.',
        'faqs': [
            ('Preciso de consultor estratégico pra usar?', 'Não. O Orbit estrutura BSC, OKR e SWOT com templates BR e o agente IA Estrategista te guia em cada etapa. Mas se quiser usar com sua consultoria, ela ganha plataforma de entrega.'),
            ('Funciona pra empresa familiar?', 'Sim — funciona MELHOR pra empresa familiar com sócios, porque o BSC força conversa estruturada sobre objetivos comuns. Vários clientes Orbit usam justamente pra alinhar conselho.'),
            ('Substitui BSC institucional tipo BSC Designer?', 'Sim e mais — substitui BSC Designer + ferramenta de OKR + planilha de SWOT, e conecta com o resto da gestão da empresa.'),
            ('Quanto tempo até ver resultado?', 'Primeiro ciclo trimestral (90 dias) você já tem reunião de revisão estratégica baseada em dado, não em feeling.'),
            ('Posso usar com BSC já feito?', 'Sim. Importamos seu BSC atual (Excel ou PowerPoint) no setup. Você não recomeça do zero.'),
            ('Quanto custa?', 'Faixa típica do ICP (R$ 500k+/30+): <strong>R$ 1.500 a R$ 4.500/mês</strong> para a plataforma toda (não só Estratégico). Fale com a Olívia para estimativa.'),
        ],
        'cta_final_h': 'Pronto para tirar a <span class="text-primary">estratégia do PowerPoint?</span>',
        'cta_final_h_b': 'Pronto para tirar a <em>estratégia do PowerPoint?</em>',
        'cta_final_sub': 'Fale com a Olívia agora — em 2 minutos ela entende seu cenário e agenda demo do BSC ao vivo.',
        'cta_final_micro': 'Sem cartão. Sem cadastro. Só uma conversa de 2 minutos.',
    },

    'indicadores': {
        'label': 'Indicadores',
        'image_available': False,
        'placeholder_icon': 'solar:chart-2-bold-duotone',
        'meta': {
            'title': 'Dashboard de KPIs para Empresas | Orbit Gestão',
            'description': 'KPIs em tempo real, conectores nativos, causa raiz com IA. Para empresas R$ 500k+/mês e 30+ funcionários.',
            'keywords': 'dashboard KPI empresa, software de indicadores empresariais, BI para PME, KPI dashboard online',
            'og_title': 'Orbit Indicadores — KPIs em tempo real, sem Power BI',
            'og_description': 'Painel único da empresa em tempo real. Decisão baseada em dado, não em feeling.',
        },
        'hero_a_h1': '<span class="text-primary">KPIs vivos</span>. Decisão por dado, não por feeling.',
        'hero_a_sub': 'Painel único da empresa com conectores nativos pros módulos internos (Financeiro, CRM, RH, Processos). Sem ETL, sem Power BI separado, sem analista intermediando.',
        'hero_b_h1': 'Direção que decide por <em>feeling</em> perde para quem decide por dado.',
        'hero_b_sub': 'Painel único da empresa com conectores nativos pros módulos internos (Financeiro, CRM, RH, Processos). Sem ETL, sem Power BI separado, sem analista intermediando.',
        'credibility_headline': '3.045+ empresas pararam de discutir "qual é o número real"',
        'stats': [
            ('22+', 'KPIs prontos no ambiente médio'),
            ('100%', 'fonte única da verdade'),
            ('80%', 'menos tempo em reuniões discutindo número'),
            ('3x', 'velocidade de identificar causa raiz'),
        ],
        'pci_headline': 'Quem ganha mais com o <span class="text-primary">Orbit Indicadores</span>',
        'pci_headline_b': 'Quem ganha mais com o <em>Orbit Indicadores</em>',
        'pci_sub': 'CEOs, CFOs e diretores que querem decisão baseada em dado, não em planilha desatualizada:',
        'pci_items': [
            ('solar:buildings-3-bold-duotone', 'Porte', '<strong>R$ 500k+/mês</strong> e <strong>30+ funcionários</strong>.'),
            ('solar:document-medicine-bold-duotone', 'Cada área com sua planilha', 'Marketing, vendas, financeiro — cada um <strong>com sua planilha</strong>.'),
            ('solar:chat-square-call-bold-duotone', 'Reunião por número', 'Reunião começa discutindo <strong>qual é o número real</strong>.'),
            ('solar:lightbulb-bolt-bold-duotone', 'Decisão no feeling', 'Direção decide <strong>no achismo</strong> e descobre erro tarde.'),
            ('solar:server-square-cloud-bold-duotone', 'Power BI caro demais', 'Power BI separado + analista + ETL = <strong>caro e lento</strong>.'),
            ('solar:eye-bold-duotone', 'Falta causa raiz', 'KPI caiu — <strong>ninguém sabe explicar</strong> por quê.'),
        ],
        'anti_target': [
            ('solar:user-linear', 'Microempresa — Excel ainda dá conta.'),
            ('solar:server-square-cloud-linear', 'Empresa com BI corporativo (Tableau, Looker) maduro.'),
            ('solar:graph-up-linear', 'Quem só quer dashboard de marketing — usa GA4 + Looker Studio.'),
        ],
        'benefits_headline': 'O painel da empresa <span class="text-primary">em tempo real</span>',
        'benefits_headline_b': 'O painel da empresa <em>em tempo real</em>',
        'benefits': [
            ('solar:chart-2-bold-duotone', 'KPIs com causa raiz', 'Cada KPI mostra o porquê, não só o número.', 'Olívia analisa o histórico do KPI e identifica fatores correlacionados. "Receita caiu 15%? Foi queda em 2 clientes do segmento X." Dado contextualizado, não só gráfico.'),
            ('solar:server-square-cloud-bold-duotone', 'Conectores nativos · sem ETL', 'Financeiro, CRM, RH, Processos puxam dados nativamente.', 'Os módulos internos do Orbit já alimentam o painel. Sem Zapier, sem ETL externo, sem precisar exportar CSV semanal. Conexão também com sistemas externos via API.'),
            ('solar:bell-bing-bold-duotone', 'Alertas inteligentes', 'KPI fora da meta? Diretor recebe alerta com hipótese de causa.', 'Não precisa olhar dashboard todo dia. Quando algo sai do padrão, alerta com contexto. Direção foca em ação, não em monitoramento.'),
            ('solar:document-add-bold-duotone', 'Importação de planilha', 'Para o que não é nativo, importa planilha e tem KPI vivo.', 'Tem fonte de dado fora dos módulos Orbit (ex: e-commerce externo)? Importa CSV ou conecta API. O KPI fica disponível no painel global.'),
        ],
        'steps_headline': 'Painel único em <span class="text-primary">3 passos</span>',
        'steps_headline_b': 'Painel único em <em>3 passos</em>',
        'steps_sub': 'Modelagem dos KPIs prioritários guiada pela equipe Orbit.',
        'steps': [
            ('01', 'Semana 1', 'Mapeamento', 'Mapeamos os KPIs prioritários por área e identificamos fontes (módulos Orbit + sistemas externos).'),
            ('02', 'Semana 2', 'Setup conectores', 'Configuramos os conectores nativos e importamos planilhas legacy. Olívia aprende padrões.'),
            ('03', 'Semana 3', 'Go-live', 'Painel ao vivo. Diretoria usa nas reuniões. Alertas configurados por meta.'),
        ],
        'compare_headline': 'Por que sair de <span class="text-primary">Power BI + Excel</span> separados',
        'compare_headline_b': 'Por que sair de <em>Power BI + Excel</em> separados',
        'compare_sub': 'Cada área com sua versão da verdade = nenhuma versão da verdade.',
        'compare_rows': [
            ('solar:document-medicine-bold-duotone', 'Excel separado por área', 'Cada área com sua planilha · ninguém bate', 'Painel único · fonte única', 'Reunião sem discutir número'),
            ('solar:server-square-cloud-bold-duotone', 'Power BI + ETL + analista', 'Caro · lento · dependência total do analista', 'Conectores nativos · 22+ KPIs prontos', '60% menos custo · setup em 3 semanas'),
            ('solar:chart-square-bold-duotone', 'Google Data Studio / Looker', 'Conector limitado · sem causa raiz', 'IA explica desvios automaticamente', 'Decisão com contexto'),
            ('solar:bell-bold-duotone', 'Sem alerta proativo', 'KPI caiu · descobre 2 semanas depois', 'Alertas inteligentes por meta', 'Ação antes de virar crise'),
            ('solar:database-bold-duotone', 'BI desconectado da operação', 'KPI bonito · operação não muda', 'KPI puxa projeto/tarefa direta', 'Insight vira ação'),
        ],
        'compare_foot': '<strong class="text-primary font-extrabold">Fonte única da verdade + IA de causa raiz</strong> = direção tomando decisão por dado, não por feeling.',
        'faqs': [
            ('Conecta com Power BI ou só substitui?', 'Funciona dos dois jeitos. Você pode exportar pra Power BI se já tem painel maduro, ou usar o Orbit como painel único e desativar o BI externo.'),
            ('Quais KPIs vêm prontos?', 'Mais de 22 KPIs no ambiente médio: financeiros (DRE, margem, runway), comerciais (taxa conversão, CAC, LTV), de marketing (CPL, CTR, CPA), operacionais (SLA, tempo de ciclo, NPS) e de RH (turnover, eNPS).'),
            ('Conecta com nosso ERP?', 'Sim. Conectores nativos com Omie, ContaAzul, Sankhya, TOTVS, SAP B1, Senior. Para outros sistemas, via API REST ou importação CSV.'),
            ('Funciona em mobile?', 'Sim. App iOS/Android com os KPIs principais e alertas push.'),
            ('Posso compartilhar com investidor / conselho?', 'Sim. Permissões por usuário e link compartilhável de painel específico (read-only).'),
            ('Quanto custa?', 'Faixa típica do ICP: <strong>R$ 1.500 a R$ 4.500/mês</strong> para a plataforma toda. Fale com a Olívia para estimativa do seu cenário.'),
        ],
        'cta_final_h': 'Pronto para parar de <span class="text-primary">decidir no feeling?</span>',
        'cta_final_h_b': 'Pronto para parar de <em>decidir no feeling?</em>',
        'cta_final_sub': 'Fale com a Olívia agora — ela mapeia seus KPIs prioritários em 2 minutos e agenda demo do painel.',
        'cta_final_micro': 'Sem cartão. Sem instalação. Só uma conversa.',
    },

    'processos': {
        'label': 'Processos',
        'image_available': False,
        'placeholder_icon': 'solar:branching-paths-up-bold-duotone',
        'meta': {
            'title': 'Software BPM e Mapeamento de Processos | Orbit Gestão',
            'description': 'Processos vivos, ISO 9001 ready, agente IA que cria fluxo automaticamente. Para empresas R$ 500k+/mês e 30+ funcionários.',
            'keywords': 'software BPM, mapeamento de processos software, software ISO 9001, BPMN online, gestão de processos',
            'og_title': 'Orbit Processos — processos vivos, não manuais em PDF',
            'og_description': 'Processo vivo, auditável, conectado ao operacional. Agente IA cria o processo a partir de descrição.',
        },
        'hero_a_h1': 'Processo <span class="text-primary">vivo</span>. Não manual em PDF.',
        'hero_a_sub': 'Mapeamento, padronização e documentação de processos com agente IA. Cadeia de valor, instruções de trabalho e ciclo de vida da informação — tudo conectado ao operacional.',
        'hero_b_h1': 'Sua empresa depende de <em>gente ou de processo?</em>',
        'hero_b_sub': 'Mapeamento, padronização e documentação de processos com agente IA. Cadeia de valor, instruções de trabalho e ciclo de vida da informação — tudo conectado ao operacional.',
        'credibility_headline': '3.045+ empresas pararam de depender da memória das pessoas',
        'stats': [
            ('40%', 'menos tempo de processos manuais'),
            ('85%', 'menos erros de execução'),
            ('100%', 'auditável para ISO 9001'),
            ('3x', 'velocidade de onboarding de novo colab'),
        ],
        'pci_headline': 'Quem ganha mais com o <span class="text-primary">Orbit Processos</span>',
        'pci_headline_b': 'Quem ganha mais com o <em>Orbit Processos</em>',
        'pci_sub': 'Diretores de operações e qualidade de empresas que querem escalar sem caos:',
        'pci_items': [
            ('solar:buildings-3-bold-duotone', 'Porte', '<strong>R$ 500k+/mês</strong> e <strong>30+ funcionários</strong>.'),
            ('solar:users-group-rounded-bold-duotone', 'Conhecimento nas pessoas', 'Quando alguém sai, <strong>o processo sai junto</strong>.'),
            ('solar:document-text-bold-duotone', 'Manual em PDF', 'Processo documentado em <strong>PDF que ninguém lê</strong>.'),
            ('solar:shield-warning-bold-duotone', 'Auditoria ISO', 'Auditoria ISO mostra processo <strong>não documentado</strong>.'),
            ('solar:branching-paths-up-bold-duotone', 'Erros se repetem', 'Erro acontece <strong>todo mês</strong> · ninguém corrige a raiz.'),
            ('solar:user-plus-bold-duotone', 'Onboarding lento', 'Colab novo leva <strong>2 meses</strong> pra entender como faz.'),
        ],
        'anti_target': [
            ('solar:user-linear', 'Microempresa com 1 dono que executa tudo.'),
            ('solar:server-square-cloud-linear', 'Empresa com BPM enterprise (Bizagi, Camunda) maduro.'),
            ('solar:document-text-linear', 'Quem só quer SOP — sem necessidade de mapa de valor.'),
        ],
        'benefits_headline': 'O conhecimento vira <span class="text-primary">ativo da empresa</span>',
        'benefits_headline_b': 'O conhecimento vira <em>ativo da empresa</em>',
        'benefits': [
            ('solar:magic-stick-3-bold-duotone', 'Agente IA cria processo', 'Descreva o processo. Agente IA monta fluxograma.', 'Você descreve em texto livre ("o cliente liga, vendedor anota no CRM, gerente aprova proposta..."). O agente IA Processos monta o fluxograma BPMN completo, com etapas, responsáveis e gatilhos.'),
            ('solar:branching-paths-up-bold-duotone', 'Cadeia de valor visual', 'Veja a empresa inteira em um mapa.', 'Cadeia de valor nativa mostra como os processos se conectam: vendas → projetos → produção → entrega → suporte. Identifica gargalo na hora.'),
            ('solar:document-add-bold-duotone', 'Instruções de trabalho', 'Cada etapa vira instrução passo-a-passo.', 'O processo gera Instruções de Trabalho (IT) automaticamente. Colab novo abre o processo e vê o que fazer. Sem manual de 80 páginas em PDF.'),
            ('solar:chart-2-bold-duotone', 'Conectado a Indicadores', 'KPI do processo medido automaticamente.', 'Cada processo tem KPIs de performance (tempo de ciclo, taxa de erro, satisfação). Os indicadores rolam direto pro painel de Indicadores — sem planilha intermediária.'),
        ],
        'steps_headline': 'Conhecimento documentado em <span class="text-primary">3 semanas</span>',
        'steps_headline_b': 'Conhecimento documentado em <em>3 semanas</em>',
        'steps_sub': 'Equipe Orbit + agente IA Processos mapeiam sua operação rapidamente.',
        'steps': [
            ('01', 'Semana 1', 'Diagnóstico', 'Identificamos os processos críticos da empresa e quem os domina hoje.'),
            ('02', 'Semana 2', 'Mapeamento com IA', 'Agente IA Processos entrevista os donos do conhecimento e gera fluxogramas.'),
            ('03', 'Semana 3', 'Validação + Go-live', 'Time valida, ajusta, e a documentação vira oficial. Onboarding novo já usa.'),
        ],
        'compare_headline': 'Por que sair de <span class="text-primary">PDF + Wiki</span> bagunçado',
        'compare_headline_b': 'Por que sair de <em>PDF + Wiki</em> bagunçado',
        'compare_sub': 'Conhecimento espalhado em PDF, Notion e cabeças = conhecimento perdido.',
        'compare_rows': [
            ('solar:document-text-bold-duotone', 'Manual em PDF', 'Ninguém abre · desatualiza · auditoria reprova', 'Processo vivo com IT auto-gerada', 'ISO ready · usado de verdade'),
            ('solar:users-group-rounded-bold-duotone', 'Conhecimento na cabeça do colab', 'Sai · processo some · empresa para', 'Mapeado · auditável · transferível', 'Independência de pessoa'),
            ('solar:notebook-bold-duotone', 'Notion / Wiki bagunçado', 'Sem padrão · sem hierarquia · perdido', 'Estrutura BPM padronizada', 'Onboarding 3x mais rápido'),
            ('solar:magic-stick-3-bold-duotone', 'Mapeamento por consultor', 'Caro · demorado · não atualiza depois', 'Agente IA Processos contínuo', '60% menos custo · sempre atual'),
            ('solar:chart-2-bold-duotone', 'KPI de processo em planilha', 'Cálculo manual · ninguém vê', 'KPI automático no painel', 'Gargalo identificado na hora'),
        ],
        'compare_foot': '<strong class="text-primary font-extrabold">Processo vivo + IA + ISO ready</strong> = empresa escala sem caos.',
        'faqs': [
            ('Funciona pra empresa que quer ISO 9001?', 'Sim. A estrutura nativa de Processos atende os requisitos da ISO 9001:2015 (mapa de processo, instrução de trabalho, controle de documentos, indicador). Vários clientes Orbit certificaram com a plataforma.'),
            ('Substitui Bizagi ou Camunda?', 'Para 90% das PMEs B2B, sim. Para empresas com BPM enterprise crítico (fluxo automatizado complexo, milhares de instâncias/dia), o Orbit complementa — não substitui.'),
            ('O agente IA realmente mapeia processo?', 'Sim. A IA conduz entrevista com o dono do conhecimento (estilo "me conta como você faz X") e gera o fluxograma BPMN. Você revisa e ajusta. Reduz tempo de mapeamento em 70%.'),
            ('Como faço o time usar de verdade?', 'O processo é o ponto de partida das tarefas. Quando uma tarefa é criada no módulo de Tarefas, ela já vem com a Instrução de Trabalho do processo correspondente. Difícil não usar.'),
            ('Exporta pra documento Word/PDF?', 'Sim. Você gera PDF ou Word do processo, da instrução de trabalho, do mapa de cadeia de valor — pronto pra auditoria.'),
            ('Quanto custa?', 'Faixa típica do ICP: <strong>R$ 1.500 a R$ 4.500/mês</strong> para a plataforma toda. Fale com a Olívia para estimativa.'),
        ],
        'cta_final_h': 'Pronto para parar de depender da <span class="text-primary">memória das pessoas?</span>',
        'cta_final_h_b': 'Pronto para parar de depender da <em>memória das pessoas?</em>',
        'cta_final_sub': 'Fale com a Olívia agora — ela mapeia seu processo crítico em 2 minutos e agenda demo do BPM.',
        'cta_final_micro': 'Sem cartão. Sem instalação. Só uma conversa.',
    },

    'pessoas': {
        'label': 'Pessoas',
        'image_available': False,
        'placeholder_icon': 'solar:users-group-two-rounded-bold-duotone',
        'meta': {
            'title': 'Software de RH para Empresa Média | Orbit Gestão',
            'description': 'RH completo em uma plataforma: cargos, PDI, treinamento, organograma, ATS. Para empresas R$ 500k+/mês e 30+ funcionários.',
            'keywords': 'software RH empresa média, sistema RH 50 funcionários, ATS recrutamento, software PDI, organograma online',
            'og_title': 'Orbit Pessoas — RH médio porte numa plataforma só',
            'og_description': 'Substitui Gupy + Kenoby + BambooHR + LMS. Cargos, PDI, treinamento e recrutamento em um lugar.',
        },
        'hero_a_h1': '<span class="text-primary">RH médio porte</span> numa plataforma só.',
        'hero_a_sub': 'Cargos, PDI, treinamento (LMS), organograma multi-modo e ATS de recrutamento — tudo em uma plataforma. Sem Gupy + Kenoby + BambooHR + LMS separados.',
        'hero_b_h1': 'A planilha do RH virou <em>meme</em> na sua empresa?',
        'hero_b_sub': 'Cargos, PDI, treinamento (LMS), organograma multi-modo e ATS de recrutamento — tudo em uma plataforma. Sem Gupy + Kenoby + BambooHR + LMS separados.',
        'credibility_headline': '3.045+ empresas tiraram o RH da planilha',
        'stats': [
            ('88%', 'mais engajamento em PDI'),
            ('40%', 'menos tempo em recrutamento'),
            ('92%', 'colaboradores treinados no microlearning'),
            ('100%', 'organograma sempre atualizado'),
        ],
        'pci_headline': 'Quem ganha mais com o <span class="text-primary">Orbit Pessoas</span>',
        'pci_headline_b': 'Quem ganha mais com o <em>Orbit Pessoas</em>',
        'pci_sub': 'Diretores de RH e fundadores de empresas que cresceram de 15 pra 50+ pessoas:',
        'pci_items': [
            ('solar:buildings-3-bold-duotone', 'Porte', '<strong>R$ 500k+/mês</strong> e <strong>30+ funcionários</strong>.'),
            ('solar:document-medicine-bold-duotone', 'RH no Excel', 'Cadastro de colab, cargo, salário tudo <strong>em planilha</strong>.'),
            ('solar:users-group-rounded-bold-duotone', 'Sem organograma vivo', 'Organograma <strong>desatualizado</strong> ou inexistente.'),
            ('solar:routing-bold-duotone', 'Sem PDI estruturado', 'Avaliação de desempenho é <strong>conversa solta</strong>.'),
            ('solar:square-academic-cap-bold-duotone', 'Treinamento ad-hoc', 'Não tem trilha de <strong>microlearning</strong>.'),
            ('solar:user-plus-bold-duotone', 'Recrutamento manual', 'Vagas no LinkedIn + e-mail + planilha = <strong>caos</strong>.'),
        ],
        'anti_target': [
            ('solar:user-linear', 'Empresa com menos de 15 funcionários — Excel ainda dá conta.'),
            ('solar:server-square-cloud-linear', 'Empresa enterprise com SAP SuccessFactors / Workday.'),
            ('solar:document-text-linear', 'Quem só quer ATS de recrutamento — usa Gupy puro.'),
        ],
        'benefits_headline': 'Do recrutamento ao <span class="text-primary">desenvolvimento</span>',
        'benefits_headline_b': 'Do recrutamento ao <em>desenvolvimento</em>',
        'benefits': [
            ('solar:user-plus-bold-duotone', 'ATS de recrutamento nativo', 'Vagas, candidatos, entrevistas e portal público.', 'Cadastre vaga, gere portal de candidatura, receba currículos no banco. Entrevistadores avaliam pela plataforma. Banco de talentos sempre vivo. Sem Gupy/Kenoby separados.'),
            ('solar:square-academic-cap-bold-duotone', 'Treinamento via WhatsApp', 'Microlearning diário no celular do colab.', 'Agente IA Treinamento envia conteúdo curto via WhatsApp, faz quiz e mede engajamento. Trilha por cargo e nível. 92% dos colabs engajam.'),
            ('solar:routing-bold-duotone', 'PDI conectado a cargo', 'Plano de desenvolvimento individual baseado em skills.', 'Cada cargo tem skills requeridas. PDI identifica gaps do colab e sugere trilha (curso, projeto, mentoria). Avaliação 360 nativa.'),
            ('solar:hierarchy-square-2-bold-duotone', 'Organograma multi-modo', 'Hierárquico, funcionograma, departamental, combinado.', 'Veja a empresa de 4 jeitos diferentes: hierarquia, função, departamento ou combinado. Atualiza automático quando muda alguém. Sem PowerPoint que envelhece.'),
        ],
        'steps_headline': 'RH integrado em <span class="text-primary">3 semanas</span>',
        'steps_headline_b': 'RH integrado em <em>3 semanas</em>',
        'steps_sub': 'Importamos seu cadastro de colaboradores e estruturamos cargos e PDI.',
        'steps': [
            ('01', 'Semana 1', 'Importação', 'Importamos cadastro de colaboradores, cargos atuais e estrutura organizacional.'),
            ('02', 'Semana 2', 'Estruturação', 'Definimos skills por cargo, configuramos PDI, trilhas de treinamento e portal de vagas.'),
            ('03', 'Semana 3', 'Go-live', 'Time treinado. RH começa a usar para avaliação, recrutamento e desenvolvimento.'),
        ],
        'compare_headline': 'Por que sair de <span class="text-primary">Excel + Gupy + Kenoby + LMS</span>',
        'compare_headline_b': 'Por que sair de <em>Excel + Gupy + Kenoby + LMS</em>',
        'compare_sub': '4 ferramentas separadas, nenhuma conversa. Custo somado > Orbit.',
        'compare_rows': [
            ('solar:document-medicine-bold-duotone', 'Excel de cadastro de colab', 'Desatualiza · ninguém mantém', 'Cadastro centralizado vivo', 'Organograma sempre atual'),
            ('solar:user-plus-bold-duotone', 'Gupy / Kenoby', 'R$ 2k+/mês só ATS · sem PDI', 'ATS nativo com PDI/treinamento', 'Mesma plataforma de tudo'),
            ('solar:square-academic-cap-bold-duotone', 'LMS separado (Voxy, Coursera)', 'Caro · sem trilha por cargo', 'Microlearning via WhatsApp por cargo', '92% engajamento'),
            ('solar:routing-bold-duotone', 'PDI em formulário Google', 'Anual · esquecido · sem ação', 'PDI conectado a cargo e skill', 'Desenvolvimento contínuo'),
            ('solar:hierarchy-square-2-bold-duotone', 'Organograma em PowerPoint', '6 meses desatualizado', 'Multi-modo · atualiza sozinho', 'Sempre verdadeiro'),
        ],
        'compare_foot': '<strong class="text-primary font-extrabold">RH integrado · uma plataforma</strong> = custo somado das 4 ferramentas substituído por 1.',
        'faqs': [
            ('Funciona pra empresa com 30 funcionários?', 'Sim — esse é o sweet spot. Empresas de 30-300 funcionários são o perfil ideal do módulo Pessoas. Acima de 1000, considere SAP SuccessFactors.'),
            ('Tem folha de pagamento?', 'Não. O Orbit faz a gestão de pessoas (cargo, PDI, treinamento, ATS), mas a folha continua no seu sistema atual (Domínio, Senior, Sankhya). Integramos via API.'),
            ('Substitui Gupy?', 'Sim, pro perfil ICP (R$ 500k+/30+). Empresas que abrem 1-5 vagas/mês têm tudo que precisam no Orbit ATS. Acima disso, considere Gupy enterprise.'),
            ('O treinamento via WhatsApp realmente funciona?', '92% dos colabs engajam (vs 30% de LMS tradicional). A IA adapta o nível do conteúdo, manda em horário relevante e mede comprensão via quiz. É o canal que o colab JÁ usa.'),
            ('Posso fazer avaliação 360?', 'Sim. Avaliação 360 nativa: colab avalia pares, gestor, e é avaliado. Olívia consolida e identifica padrões.'),
            ('Quanto custa?', 'Faixa típica do ICP: <strong>R$ 1.500 a R$ 4.500/mês</strong> para a plataforma toda. Fale com a Olívia para estimativa.'),
        ],
        'cta_final_h': 'Pronto para tirar o RH <span class="text-primary">da planilha?</span>',
        'cta_final_h_b': 'Pronto para tirar o RH <em>da planilha?</em>',
        'cta_final_sub': 'Fale com a Olívia agora — ela entende seu time em 2 minutos e agenda demo do ATS + PDI.',
        'cta_final_micro': 'Sem cartão. Sem instalação. Só uma conversa.',
    },

    'projetos': {
        'label': 'Projetos',
        'image_available': False,
        'placeholder_icon': 'solar:layers-bold-duotone',
        'meta': {
            'title': 'Software de Gestão de Projetos para Empresas | Orbit Gestão',
            'description': 'Projetos do plano estratégico à tarefa do colab. Cards, Kanban, Gantt e agente IA. Para empresas R$ 500k+/mês e 30+ funcionários.',
            'keywords': 'software gestão de projetos empresa, PMO software, alternativa Asana, alternativa Monday, gestão de projetos B2B',
            'og_title': 'Orbit Projetos — projetos do plano à tarefa',
            'og_description': 'Conecta projeto a BSC, CRM, Financeiro e RH. Único concorrente brasileiro com integração nativa.',
        },
        'hero_a_h1': 'Projetos do <span class="text-primary">plano estratégico</span> à tarefa do colaborador.',
        'hero_a_sub': 'Cards, Kanban, Lista e Gantt em uma plataforma. Agente IA cria o projeto. Conectado a BSC (Estratégico), CRM (entregáveis a cliente), Financeiro (orçado vs realizado) e RH (alocação).',
        'hero_b_h1': 'Projetos que atrasam <em>às escuras?</em>',
        'hero_b_sub': 'Cards, Kanban, Lista e Gantt em uma plataforma. Agente IA cria o projeto. Conectado a BSC (Estratégico), CRM (entregáveis a cliente), Financeiro (orçado vs realizado) e RH (alocação).',
        'credibility_headline': '3.045+ empresas pararam de descobrir atraso pelo cliente',
        'stats': [
            ('86%', 'projetos entregues no prazo'),
            ('60%', 'menos tempo em reunião de status'),
            ('100%', 'visibilidade do progresso real'),
            ('3x', 'velocidade de setup com IA'),
        ],
        'pci_headline': 'Quem ganha mais com o <span class="text-primary">Orbit Projetos</span>',
        'pci_headline_b': 'Quem ganha mais com o <em>Orbit Projetos</em>',
        'pci_sub': 'Diretores de operações, PMO e gerentes que cansaram de "tá tudo bem" sem dado:',
        'pci_items': [
            ('solar:buildings-3-bold-duotone', 'Porte', '<strong>R$ 500k+/mês</strong> e <strong>30+ funcionários</strong>.'),
            ('solar:document-medicine-bold-duotone', 'Tarefa em planilha', 'Lista de projetos <strong>em Excel</strong> que ninguém mantém.'),
            ('solar:chat-square-call-bold-duotone', 'Status por WhatsApp', '"E aquele projeto?" via grupo no <strong>WhatsApp</strong>.'),
            ('solar:eye-closed-bold-duotone', 'Atraso descoberto tarde', 'Direção descobre atraso quando <strong>cliente reclama</strong>.'),
            ('solar:server-square-cloud-bold-duotone', 'Asana/Monday isolado', 'Tem Asana, mas <strong>não conversa</strong> com financeiro/RH.'),
            ('solar:magic-stick-3-bold-duotone', 'Setup demorado', 'Cada projeto novo é <strong>uma reunião de setup</strong>.'),
        ],
        'anti_target': [
            ('solar:user-linear', 'Empresa com 1 projeto recorrente — Trello dá conta.'),
            ('solar:server-square-cloud-linear', 'Quem tem MS Project enterprise + PMO maduro.'),
            ('solar:document-text-linear', 'Quem só quer Kanban de marketing — usa Trello.'),
        ],
        'benefits_headline': 'PMO conectado <span class="text-primary">à estratégia</span>',
        'benefits_headline_b': 'PMO conectado <em>à estratégia</em>',
        'benefits': [
            ('solar:magic-stick-3-bold-duotone', '"Criar com agente IA"', 'Descreva o objetivo. IA monta o projeto.', 'Você diz "preciso lançar um novo produto em 90 dias". A IA gera escopo, fases, tarefas e estimativas. Você revisa e ajusta. Setup em minutos, não em reunião de horas.'),
            ('solar:layers-bold-duotone', 'Cards, Kanban, Lista, Gantt', 'Visualize do jeito que cada time prefere.', 'Diretor quer Gantt? Tem. Time prefere Kanban? Tem. Cliente externo precisa de Lista? Tem. Tudo a partir do mesmo dado, sem migração entre ferramentas.'),
            ('solar:branching-paths-up-bold-duotone', 'Conectado a BSC, CRM, Financeiro', 'Projeto puxa objetivo estratégico e orçamento.', 'Cada projeto liga a um objetivo do BSC (estratégico), pode ter cliente do CRM (entregáveis), tem orçamento do Financeiro (orçado × realizado) e alocação do RH.'),
            ('solar:bell-bing-bold-duotone', 'Alertas de atraso preditivos', 'Olívia avisa antes do projeto virar crise.', 'A IA analisa progresso, dependências e capacidade do time. Quando detecta risco de atraso, alerta direção com hipótese de causa e sugestão de ação.'),
        ],
        'steps_headline': 'PMO em <span class="text-primary">3 passos</span>',
        'steps_headline_b': 'PMO em <em>3 passos</em>',
        'steps_sub': 'Migramos seus projetos atuais e estruturamos a metodologia.',
        'steps': [
            ('01', 'Semana 1', 'Diagnóstico', 'Mapeamos projetos atuais (Asana/Monday/planilha/Trello) e a metodologia da empresa.'),
            ('02', 'Semana 2', 'Migração + Templates', 'Importamos projetos ativos e configuramos templates por tipo (cliente, interno, estratégico).'),
            ('03', 'Semana 3', 'Go-live', 'Time treinado. Diretor vê status real. Olívia configurada pra alertas.'),
        ],
        'compare_headline': 'Por que sair de <span class="text-primary">Asana + Monday + Trello</span>',
        'compare_headline_b': 'Por que sair de <em>Asana + Monday + Trello</em>',
        'compare_sub': 'Ferramenta de projeto desconectada do resto = projeto bonito, empresa fragmentada.',
        'compare_rows': [
            ('solar:server-square-cloud-bold-duotone', 'Asana / Monday isolado', 'R$ 60/usuário · não integra com Fin/CRM', 'Projetos nativamente integrados', 'Sem Zapier · sem retrabalho'),
            ('solar:document-medicine-bold-duotone', 'Lista de projetos em Excel', 'Desatualiza · sem accountability', 'Visão única atualizada em real-time', 'Status sem perguntar'),
            ('solar:chat-square-call-bold-duotone', 'Status por WhatsApp/reunião', '4h/semana só de status', 'Painel projeto sempre vivo', '60% menos reunião'),
            ('solar:eye-closed-bold-duotone', 'Atraso descoberto tarde', 'Cliente reclama → você descobre', 'IA prediz risco · alerta cedo', 'Ação antes da crise'),
            ('solar:routing-bold-duotone', 'Projeto sem ligação à estratégia', 'Time bate prazo · empresa não cresce', 'Ligado ao BSC (objetivo estratégico)', 'Projeto move ponteiro'),
        ],
        'compare_foot': '<strong class="text-primary font-extrabold">Projetos conectados à estratégia + IA preditiva</strong> = 86% entregues no prazo.',
        'faqs': [
            ('Importa do Asana / Monday / Trello?', 'Sim. Migração guiada pela equipe Orbit. Importamos projetos, tarefas, atribuições e comentários históricos.'),
            ('Substitui MS Project?', 'Pra 90% dos casos B2B, sim. Para projetos de construção pesada com Gantt complexo e dependências críticas, MS Project ainda é melhor — Orbit complementa nesses casos.'),
            ('Tem Gantt?', 'Sim. Gantt com dependências, marcos e baseline. Visualização timeline e calendário também.'),
            ('Como funciona "Criar com agente IA"?', 'Você descreve o projeto em linguagem natural ("lançar nova feature X em 60 dias"). A IA propõe escopo, fases, tarefas, responsáveis e estimativas baseado em projetos similares. Você revisa e ajusta.'),
            ('Funciona pra projeto com cliente externo (entregável)?', 'Sim. Modo cliente: o lead do CRM vira projeto, com entregáveis, milestones e acesso controlado pro cliente acompanhar.'),
            ('Quanto custa?', 'Faixa típica do ICP: <strong>R$ 1.500 a R$ 4.500/mês</strong> para a plataforma toda (não cobra por usuário). Fale com a Olívia para estimativa.'),
        ],
        'cta_final_h': 'Pronto para parar de descobrir atraso <span class="text-primary">pelo cliente?</span>',
        'cta_final_h_b': 'Pronto para parar de descobrir atraso <em>pelo cliente?</em>',
        'cta_final_sub': 'Fale com a Olívia agora — ela entende seus projetos críticos em 2 minutos e agenda demo do PMO.',
        'cta_final_micro': 'Sem cartão. Sem instalação. Só uma conversa.',
    },

    'canal-orbit': {
        'label': 'Canal Orbit',
        'image_available': False,
        'placeholder_icon': 'solar:hand-shake-bold-duotone',
        'meta': {
            'title': 'Plataforma White-label para Consultorias | Canal Orbit',
            'description': 'Escale sua consultoria sem contratar. Plataforma white-label com IA, recorrência e acesso direto ao cliente. Para consultorias R$ 100k+/mês.',
            'keywords': 'plataforma para consultoria empresarial, software para consultor, consultoria white label, plataforma BPM consultoria, recorrência consultoria',
            'og_title': 'Canal Orbit — sua consultoria entrega 3x mais valor',
            'og_description': 'Plataforma white-label para consultorias R$ 100k+/mês. Agentes de IA, recorrência embutida, acesso direto à operação do cliente.',
        },
        'hero_a_h1': 'Sua consultoria entrega <span class="text-primary">3x mais valor</span> com o mesmo time.',
        'hero_a_sub': 'Plataforma white-label onde seu cliente faz BSC, processos e indicadores na sua marca. Agentes de IA inclusos. Modelo de recorrência embutido.',
        'hero_b_h1': 'Sua margem despenca com <em>cada cliente novo?</em>',
        'hero_b_sub': 'Plataforma white-label onde seu cliente faz BSC, processos e indicadores na sua marca. Agentes de IA inclusos. Modelo de recorrência embutido.',
        'credibility_headline': '+25 consultorias escalaram com o Canal Orbit',
        'stats': [
            ('3x', 'valor entregue com o mesmo time'),
            ('40%', 'aumento de margem por cliente'),
            ('100%', 'recorrência mensal embutida'),
            ('60%', 'menos tempo em entregáveis manuais'),
        ],
        'pci_headline': 'Quem ganha mais com o <span class="text-primary">Canal Orbit</span>',
        'pci_headline_b': 'Quem ganha mais com o <em>Canal Orbit</em>',
        'pci_sub': 'Sócios de consultoria empresarial que querem escalar sem contratar:',
        'pci_items': [
            ('solar:buildings-3-bold-duotone', 'Porte da consultoria', 'Sua consultoria fatura <strong>R$ 100k+/mês</strong>.'),
            ('solar:users-group-rounded-bold-duotone', 'Escala via headcount', 'Mais cliente = mais consultor = <strong>margem cai</strong>.'),
            ('solar:document-medicine-bold-duotone', 'Entrega em PowerPoint', 'Cliente recebe slide e PDF · <strong>não acessa nada</strong>.'),
            ('solar:routing-bold-duotone', 'Pontual, não recorrente', 'Modelo de projeto pontual · <strong>sem recorrência</strong>.'),
            ('solar:eye-closed-bold-duotone', 'Sem acesso ao cliente', 'Você opera <strong>às escuras</strong> entre reuniões.'),
            ('solar:cpu-bolt-bold-duotone', 'Cliente quer digital', 'Cliente reclama: "quero plataforma, não <strong>PDF</strong>".'),
        ],
        'anti_target': [
            ('solar:user-linear', 'Consultor solo iniciante — Orbit é overkill.'),
            ('solar:server-square-cloud-linear', 'Big4 (Deloitte, EY, KPMG, PwC) com plataformas próprias.'),
            ('solar:graph-up-linear', 'Quem só vende treinamento — não é nosso foco.'),
        ],
        'benefits_headline': 'A plataforma <span class="text-primary">como ferramenta</span> da sua consultoria',
        'benefits_headline_b': 'A plataforma <em>como ferramenta</em> da sua consultoria',
        'benefits': [
            ('solar:palette-bold-duotone', 'White-label nativo', 'Sua marca, suas cores, seu domínio.', 'O cliente acessa numa URL sua (clientes.suaconsultoria.com.br) com sua marca. Não vê "Orbit" em lugar nenhum. Ferramenta é sua, customer success é seu, recorrência é sua.'),
            ('solar:magic-stick-3-bold-duotone', '7 agentes IA inclusos', 'Estrategista, Processos, Indicadores, Pessoas...', 'Cada consultor seu opera 3x mais clientes porque os agentes IA fazem o trabalho repetitivo: mapear processo, montar BSC, analisar KPI. Consultor foca em estratégia, não em entregável.'),
            ('solar:wallet-money-bold-duotone', 'Recorrência embutida', 'Cliente paga assinatura mensal automaticamente.', 'Sai do modelo "projeto de 6 meses → silêncio". Cliente paga assinatura mensal pra você. Você entrega valor contínuo via plataforma. MRR previsível, churn auditável.'),
            ('solar:eye-bold-duotone', 'Acesso direto à operação', 'Você vê o dia-a-dia do cliente, não só na reunião.', 'Entre encontros, você acompanha pelo painel: o cliente está usando? Atingindo metas? Em qual gargalo? Sem precisar reagendar pra entender contexto.'),
        ],
        'steps_headline': 'Sua consultoria escala em <span class="text-primary">4 semanas</span>',
        'steps_headline_b': 'Sua consultoria escala em <em>4 semanas</em>',
        'steps_sub': 'Setup white-label e treinamento do seu time de consultores.',
        'steps': [
            ('01', 'Semanas 1-2', 'Setup white-label', 'Customizamos cores, logo, domínio, e seu portfólio de entregáveis na plataforma.'),
            ('02', 'Semana 3', 'Treinamento consultor', 'Seu time aprende a operar plataforma e usar os 7 agentes IA.'),
            ('03', 'Semana 4', 'Onboarding primeiro cliente', 'Migramos seu primeiro cliente, com sua marca, em produção real.'),
        ],
        'compare_headline': 'Por que sair do <span class="text-primary">modelo PowerPoint</span>',
        'compare_headline_b': 'Por que sair do <em>modelo PowerPoint</em>',
        'compare_sub': 'Consultoria que escala via headcount = margem que cai a cada cliente.',
        'compare_rows': [
            ('solar:document-text-bold-duotone', 'Entrega em PowerPoint + PDF', 'Cliente arquiva · não usa · não percebe valor', 'Plataforma viva white-label', 'Valor percebido contínuo'),
            ('solar:users-group-rounded-bold-duotone', 'Mais cliente = mais consultor', 'Margem despenca a cada cliente novo', 'IA opera o trabalho repetitivo', '3x mais clientes · mesmo time'),
            ('solar:wallet-money-bold-duotone', 'Projeto pontual de 6 meses', 'Pico de receita · depois silêncio', 'Recorrência mensal embutida', 'MRR previsível · churn medido'),
            ('solar:eye-closed-bold-duotone', 'Cliente entre reuniões', 'Você opera às escuras', 'Painel sempre disponível', 'Diagnóstico contínuo'),
            ('solar:branching-paths-up-bold-duotone', 'Stack do cliente fragmentada', 'Você não controla as ferramentas', 'Plataforma única white-label', 'Ecossistema seu'),
        ],
        'compare_foot': '<strong class="text-primary font-extrabold">Plataforma + IA + recorrência</strong> = consultoria com unit economics de SaaS.',
        'faqs': [
            ('White-label é total mesmo?', 'Sim. Você define cores, logo, domínio, nome dos módulos, copy. Cliente acessa em URL sua (ex: clientes.suaconsultoria.com.br) e não vê "Orbit" em lugar nenhum. A plataforma é "sua".'),
            ('Como funciona a precificação para meu cliente?', 'Você define. Modelo recomendado: assinatura mensal por cliente (ex: R$ 2.000 a R$ 8.000/mês conforme porte). Você fica com a margem sobre o custo da plataforma Orbit.'),
            ('Quanto custa pra consultoria?', 'Modelo de revenue share: você paga uma fração do que cobra do cliente final. Tipicamente sua margem fica entre 60-75%. Fale com a Olívia para o modelo exato.'),
            ('Posso usar pra meu próprio escritório de consultoria também?', 'Sim. Muitos parceiros usam o Canal Orbit primeiro internamente, depois oferecem aos clientes.'),
            ('E se meu cliente quiser mudar de consultor?', 'Os dados ficam no cliente. Se ele trocar de consultor parceiro Orbit, a transição é tranquila. Você protege seu valor com qualidade de entrega, não com lock-in técnico.'),
            ('Qual o perfil de consultoria que mais funciona?', 'Consultorias de gestão (BPM, BSC, ISO), estratégia, RH/people analytics, financeira e qualidade. Cliente final deles é empresa B2B de R$ 100k+/mês de faturamento.'),
        ],
        'cta_final_h': 'Pronto para escalar sua consultoria <span class="text-primary">sem contratar?</span>',
        'cta_final_h_b': 'Pronto para escalar sua consultoria <em>sem contratar?</em>',
        'cta_final_sub': 'Fale com a Olívia agora — em 2 minutos ela entende seu modelo e agenda demo do white-label.',
        'cta_final_micro': 'Sem cartão. Sem instalação. Só uma conversa.',
    },
}


# ─────────────────────────────────────────────────────────────────
# REPLACEMENTS · cada (find, key) define o que pegar do template e
# o que colocar do config do módulo
# ─────────────────────────────────────────────────────────────────

def apply_module(html, slug, cfg, variant):
    """Aplica os swaps do config sobre o template."""
    # URLs e meta
    html = html.replace('/financeiro-variant-a', f'/{slug}-variant-{variant}')
    html = html.replace('/financeiro-variant-b', f'/{slug}-variant-{variant}')
    html = html.replace('https://mkt.orbitgestao.com.br/' + f'{slug}-variant-a', f'https://mkt.orbitgestao.com.br/{slug}-variant-{variant}')

    # Meta tags
    html = re.sub(r'<title>[^<]+</title>', f'<title>{cfg["meta"]["title"]}</title>', html, count=1)
    html = re.sub(r'<meta name="description" content="[^"]+">', f'<meta name="description" content="{cfg["meta"]["description"]}">', html, count=1)
    html = re.sub(r'<meta name="keywords" content="[^"]+">', f'<meta name="keywords" content="{cfg["meta"]["keywords"]}">', html, count=1)
    html = re.sub(r'<meta property="og:title" content="[^"]+">', f'<meta property="og:title" content="{cfg["meta"]["og_title"]}">', html, count=1)
    html = re.sub(r'<meta property="og:description" content="[^"]+">', f'<meta property="og:description" content="{cfg["meta"]["og_description"]}">', html, count=1)
    html = html.replace('og-financeiro.png', f'og-{slug}.png')

    # Subtítulo do produto no nav/sidebar/footer (LP A: dentro de <span class="text-primary ...">Financeiro</span>)
    if variant == 'a':
        html = html.replace('<span class="text-primary font-semibold tracking-tight text-sm">Financeiro</span>',
                            f'<span class="text-primary font-semibold tracking-tight text-sm">{cfg["label"]}</span>')
        html = html.replace('<span class="text-xs font-semibold text-primary">Financeiro</span>',
                            f'<span class="text-xs font-semibold text-primary">{cfg["label"]}</span>')
    else:  # variant b
        html = html.replace('Orbit <span class="product">Financeiro</span>',
                            f'Orbit <span class="product">{cfg["label"]}</span>')

    # data-variant
    html = re.sub(r'data-variant="[ab]"', f'data-variant="{variant}"', html)

    # Hero H1 + sub
    if variant == 'a':
        old_h1 = '''<h1 class="text-center text-4xl sm:text-5xl md:text-7xl leading-[1.05] max-w-5xl mx-auto font-display font-extrabold tracking-tight scroll-item scroll-blur-in d-100">
    Sua <span class="text-primary">CFO em IA</span>.
    <br class="hidden md:block">DRE e fluxo de caixa em tempo real.
  </h1>'''
        new_h1 = f'''<h1 class="text-center text-4xl sm:text-5xl md:text-7xl leading-[1.05] max-w-5xl mx-auto font-display font-extrabold tracking-tight scroll-item scroll-blur-in d-100">
    {cfg["hero_a_h1"]}
  </h1>'''
        html = html.replace(old_h1, new_h1)
        html = html.replace('Substitua planilha, ContaAzul e o financeiro improvisado por uma plataforma com IA que mostra DRE, fluxo, burn rate e runway em segundos.',
                            cfg['hero_a_sub'])
    else:
        old_h1 = '''<h1 class="hero-headline">
            Pare de descobrir o caixa <em>depois</em> que ele já acabou.
          </h1>'''
        new_h1 = f'''<h1 class="hero-headline">
            {cfg["hero_b_h1"]}
          </h1>'''
        html = html.replace(old_h1, new_h1)
        html = html.replace('Substitua planilha, ContaAzul e o financeiro improvisado por uma plataforma com IA\n              que mostra DRE, fluxo, burn rate e runway em segundos. Olívia responde em linguagem natural.',
                            cfg['hero_b_sub'])

    # Faixa de credibilidade - headline
    html = html.replace('3.045+ empresas já tiraram o financeiro da planilha', cfg['credibility_headline'])

    # Stats (4)
    if variant == 'a':
        # Pattern matches the LP A stat blocks
        old_stats = [
            ('85%', 'menos erros de lançamento'),
            ('80%', 'menos tempo em análise financeira'),
            ('65%', 'mais produtividade do time financeiro'),
            ('40%', 'menos tempo em processos manuais'),
        ]
    else:
        # LP B uses different structure
        old_stats = [
            ('85%', 'menos erros de lançamento'),
            ('80%', 'menos tempo em análise financeira'),
            ('65%', 'mais produtividade do time financeiro'),
            ('40%', 'menos tempo em processos manuais'),
        ]
    for (old_v, old_l), (new_v, new_l) in zip(old_stats, cfg['stats']):
        # Replace by exact match of label text (unique per stat)
        html = html.replace(f'>{old_v}<', f'>{new_v}<', 1)
        html = html.replace(old_l, new_l)

    # Para Quem É headline e sub
    if variant == 'a':
        html = html.replace('Quem ganha mais com o <span class="text-primary">Orbit Financeiro</span>',
                            cfg['pci_headline'])
    else:
        html = html.replace('Quem ganha mais com o <em>Orbit Financeiro</em>',
                            cfg['pci_headline_b'])
    html = html.replace('Não é qualquer empresa. É a sua, se você se reconhece aqui:', cfg['pci_sub'])

    # PCI items (6 items)
    old_pci_a = [
        ('solar:buildings-3-bold-duotone', 'Porte', '<strong class="font-extrabold">R$ 500.000+/mês de faturamento</strong> e <strong class="font-extrabold">30 ou mais funcionários</strong>.'),
        ('solar:document-text-bold-duotone', 'Planilha', 'Você (ou seu CFO) ainda monta o fluxo de caixa em <strong class="font-extrabold">planilha toda semana</strong>.'),
        ('solar:clock-circle-bold-duotone', 'DRE atrasado', 'DRE só sai <strong class="font-extrabold">15-30 dias depois</strong> do mês fechado.'),
        ('solar:exit-bold-duotone', 'Stack estourou', 'Já <strong class="font-extrabold">estourou o ContaAzul/Omie/Bling</strong>, mas TOTVS/Sankhya é caro demais.'),
        ('solar:users-group-rounded-bold-duotone', 'Risco operacional', 'Decisões financeiras dependem da <strong class="font-extrabold">memória da equipe</strong>, não do sistema.'),
        ('solar:chat-round-dots-bold-duotone', 'Autonomia', 'Quer falar com sua área financeira <strong class="font-extrabold">sem precisar \'pedir\' relatório</strong>.'),
    ]
    old_pci_b = [
        ('solar:buildings-3-bold-duotone', 'Porte', '<strong>R$ 500.000+/mês de faturamento</strong> e <strong>30 ou mais funcionários</strong>.'),
        ('solar:document-text-bold-duotone', 'Planilha', 'Você (ou seu CFO) ainda monta o fluxo de caixa em <strong>planilha toda semana</strong>.'),
        ('solar:clock-circle-bold-duotone', 'DRE atrasado', 'DRE só sai <strong>15-30 dias depois</strong> do mês fechado.'),
        ('solar:exit-bold-duotone', 'Stack estourou', 'Já <strong>estourou o ContaAzul/Omie/Bling</strong>, mas TOTVS/Sankhya é caro demais.'),
        ('solar:users-group-rounded-bold-duotone', 'Risco operacional', 'Decisões financeiras dependem da <strong>memória da equipe</strong>, não do sistema.'),
        ('solar:chat-round-dots-bold-duotone', 'Autonomia', 'Quer falar com sua área financeira <strong>sem precisar "pedir" relatório</strong>.'),
    ]
    old_pci = old_pci_a if variant == 'a' else old_pci_b
    strong_class = 'class="font-extrabold"' if variant == 'a' else ''
    for (old_icon, old_tag, old_text), (new_icon, new_tag, new_text) in zip(old_pci, cfg['pci_items']):
        # Replace tag and text together. Icons are global swap (each unique in pci section).
        html = html.replace(old_icon, new_icon, 1)
        # tag
        html = html.replace(f'>{old_tag}<', f'>{new_tag}<', 1)
        # text — adapt strong tags
        if variant == 'a':
            adapted_text = new_text.replace('<strong>', f'<strong class="font-extrabold">')
        else:
            adapted_text = new_text
        html = html.replace(old_text, adapted_text, 1)

    # Anti-target (3 items)
    old_anti = [
        ('solar:user-linear', 'Microempresa, MEI ou autônomo — Orbit é overkill.'),
        ('solar:server-square-cloud-linear', 'Empresa com ERP enterprise (SAP, Oracle) + BI dedicado.'),
        ('solar:bill-list-linear', 'Quem quer só emissor de nota fiscal — não é nosso foco.'),
    ]
    for (old_icon, old_text), (new_icon, new_text) in zip(old_anti, cfg['anti_target']):
        html = html.replace(old_icon, new_icon, 1)
        html = html.replace(old_text, new_text, 1)

    # Benefícios headline
    if variant == 'a':
        html = html.replace('O que muda quando o financeiro vira <span class="text-primary">inteligência</span>',
                            cfg['benefits_headline'])
    else:
        html = html.replace('O que muda quando o financeiro vira <em>inteligência</em>',
                            cfg['benefits_headline_b'])

    # Benefits (4 cards)
    old_benefits = [
        ('Olívia, sua IA financeira', 'Pergunte em linguagem natural. Receba resposta com gráfico, contexto e drill-down.', 'Quanto ganhei esse mês? Qual cliente está atrasando? Meu fluxo de caixa cabe na próxima folha? A Olívia responde em segundos — em linguagem humana, com base nos seus dados reais.'),
        ('DRE, fluxo de caixa e burn rate prontos', 'Operacional e gerencial conectados. Sem fechamento manual.', 'Operacional (contas a pagar/receber, conciliação, aprovações) e controladoria (DRE, orçamento, simulação) na mesma plataforma. Fluxo de caixa projeta automaticamente — burn rate, runway e days cash on hand vivos.'),
        ('Aprovações no clique, sem WhatsApp', 'Workflow configurável por valor, centro de custo, fornecedor.', 'Cada compra ou pagamento passa por aprovador certo, com histórico e trilha de auditoria. Acabou aprovação \'pelo WhatsApp\' sem rastro.'),
        ('Conectado com CRM, RH e Processos', 'Sua margem por cliente em uma única tela.', 'O lead que virou cliente no CRM já aparece no financeiro. A folha do RH alimenta o DRE. O processo de compra fala com Contas a Pagar. Tudo integrado nativamente — sem Zapier, sem integração paga.'),
    ]
    # B template uses slightly different markup ("aspas" para "linguagem natural")
    old_benefits_b = [
        ('Olívia, sua IA financeira', 'Pergunte em linguagem natural. Receba resposta com gráfico, contexto e drill-down.', 'Quanto ganhei esse mês? Qual cliente está atrasando? Meu fluxo de caixa cabe na próxima folha? A Olívia responde em segundos — em linguagem humana, com base nos seus dados reais.'),
        ('DRE, fluxo de caixa e burn rate prontos', 'Operacional e gerencial conectados. Sem fechamento manual.', 'Operacional (contas a pagar/receber, conciliação, aprovações) e controladoria (DRE, orçamento, simulação) na mesma plataforma. Fluxo projeta automaticamente — burn rate, runway e days cash on hand vivos.'),
        ('Aprovações no clique, sem WhatsApp', 'Workflow configurável por valor, centro de custo e fornecedor.', 'Cada compra ou pagamento passa por aprovador certo, com histórico e trilha de auditoria. Acabou aprovação "pelo WhatsApp" sem rastro.'),
        ('Conectado com CRM, RH e Processos', 'Sua margem por cliente em uma única tela.', 'O lead que virou cliente no CRM já aparece no financeiro. A folha do RH alimenta o DRE. O processo de compra fala com Contas a Pagar. Tudo integrado nativamente — sem Zapier, sem integração paga.'),
    ]
    old_b_list = old_benefits if variant == 'a' else old_benefits_b
    # Icons for benefits (LP A and B differ on first one)
    old_benefit_icons = [
        # in order of benefit
        'M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z',  # message bubble (Olívia)
        'polyline points="22 7 13.5 15.5 8.5 10.5 2 17"',  # trending-up
        'M22 11.08V12a10 10 0 1 1-5.93-9.14',  # check-circle
        'M9 11H1l4-4',  # integration
    ] if variant == 'a' else None

    # LP B uses iconify icons for benefits
    old_benefit_icons_b = [
        'solar:chat-round-dots-linear',
        'solar:graph-up-linear',
        'solar:check-circle-linear',
        'solar:branching-paths-up-linear',
    ] if variant == 'b' else None

    new_icons_b = [b[0] for b in cfg['benefits']]

    for i, ((old_t, old_s, old_b), (new_icon, new_t, new_s, new_b)) in enumerate(zip(old_b_list, cfg['benefits'])):
        html = html.replace(old_t, new_t, 1)
        html = html.replace(old_s, new_s, 1)
        html = html.replace(old_b, new_b, 1)
        # Replace icon for LP B
        if variant == 'b' and old_benefit_icons_b:
            html = html.replace(old_benefit_icons_b[i], new_icon, 1)

    # Como funciona headline
    if variant == 'a':
        html = html.replace('Sair da planilha em <span class="text-primary">3 passos</span>', cfg['steps_headline'])
    else:
        html = html.replace('Sair da planilha em <em>3 passos</em>', cfg['steps_headline_b'])
    html = html.replace('Implementação guiada por especialistas Orbit. Resultado mensurável em 30 dias.', cfg['steps_sub'])

    # Steps (3)
    old_steps = [
        ('01', 'Semana 1', 'Diagnóstico', 'Equipe Orbit revisa seu plano de contas, importa o histórico financeiro e mapeia o fluxo atual.'),
        ('02', 'Semana 2', 'Setup com Olívia', 'Configuramos contas, fornecedores, centros de custo, aprovadores. Olívia aprende com seu histórico.'),
        ('03', 'Semanas 3-4', 'Go-live e treinamento', 'Time treinado em 4h. Você começa a perguntar para Olívia no mesmo dia.'),
    ]
    for (old_num, old_when, old_t, old_text), (new_num, new_when, new_t, new_text) in zip(old_steps, cfg['steps']):
        # Number stays the same usually
        html = html.replace(old_when, new_when, 1)
        html = html.replace(old_t, new_t, 1)
        html = html.replace(old_text, new_text, 1)

    # Comparativo headline + sub
    if variant == 'a':
        html = html.replace('Por que sair de <span class="text-primary">4 ferramentas</span> para 1', cfg['compare_headline'])
    else:
        html = html.replace('Por que sair de <em>4 ferramentas</em> para 1', cfg['compare_headline_b'])
    html = html.replace('Quanto custa o seu "patchwork" financeiro hoje?', cfg['compare_sub'])

    # Comparativo rows (5)
    old_compare_rows = [
        ('solar:document-medicine-bold-duotone', 'ContaAzul + planilhas', 'Limite de funcionalidade · export/import constante', 'Operacional + DRE + projeção', 'Visão única, sem export/import'),
        ('solar:calculator-minimalistic-bold-duotone', 'Excel para fluxo de caixa', 'Planilha quebra, fórmula falha, ninguém atualiza', 'Fluxo projetado até 18 meses', 'Sem erro de fórmula, runway vivo'),
        ('solar:chat-round-dots-bold-duotone', 'WhatsApp para aprovar pagamentos', '"Foi tio?" · sem histórico · sem rastro', 'Workflow de aprovação', 'Compliance LGPD · histórico imutável'),
        ('solar:user-id-bold-duotone', 'Analista financeiro respondendo perguntas básicas', 'Pergunta segunda · resposta sexta', 'Olívia IA responde em segundos', 'Time foca em estratégia'),
        ('solar:database-bold-duotone', 'CRM, RH e Financeiro separados', 'Cada área com sua planilha · sem cruzamento', 'Tudo conectado nativamente', 'Margem por cliente em 1 clique'),
    ]
    for (old_icon, old_hoje, old_sub, old_orbit, old_gain), (new_icon, new_hoje, new_sub, new_orbit, new_gain) in zip(old_compare_rows, cfg['compare_rows']):
        html = html.replace(old_icon, new_icon, 1)
        html = html.replace(old_hoje, new_hoje, 1)
        html = html.replace(old_sub, new_sub, 1)
        html = html.replace(old_orbit, new_orbit, 1)
        html = html.replace(old_gain, new_gain, 1)

    # Compare foot
    html = html.replace('<span class="text-primary font-extrabold">Soma o custo das ferramentas + horas perdidas + erro humano</span>',
                        cfg['compare_foot'].replace('<strong', '<span').replace('</strong>', '</span>') if variant == 'a' else cfg['compare_foot'])
    # B uses <strong>
    if variant == 'b':
        html = html.replace('<strong>Soma o custo das ferramentas + horas perdidas + erro humano</strong>', cfg['compare_foot'])

    # FAQ (6 questions)
    old_faqs = [
        ('Funciona se já uso ContaAzul/Omie/Bling?', 'Sim. Importamos seu histórico no setup. A migração é guiada por especialistas Orbit — você não fica sem operação um único dia.'),
        ('A Olívia entende minhas perguntas em português?', 'Sim. Olívia foi treinada em português brasileiro e entende terminologia financeira local (regime caixa/competência, DRE gerencial, plano de contas brasileiro).'),
        ('Meus dados ficam seguros?', 'Sim. Dados criptografados em trânsito e em repouso. Conformidade com LGPD. Acessos por perfil e trilha de auditoria completa.'),
        ('Preciso de um time de TI para implantar?', 'Não. A implantação é guiada pela equipe Orbit. Em média leva 3-4 semanas para ir ao ar com tudo configurado.'),
        ('Quanto custa?', 'O preço varia por porte e número de usuários. Para empresas no perfil ICP (R$ 500k+/30+), a faixa típica fica entre'),
        ('E se eu já tenho ERP grande (TOTVS, SAP)?', 'Nesse caso o Orbit complementa: você usa o ERP para fiscal/folha e o Orbit para gestão executiva (DRE gerencial, Olívia, CRM, BSC). Vários clientes operam assim.'),
    ]
    for (old_q, old_a), (new_q, new_a) in zip(old_faqs, cfg['faqs']):
        html = html.replace(old_q, new_q, 1)
        # answers may have <strong>, so do raw replace
        # special: 5th answer contains "<strong" text from financeiro — find by old_a start
        html = re.sub(re.escape(old_a) + r'[^<]*<strong[^>]*>[^<]*</strong>[^<]*\.', new_a, html, count=1)
        # fallback for answers without strong tag
        html = html.replace(old_a, new_a, 1)

    # CTA Final
    if variant == 'a':
        html = html.replace('Pronto para parar de <span class="text-primary">decidir financeiro no escuro?</span>',
                            cfg['cta_final_h'])
    else:
        html = html.replace('Pronto para parar de <em>decidir financeiro no escuro?</em>',
                            cfg['cta_final_h_b'])
    html = html.replace('Fale com a Olívia agora — em até 1 minuto ela entende seu cenário e agenda uma demonstração com nosso especialista.',
                        cfg['cta_final_sub'])
    html = html.replace('Sem cadastro complicado. Sem cartão de crédito. Você decide se quer agendar.',
                        cfg['cta_final_micro'])

    # Para LP B: imagem hero
    if variant == 'b':
        if cfg.get('image_available'):
            html = html.replace('../shared/assets/modules/financeiro/hero.webp',
                                f'../shared/assets/modules/{slug}/hero.webp')
            html = html.replace('../shared/assets/modules/financeiro/hero.png',
                                f'../shared/assets/modules/{slug}/hero.png')
            html = html.replace('CFO acompanhando DRE, fluxo de caixa e indicadores em tempo real no Orbit Financeiro',
                                f'Equipe usando o módulo {cfg["label"]} do Orbit Gestão')
        else:
            # Sem imagem: substituir <picture> por um placeholder com ícone gold
            placeholder = f'''<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,var(--gold-mid),var(--gold-dark));position:absolute;inset:0">
              <iconify-icon icon="{cfg["placeholder_icon"]}" style="font-size:160px;color:rgba(13,17,23,.5)"></iconify-icon>
            </div>'''
            # encontrar bloco <picture>...</picture>
            html = re.sub(r'<picture>\s*<source[^>]+>\s*<img[^>]+/>\s*</picture>', placeholder, html, count=1)

    # Aria-hidden, alt texts, etc. (não vou cobrir tudo, mas o essencial)
    # Hero alt-text (LP A · "Tela do módulo Financeiro..." → genérico)
    html = re.sub(r'data-swap="screenshot-painel-financeiro"', f'data-swap="screenshot-painel-{slug}"', html)

    return html


def main():
    public_dir = ROOT / 'public'
    for slug, cfg in MODULES.items():
        for variant in ('a', 'b'):
            out_dir = public_dir / f'{slug}-variant-{variant}'
            out_dir.mkdir(parents=True, exist_ok=True)
            template = TPL_A if variant == 'a' else TPL_B
            html = apply_module(template, slug, cfg, variant)
            (out_dir / 'index.html').write_text(html)
            # obrigado é genérico - copia do template financeiro
            src_obrigado = ROOT / f'public/financeiro-variant-{variant}/obrigado.html'
            shutil.copy(src_obrigado, out_dir / 'obrigado.html')
            print(f'  ✓ {out_dir.relative_to(ROOT)}')
        print(f'· {slug} OK')


if __name__ == '__main__':
    main()
    print('\nDone.')
