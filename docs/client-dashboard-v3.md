# BRILHAH AI Manager — Painel do cliente, sem ficheiros nem chaves
Atualização: 29/10/2026 | Estado: protótipo HTML testado localmente (não publicado)

## Requisito de experiência
Um cliente deve poder entrar na aplicação, indicar o tipo e nome do negócio, e carregar num único botão «Criar o meu gestor». A aplicação abre diretamente o painel do negócio, sem exportar ficheiros .json e sem pedir chaves API. Ao regressar, o mesmo espaço deve ser recuperado a partir da conta do cliente; na demo HTML, existe apenas uma tentativa de guardar o estado no navegador.

## Painel inicial
- Início: resumo e módulos do negócio
- Tarefas: exemplos/revisões
- Agentes IA: ativar/desativar módulos
- Ligações: serviços por autorizar
- Controlo: permissões por ação

## Setores de demonstração
- Moda e comércio: encomendas, produtos, fornecedores, margens, marketing, atendimento, proteção
- Audiovisual e fotografia: agenda, projetos, orçamentos, portefólio, atendimento, direitos
- Outros: genérico, ainda experimental

## Restrições e implementação futura
- O HTML é uma interface demonstrativa; não contém agentes ativos nem OAuth/Shopify reais. Não afirmar que as contas estão ligadas.
- Na versão comercial, login e espaço persistente no servidor, configurações separadas por empresa e segurança por permissões.
- Ligações via autorização oficial do fornecedor: botão «Ligar», o cliente inicia sessão no fornecedor, autoriza permissões mínimas e regressa ao painel. A BRILHAH configura e mantém o lado técnico, sem pedir chaves ao cliente.
- Cada módulo pode existir em modo interno sem ligação, mas dados de terceiros só estão acessíveis após autorização real.
- Publicações, mensagens, pagamentos, reembolsos, preços e outros atos sensíveis exigem consentimento e controlo no servidor, não apenas visual.
- Google/Gmail e certos fornecedores exigem verificação/aprovação da aplicação, que pode ser dispendiosa.

## Testes realizados ao HTML V3
- Chrome em viewport móvel 390×844
- Criar empresa num passo → painel
- Navegação por cinco secções
- Criar três tarefas fictícias e rever uma
- Ativar/desativar módulo e atualizar contador
- Apresentação clara dos limites das ligações
- Seleção de setor Audiovisual mostra agentes e conectores próprios
- Não ocorreram erros JavaScript nos testes acima
- Não foi testada ligação real nem persistência via conta; este é o próximo desenvolvimento.

## Prioridade técnica
1. Ecrã inicial + painel autenticado, guardado na base de dados por empresa
2. Motor real de módulos e tarefas internas
3. Ligação Google Calendar básica (permissão mínima, se elegível) e primeira integração sectorial
4. Orquestrador de agentes e testes de segurança
5. Regras financeiras, documentos e auditoria de decisões

O protótipo HTML V3 é artefacto independente do ambiente de produção e NÃO altera a Shopify nem o Supabase.
