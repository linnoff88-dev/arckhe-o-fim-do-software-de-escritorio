# The End of Office Software

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![The End of Office Software](guia/assets/banner-en.jpg)](https://inematds.github.io/o-fim-do-software-de-escritorio/guia/en/)

## What It Is

The End of Office Software is Nei Maldaner’s vision for working with artificial intelligence based on business goals. It is for professionals, managers, and business owners who spend time preparing materials, filling out systems, and repeating information. The guide shows how to move from this preparatory work to a process of decision-making and supervised execution. You’ll find examples, a transition plan, and a free kit for testing a process with fictional data. To get started, simply read the guide and choose a task you know well.

## Free Guide and Kit

Read the **[complete guide](https://inematds.github.io/o-fim-do-software-de-escritorio/guia/en/)** and download the **[kit](https://inematds.github.io/o-fim-do-software-de-escritorio/kit-inteligencia-operacional.zip)**.

- [Nei Maldaner’s original vision](docs/visao-original.md) (in Portuguese).
- [Request by outcome, example, and expected response](kit/en/pedido-por-resultado.md).
- [Process map](kit/en/mapa-do-processo.md).
- [Time and quality measurement](kit/en/medir-antes-depois.md).
- [Decision and follow-up record](kit/en/decisao-e-acompanhamento.md).

## Run the Optional Example

Requires Python 3.9+. Extract the ZIP and open a terminal in the folder containing kit, or run this from the root of this repository:

```bash
python3 kit/conferir_exemplo.py
```

Windows: `py -3 kit/conferir_exemplo.py`. Without Python, follow the manual verification steps in the guide.

Expected: C001 (76 days) and C004 (46 days), duplicate C004, and missing date C003. Zero messages sent. **Deterministic checker, with no AI or network.** To use AI, copy the request and attach the CSV in a conversation with a tool you already use. No business productivity gains have been measured.

## Video

🎬 [Watch the video](https://inematds.github.io/o-fim-do-software-de-escritorio/videos/) — Video with Portuguese voice and subtitles.

## Authorship and Sources

Thesis by Nei Maldaner; open educational content. Business failures and team reductions are scenarios, not guaranteed predictions. [ILO (2025)](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) · [Microsoft Work IQ](https://www.microsoft.com/en-us/copilot/features/work-iq).

## Maintenance

The PT content is in docs/guia-completo.md (in Portuguese). `python3 scripts/gerar_guia.py` uses the preserved INEMA template and requires the Python markdown package. Translations: inema-traduz via subscription. Generating the guide replaces the PT HTML; preserve any video embed that has already been published. Publication via git/GitHub Pages.

## Shift to a new role

The kit includes a [migration map](kit/en/migrar-por-resultado.md), [rules and exceptions](kit/en/regras-e-excecoes.md), and [new roles and responsibilities](kit/en/novas-funcoes.md). These are planning and testing templates, with no automatic implementation.
