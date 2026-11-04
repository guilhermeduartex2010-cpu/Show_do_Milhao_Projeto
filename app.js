const statusEl = document.querySelector("#status");
const selectEl = document.querySelector("#jogo");
const tbody = document.querySelector("#ranking");
const headers = {
  apikey: window.SUPABASE_ANON_KEY,
  Authorization: `Bearer ${window.SUPABASE_ANON_KEY}`
};
function configurado() {
  return window.SUPABASE_URL && !window.SUPABASE_URL.includes("SEU-PROJETO") &&
    window.SUPABASE_ANON_KEY && !window.SUPABASE_ANON_KEY.includes("SUA_CHAVE");
}
async function consultar(tabela, params) {
  const url = new URL(`${window.SUPABASE_URL}/rest/v1/${tabela}`);
  Object.entries(params).forEach(([k,v]) => url.searchParams.set(k,v));
  const response = await fetch(url, {headers});
  if (!response.ok) throw new Error(`Consulta falhou (${response.status}).`);
  return response.json();
}
async function carregarJogos() {
  if (!configurado()) throw new Error("Configure URL e chave anon no arquivo config.js.");
  const jogos = await consultar("jogos", {select:"id,nome",order:"nome.asc"});
  selectEl.innerHTML = "";
  jogos.forEach(j => {
    const option = document.createElement("option");
    option.value = j.id; option.textContent = j.nome; selectEl.append(option);
  });
  if (!jogos.length) statusEl.textContent = "Nenhum jogo cadastrado.";
  else await carregarRanking();
}
function moeda(valor) {
  return Number(valor).toLocaleString("pt-BR",{style:"currency",currency:"BRL"});
}
function tempo(segundos) {
  const total = Math.max(0, Math.floor(Number(segundos)));
  return `${Math.floor(total/60)}m ${String(total%60).padStart(2,"0")}s`;
}
async function carregarRanking() {
  try {
    if (!selectEl.value) { tbody.innerHTML=""; return; }
    statusEl.textContent = "Atualizando...";
    const jogo = await consultar("jogos", {select:"id,nome",id:`eq.${selectEl.value}`});
    const partidas = await consultar("partidas", {
      select:"id,apelido,valor_ganho,tempo_segundos,data_hora,jogo_id",
      jogo_id:`eq.${selectEl.value}`,
      order:"valor_ganho.desc,tempo_segundos.asc,data_hora.asc,id.asc"
    });
    const melhores = new Map();
    for (const p of partidas) {
      const chave = p.apelido.trim().toLocaleLowerCase("pt-BR");
      if (!melhores.has(chave)) melhores.set(chave,p);
    }
    const top = [...melhores.values()].slice(0,10);
    tbody.innerHTML = "";
    top.forEach((p,i) => {
      const tr = document.createElement("tr");
      const data = new Date(p.data_hora).toLocaleString("pt-BR");
      [i+1, jogo[0]?.nome || "—", p.apelido, moeda(p.valor_ganho), tempo(p.tempo_segundos), data]
        .forEach(v => { const td=document.createElement("td"); td.textContent=v; tr.append(td); });
      tbody.append(tr);
    });
    statusEl.textContent = top.length ? `${top.length} resultado(s) encontrado(s).` : "Ainda não há resultados para este jogo.";
  } catch (e) { statusEl.textContent = `Não foi possível consultar o ranking: ${e.message}`; }
}
selectEl.addEventListener("change", carregarRanking);
document.querySelector("#atualizar").addEventListener("click", carregarRanking);
carregarJogos().catch(e => statusEl.textContent = `Erro de conexão: ${e.message}`);
