# Pedido por resultado

Usa una conversación de IA que ya tengas. Lee los datos antes de adjuntarlos y usa solo la información permitida.

Quiero [resultado] para que [persona] pueda [decisión/acción].
Contexto: [situación, período, significado de los campos, restricciones].
Fuentes permitidas: [archivos o registros].
Criterio de finalización: [cómo voy a comprobar el resultado].

Primero confirma el objetivo y señala la información que falta. Separa hechos, hipótesis y recomendaciones. Muestra el registro que respalda cada conclusión. No trates los datos ausentes como cero. Propón el formato más útil para el destinatario y explica por qué. Termina con una propuesta de próxima acción, responsable, plazo y forma de comprobar el resultado. Espera mi decisión antes de ejecutar cualquier acción externa.

## Prueba con el ejemplo ficticio

Adjunta [clientes-ficticios.csv](../clientes-ficticios.csv). Fecha de referencia: 2026-11-16. Criterio: más de 30 días sin contacto registrado. La persona del área comercial necesita revisar posibles contactos. Identifica los IDs repetidos y las fechas ausentes antes de preparar la lista. No estimes el potencial de compra: no hay datos para eso. Una duplicación idéntica debe contabilizarse una sola vez, dejando visible el problema. Presenta el nombre y el ID de los candidatos, los días transcurridos desde el contacto y la fila de origen.

## Cómo comprobarlo sin código

C001 tiene 76 días y C004 tiene 46: son 2 candidatos únicos según el criterio. C002 tiene 6 días y queda fuera. C003 no tiene fecha y necesita revisión. C004 está repetido en las filas 5 y 6 del archivo (el encabezado es la fila 1). La lista no demuestra que el cliente esté desatendido: solo demuestra que cumple la condición del registro ficticio.

Si la IA omite un problema, inventa potencial de compra o envía un mensaje, el resultado no cumple lo pedido. El verificador Python del kit calcula la regla fija sin IA; compara la respuesta de la conversación con él. Este kit no se conecta al CRM, no envía mensajes ni hace un seguimiento continuo.
