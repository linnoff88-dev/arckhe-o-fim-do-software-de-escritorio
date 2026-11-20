# Revisão visual — tentativa 1

MP4 de 177,04 s; QA técnico aprovado com aviso. Cinco quadros e folha marcada vistos nesta sessão.

- Visual: 6/10. Avatar herdou posição alta e cobriu o segundo bloco OIT em 75%; imagem de leitura ocupou a borda sob a marca. A chamada final não apareceu porque a pose mini herdada prevaleceu sobre o rosto.
- Ritmo: 8/10. Dez cenas e deixas da fala; a última chamada precisava aparecer mais cedo.
- Marca: 9/10. Linha INEMA âmbar, Montserrat e marca consistentes; capa legível no primeiro quadro.

Reprovado para publicação. Menor correção: avatar mini em cada foto de leitura; imagem inteira contida em área própria abaixo da marca e à esquerda do avatar; encerramento cinético visível na deixa, com três entradas. Patch apenas no runtime copiado desta produção. Nenhum reenvio HeyGen. Build estrito corrigido passou sem avisos. Segunda renderização local em andamento.

# Revisão final — tentativa 2, aprovada

MP4 final 177,04 s (2 min 57 s), 1920×1080, 25 fps, voz e trilha. Cinco quadros finais e folha marcada revistos após o render (01:58). Snapshots adicionais em 132,78 / 174,08 / 176,9 s conferidos.

- Visual: 8/10. Diagramas inteiros, sem sobreposição do avatar; legenda em área própria. Capa já visível no frame zero. Fundo desfocado das cinéticas é decorativo, não material de leitura; no último décimo de segundo a manchete sai com desfoque, mas foi legível antes (snapshot 176,9 s).
- Ritmo: 8/10. Dez cenas distintas, cinéticas nas deixas e encerramento com três entradas. Quadros de leitura ficam estáveis para permitir conferir as linhas; o avatar e as legendas continuam ativos.
- Marca: 9/10. Linha INEMA âmbar, marca superior e tipografia consistentes.

QA: aprovado com aviso de áreas lisas nos diagramas contidos (fundos pretos e cartões claros intencionais). Nenhum quadro vazio ou trecho parado reprovado; área lisa forte acima de 60% em 0% da duração. HyperFrames: lint/runtime/layout sem erros; 27/27 contrastes AA; informação de sobreposição em 174,08 s corresponde à entrada animada, texto estável conferido sem colisão. Build estrito sem avisos, alinhamento 0,9878. Mesmo ID HeyGen preservado.

Player: controles e layouts 390/1440 aprovados sem overflow ou erros JS. URLs públicas do MP4, VTT, player e guias PT/EN/ES respondem200. Reprodução no Chromium headless não confirmada: canPlayType H.264/AAC retorna vazio neste ambiente; arquivo H.264 High/yuv420p/AAC decodificado integralmente pelo FFmpeg.
