# BRILHAH AI Manager — Adaptive Business OS (conceito V3)
Data: 29/10/2026 | Estado: conceção validada pelo proprietário; NÃO implementado nem testado em produção.

## Proposta
"Diz-nos que negócio queres gerir. A BRILHAH AI Manager prepara os módulos, processos, agentes e regras de segurança adequados à tua atividade."

A diferença pretendida não é ter modelos prontos para 30 setores. É gerar, com base numa entrevista ao empresário, uma configuração operacional verificável: organização, funções, processos, entradas/saídas, ferramentas, autorizações, painel, indicadores, revisão humana, teste e melhorias contínuas.

## Exemplo: clínica dentária (ADMINISTRAÇÃO, não medicina)
Entrevista: país, dimensão, colaboradores, serviços, calendário, consentimentos, sistemas existentes, horários, tipo de faturação, objetivos e permissões.
A IA propõe: gestão de agenda, pedidos de marcação, confirmações, lembretes consentidos, faltas, inventário de materiais não clínicos, faturação administrativa (com revisão), indicadores agregados, tarefas do pessoal e apoio a receção.
Proteção: **NÃO diagnosticar, não recomendar tratamentos, não interpretar radiografias, não decidir urgência clínica nem tratar dados de saúde reais no protótipo.** Dados de saúde requerem avaliação jurídica, base legal, segurança, segregação e medidas adicionais RGPD. Funcionalidades clínicas podem constituir software médico regulamentado; seriam produto separado e dependente de análise e validação especializada.

## Outros exemplos (abordagem escalonada)
* E-commerce: encomendas, fornecedores, catálogo, margens, entrega, atendimento, redes.
* Fotografia de eventos: pedidos de orçamento, contratos, disponibilidade, reservas, lista de fotografias, entregas e cobranças.
* Salão/cabeleireiro: agendamentos, produtos, horários, campanhas consentidas, pagamentos e faltas.
* Restaurante: reservas, compras, desperdício, turnos, lotação e inventário.

## Cinco capacidades a validar como diferenciação
1. **Entrevista inteligente:** perguntas curtas e dinâmicas para conhecer o negócio, identificar lacunas e pedir autorização; nunca adivinhar dados obrigatórios.
2. **Gerador de empresa digital:** cria esquema de processos, perfis, agentes, painéis, indicadores, políticas e ligações recomendadas — inicialmente em rascunho.
3. **Gémeo do negócio:** simula preços, agendamento, margem, lotação, compras, campanhas e erros antes de qualquer ação real.
4. **Motor de segurança setorial:** bloqueia ações sem autorização, dados suficientes ou cumprimento legal; modo simulação por defeito e emergência para parar.
5. **Ciclo de prova:** observa métricas, mostra ganhos e erros mensuráveis, propõe ajustes e regista quem aprovou cada modificação.

## Fluxo de utilização
1. O empresário descreve o negócio em linguagem comum.
2. O sistema identifica setor, país, riscos e prioridades.
3. Apresenta a estrutura para revisão: módulos, agentes, ligações e custos.
4. O empresário confirma; a aplicação monta um ambiente de TESTE.
5. A IA simula tarefas com dados fictícios e produz relatório simples de erros.
6. Só depois liga dados reais com consentimento/permissões verificadas.
7. Ações sensíveis exigem aprovação humana; todas são registadas.
8. O sistema mede resultados reais e apresenta melhorias sem as aplicar automaticamente quando são sensíveis.

## Arquitetura modular recomendada
- Núcleo comum: identidades e empresas, permissões, custos, tarefas, eventos, auditoria, relatórios, aprovações e memória por empresa.
- "Pacote de setor": processos, indicadores, regras, limitações, linguagem, dados e formulários específicos.
- Conectores: e-mail, calendário, pagamentos, POS, Shopify, ERP e sistemas de terceiros, se permitirem API.
- Agentes: orquestrador, receção/atendimento, operações, financeiro administrativo, marketing, segurança e análise.
- Verificadores independentes: conformidade, custos, identidade, autorização, disponibilidade de dados, conflito entre agentes e duplicação de ações.
- Isolamento: um negócio nunca pode ver dados de outro; multiempresa com acessos estritos e RGPD.
- Modo inicial: só leitura e rascunho; sem publicação, cobrança, envios ou reembolsos sem autorização expressa.

## Prova de conceito prioritária
Fazer duas demonstrações a partir do mesmo núcleo, com dados fictícios:
A) loja de moda BRILHAH — simulação de produto, fornecedores e margem;
B) clínica dentária fictícia — configuração de agenda e marcações administrativas sem dados clínicos.
Aceitação: 80% da estrutura inicial gerada após entrevista, 0 ações sem autorização, nenhum acesso cruzado, testes de bloqueio de dados sensíveis, registo completo das decisões. Métricas de aceitação são METAS, não resultados atingidos.

## Concurso EIT Culture & Creativity Innovation Projects 2026
Prazo da 1ª fase: 30/10/2026. Apenas moda, audiovisual e arquitetura (ou serviço direto desses setores). O apoio fixo de 20.000€ é para preparação do plano dos candidatos selecionados após a primeira avaliação, não para construir de raiz o produto. Requer projeto no nível TRL7 (protótipo já demonstrado num ambiente operacional real); a abordagem multiatividade NOVA não tem essa prova. Implementação posterior pode implicar cofinanciamento e partilha de receitas/SAFE. Não reivindicar elegibilidade do ENI, TRL7 nem pioneirismo mundial sem validação documental. Para este concurso, só um caso centrado em moda poderia encaixar tematicamente.

## Linguagem para comunicação
Evitar "a primeira do mundo", "autonomia 100%", "zero perdas" ou "cumprimento garantido" sem prova. Usar "gestor empresarial de IA adaptável ao setor, com controlo humano, simulação e registo de decisões".

## Próximas decisões
1. Não alterar produção.
2. Criar motor de configuração por setor e formulário de entrevista.
3. Testar as duas demonstrações com dados fictícios.
4. Rever tecnicamente segurança, licença, custos e independência de fornecedores de IA.
5. Comparar com Copilot Studio, Agentforce, Relevance AI e plataformas de gestão setorial com uma matriz verificável de funcionalidades.
