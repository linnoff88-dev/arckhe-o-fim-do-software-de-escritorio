# El fin del software de oficina

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![El fin del software de oficina](guia/assets/banner-es.jpg)](https://inematds.github.io/o-fim-do-software-de-escritorio/guia/es/)

## Qué es

El fin del software de oficina es una visión de Nei Maldaner sobre trabajar con inteligencia artificial a partir de los objetivos del negocio. Está dirigido a profesionales, gestores y dueños de empresas que dedican tiempo a preparar materiales, completar sistemas y repetir información. La guía muestra cómo pasar de este trabajo de preparación a un proceso de decisión y ejecución con acompañamiento. Encontrarás ejemplos, un plan de transición y un kit gratuito para probar un proceso con datos ficticios. Para empezar, basta con leer y elegir una tarea que conozcas bien.

## Guía y kit gratuitos

Lee la **[guía completa](https://inematds.github.io/o-fim-do-software-de-escritorio/guia/es/)** y descarga el **[kit](https://inematds.github.io/o-fim-do-software-de-escritorio/kit-inteligencia-operacional.zip)**.

- [Visión original de Nei Maldaner (en portugués)](docs/visao-original.md).
- [Solicitud por resultado, ejemplo y respuesta esperada](kit/es/pedido-por-resultado.md).
- [Mapa del proceso](kit/es/mapa-do-processo.md).
- [Medición de tiempo y calidad](kit/medir-antes-depois.csv) · [Guía de la ficha de medición](kit/es/medir-antes-depois.md).
- [Registro de decisiones y seguimiento](kit/es/decisao-e-acompanhamento.md).

## Migración del trabajo

- [Mapear mi migración](kit/es/migrar-por-resultado.md).
- [Definir reglas y excepciones](kit/es/regras-e-excecoes.md).
- [Rediseñar mi función](kit/es/novas-funcoes.md).

## Ejecutar el ejemplo opcional

Requiere Python 3.9+. Extrae el ZIP y abre la terminal en la carpeta que contiene kit, o ejecuta desde la raíz de este repositorio:

```bash
python3 kit/conferir_exemplo.py
```

Windows: `py -3 kit/conferir_exemplo.py`. Si no tienes Python, sigue la revisión manual de la guía.

Resultado esperado: C001 (76 días) y C004 (46 días), duplicidad C004 y fecha faltante C003. Cero mensajes enviados. **Verificador determinístico, sin IA ni red.** Para usar IA, copia la solicitud y adjunta el CSV en la conversación de una herramienta que ya utilices. No se midió ninguna mejora de productividad empresarial.

## Video

🎬 [Ver el video](https://inematds.github.io/o-fim-do-software-de-escritorio/videos/) — Video con voz y subtítulos en portugués.

## Autoría y fuentes

Tesis de Nei Maldaner; contenido educativo abierto. Las quiebras y la reducción de equipos son escenarios, no predicciones garantizadas. [OIT (2025)](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) · [Microsoft Work IQ](https://www.microsoft.com/en-us/copilot/features/work-iq).

## Mantenimiento

El contenido PT está en docs/guia-completo.md (en portugués). `python3 scripts/gerar_guia.py` usa la plantilla INEMA preservada y requiere el paquete Python markdown. Traducciones: inema-traduz mediante suscripción. La generación de la guía reemplaza el HTML PT; conserva cualquier inserción de video que ya se haya publicado. Publicación mediante git/GitHub Pages.
