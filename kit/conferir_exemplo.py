#!/usr/bin/env python3
"""Conferência determinística local, sem IA, rede ou ações externas."""
import argparse
import csv
import datetime as dt
import json
from pathlib import Path

def conferir(arquivo, referencia):
    vistos={}; candidatos=[]; problemas=[]
    with Path(arquivo).open(encoding='utf-8',newline='') as f:
        leitor=csv.DictReader(f)
        if not {'id','nome','ultimo_contato','interesse'} <= set(leitor.fieldnames or []):
            raise ValueError('CSV sem colunas obrigatórias: id,nome,ultimo_contato,interesse')
        for linha,r in enumerate(leitor,2):
            if not r['id'].strip():
                problemas.append({'linha':linha,'problema':'id ausente'}); continue
            if r['id'] in vistos:
                problemas.append({'linha':linha,'id':r['id'],'problema':'id duplicado','primeira_linha':vistos[r['id']]['linha']})
                if r != vistos[r['id']]['registro']:
                    candidatos[:]=[c for c in candidatos if c['id']!=r['id']]
                    vistos[r['id']]['conflito']=True
                    problemas.append({'linha':linha,'id':r['id'],'problema':'registros conflitantes: revisar antes de recomendar'})
                continue
            vistos[r['id']]={'linha':linha,'registro':r}
            try:
                data=dt.date.fromisoformat(r['ultimo_contato'])
                if data>referencia: raise ValueError('data futura')
            except ValueError:
                problemas.append({'linha':linha,'id':r['id'],'problema':'data ausente, inválida ou futura'}); continue
            dias=(referencia-data).days
            if dias>30:
                candidatos.append({'id':r['id'],'nome':r['nome'],'dias':dias,'linha':linha})
    return {'modo':'regra fixa sem IA','dados':'exemplo fictício; nenhum ganho medido','referencia':str(referencia),'criterio':'mais de 30 dias sem contato registrado','candidatos':candidatos,'problemas':problemas,'mensagens_enviadas':0}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--arquivo',type=Path,default=Path(__file__).with_name('clientes-ficticios.csv'))
    p.add_argument('--referencia',type=dt.date.fromisoformat,default=dt.date(2026,11,16))
    a=p.parse_args()
    try: print(json.dumps(conferir(a.arquivo,a.referencia),ensure_ascii=False,indent=2))
    except (OSError,ValueError) as e: p.exit(1,f'Erro: {e}\n')
