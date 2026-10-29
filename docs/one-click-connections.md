# BRILHAH AI Manager — Ligações com um clique e permissões

Data: 29/10/2026 | Estado: especificação técnica; as integrações multiempresa NÃO estão implementadas.

## Promessa simples
O cliente não procura chaves API nem cola segredos técnicos. Seleciona o serviço, entra no ecrã oficial e aprova o acesso necessário. A BRILHAH mantém a configuração técnica do lado do fornecedor da app.

## Percurso
1. Escolher setor: Moda / Audiovisual / Outro (experimental).
2. Introduzir nome do negócio, país e objetivos.
3. Receber proposta de módulos e processos adaptados ao setor.
4. Selecionar "Ligar Google / Shopify / YouTube...".
5. Abrir página oficial de autorização (OAuth ou instalação autorizada) com acessos mínimos.
6. Receber confirmação da ligação, estado da sincronização, ação de desligar e histórico de permissões.
7. Escolher autonomia (apenas leitura / criar rascunhos / pedir aprovação / automatizar apenas ações de risco baixo).
8. Testar em ambiente de simulação; habilitar ações reais só com aprovação e registo.

## Implementação segura
- OAuth 2.0/OIDC, PKCE quando aplicável, estado antifalsificação CSRF, proteção contra troca de contas, redirecionamentos exatos.
- Shopify: instalação de app e consentimento de permissões pela loja; distribuir app segundo as regras da Shopify.
- Google: começar por Calendário e Drive com acesso mínimo; Gmail pode usar âmbitos restritos e implicar verificação de app + avaliação de segurança, o que pode inviabilizar um arranque de baixo custo.
- YouTube: autorização Google limitada às ações necessárias e confirmação antes de publicar.
- Instagram/Meta/WhatsApp: revisão de aplicação e verificações adicionais podem ser exigidas; não prometer um clique se a plataforma exigir onboarding.
- Cada ligação é específica de uma empresa e pode ser revogada; não partilhar tokens ou dados entre empresas.
- Tokens cifrados do lado do servidor, nunca em HTML, GitHub ou logs.
- Políticas de ações verificadas no servidor, não apenas na interface.
- Publicações, pagamentos, reembolsos, alterações de preço e contactos de clientes exigem autorização explícita.
- Registo de eventos e reversão/idempotência quando possíveis; desligar tudo rapidamente.

## Níveis de autonomia na interface
A. Só consultar.
B. Preparar rascunhos.
C. Pedir aprovação antes da execução.
D. Executar automaticamente SOMENTE ações reversíveis de baixo risco definidas pelo empresário.

## Primeiros testes de mercado
1. Moda: lista de produtos, margem simulada, proposta de conteúdo, aprovação.
2. Audiovisual: receção de pedido, agenda proposta, orçamento preliminar e lembrete consentido.
3. Os outros setores permanecem experimentais até terem pacotes setoriais e validação.

## Situação concreta
Foi criado um HTML demonstrativo independente com escolha do setor, módulos, explicação das ligações e controlos de permissões. NÃO abre contas reais, NÃO armazena credenciais e NÃO produz automações verdadeiras. Executaram-se testes manuais automatizados de navegação dos percursos Moda e Audiovisual, sem erros JavaScript reportados.

## Concurso EIT
Para a candidatura de 30/10/2026, destacar um caso já testado em MODA ou AUDIOVISUAL; a vertente multiempresa serve como perspetiva futura. Não alegar TRL 7 para funções novas ainda não testadas em condições reais.
