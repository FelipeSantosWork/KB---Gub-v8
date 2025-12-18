# Heurísticas e exemplos para geração de casos (consulta do agente)

## 1. Princípios
- Atomicidade: um caso por funcionalidade/validação/estado.
- Títulos: “Deve …”/“Não deve …” + referência explícita ao modal/componente.
- IDs e Suite: suite.id=1; suite.title="Presente do Gub"; case.id=1.
- Tags: presentes porém `[]` por padrão.
- Schema completo: não remover campos.

## 2. Steps — regras
- 4–8 steps; `expected_result=""`, `data=""`, `steps=[]` em todos.
- Último step: `action` contém “Resultado esperado: …”.
- Sem texto genérico nos steps.

## 3. Heurísticas por tipo
- Obrigatoriedade: abrir → vazio → acionar → Resultado esperado.
- Limite de caracteres: abrir → exceder → tentar salvar → Resultado esperado.
- Formato: abrir → informar inválido → validar/salvar → Resultado esperado.
- Unicidade: abrir → valor existente → salvar → Resultado esperado.
- Botão habilitar/desabilitar: abrir → preparar estado → checar/acionar → Resultado esperado.
- Modal: abrir → foco/elementos → ação principal → fechar/ESC/backdrop → Resultado esperado.

## 4. Exemplos bons
- Último step com “Resultado esperado: …” no `action`.
- Steps detalham o caminho real (elementos, ações, estados).

## 5. Exemplos ruins (evitar)
- “Navegar até a página”, “Observar comportamento”, “Executar ação”, “Resultado esperado: como no título”.
- `expected_result` preenchido com o texto do resultado (deve ser vazio).
- Somente 1 step.

## 6. Checklist rápido
- Ordem: títulos → JSON.
- Suite e IDs corretos.
- Steps ≥4; `expected_result` vazio; último `action` com “Resultado esperado: …”.
- Sem steps genéricos; tags `[]`.
- Nenhum campo ausente.
