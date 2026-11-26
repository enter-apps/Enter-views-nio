# App Subsídios Nio — Requisitos e listas (rascunho vivo)

Atualizado: 2026-11-18. Fonte: Gabrieli (texto e voz). Foco atual: **artefato/protótipo** com os pontos principais (OCR, JS, validações). Infraestrutura (Railway, histórico, backend) fica para depois.

## Decisões já tomadas
- Capa Nio com o logo de **cauda longa** (logo gráfico ampliado, verde-neon, colado nas extremidades), como nos materiais de dossiê.
- Template padrão com campos fixos obrigatórios. Sempre que possível, **lista suspensa** para evitar erro de digitação (público com dificuldade; facilitar ao máximo).
- Imagens de alta qualidade; o app deve **educar** o operador (orientação, exemplos bom/ruim).
- Saídas: PDF, PPTX e DOCX; uma tela por página/slide, grande.
- Parte 2 (futura): indicadores de subsídios.

## Fluxo de perguntas (rascunho)
0. **Confirmação do subobjeto**: o app mostra o subobjeto (da lista); operador dá OK ou corrige. Se corrigir, abre campo para informar o correto e **registra o rastro** do subobjeto original.
1. **Cliente tem cadastro ou contrato com a Nio?**
   - **Sim** (inclusive de terceiro, sem especificar) → segue o fluxo de telas: telas comuns e árvore do subobjeto.
   - **Não** → abre o campo para a **evidência de que não existe cadastro** e as perguntas de tentativa: já checou por **linha telefônica, nome parcial, CPF e número do contrato**. Nesse caso **as demais telas não são exigidas**, porque não existem.
2. Perguntas seguintes por tese/tela (a definir com a lista de erros dos operadores).
3. Ao final: conclusão, área de risco, legitimidade passiva (abaixo).

## Campos obrigatórios do template
| Campo | Tipo | Observações |
|---|---|---|
| Data da análise | data | preenchimento assistido |
| ID Pasta | texto | inserir |
| ID Subsídio | texto | inserir |
| Conclusão da análise | lista fechada | Autor tem razão / Autor não tem razão – provas robustas / Autor não tem razão – provas insuficientes |
| Causa real | lista (abaixo) ou "outro" | permitir texto livre se não estiver na lista |
| Fundamentação da conclusão | texto descritivo | motivos que levaram à conclusão; mínimo de caracteres |
| Subobjeto | lista (abaixo) | confirmar/corrigir, com rastro do original |

## Campos de decisão com OK explícito (checkbox + especificação)
- **Área de risco?** Sim → especificar. 
- **Caso de legitimidade passiva?** Sim → especificar.
- Cliente em nome de terceiro? (ver fluxo)

## Confirmações finais antes de baixar (checkboxes)
- Confirmo que **todas as telas estão legíveis**.
- Confirmo que **todos os campos descritivos foram preenchidos devidamente**.

## Pendências
- Logo em SVG e fonte BW Gradual (licença); fallback Plus Jakarta Sans.
- Mapa pergunta → tela ativada → ordem → orientação.
- Lista de erros recorrentes dos operadores.
- Higienizar duplicatas/variações na lista de causa real (ver nota no fim).

---

## Lista: causa real (como enviada)

SOLICITAÇÃO DE CANCELAMENTO NÃO FINALIZADA
COBRANÇA REALIZADA CORRETAMENTE
COBRANÇA DE ACORDO COM A RENEGOCIAÇÃO
MASSIVA - FALHA NA INFRAESTRUTURA
REGULARIDADE JURÍDICA - ILEGITIMIDADE PASSIVA
CANCELAMENTO NÃO PROCESSADO VIA SAC
ALTERAÇÃO INDEVIDA DE ENDEREÇO
COBRANÇA INDEVIDA DA PERMANÊNCIA
EXCESSO DE LIGAÇÕES NÃO LOCALIZADO
VENDA SEM VIABILIDADE OPERACIONAL
DÉBITO REGULAR / AUTOR INADIMPLENTE
DESALINHAMENTO DE SINAL
BLOQUEIO POR INADIMPLÊNCIA
FALHA NA COMPENSAÇÃO DO PAGAMENTO
AUTOR NÃO FINALIZOU A SOLICITAÇÃO DE CANCELAMENTO
AUSÊNCIA DE COBERTURA – COBRANÇA DE PERMANÊNCIA
AUSÊNCIA DE DOCUMENTOS DA CONTRATAÇÃO
COBRANÇA DEVIDA DA PERMANÊNCIA
CLIENTE SEM FIDELIDADE COM HABILITAÇÃO
COBRANÇA DE PERMANÊNCIA EM ÁREA DE RISCO
ENDEREÇO FORA DA ÁREA DE COBERTURA
IMPOSSIBILIDADE TÉCNICA EM ÁREA DE RISCO
CANCELAMENTO NÃO LOCALIZADO
FALHA NÃO IDENTIFICADA
VELOCIDADE COMPATÍVEL COM O PLANO
ALTERAÇÃO INDEVIDA
ALTERAÇÃO CADASTRAL NÃO REALIZADA
CANCELAMENTO PROCESSADO
CONTRATAÇÃO REALIZADA PELO AUTOR
VELOCIDADE NÃO COMPATÍVEL COM O PLANO
PAGAMENTO NÃO LOCALIZADO
PAGAMENTO REALIZADO EM ATRASO
INSTALAÇÃO CONCLUÍDA
AGENDAMENTO NÃO REALIZADO
FALHA MASSIVA DE INFRAESTRUTURA
INSTABILIDADE NÃO IDENTIFICADA
INCONSISTÊNCIA NO VALOR DA COBRANÇA
ATENDIMENTO REALIZADO CORRETAMENTE
NÃO LOCALIZADO EXCESSO DE LIGAÇÕES
COBRANÇA VEXATÓRIA
INEXISTÊNCIA DE NEGATIVAÇÃO (SERASA LIMPA NOME)
PORTABILIDADE CONCLUÍDA
VAZAMENTO NÃO COMPROVADO
CANCELAMENTO INDEVIDO
CLIENTE NÃO FINALIZOU SOLICITAÇÃO
CONTRATAÇÃO REALIZADA POR TERCEIRO
SOLICITAÇÃO NÃO FINALIZADA PELO CLIENTE
FIDELIDADE NEGOCIADA COM O CLIENTE
VANDALISMO EM INFRAESTRUTURA
NEGATIVAÇÃO INDEVIDA
TRANSFERÊNCIA REALIZADA SEM SOLICITAÇÃO
ATENDIMENTO INADEQUADO
ACIDENTE DURANTE ATIVIDADE DE CAMPO
ORIENTAÇÕES DIVERGENTES FORNECIDAS AO AUTOR
ALTERAÇÃO SOLICITADA PELO AUTOR
FRAUDE EXTERNA POR BOLETO FALSIFICADO
ATENDIMENTO OFENSIVO
AUSÊNCIA DE NEXO CAUSAL
AUTOR INADIMPLENTE
DANO MATERIAL COMPROVADO
DESVIO DE VENDA IDENTIFICADO
REESTABELECIMENTO DENTRO DO PRAZO REGULATÓRIO
INEXISTÊNCIA DE NEGATIVAÇÃO 
DÉBITO ANTERIOR AO CANCELAMENTO
CONDUTA INADEQUADA NÃO COMPROVADA
PAGAMENTO NÃO IDENTIFICADO / NEGATIVAÇÃO REGULAR
EXECUÇÃO TÉCNICA NÃO CONCLUÍDA
NEGATIVAÇÃO INDEVIDA APÓS CANCELAMENTO
NEGATIVAÇÃO INDEVIDA POR FRAUDE CONFIRMADA
CANCELAMENTO NÃO PROCESSADO VIA SITE
FATURA NÃO DISPONIBILIZADA
COBRANÇA PÓS-CANCELAMENTO NÃO REALIZADO
AUSÊNCIA DE SLOT NA REDE
MANUTENÇÃO PROGRAMADA COMUNICADA
RESPONSÁVEL AUSENTE
PAGAMENTO NÃO PROCESSADO
CDOE/I DANIFICADA
AUSÊNCIA DE PROVAS DO AUTOR
MANUTENÇÃO PROGRAMADA NÃO COMUNICADA
RESTRIÇÃO NO NOME DO TERCEIRO
PEDIDO DE CANCELAMENTO CONFIRMADO
PHISHING OU LINK MALICIOSO
PAGAMENTO NÃO BAIXADO / NEGATIVAÇÃO MANTIDA INDEVIDAMENTE
SOLICITAÇÃO DE ALTERAÇÃO NÃO IDENTIFICADA
AUSÊNCIA DE DOCUMENTOS
CONTATO EXCESSIVO ORIGINADO POR PARCEIRO
VENDA REALIZADA CORRETAMENTE
CANCELAMENTO NÃO PROCESSADO VIA APP
FALHA NA ATIVAÇÃO DO PARCEIRO
FALHA NA PORTABILIDADE
SOLICITAÇÃO DE PORTABILIDADE NÃO LOCALIZADA
VAZAMENTO IDENTIFICADO
SOLICITAÇÃO DE TRANSFERÊNCIA NÃO LOCALIZADA
FATURA DISPONIBILIZADA
CANCELAMENTO NÃO PROCESSADO VIA URA
FALHA DE ACESSO INTERNA
CONDUTA INADEQUADA NÃO LOCALIZADA
PAGAMENTO DA RENEGOCIAÇÃO NÃO BAIXADO
FALHA NA ATIVAÇÃO INTERNA
VOUCHER NÃO DISPONIBILIZADO
IDENTIFICADA FALHA ISOLADA
CANCELAMENTO REALIZADO
DIVERGENCIA NO VALOR DO DÉBITO
CANCELAMENTO NÃO ATENDIDO SAC
ADESÃO DO DÉBITO AUTOMATICO PELO CLIENTE
VALOR DE CRÉDITO DISPONIVEL CORRETAMENTE
PEDIDO DE CANCELAMENTO LOCALIZADO
CLIENTE NÃO SOLICITOU TRANSFERÊNCIA
MODIFICAÇÃO NÃO AUTORIZADA DE DADOS
TRANSFERÊNCIA CONCLUÍDA
SERASA LIMPA NOME – SEM NEGATIVAÇÃO
AUSÊNCIA DE DOCUMENTOS PARA ANÁLISE
HABILITAÇÃO NEGOCIADA COM O CLIENTE
VELOCIDADE NÃO COMPATÍVEL COM PLANO
PORTABILIDADE SOLICITADA PELO AUTOR
ALTERAÇÃO NÃO É POSSÍVEL SISTEMICAMENTE
CONFIRMAÇÃO DE DISPONIBILIZAÇÃO DA FATURA
CANCELAMENTO NÃO ATENDIDO SITE
GAP SISTÊMICO
DIVERGÊNCIA DE CONDIÇÃO COMERCIAL
USO INADEQUADO OU AMBIENTE INTERNO
PAGAMENTO DA RENEGOCIAÇÃO EM VALOR DIVERGENTE
DOCUMENTOS INSUFICIENTES
ORDEM DE SERVIÇO NÃO CRIADA
COBRANÇA VEXATORIA
CLIENTE INADIMPLENTE
FRAUDE INTERNA VIA ATENDIMENTO
CANCELAMENTO POR INADIMPLÊNCIA
MUDANÇA CONCLUÍDA
CANCELAMENTO DE SERVIÇO DIGITAL NÃO REALIZADO
COMUNICAÇÃO INCOMPLETA AO AUTOR
PAGAMENTO PARCIAL / DÉBITO REMANESCENTE
FALHA DA OPERADORA TERCEIRA
DATA DE VENCIMENTO APLICADA CORRETAMENTE
SOLICITAÇÃO INDEVIDA POR TERCEIRO
INEXISTÊNCIA DE DÉBITO EM ABERTO
COLETA AGENDADA NÃO REALIZADA
DADOS DIVERGENTES INFORMADOS
EXISTÊNCIA DE DÉBITO EM ABERTO EXIGE TRATAMENTO ADEQUADO
AUSÊNCIA DE ENVIO DE DOCUMENTOS
DADOS CADASTRAIS DESATUALIZADOS
ERRO DE AUTENTICAÇÃO DO USUÁRIO
TRANSFERÊNCIA SOLICITADA PELO AUTOR
CRÉDITO NÃO EFETIVADO
CONTRATAÇÃO REALIZADA PELO CLIENTE
AUTOR NÃO VIABILIZOU A DEVOLUÇÃO
AUSÊNCIA DE RESPONSÁVEL
AUSÊNCIA DE NEXO CAUSAL COM O ATENDIMENTO
MUDANÇA DE TITULARIDADE NÃO LOCALIZADA
ÁREA DE RISCO - IMPOSSIBILIDADE
NÃO LOCALIZAÇÃO DA CONDUTA INADEQUADA
PEDIDO DE CANCELAMENTO NÃO LOCALIZADO
SERVIÇO/PRODUTO NÃO COMERCIALIZADO
USO INADEQUADO PELO CLIENTE
INFORMAÇÕES CORRETAS DISPONIBILIZADAS NO SITE
TERCEIRO - FALHA NA PORTABILIDADE
CLIENTE NÃO VIABILIZOU A DEVOLUÇÃO
CLIENTE REALIZOU O PAGAMENTO
PORTABILIDADE SOLICITADA PELO CLIENTE
INSTALAÇÃO NÃO REALIZADA
ENDEREÇO INFORMADO FORA DA ÁREA DE COBERTURA
VALOR DE CRÉDITO DIVERGENTE AO ESPERADO
NÃO DISPONIBILIZAÇÃO DA FATURA
CLIENTE SOLICITOU TRANSFERÊNCIA
CANCELAMENTO NÃO ATENDIDO APP
MASSIVA – VANDALISMO
PORTABILIDADE NÃO SOLICITADA
AUSÊNCIA DE PROVAS
NENHUMA RESTRIÇÃO LOCALIZADA
FRAUDE EXTERNA POR MEIO DE BOLETO FALSIFICADO
VALOR DIVERGENTE DA RENEGOCIAÇÃO
PERMANÊNCIA
VAZAMENTO DE DADOS NÃO COMPROVADO
CANCELAMENTO NÃO ATENDIDO URA
FALHA DE ACESSO NIO
COBRANÇA INDEVIDA OU SEM CONTRATAÇÃO
ERRO NA DISPONIBILIZAÇÃO DAS INFORMAÇÕES
NÃO RETIRADA DE EQUIPAMENTO
CLIENTE SOLICITOU ALTERAÇÃO DOS DADOS
STREAMING ATIVADO E FUNCIONANDO
PORTABILIDADE REALIZADA
ALTERAÇÃO SOLICITADA PELO CLIENTE
SOLICITAÇÃO LOCALIZADA E NÃO REALIZADA
REATIVAÇÃO REALIZADA
ALTERAÇÃO INDEVIDA DE DADOS PESSOAIS
ALTERAÇÃO NÃO SOLICITADA
ALTERAÇÃO CADASTRAL CONCLUÍDA
ÁREA DE RISCO – COBRANÇA DA PERMANÊNCIA
COLETA NÃO AGENDADA
LIMITAÇÃO DE EQUIPAMENTO OU REDE INTERNA
TERCEIRO - SOLICITAÇÃO INDEVIDA
AUSÊNCIA DE INCONSISTÊNCIA DE USO
NIO - SOLICITAÇÃO INDEVIDA
COBRANÇA CONFORME RENEGOCIAÇÃO
ENDEREÇO INFORMADO DIVERGENTE
EQUIPAMENTO COM VICIO OU OBSOLETO
COBRANÇA REALIZADA USO DE CSP DE OUTRA OPERADORA
VELOCIDADE COMPATÍVEL COM PLANO
FALHA NA PLATAFORMA OU INTEGRAÇÃO DO SERVIÇO
COBRANÇA INDEVIDA POR LIGAÇÕES
EQUIPAMENTO OPERANTE
RESTRIÇÃO CADASTRAL NO SISTEMA - SUSPEITA DE FRAUDE
CLIENTE SEM HABILITAÇÃO COM FIDELIDADE
NÃO HOUVE COBRANÇA
TRANSFERÊNCIA DE TITULARIDADE CONCLUÍDA
PAGAMENTO EM CANAL FRAUDULENTO
PAGAMENTO EM CANAL NÃO OFICIAL / FRAUDULENTO
NÃO CUMPRIMENTO DE PEDIDO DE TRATAMENTO
DISPONIBILIZAÇÃO DE DADOS CADASTRAIS MEDIANTE ORDEM
PROTOCOLO SEM GRAVAÇÃO
PENDÊNCIA FINANCEIRA
AMEAÇA EM CAMPO
LIMITAÇÃO PROBATÓRIA - AUSÊNCIA DE DOCUMENTOS DO PARCEIRO
RETENÇÃO COM ACEITE DO AUTOR
FRAUDE INTERNA VIA ATENDIMENTO COM BOLETO FALSIFICADO

## Lista: subobjetos possíveis

EXCESSO DE LIGAÇÕES
INTERRUPÇÃO
INSTABILIDADE
CONTESTAÇÃO DE PERMANÊNCIA
ALTERAÇÃO DE DATA DE VENCIMENTO
PAGAMENTO NÃO RECONHECIDO
VALOR DIVERGENTE
CANCELAMENTO NÃO REALIZADO
MUDANÇA NÃO REALIZADA
INCONSISTÊNCIA DE INFORMAÇÃO
COLETA DE EQUIPAMENTO
CONTRATAÇÃO NÃO RECONHECIDA
ALTERAÇÃO DE CADASTRO NÃO REALIZADA
NEGATIVAÇÃO APÓS PAGAMENTO
VELOCIDADE INFERIOR
SERVIÇO DIGITAL
INSTALAÇÃO NÃO REALIZADA
CONDUTA INADEQUADA - ATENDIMENTO
INCONSISTÊNCIA NA PORTABILIDADE
SUPERENDIVIDAMENTO
TRATAMENTO DE DADOS
FATURA NÃO RECEBIDA
VAZAMENTO DE DADOS
DÉBITO NÃO RECONHECIDO
QUEBRA DE SIGILO
TRANSFERÊNCIA DE TITULARIDADE
NÃO DEFINIDO
CANCELAMENTO NÃO SOLICITADO
BOLETO FALSO
ALUGUEL DE INFRAESTRUTURA
ACIDENTE COM INFRAESTRUTURA
REMOÇÃO DE CABOS OU EQUIPAMENTOS
DANO EM ATENDIMENTO
RENEGOCIAÇÃO DESCUMPRIDA
LINK FALSO
DESVIO DE VENDA
COBRANÇA APÓS CANCELAMENTO
ALTERAÇÃO DE CADASTRO INDEVIDA
NEGATIVAÇÃO APÓS CANCELAMENTO
AUSÊNCIA DE POSITIVAÇÃO
SEM VIABILIDADE TÉCNICA
CONDUTA INADEQUADA - CAMPO

## Nota: variações próximas na lista de causa real (candidatas a unificar, decidir com a Gabrieli)
- VELOCIDADE (NÃO) COMPATÍVEL COM (O) PLANO — 4 grafias
- COBRANÇA VEXATÓRIA / VEXATORIA
- FRAUDE EXTERNA POR BOLETO FALSIFICADO / POR MEIO DE BOLETO FALSIFICADO
- INEXISTÊNCIA DE NEGATIVAÇÃO (com e sem complemento) / SERASA LIMPA NOME
- MASSIVA - FALHA NA INFRAESTRUTURA / FALHA MASSIVA DE INFRAESTRUTURA
- AUTOR INADIMPLENTE / CLIENTE INADIMPLENTE / DÉBITO REGULAR
- PAGAMENTO EM CANAL FRAUDULENTO / ...NÃO OFICIAL / FRAUDULENTO
- FALHA DE ACESSO INTERNA / FALHA DE ACESSO NIO
- AUSÊNCIA DE DOCUMENTOS / DOCUMENTOS INSUFICIENTES / AUSÊNCIA DE DOCUMENTOS PARA ANÁLISE / AUSÊNCIA DE ENVIO DE DOCUMENTOS
- Termos "autor" vs "cliente" e "Nio" (a marca se escreve só com N maiúsculo)

## Estrutura de cada tela no documento final (definido em 18/11)
- Cada tela traz o **nome da tela** (escolhido em lista de opções, para não digitar), a **imagem abaixo do nome** e o **texto de descrição abaixo da imagem**.
- Uma tela por página/slide, imagem grande.

## Decisões de 18/11
- Sugestões de causa real **por subobjeto**, a partir da base histórica (29.063 subsídios): destacar as mais prováveis, **sem restringir** a lista.
- Lista de causa real deve ser **MECE**: proposta com 150 causas canônicas em 13 grupos (arquivo Subsidios_Nio_causas_MECE_e_sugestoes.xlsx; também causas_mece.json e sugestoes_por_subobjeto.json).
- Achado: "ALTERAÇÃO INDEVIDA" (2.843 casos) aparece entre as 3 causas mais frequentes em quase todo subobjeto, parece causa-padrão antiga; significado a confirmar.
- Base tem conclusões antigas (DEFESA, ACORDO, CLIENTE...); tratar como pendência.

## Atualização (18/11, 2)
- **Conclusões antigas (DEFESA, ACORDO, CLIENTE...) não entram**: nem na lista do app, nem nas sugestões. Só as 3 conclusões válidas.
- **Nome da tela = sistema** (ex.: SIEBEL, PAINEL ATT-CLIENTE, TELA ÚNICA, RAID, PAINEL GERAL, PORTAL V.TAL, CONSULTA SPC/SERASA) + opção OUTRO (informar).
- Significado das causas em aberto (ex.: ALTERAÇÃO INDEVIDA) será confirmado pela Gabrieli; seguimos com a lista atual enquanto isso.
- Achado: ALTERAÇÃO INDEVIDA (2.843 casos) existe só em conclusões antigas; com as 3 válidas, nenhum caso. Fica fora das sugestões automaticamente.

## Nota de qualidade do dossiê (gamificação) — definido em 18/11
- Nota de 0 a 10, mostrada ao vivo ao operador, para motivar e orientar. **A nota só orienta: não bloqueia o download** (quem bloqueia são as regras duras e as confirmações finais).
- Mede a qualidade do dossiê, não se a análise está certa. Não premia quantidade: só conta tela esperada para o subobjeto/causa.
- Proposta de pesos (a calibrar): completude 40%, qualidade da imagem 25%, texto 15%, coerência 10%, sem pendências 10%.
- Mostrar "como subir a nota" (ações concretas), nota por dimensão, selo de dossiê completo e evolução pessoal.
- A nota entra no histórico de cada geração (insumo da parte 2).
- **Em aberto:** quem vê a nota (só o operador, ou equipe/Nio também). Ranking entre operadores depende de alinhamento com a Nio.

## Telas comuns e árvore por subobjeto — definido em 18/11
- Depois de "cliente tem registro na Nio = sim", entram as **telas comuns a todos os casos** (principalmente status do contrato e dados cadastrais). São exigidas em todos.
- Mecanismo: lista suspensa **"Sistema – tela"** (ex.: SIEBEL – Dados cadastrais, SALESFORCE – Dados cadastrais). Ao escolher, abre um campo para a imagem e a descrição, e **a opção usada some da lista**. Isso evita deixar todos os campos expandidos e, ao mesmo tempo, avisa o operador de que a tela existe. Serve principalmente para casos em que não há todas as telas.
- Fora as telas comuns, cada **subobjeto tem sua própria árvore de perguntas** (issue tree). As respostas indicam quais telas deveriam existir.
- Ordem no documento final segue a ordem definida nas regras, não a ordem em que o operador adiciona.
- Priorização dos subobjetos (base histórica): os 7 maiores (Interrupção, Cancelamento Não Realizado, Pagamento Não Reconhecido, Contestação de Permanência, Negativação Após Pagamento, Contratação Não Reconhecida, Cobrança Após Cancelamento) cobrem cerca de 75% dos casos; com mais 5 (Instabilidade, Débito Não Reconhecido, Alteração de Data de Vencimento, Mudança Não Realizada, Valor Divergente) chega a cerca de 88%.
- Candidatas a tela comum (itens do checklist marcados como "todos os subobjetos"): dados cadastrais (A01), contrato/terminal/produto (A02), oferta apresentada (A07), OS/TT (B14), disponibilidade do sinal (C29), histórico de faturas (F51), histórico de inadimplência (F55), documentos da contratação (H71). Definir quais são obrigatórias.

## Fonte do questionário por subobjeto — definido em 18/11
- **Fonte principal: os arquivos .xlsx da pasta "Checklist - Subsidios"** (ex.: `01. Interrupcao.xlsx`, com abas Questionário e Listas e regra automática de conclusão). Eles prevalecem sobre as abas por subobjeto da planilha da árvore.
- Começar o protótipo por **Interrupção**: triagem guiada em ordem de investigação (sinal/equipamento, área de risco, massiva, manutenção programada, vandalismo, inadimplência, ambiente do cliente, falha não identificada), com telas por etapa.
- Conclusão sugerida pela regra do arquivo; operador confirma e deixa rastro se mudar.
- Matriz Causa Real (planilha da árvore) como referência de causa por subobjeto; a lista MECE da base histórica é apoio.
- Tipos de evidência: tela de sistema e documento anexo.

## Área de risco e BO — definido em 18/11
- **Área de risco:** as duas telas servem como prova, **Portal V.tal (validação de área de risco)** e **CEC**. O app aceita qualquer uma das duas (ou ambas). O Portal BI – Área de Risco não foi citado e fica de fora até ela dizer o contrário.
- **BO de ocorrência:** fica **por fora, não entra no dossiê**. Não gera tela nem item de nota no app.

## Fluxo de cadastro — definido em 18/11 (versão final)
- Pergunta única: "O cliente tem cadastro ou contrato com a Nio?"
- Sim: fluxo normal de telas (comuns + árvore do subobjeto). Não pergunta próprio vs terceiro.
- Não: evidência de ausência + perguntas de tentativa (linha, nome parcial, CPF, contrato); as demais telas deixam de ser exigidas.
- Em aberto: a conclusão nesse caso é sugerida automaticamente (ex.: autor não tem razão) ou o operador escolhe? Quantas checagens são obrigatórias?

## Protótipo v1 (Interrupção) — 18/11
- Artefato publicado: etapas Identificação, Cadastro, Telas comuns, Triagem de Interrupção (blocos 1 a 9 na ordem do xlsx), Conclusão, Revisão e download.
- Pontos que decidi sozinha e precisam de validação: (1) telas comuns obrigatórias = uma tela de contrato (Tela Única, Siebel ou Salesforce); protocolos como sugerida; (2) com "Não" no cadastro, as quatro checagens são obrigatórias para liberar a evidência; (3) bloco 8 (prova técnica) foi unificado com o bloco 2 nas perguntas de estabilidade e "print anexado" virou a própria tela; (4) o tipo "ambiente interno do cliente" não consta na lista de tipos de excludente do xlsx; (5) Falha na ONT, Drop rompido e Manutenção não programada seguem sem causa real final no xlsx; (6) nomes de tela marcados "a validar" no app: Siebel – Detalhe do TT, CEC – Histórico de interrupções, CEC – Área de risco, NAF – Estabilidade, Portal V.tal – Manutenção programada, Portal Operacional V.tal – Chamados, Comunicação ao cliente, RST assinado.
- Limites desta versão: logotipo de cauda longa provisório (falta o SVG oficial); leitura de texto (OCR) pode não rodar dentro do visualizador do artefato, então a confirmação humana de legibilidade continua obrigatória; sem histórico de gerações (parte 2).

## Identidade visual e dossiê — definido em 18/11 (v8)
- **Paleta:** foco nos verdes da identidade (neon #32E000, verde-escuro #192B1C, verde-médio #1A7200, verde-claro #D6E3D8, abacate #C3FF05, areia #F8F7F0, areia-escuro #A7AC98). Cores secundárias (coral, laranja, amarelo) só como **detalhe pequeno** (pontos de cor em tags e cartões, nunca fundos grandes).
- **Gradientes:** suaves, da marca (areia-escuro → abacate → neon). Nota 0–10 muda de cor conforme se aproxima de 10.
- **Nota:** descrição de cada dimensão fica num ícone "i" (não escrita na tela). Segue apenas orientativa.
- **Tags de destaque no dossiê:** Área de risco, Legitimidade passiva e **Subobjeto alterado** (com original → novo), aparecendo na capa e na página de resumo (PDF, PPTX e DOCX).
- **Capa:** fundo verde-escuro com ondas, logo completo da Nio em verde-neon, campos como tags maiores. Telas: título e rodapé do template anterior, área de imagem maior.
- **Menu lateral:** bloco do logo com divisor, barra "Etapa X de 6", linha do tempo vertical ligando as etapas (concluída = check vazado, ativa = realce verde suave), links secundários discretos.
- **Logo e ondas** extraídos do PDF de referência (Dossiê de Litigância Abusiva); o SVG oficial ainda não foi enviado.
- **Verificação de imagem:** formato, resolução, contraste e nitidez rodam no visualizador. A leitura de texto (OCR) não roda no visualizador do artefato: há botão "Pedir leitura por IA" e a confirmação humana de legibilidade segue obrigatória (botão por IA ainda não testado no visualizador real).
- **Em aberto:** destacar legitimidade passiva quando "Sim" ou quando "Não" (ilegitimidade)?

## Identidade visual do app — decisão de 18/11 (v16)
- A Gabrieli preferiu manter o visual do artefato como estava antes dos ajustes pelo guia de identidade (v16 do app). Essa é a base para novas construções e ajustes.
- Resumo: fundo areia, verdes da marca protagonistas, cores secundárias só como pontos pequenos, gradientes suaves, cartão da nota em verde-claro com número leve, menu lateral com linha do tempo e ondas no rodapé, PDF em destaque no download, botão de colar imagem, sem leitura por IA.
- O guia do Manual de Identidade (fev/2026) foi lido por completo. Regras de módulos (sem cor de apoio, gradiente ou logo dentro de pílulas), ícones funcionais, tamanho mínimo de fonte (16 px) e pesos não muito leves ficam como referência, sem aplicar ao app por ora.
- Pendências: logo em SVG, ícones oficiais (check etc.) e fonte BW Gradual.
