#!/usr/bin/env python3
"""Gera a página PT a partir de docs/guia-completo.md e do template INEMA preservado."""
from pathlib import Path
import re,markdown,html
R=Path(__file__).resolve().parents[1]
template=(R/'scripts/template-inema.html').read_text()
css=re.search(r'<style>(.*?)</style>',template,re.S)[1]
css=css.replace('#E2A23B','#FACC15').replace('#e2a23b','#FACC15').replace('#b9791d','#a16207')
body=markdown.markdown((R/'docs/guia-completo.md').read_text(),extensions=['tables','fenced_code'])
parts=re.split(r'<h2>(.*?)</h2>',body)
sections=[]
slugs=['resumo','pergunta','comparacao','exemplo','capacidade','arquitetura','destinatario','software','pessoas','preparar','plano','tempo','limites','dentro']
for i in range(1,len(parts),2):
 title,content=parts[i:i+2];slug=slugs[(i-1)//2]
 content=re.sub(r'(<table>.*?</table>)',r'<div class="table-wrap" tabindex="0" role="region" aria-label="Tabela com rolagem horizontal">\1</div>',content,flags=re.S)
 if slug=='resumo': content+='<figure class="wide"><img src="assets/banner-grade.jpg" width="1400" height="788" alt="Planilha, documento, apresentação, CRM, reunião e indicadores conectados a um resultado" loading="lazy"><figcaption>As ferramentas se organizam em torno do trabalho que precisa acontecer.</figcaption></figure>'
 sections.append(f'<section id="{slug}"><div class="wrap"><h2>{title}</h2>{content}</div></section>')
 if slug=='resumo':sections.append('<section id="video"><div class="wrap"><h2>Entenda a visão em vídeo</h2><!-- VIDEO: entra o explicavideo do projeto quando publicado --><p>O vídeo com Nei Maldaner está em produção. Enquanto isso, acompanhe o exemplo e o plano de transição abaixo.</p><a class="btn" href="#exemplo">Ver o exemplo do começo ao fim</a></div></section>')
extra='''
nav{background:var(--bg)}
:root{--btn-ink:#1a1206;--code-bg:#0a0a0e;--code-txt:#e9e9ee;--focus:#FACC15;--glow:rgba(250,204,21,.12)}
body.light{--amb:#854d0e;--focus:#854d0e;--glow:rgba(250,204,21,.15)}
*{scroll-margin-top:120px}body{font-size:16px;line-height:1.7}main p,main li{max-width:74ch}main p{margin:1em 0}main ul,main ol{padding-left:24px;margin:16px 0}h2{margin-bottom:24px;line-height:1.2}h3{margin:32px 0 12px;line-height:1.2;font-family:Sora}a{text-underline-offset:4px}a:hover{text-decoration:underline}a:active,button:active{transform:translateY(1px)}:focus-visible{outline:3px solid var(--focus);outline-offset:4px}.skip{position:absolute;top:-100px;left:16px;background:var(--bg);padding:12px;z-index:100}.skip:focus{top:8px}.chip{font-size:.75rem}.wrap{max-width:1160px}.hero .wrap{display:block;padding-top:64px}.hero h1{max-width:21ch;font-size:clamp(2.1rem,5vw,3.6rem);line-height:1.1}.hero p.lead{max-width:65ch}.hero figure{margin-top:32px;max-width:1160px}.hero figure img{aspect-ratio:1400/788;object-fit:cover}.wide{margin:32px 0 0}.wide img{width:100%;height:auto;display:block;border-radius:16px}.wide figcaption{font-size:.9rem;color:var(--mut);margin-top:8px}.table-wrap{overflow-x:auto;margin:24px 0;border:1px solid var(--line);border-radius:12px}table{width:100%;border-collapse:collapse;min-width:640px;text-align:left}th,td{padding:16px;border-bottom:1px solid var(--line);vertical-align:top}th{font-family:Sora;background:var(--bg2);font-size:.9rem}td{font-size:1rem}tr:last-child td{border:0}.techhead,.techzone{background:var(--bg2)}.techhead{border-top:1px solid var(--amb);padding:48px 0 0}.techzone section{background:var(--bg2)}pre{background:var(--code-bg);color:var(--code-txt);white-space:pre-wrap;overflow-wrap:anywhere;font-size:.9rem}.hero .glow{background:radial-gradient(closest-side,var(--glow),transparent 70%)}.btn{min-height:44px;display:inline-flex;align-items:center}.btn:not(.ghost){background:var(--focus);color:var(--btn-ink)}body.light .btn:not(.ghost){background:var(--focus);color:var(--txt);background:#FACC15}.tgl{width:44px;height:44px;flex-shrink:0}.lang a{min-width:44px;min-height:44px;display:inline-flex;align-items:center;justify-content:center}.downloads{display:flex;gap:16px;flex-wrap:wrap}.downloads a{padding:12px 0}.brand{font-size:.95rem;max-width:22ch;white-space:normal}.lang{display:flex;gap:8px}nav .wrap{min-height:72px;height:auto;padding-top:8px;padding-bottom:8px;flex-wrap:wrap}nav .links{flex-wrap:wrap}.sep{margin:0 4px}.clubpro{white-space:nowrap}.hero .cta{gap:16px}summary{cursor:pointer;min-height:44px;padding:12px 0;color:var(--amb);font-weight:700}details{border-block:1px solid var(--line);margin:24px 0}#conteudo{scroll-margin-top:120px}.muted{color:var(--mut)}@media(max-width:820px){nav .links .sec{display:none}.hero .wrap,section .wrap,footer .wrap{padding-left:16px;padding-right:16px}section{padding:40px 0}.hero .wrap{padding-top:40px}.brand{max-width:18ch}}@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important;transition:none!important;animation:none!important}}@media print{nav,.hero .cta,.tgl{display:none}body{background:white;color:black}.hero .wrap,section{padding-top:24px;padding-bottom:24px}.table-wrap{overflow:visible}a{color:inherit}section{break-inside:auto}}
'''
repo='https://github.com/inematds/o-fim-do-software-de-escritorio';base='https://inematds.github.io/o-fim-do-software-de-escritorio/guia/'
nav=f'''<a class="skip" href="#conteudo">Pular para o conteúdo</a><nav aria-label="Navegação principal"><div class="wrap"><a class="brand" href="#top">O fim do software de escritório</a><span class="sep">|</span><span class="clubpro"><a class="inema" href="https://inema.club" target="_blank" rel="noopener">INEMA.CLUB</a> · <a class="pro" href="https://inema.pro" target="_blank" rel="noopener">PRO</a></span><div class="links"><a class="sec" href="#comparacao">O que muda</a><a class="sec" href="#plano">Como se preparar</a><a class="sec" href="#tecnico">Kit (técnico)</a><span class="lang"><a class="on" href="./" lang="pt">PT</a><a href="en/" lang="en">EN</a><a href="es/" lang="es">ES</a></span><button class="tgl" id="themeToggle" aria-label="Alternar tema claro e escuro">☀</button></div></div></nav>'''
hero='''<header class="hero" id="top"><div class="glow"></div><div class="wrap"><span class="chip">Visão de Nei Maldaner · INEMA</span><h1>O fim do software de <span class="amb">escritório</span></h1><p class="lead">Você gasta o dia alimentando ferramentas enquanto as decisões ficam esperando? Aprenda a trabalhar pelo resultado, com a IA participando da análise e da execução.</p><div class="cta"><a class="btn" href="#pergunta">Entender a mudança</a><a class="btn ghost" href="#tecnico">Usar o kit gratuito</a></div><figure><img src="assets/banner.jpg" width="1400" height="788" fetchpriority="high" alt="O fim do software de escritório: Office, CRM, reuniões e relatórios conectados pela IA"></figure></div></header>'''
tech='''<div id="tecnico" class="techhead"><div class="wrap"><span class="chip">Parte técnica</span><h2>O kit: para quem quer testar no próprio trabalho</h2><p>Você não precisa desta parte para entender o que está acima.</p></div></div><div class="techzone"><section id="kit"><div class="wrap"><h2>Escolha um processo e faça um teste conferível</h2><p>O kit contém modelos de pedido, mapa de processo, medição de tempo e registro de decisão. O exemplo usa dados fictícios e um conferidor local de regra fixa. A conversa com IA é feita na ferramenta que você já utiliza; este projeto não fornece um modelo, integração ou agente autônomo.</p><div class="downloads"><a class="btn" href="../kit-inteligencia-operacional.zip" download>Baixar o kit completo (.zip)</a><a href="../kit/pedido-por-resultado.md">Abrir o pedido e a resposta esperada</a><a href="../kit/mapa-do-processo.md">Mapa do processo</a><a href="../kit/medir-antes-depois.csv">Ficha de medição (.csv)</a><a href="../kit/decisao-e-acompanhamento.md">Registro de decisão</a></div><h3>Primeiro uso, sem terminal</h3><ol><li>Baixe o ZIP, extraia e abra a pasta <strong>kit</strong>. Os arquivos .md são textos: use um editor de texto.</li><li>Abra <strong>pedido-por-resultado.md</strong>, leia o pedido e anexe <strong>clientes-ficticios.csv</strong> na conversa de IA que você já utiliza.</li><li>Faça o pedido do exemplo, mantendo os nomes de arquivo, IDs e data de referência. Nenhuma conexão ao CRM é necessária.</li><li>Compare a resposta com “Como conferir sem código”. Esperado: C001 e C004 candidatos únicos; C003 sem data; C004 duplicado. Isso é análise do cadastro fictício, sem envio de mensagens.</li><li>Preencha o mapa de um processo real. Só use dados empresariais em uma ferramenta aprovada pela organização.</li><li>Registre tempo completo e qualidade na ficha. Decida se vale repetir antes de automatizar.</li></ol><details><summary>Conferência opcional com Python</summary><p>Requer Python 3.9 ou superior. Este comando usa apenas a biblioteca padrão, funciona sem rede e não chama IA ou API. Abra o terminal na pasta extraída, que contém a pasta kit.</p><pre>python3 kit/conferir_exemplo.py</pre><p>No Windows, com Python instalado, use:</p><pre>py -3 kit/conferir_exemplo.py</pre><p>Para usar outro arquivo no mesmo formato e uma data explícita:</p><pre>python3 kit/conferir_exemplo.py --arquivo kit/clientes-ficticios.csv --referencia 2026-11-16</pre><p>Saída esperada: 2 candidatos únicos (76 e 46 dias), 2 problemas de cadastro e 0 mensagens enviadas. Duplicatas conflitantes são retiradas da recomendação. O campo <strong>modo</strong> declara “regra fixa sem IA”.</p><p>Se o comando não existir, instale Python pela distribuição oficial do seu sistema ou faça a conferência manual acima.</p></details></div></section><section id="fontes"><div class="wrap"><h2>Fontes, autoria e limites</h2><ul><li>Visão autoral de Nei Maldaner, documento de 15/11/2026: <a href="../docs/visao-original.md">Do software à inteligência operacional</a>.</li><li><a href="https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure">OIT — exposição ocupacional à IA generativa (2025)</a>. Exposição de tarefas não é uma previsão de demissões.</li><li><a href="https://www.microsoft.com/en-us/copilot/features/work-iq">Microsoft — Work IQ</a>. Descrição de uma camada de contexto organizacional, sem medição de produtividade deste projeto.</li><li><a href="../docs/resultado-exemplo.json">Resultado real do conferidor local</a>, com cadastro inteiramente fictício.</li></ul><p>Análise editorial preparada em 16/11/2026. As previsões de mercado são cenários; o exemplo é didático. Não medimos ganhos em empresas neste projeto.</p></div></section></div>'''
js="""(()=>{const b=document.body,t=document.getElementById('themeToggle');let saved;try{saved=localStorage.getItem('fim-software-theme')}catch(e){}if(saved==='light')b.classList.add('light');function label(){const l=b.classList.contains('light');t.textContent=l?'☾':'☀';t.setAttribute('aria-pressed',String(l))}label();t.addEventListener('click',()=>{b.classList.toggle('light');label();try{localStorage.setItem('fim-software-theme',b.classList.contains('light')?'light':'dark')}catch(e){}})})();"""
head=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>O fim do software de escritório | Nei Maldaner · INEMA</title><meta name="description" content="Da operação de Office e CRM à inteligência operacional: visão, exemplos, impacto nas funções e kit gratuito para trabalhar pelo resultado."><meta name="theme-color" content="#0c0c10"><meta property="og:title" content="O fim do software de escritório"><meta property="og:description" content="Você ainda trabalha para alimentar ferramentas? Aprenda a começar pelo resultado."><meta property="og:image" content="{base}assets/banner.jpg"><link rel="canonical" href="{base}"><link rel="alternate" hreflang="pt-BR" href="{base}"><link rel="alternate" hreflang="en" href="{base}en/"><link rel="alternate" hreflang="es" href="{base}es/"><link rel="alternate" hreflang="x-default" href="{base}"><link rel="icon" href="assets/logo.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet"><style>{css}\n{extra}</style></head><body>'''
footer=f'<footer><div class="wrap"><p>Nei Maldaner · Conteúdo aberto e gratuito · v1.1.1</p><a href="{repo}">Repositório e materiais</a> · <a href="https://inema.club">INEMA.CLUB</a> · <a href="https://inema.pro">INEMA.PRO</a></div></footer>'
(R/'guia/index.html').write_text(head+nav+hero+'<main id="conteudo">'+''.join(sections)+tech+'</main>'+footer+f'<script>{js}</script></body></html>')
resumo=re.search(r'<section id="resumo".*?<p>(.*?)</p>', ''.join(sections),re.S)[1]
(R/'README.md').write_text(f'''# O fim do software de escritório

[![O fim do software de escritório](guia/assets/banner.jpg)]({base})

**[Português](README.md) · [English](README.en.md) · [Español](README.es.md)**

## O que é

{resumo}

## Guia e kit gratuitos

Leia o **[guia completo]({base})** e baixe o **[kit]({base.replace('/guia/','/')}kit-inteligencia-operacional.zip)**.

- [Visão original de Nei Maldaner](docs/visao-original.md).
- [Pedido por resultado, exemplo e resposta esperada](kit/pedido-por-resultado.md).
- [Mapa do processo](kit/mapa-do-processo.md).
- [Medição de tempo e qualidade](kit/medir-antes-depois.csv).
- [Registro de decisão e acompanhamento](kit/decisao-e-acompanhamento.md).

## Executar o exemplo opcional

Requer Python 3.9+. Extraia o ZIP e abra o terminal na pasta que contém kit, ou execute na raiz deste repositório:

```bash
python3 kit/conferir_exemplo.py
```

Windows: `py -3 kit/conferir_exemplo.py`. Sem Python, siga a conferência manual no guia.

Esperado: C001 (76 dias) e C004 (46 dias), duplicidade C004 e data ausente C003. Zero mensagens enviadas. **Conferidor determinístico, sem IA ou rede.** Para usar IA, copie o pedido e anexe o CSV na conversa de uma ferramenta que você já utiliza. Nenhum ganho de produtividade empresarial foi medido.

## Vídeo

Explicavideo com o avatar de Nei Maldaner em produção para lives11. O link será inserido aqui e no guia quando publicado.

## Autoria e fontes

Tese de Nei Maldaner; conteúdo educacional aberto. Falências e redução de equipes são cenários, não previsões garantidas. [OIT (2025)](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) · [Microsoft Work IQ](https://www.microsoft.com/en-us/copilot/features/work-iq).

## Manutenção

O conteúdo PT está em docs/guia-completo.md. `python3 scripts/gerar_guia.py` usa o template INEMA preservado e requer o pacote Python markdown. Traduções: inema-traduz pela assinatura. A geração do guia substitui o HTML PT; preserve qualquer embed de vídeo que já tiver sido publicado. Publicação via git/GitHub Pages.
''')
print('Guia PT gerado:',len(sections),'seções editoriais')
