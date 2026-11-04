# Plano e registro de testes

Preencher a coluna “Resultado observado” após executar o projeto. Não marcar como aprovado sem testar.

| Caso | Resultado esperado | Resultado observado |
|---|---|---|
| Partida com 9 acertos | Prêmio final R$ 1.000.000,00; valores não somados | Pendente |
| Erro na primeira questão | Encerrar com R$ 0,00 | Pendente |
| Erro após alguns acertos | Manter o último prêmio alcançado | Pendente |
| Desistência | Encerrar e manter o prêmio atual | Pendente |
| Apelido vazio | Solicitar novamente | Pendente |
| Alternativa inválida | Solicitar novamente | Pendente |
| Ordem das perguntas | 3 fáceis, 3 médias, 3 difíceis | Pendente |
| Sem repetição | Nenhuma pergunta repetida na partida | Pendente |
| Menos de 3 perguntas em um nível | Informar insuficiência e não iniciar | Pendente |
| Falha de conexão ao consultar | Exibir mensagem sem encerrar abruptamente | Pendente |
| Falha ao salvar e tentar novamente | Salvar uma única vez usando o mesmo UUID | Pendente |
| Mesmo prêmio, tempos diferentes | Menor tempo primeiro | Pendente |
| Apelido com várias partidas | Mostrar apenas sua melhor partida naquele jogo | Pendente |
| Jogos diferentes | Rankings separados | Pendente |
| Ranking sem resultados | Mostrar mensagem de ranking vazio | Pendente |
| Site com banco indisponível | Mostrar mensagem de falha | Pendente |

## Evidências a capturar
1. Terminal mostrando uma partida, apelido, prêmio e duração.
2. Supabase mostrando o registro da mesma partida.
3. Site publicado mostrando o mesmo apelido, prêmio e tempo.
4. Teste de ranking vazio e falha de consulta, se possível.
