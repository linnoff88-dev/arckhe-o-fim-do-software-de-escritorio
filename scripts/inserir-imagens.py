#!/usr/bin/env python3
"""Insere a ilustração de cada tópico ao lado do h2 (float à direita, antes do h2) da seção, no guia PT, EN e ES. Idempotente."""
import json, re, html
from pathlib import Path
from PIL import Image

R = Path(__file__).resolve().parents[1]
dados = json.loads((R / 'scripts/imagens.json').read_text())
paginas = {'pt': (R / 'guia/index.html', 'assets/topicos/'),
           'en': (R / 'guia/en/index.html', '../assets/topicos/'),
           'es': (R / 'guia/es/index.html', '../assets/topicos/')}

for lang, (arq, pref) in paginas.items():
    s = arq.read_text()
    n = 0
    for sid, leg in dados['legendas'].items():
        jpg = R / 'guia/assets/topicos' / f'{sid}.jpg'
        if not jpg.exists() or f'data-topico="{sid}"' in s:
            continue
        w, h = Image.open(jpg).size
        txt = html.escape(leg[lang])
        fig = (f'<figure class="wide topico" data-topico="{sid}"><img src="{pref}{sid}.jpg" width="{w}" height="{h}" '
               f'alt="{txt}" loading="lazy" decoding="async"><figcaption>{txt}</figcaption></figure>')
        pat = re.compile(rf'(<section id="{sid}"><div class="wrap">)(?=<h2>)', re.S)
        s, k = pat.subn(lambda m: m.group(1) + fig, s, count=1)
        n += k
    if '.topico{' not in s:
        s = s.replace('</style>', 'section .wrap{display:flow-root}.topico{float:right;width:min(38%,400px);margin:4px 0 16px 32px}.topico img{aspect-ratio:3/2;object-fit:cover;border-radius:12px}.topico figcaption{font-size:.8rem;line-height:1.4}.table-wrap{clear:both}.topico:has(+h2+.table-wrap){width:min(30%,280px)}@media(max-width:820px){.topico{width:42%;margin:4px 0 8px 16px}.topico figcaption{display:none}}</style>', 1)
    arq.write_text(s)
    print(lang, 'inseridas', n)
