#!/usr/bin/env bash
# Gera uma ilustração por tópico do guia pelo Codex (image_gen, assinatura), sem texto (serve PT/EN/ES).
# Uso: scripts/gerar-imagens.sh [id ...]   (sem argumento = todas que faltam). 4 em paralelo.
set -u
cd "$(dirname "$0")/.."
RAIZ="$PWD"
mkdir -p guia/assets/topicos
IDS=("$@")
[ ${#IDS[@]} -eq 0 ] && mapfile -t IDS < <(python3 -c "import json;print('\n'.join(json.load(open('scripts/imagens.json'))['cenas']))")
gera() {
  id="$1"; cd "$RAIZ"
  d=guia/assets/topicos; jpg="$d/$id.jpg"; png="$d/$id.png"; log="$d/$id.log"
  [ -s "$jpg" ] && { echo "[$id] já existe"; return 0; }
  prompt=$(python3 - "$id" <<'PY'
import json,sys
d=json.load(open('scripts/imagens.json')); i=sys.argv[1]
print(f"Use sua ferramenta de geração de imagem (image_gen) para criar UMA imagem horizontal 16:9 e salve o PNG em guia/assets/topicos/{i}.png dentro deste diretório. Não edite nenhum outro arquivo.\n\nCena: {d['cenas'][i]}\n\nEstilo: {d['estilo']}")
PY
)
  rm -f "$png"
  printf '%s' "$prompt" | timeout 900 codex exec --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox - >"$log" 2>&1
  if [ -s "$png" ]; then
    ffmpeg -y -loglevel error -i "$png" -vf scale=1200:-2 -q:v 4 "$jpg" && rm -f "$png" "$log"
    echo "[$id] ok"
  else
    echo "[$id] FALHOU (ver $log)"
  fi
}
export -f gera; export RAIZ
printf '%s\n' "${IDS[@]}" | xargs -P 4 -I{} bash -c 'gera {}'
