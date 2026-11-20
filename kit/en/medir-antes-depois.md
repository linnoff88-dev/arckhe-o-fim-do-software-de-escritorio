# Measure before and after

Use the empty [medir-antes-depois.csv](../medir-antes-depois.csv) template to record comparable cases before and after a process change. Rows track complete elapsed work time in minutes and whether quality was accepted. This is an empty measurement template; no business productivity improvement has been measured.

CSV columns:

- `caso` — Case or work item identifier.
- `data` — Date of the case.
- `modo` — Process mode used. The Python checker reports `regra fixa sem IA` (fixed rule without AI).
- `volume` — Amount of work in the case.
- `complexidade` — Case complexity.
- `busca_min` — Minutes spent searching.
- `preparacao_min` — Minutes spent preparing.
- `ia_min` — Minutes spent using AI.
- `revisao_min` — Minutes spent reviewing.
- `correcao_min` — Minutes spent correcting.
- `acompanhamento_min` — Minutes spent following up.
- `erros` — Errors observed.
- `qualidade_aceita` — Whether the quality was accepted.
- `resultado_observado` — Observed result.
