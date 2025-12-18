# INDEX — KB de QA para agentes (OneDrive)

Este índice organiza e explica os arquivos de referência que o agente deve consultar ao gerar casos de teste para o Qase.

## 📂 Estrutura recomendada da pasta
- `Script_gub_v8.md` — Direcionamento oficial do agente (guardrails, reancoragem e auto‑check)
- `Prompt_Time_Gub_v8.md` — Prompt enxuto (copiar/colar no chat do agente com a história/protótipo)
- `QA_Guide_Heuristicas_Casos_Qase.md` — Heurísticas por tipo de validação + exemplos bons/ruins
- `Checklist_PosGeracao.md` — Checklist para revisão pós‑geração (bloco a bloco)
- `Exemplo_Perfeito_JSON.json` — Exemplo de bloco “perfeito” (IDs=1, steps≥4, expected_result="", último action com “Resultado esperado: …”, tags=[])
- `schema.json` — **JSON Schema** do formato esperado (raiz/suite/case/steps)

## 🚀 Como usar (passo a passo)
1. Abra o **Prompt enxuto** (\`Prompt_Time_Gub_v8.md\`) e cole no chat do agente **junto com a história/protótipo**.
2. Gere **blocos de até 20 casos**; o agente deve **listar títulos** antes do JSON e aplicar o **auto‑check**.
3. Se notar deriva ou erro de formatação, reancore com o **Script_gub_v8.md** e valide com o **Checklist_PosGeracao.md**.
4. Consulte **Heurísticas** para construir steps detalhados e evitar texto genérico.
5. Compare a saída com o **Exemplo_Perfeito_JSON.json** e valide contra o **schema.json** (se desejar usar um validador).

## 🔎 Dicas
- Mantenha os arquivos **acessíveis** (link “People in your organization” ou “Specific people”).
- Para histórias longas, gere por **tema/categoria**; se não for possível, use sufixos **parte 1, parte 2, …**.
- Sempre releia a história/protótipo **antes de cada bloco**.

## 🧩 Links (subir todos na mesma pasta)
- Script: `Script_gub_v8.md`
- Prompt: `Prompt_Time_Gub_v8.md`
- Heurísticas: `QA_Guide_Heuristicas_Casos_Qase.md`
- Checklist: `Checklist_PosGeracao.md`
- Exemplo JSON: `Exemplo_Perfeito_JSON.json`
- **Schema**: `schema.json`
