# Request by outcome

Use an AI conversation you already have. Review the data before attaching it, and use only permitted information.

I want [result] so that [person] can [decision/action].
Context: [situation, period, meaning of fields, constraints].
Permitted sources: [files or records].
Completion criteria: [how I will check the result].

First, confirm the objective and point out any missing information. Separate facts, assumptions, and recommendations. Show the record supporting each conclusion. Do not treat missing data as zero. Suggest the most useful format for the recipient and explain why. End with a proposed next action, owner, deadline, and way to check the response. Wait for my decision before taking any external action.

## Test with the fictional example

Attach [clientes-ficticios.csv](../clientes-ficticios.csv). Reference date: 2026-11-16. Criterion: more than 30 days without a recorded contact. The sales representative needs to check possible contacts. Identify repeated IDs and missing dates before producing the list. Do not estimate purchase potential: there is no data for that. An identical duplicate should be counted once, with the issue made visible. Present each candidate's name and ID, days since contact, and source row.

## How to check without code

C001 has 76 days and C004 has 46: there are 2 unique candidates under this criterion. C002 has 6 days and is excluded. C003 has no date and needs review. C004 is duplicated in rows 5 and 6 of the file (the header is row 1). The list does not prove that the customer is being neglected; it proves only that the condition is met in the fictional dataset.

If the AI omits an issue, invents purchase potential, or sends a message, the output does not meet the request. The kit's Python checker calculates the fixed rule without AI; compare the conversation's response with it. This kit does not connect to a CRM, send messages, or provide ongoing monitoring.
