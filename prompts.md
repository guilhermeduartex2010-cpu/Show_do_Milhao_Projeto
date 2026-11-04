# Registro de uso de IA — atualizar durante o projeto

> Importante: este arquivo contém o prompt inicial desta conversa. Acrescente, em ordem cronológica, o texto integral de cada prompt usado por cada integrante em qualquer ferramenta de IA. Não registre apenas resumos. Remova credenciais e dados pessoais.

## Registro 1
- Data: 03/11/2026
- Integrante responsável: preencher
- Ferramenta: ChatGPT
- Modelo: GPT-6
- Objetivo: desenvolver o projeto escolar descrito no arquivo AC04_Show_Milhão_v1.docx.
- Prompt completo:
  "Desenvolva um projeto acadêmico completo chamado **Show do Milhão**, seguindo rigorosamente todos os requisitos do documento `AC04_Show_Milhão_v1.docx`.

O projeto deve utilizar Python para o jogo, Supabase como banco de dados e HTML, CSS e JavaScript para um site de ranking online.

### 1. Jogo em Python
- Solicite um apelido não vazio ao jogador e utilize somente esse apelido no ranking público.
- Apresente 9 perguntas por partida, sem repetição: 3 fáceis, 3 médias e 3 difíceis, nessa ordem.
- Mantenha pelo menos 15 perguntas cadastradas no banco, sendo 5 de cada dificuldade.
- Cada pergunta deve ter quatro alternativas e exatamente uma resposta correta.
- Utilize os seguintes prêmios: R$ 1.000,00, R$ 5.000,00, R$ 10.000,00, R$ 25.000,00, R$ 50.000,00, R$ 100.000,00, R$ 200.000,00, R$ 500.000,00 e R$ 1.000.000,00.
- O prêmio conquistado substitui o anterior, sem somar os valores.
- Encerre a partida quando o jogador errar, desistir ou responder às nove perguntas.
- Permita tentar novamente quando a entrada for inválida, sem contabilizar a tentativa como resposta.
- Meça o tempo da partida com `time.perf_counter()`, excluindo o menu e o tempo de gravação no banco.
- Utilize funções separadas para buscar perguntas, executar a partida, calcular prêmios e salvar resultados.

### 2. Banco de dados e Supabase
- Utilize as tabelas `jogos`, `perguntas` e `partidas`, conforme o enunciado.
- Configure a conexão por variáveis de ambiente, utilizando `.env` localmente e `.env.example` sem credenciais reais no projeto.
- Salve cada partida apenas uma vez, utilizando um identificador único para evitar duplicações em tentativas de reenvio.
- Caso ocorra falha de conexão, informe o jogador e mantenha o resultado em memória para permitir nova tentativa de gravação.
- Nunca informe que uma partida foi salva sem confirmar o sucesso da operação.
- Prepare o SQL de criação das tabelas, as permissões necessárias e as consultas utilizadas pelo ranking.
- Não exponha chaves secretas ou permissões administrativas no código público do site.

### 3. Site de ranking
- Consulte os resultados diretamente no Supabase, sem utilizar uma lista fixa de partidas.
- Exiba posição, nome do jogo, apelido, prêmio, duração e data da partida.
- Formate os valores em reais, como `R$ 1.000.000,00`, e o tempo em minutos e segundos.
- Disponibilize filtro por jogo e botão para atualizar o ranking.
- Mostre os dez melhores resultados do jogo selecionado.
- Ordene por maior prêmio, menor duração, data mais antiga e identificador da partida, conforme o enunciado.
- Considere o melhor resultado de cada apelido em cada jogo.
- Apresente mensagens claras quando não houver resultados ou quando ocorrer erro na consulta.
- Garanta que o site funcione independentemente de o programa Python estar aberto.

### 4. Perguntas e fontes
- Cadastre pelo menos 15 perguntas revisadas, com 5 de cada dificuldade.
- Confira os enunciados, as quatro alternativas, o gabarito e a dificuldade.
- Registre fontes confiáveis para verificar as informações e os gabaritos.
- Não invente referências nem considere uma resposta correta sem verificá-la.

### 5. Documentação e testes
- Atualize o `README.md` com nomes completos dos dois integrantes, turma, regras, instalação, execução, configurações e links do repositório e do site publicado.
- Mantenha `requirements.txt` atualizado com as dependências utilizadas.
- Registre os prompts completos de inteligência artificial em ordem cronológica no `prompts.md`, incluindo correções, ferramenta/modelo, data, responsável, finalidade, utilização das respostas, arquivos afetados e testes realizados.
- Documente os testes com resultado esperado, resultado observado e correções aplicadas.
- Teste uma partida perfeita, uma resposta errada, desistência, apelido vazio, alternativa inválida, desempate, falha de conexão, nova tentativa de gravação e atualização do ranking.
- Registre somente testes que realmente foram executados.
- Prepare capturas de tela do jogo Python e do site exibindo o resultado da mesma partida, com apelido, prêmio e duração.

### 6. Forma de trabalho
Antes de alterar o código, analise todos os arquivos existentes e compare-os com o enunciado. Preserve as funcionalidades corretas e não substitua arquivos completos sem necessidade.

Trabalhe de forma incremental: identifique um problema, explique a causa, apresente a alteração necessária e forneça os passos para executá-la e testá-la. Não afirme que algo está funcionando sem evidências.

Ao concluir, apresente uma lista dos requisitos atendidos e pendentes, os testes executados e as instruções para preparar o ZIP final. Não inclua `.env`, chaves secretas ou a pasta `.venv` no ZIP.

**Prioridade máxima:** cumprir fielmente o enunciado oficial, manter o jogo, o banco e o ranking integrados e produzir um projeto que os integrantes consigam executar, testar e explicar na apresentação."
- Arquivos/funções envolvidos: estrutura inicial do projeto; `jogo.py`, `schema.sql`, arquivos do site.
- Como a resposta foi utilizada: base inicial de implementação, que deve ser revisada, testada e modificada pela dupla.
- Teste realizado: ainda não executado nesta geração.
- Problema encontrado e correção: pendente de registrar após os testes.

## Fontes consultadas para as perguntas
- Tutorial oficial Python: https://docs.python.org/3/tutorial/
- Funções embutidas: https://docs.python.org/3/library/functions.html
- Módulo time: https://docs.python.org/3/library/time.html
- Requests Quickstart: https://requests.readthedocs.io/en/latest/user/quickstart/

## Próximos registros
Adicionar cada prompt integral de correção/refinamento e documentar o teste e a alteração correspondente.
