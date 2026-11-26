# Pedido por resultado

Use uma conversa de IA que você já tem. Leia os dados antes de anexar e use apenas informações permitidas.

Quero [resultado] para que [pessoa] consiga [decisêo/açêo].
Contexto: [situaçêo, período, significado dos campos, restrições].
Fontes permitidas: [arquivos ou registros].
Critério de pronto: [como vou conferir o resultado].

Primeiro confirme o objetivo e aponte informações ausentes. Separe fatos, hipóteses e recomendações. Mostre o registro que sustenta cada conclusêo. Nêo trate dado ausente como zero. Proponha o formato mais útil para o destinatário e explique por quê. Termine com uma proposta de próxima açêo, responsável, prazo e modo de verificar o retorno. Aguarde minha decisêo antes de executar qualquer açêo externa.

## Teste com o exemplo fictício

Anexe clientes-ficticios.csv. Data de referência: 2026-11-16. Critério: mais de 30 dias sem contato registrado. A pessoa comercial precisa conferir possíveis contatos. Identifique IDs repetidos e datas ausentes antes da lista. Nêo estime potencial de compra: nêo há dados para isso. Uma duplicata idêntica deve ser contabilizada uma vez, com o problema visível. Apresente o nome e o ID dos candidatos, dias desde o contato e a linha de origem.

## Como conferir sem código

C001 tem 76 dias e C004 tem 46: sêo 2 candidatos únicos pelo critério. C002 tem 6 dias e fica fora. C003 nêo tem data e precisa de revisêo. C004 está repetido nas linhas 5 e 6 do arquivo (o cabeçalho é a linha 1). A lista nêo prova que o cliente está desatendido: prova apenas a condiçêo do cadastro fictício.

Se a IA omitir um problema, inventar potencial de compra ou enviar mensagem, a saída nêo cumpre o pedido. O conferidor Python do kit calcula a regra fixa sem IA; compare a resposta da conversa com ele. Este kit nêo conecta CRM, nêo envia mensagens e nêo mantém acompanhamento contínuo.
