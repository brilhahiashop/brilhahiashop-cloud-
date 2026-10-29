# BRILHAH AI Manager 2.0 — Autonomous Business Twin
Status: proposta técnica / protótipo de simulação separado da produção
Data: 2026-10-29
Origem: BRILHAH AI Manager V1 ("Uma loja. Um cérebro. Sete agentes.")
 
## Problema
Microempresas de e-commerce usam várias aplicações separadas. A automatização fragmentada gera erros de margem, duplicação de ações, riscos com fornecedores e decisões difíceis de auditar.

## Hipótese diferenciadora (não reivindicar exclusividade mundial sem levantamento de anterioridade)
Um sistema operativo de microcomércio que recebe eventos de várias fontes, reconstrói o estado do negócio, simula alternativas, impede perdas evitáveis e só executa ações dentro de limites aprovados — com prova do resultado e reversão.

## Cinco componentes fundamentais
1. **Autonomous Business Twin:** cenário digital da loja, modelos financeiros e comparação entre decisão recomendada e contrafactual.
2. **Zero-Loss Guardrails:** teto diário de gastos, margem mínima, orçamento por mercado, permissões por ação, limite de reembolsos, regra de saldo e modo de emergência. Não garantir ausência de perdas.
3. **Evidence Passport:** rastreabilidade de fornecedor, origem de fotografias e textos, dados de composição/tamanho, informações de segurança e conformidade por país; bloquear quando falta prova.
4. **Coordinated Agents:** produtos, fornecedor, marketing, encomendas, atendimento, margem e gestão operam com uma fila partilhada de tarefas, nunca com poderes ilimitados.
5. **Outcome Ledger:** event sourcing com antes/depois, usuário aprovador, hipótese, previsão, custo real, resultado e rollback, com trilha inviolável ao nível da aplicação.

## Fluxo de decisão
Evento (ex.: stock baixo ou prazo de entrega alterado)
  → consolidar estado com fontes
  → gerar opções
  → validar políticas, margem e evidências
  → simular impacto (incluindo incerteza)
  → solicitar aprovação se ação sensível
  → executar de forma idempotente (futuro)
  → verificar efeito real, registar e compensar/retomar em erro.

## Critérios de segurança antes de qualquer API real
- **Default:** simulação/read-only. Sem permissões de edição ou pagamento.
- Não confiar em prompts como mecanismo de autorização; políticas verificadas no backend.
- Segredos apenas em ambiente seguro, nunca em navegador ou GitHub.
- Se uma integração falhar ou os dados estiverem desatualizados, não executar.
- Ações: níveis READ / DRAFT / REVERSIBLE / APPROVAL / FORBIDDEN.
- Aprovação vinculada ao hash do plano e à versão dos dados.
- Idempotency key para evitar ações duplicadas.
- Logs sem dados pessoais desnecessários; isolamento multiempresa, RLS e proteção RGPD.
- Validações de margem são estimativas, não contabilidade fiscal nem aconselhamento jurídico.

## Realidade técnica observada em 29/10/2026 (somente leitura)
Supabase existente: projeto "BRILHAH IA SHOP", criado em 19/11/2025; tem tabelas de produtos, fornecedores, mercados, encomendas, tarefas e integrações. Várias Edge Functions existem. A existência não comprova disponibilidade de ponta a ponta. Reutilizar apenas após revisão de permissões, credenciais, webhooks e logs.

## MVP demonstrável
- Simular uma ficha de produto com preço, custo, portes, taxas e devolução esperada.
- Aplicar três bloqueios: margem mínima, validação do fornecedor e dados/portes ao cliente.
- Pedir aprovação, rejeitar planos alterados depois da simulação.
- Registar decisões locais, sem tocar em dados reais.
- Evolução seguinte: conectores read-only, persistência segura, testes e piloto supervisionado.

## Métricas de prova
- % de tarefas concluídas autonomamente sem erro
- € estimados e efetivamente poupados vs. cenário de controlo
- Nº de bloqueios corretos / falsos positivos
- Tempo poupado por processo
- Incidentes de duplicação, gasto e reversão (alvo zero, não garantia)
- % de fichas com evidências completas

## Concursos e alegações
Não utilizar "primeiro do mundo" sem análise independente de concorrência/anterioridade.
EIT Culture & Creativity Innovation Projects: TRL 7 exigido na etapa 1; não afirmar essa maturidade se a prova é apenas um protótipo.
A BRILHAH é ENI; verificar separadamente exigências de pessoa coletiva, financiamento, equity/SAFE, deslocações e elegibilidade do setor.
