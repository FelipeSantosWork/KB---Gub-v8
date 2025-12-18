# Script gub v8 — Direcionamento oficial para o agente (conciso)

> Objetivo: instruir o agente a gerar **casos de teste atômicos** para Qase, em **blocos de até 20 casos**, com **ordem de resposta disciplinada**, **schema completo** (sem remover campos) e **guardrails** contra erros comuns.

## 1. Princípios vitais (reancoragem no início de cada bloco)
- **Re‑análise**: **sempre** releia a **história/protótipo completo** antes de gerar cada bloco (garante contexto e consistência).
- **Blocos**: gere **ATÉ 20 casos por bloco**.
  - Se possível, **agrupe por tema/categoria**.
  - Se não houver agrupamento natural, use sufixos **“parte 1”, “parte 2”, …”** nos títulos do bloco.
- **Atomicidade**: cada caso cobre **apenas uma** funcionalidade/validação/estado.
- **Títulos**: iniciar com **“Deve …”** ou **“Não deve …”** e **citar explicitamente** o **modal/componente**.
- **IDs e Suite**: `suite.id=1`, `suite.title="Presente do Gub"` e **todos os `case.id=1`**.
- **Tags**: devem estar presentes no schema, porém **`[]` vazio por padrão** (só preencher se solicitado).
- **Schema completo**: **não remover nenhum campo** do objeto de caso.
- **Steps (rigor)**:
  - **≥ 4 e ≤ 8 steps** por caso (nunca 1).
  - Em **todos** os steps: `expected_result=""`, `data=""`, `steps=[]`.
  - **Último step**: o campo **`action`** deve conter **“Resultado esperado: …”** (exatamente).
  - **Proibido** steps genéricos (ex.: “Navegar até a página”, “Observar comportamento”, “Executar ação”, “Resultado esperado: como no título”).

## 2. Ordem da resposta (imutável)
1) **[Lista de títulos planejados do bloco]** — listar **TODOS** os títulos e indicar agrupamento por **tema** ou **parte N**.
2) **[JSON]** — arquivo único com **`suites`** no topo.
3) **[Opcional]** **Critérios de aprovação** — somente se solicitado.
4) **[Opcional]** **Tabela de decisão** — somente se solicitado.

## 3. Schema padrão Qase (não remover campos)
Estrutura mínima (o agente deve preencher os valores):

```json
{
  "suites": [
    {
      "id": 1,
      "title": "Presente do Gub",
      "description": null,
      "preconditions": null,
      "suites": [],
      "cases": [
        {
          "id": 1,
          "title": "Deve … (referência explícita ao componente/modal)",
          "description": "Objetivo/escopo claro",
          "preconditions": "Pré-condições necessárias",
          "postconditions": null,
          "priority": "alta",
          "severity": "indefinido",
          "type": "funcional",
          "behavior": "indefinido",
          "automation": "is-not-automated",
          "status": "actual",
          "is_flaky": "no",
          "layer": "e2e",
          "milestone": null,
          "custom_fields": [],
          "steps_type": "classic",
          "steps": [
            { "position": 1, "action": "…", "expected_result": "", "data": "", "steps": [] },
            { "position": 2, "action": "…", "expected_result": "", "data": "", "steps": [] },
            { "position": 3, "action": "…", "expected_result": "", "data": "", "steps": [] },
            { "position": 4, "action": "Resultado esperado: …", "expected_result": "", "data": "", "steps": [] }
          ],
          "tags": [],
          "params": [],
          "is_muted": "no"
        }
      ]
    }
  ]
}
```

> **Nota**: manter **todos** os campos (`severity`, `behavior`, `status`, etc.). Valores padrão podem ser ajustados conforme o caso, mas **não omitir campos**.

## 4. Heurísticas de steps por tipo
- **Obrigatoriedade de campo**: (1) Abrir tela/modal; (2) Campo vazio/preparar contexto; (3) Acionar salvar/validar; (4) **Resultado esperado**: bloquear + mensagem de obrigatoriedade.
- **Limite de caracteres**: (1) Abrir; (2) Digitar acima do limite; (3) Salvar; (4) **Resultado esperado**: impedir excedente + erro.
- **Formato inválido (e-mail/CPF/etc.)**: (1) Abrir; (2) Informar inválido; (3) Validar/Salvar; (4) **Resultado esperado**: erro de formato + bloqueio.
- **Unicidade**: (1) Abrir; (2) Informar valor já existente; (3) Salvar; (4) **Resultado esperado**: erro de duplicidade.
- **Botão habilitar/desabilitar**: (1) Abrir; (2) Preparar campos incompletos/completos; (3) Checar estado; (4) **Resultado esperado**: estado correto; (5) (opcional) clicar.
- **Modal**: (1) Abrir; (2) Foco/elementos; (3) Ação principal; (4) Fechamento/ESC/backdrop; (5) **Resultado esperado**.

## 5. Auto‑check (ao final de **cada bloco**)
- Ordem correta: títulos → JSON → (critérios/tabela, se solicitado).
- Suite: `id=1`, `title="Presente do Gub"`.
- Casos: `id=1` em **todos**; títulos “Deve/Não deve…” com **modal/componente** explícito.
- Atomicidade: **uma** funcionalidade por caso.
- Steps: **≥ 4** e **≤ 8**; `expected_result=""`, `data=""`, `steps=[]` em todos.
- Último step: `action` contém **“Resultado esperado: …”** (não colocar no `expected_result`).
- Sem steps genéricos; cada step reflete o **caminho real** da tela.
- Tags presentes porém **`[]`** por padrão.
- **Nenhum campo do schema ausente**.

## 6. Reancoragem crítica (reforçar no fim de cada bloco)
IDs (suite/caso=1); título da suíte fixo; atomicidade; títulos com modal/componente; steps com **resultado esperado no último `action`**; tags vazias; releitura de história; blocos até 20; agrupamento por tema/parte.
