# Prompt enxuto — uso pelo time (copiar/colar no chat do agente)

Leia a HISTÓRIA/PROTÓTIPO COMPLETO antes de gerar **cada bloco**.

**Regras críticas**:
- Atomicidade: um caso por funcionalidade/validação/estado.
- Títulos: começar com “Deve …” ou “Não deve …” e citar o modal/componente.
- IDs: suite.id=1 e case.id=1; suite.title="Presente do Gub".
- Schema: **não remover nenhum campo**; `tags=[]` por padrão (preencha só se eu solicitar).
- Steps: 4–8 por caso; em todos os steps, `expected_result=""`, `data=""`, `steps=[]`.
- Último step: o campo `action` deve conter **“Resultado esperado: …”** (exatamente).
- Proibido steps genéricos; cada step deve refletir o caminho real da tela.

**Entrega por blocos** (até 20 casos):
- Agrupe por tema/categoria; se não der, use sufixos “parte 1”, “parte 2”, …
- Antes do JSON, liste **TODOS** os títulos do bloco.

**Auto‑check** (antes de enviar):
- Atomicidade ok; títulos corretos; steps ≥4 e ≤8; `expected_result` vazio; último `action` com “Resultado esperado: …”; `tags=[]`;
- Nenhum campo do schema ausente.

**Contexto** (cole abaixo os links/descrições):
- História/Protótipo: <link ou resumo>
- Temas/Categorias sugeridos: <opcional>
- Observações específicas desta história: <opcional>
