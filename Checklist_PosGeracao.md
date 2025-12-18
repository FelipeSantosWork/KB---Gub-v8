# Checklist pós‑geração (para consulta e revisão)

- [ ] Lista de títulos antes do JSON (organizada por tema ou parte)
- [ ] Suite: `id=1`, `title="Presente do Gub"`
- [ ] Casos: `id=1` em todos; títulos “Deve/Não deve…” citam modal/componente
- [ ] Atomicidade: um recurso/validação/estado por caso
- [ ] Steps: **≥ 4 e ≤ 8**; `expected_result=""`, `data=""`, `steps=[]` em todos
- [ ] Último step: `action` contém “Resultado esperado: …”
- [ ] Sem passos genéricos; caminho real da tela
- [ ] Tags presentes porém `[]` por padrão
- [ ] **Nenhum campo do schema ausente**
