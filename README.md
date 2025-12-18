
# Gub v8 KB — Casos de teste para Qase (Guia, Schema e Validador)

Repositório público com a *Knowledge Base* do **Gub v8** para padronizar a geração de casos de teste (Qase) por agentes.  
Inclui **guia de uso**, **schema JSON**, **validador** e **exemplo “perfeito”** para consulta.

---

## 🎯 Objetivo

Garantir que os casos gerados pelo agente:
- sejam **atômicos** (uma funcionalidade/validação/estado por caso),
- mantenham **IDs=1** e **suite.title="Presente do Gub"**,
- usem **títulos “Deve …” / “Não deve …”** com referência explícita ao **componente/modal**,
- tragam **steps ≥ 4** e **≤ 8**, com `expected_result=""` em **todos** os steps,
- registrem o **“Resultado esperado: …”** **no último `action`**,
- preservem **todos os campos do schema**, com **`tags=[]`** por padrão,
- respeitem a **ordem de resposta**: **Lista de títulos → JSON → (Opcional) Critérios/Tabela**.

---

## 📁 Conteúdo do repositório

- `INDEX.md` — Índice da KB (como usar + referências).
- `Script_gub_v8.md` — Direcionamento oficial (guardrails, reancoragem, auto‑check).
- `Prompt_Time_Gub_v8.md` — Prompt **enxuto** para usar no chat com o agente.
- `QA_Guide_Heuristicas_Casos_Qase.md` — Heurísticas por tipo de validação, exemplos bons/ruins.
- `Checklist_PosGeracao.md` — Checklist de revisão **pós‑geração** por bloco.
- `schema.json` — **JSON Schema** (draft 2020‑12) para validar a estrutura dos casos.
- `validate_qase.py` — **Validador** (schema + guardrails) para arquivos JSON gerados.
- `Exemplo_Perfeito_JSON.json` — Bloco exemplo- `Exemplo_Perfeito_JSON.json` — Bloco exemplo com 5 casos (conforme as regras do v8).

