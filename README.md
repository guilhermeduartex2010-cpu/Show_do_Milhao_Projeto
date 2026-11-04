# Projeto Show do Milhão — Python + Supabase + Ranking Web

## Integrantes
- Integrante 1: Guilherme Duarte Araujo
- Turma: 1 IA B

## O que está implementado
- Jogo de terminal em Python com apelido obrigatório, menu e até 9 perguntas sem repetição.
- Sequência de dificuldades: 3 fáceis, 3 médias e 3 difíceis.
- Prêmios fictícios conforme o enunciado; o prêmio substitui o anterior, não soma.
- Cronometragem com `time.perf_counter()`.
- Banco Supabase para perguntas, jogos e partidas.
- ID UUID por partida para impedir duplicação em uma repetição do mesmo envio.
- Ranking online por jogo, melhor partida de cada apelido e desempate por valor, tempo, data e ID.
- Site estático compatível com GitHub Pages.

## 1. Criar o banco
1. Crie um projeto no Supabase.
2. Abra SQL Editor e execute `schema.sql`.
3. Confira se foram criadas 15 perguntas (5 por dificuldade).
4. Revise perguntas e gabaritos antes da entrega.

## 2. Executar o jogo   
```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```
Copie `.env.example` para `.env` e preencha `SUPABASE_URL` e `SUPABASE_KEY` com a URL e a chave anon/public do projeto. Execute:
```bash
python jogo.py
```

## 3. Publicar o site
1. Edite `config.js` com a URL do projeto e a chave anon/public.
2. Publique `index.html`, `style.css`, `app.js` e `config.js` em um repositório GitHub.
3. Em Settings > Pages, publique a branch/pasta escolhida.
4. Abra o link publicado e teste o filtro e o botão Atualizar.

**Segurança:** nunca use a chave `service_role` no navegador, no repositório ou na entrega. As políticas SQL são permissivas para protótipo escolar; peça ao professor para revisar permissões. Para uma competição pública, a pontuação deve ser validada no servidor.

## Arquivos
- `jogo.py`: programa Python.
- `schema.sql`: tabelas, políticas e perguntas.
- `index.html`, `style.css`, `app.js`, `config.js`: site.
- `requirements.txt`: dependências.
- `.env.example`: modelo de configuração sem credenciais.
- `prompts.md`: registro inicial dos prompts; acrescentar todos os prompts reais usados durante o projeto.
- `testes.md`: roteiro de validação.

## Links do projeto

Repositório GitHub: https://github.com/guilhermeduartex2010-cpu/Show_do_Milhao_Projeto

Site publicado (GitHub Pages): https://guilhermeduartex2010-cpu.github.io/Show_do_Milhao_Projeto/

## Pendências antes da entrega
- Configurar o Supabase e testar a conexão real.
- Realizar e registrar os testes; capturar evidências reais.
- Atualizar `prompts.md` com todos os prompts completos, datas, responsáveis, ferramenta/modelo, uso e testes.
