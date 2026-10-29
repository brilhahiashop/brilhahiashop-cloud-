# BRILHAH AI Manager — Painéis Setoriais V4
Data: 29/10/2026
Estado: protótipo HTML interativo, fora da produção. **Não publicado na app nem ligado à Shopify.**

## Pedido
A escolha do setor deve originar um painel próprio com identidade gráfica, fotografia de fundo e módulos próprios, sem parecer a mesma aplicação com textos trocados.

## Painel Moda & Comércio
Visual editorial, paleta rosa/champagne escuro e fotografia de moda.
Menu: Início, Produtos, Coleções, Fornecedores, Encomendas, Marketing, Conteúdos, Clientes, Agentes IA, Ligações e Controlo.
Demonstrações funcionais: adicionar produtos fictícios, simular margens, criar campanhas em rascunho, consultar tarefas, ativar/desativar módulos e regras.

## Painel Fotografia & Audiovisual
Visual cinematográfico azul, imagem de câmara e produção.
Menu: Início, Agenda, Clientes, Orçamentos, Projetos, Sessões, Edição & Entregas, Portefólio, Agentes IA, Ligações e Controlo.
Demonstrações funcionais: criar marcação fictícia, orçamento simulado por horas, projeto de produção com estado de entrega e lista de tarefas.

## Experiência de primeiro acesso
1. Selecionar setor.
2. Escrever nome do negócio.
3. Carregar em «Criar o meu painel».
4. Abrir diretamente o espaço do setor.
5. Alternar para outro setor se necessário. Dados de teste guardados no armazenamento local do navegador (quando permitido).

## Ligação de contas sem chaves técnicas
Futura versão: ligação por botão usando OAuth ou instalação oficial do serviço, com autorizações mínimas e cancelamento/revogação; nenhuma credencial pedida ou guardada no frontend.
O protótipo V4 apresenta apenas explicação dos passos; **não executa autorização OAuth real**.

## Verificações de interface feitas
Navegação desktop e mobile; criação de produto e campanha; criação de sessão e orçamento; alternância para módulo de projetos; ecrã de agentes; caixas de diálogo de ligações; sem erros de JavaScript nos percursos testados.
Armazenamento persistente numa navegação real com URL público não testado, devido a limitações do navegador de testes. Não afirmar verificação dessa persistência como concluída.

## Próximos passos
- Levar V4 para uma aplicação protegida com contas e armazenamento no servidor.
- Criar módulo de identificação do cliente e de empresas/serviços.
- Converter módulos de demonstração em serviços reais com base de dados isolada por cliente.
- Desenvolver primeiro ligação Google Calendar no audiovisual e ligação Shopify na moda.
- Só depois ligar agente IA a dados reais, com aprovação e controlo no backend.
- Manter a BRILHAH atual intocada até avaliação e aprovação de uma versão testada.
