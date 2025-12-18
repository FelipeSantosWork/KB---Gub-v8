#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python validate_qase.py teste.json --schema schema.json - padrão
# python validate_qase.py teste.json --strict-component-ref - Se quiser a heurística que alerta quando o título não referencia claramente um componente/modal
# python validate_qase.py bloco_1.json --schema schema.json --strict-component-ref - Se quiser a heurística que alerta quando o título não referencia claramente um componente/modal
# python validate_qase.py teste.json --schema schema.json --allow-tags - Se quiser permitir tags preenchidas (quando você solicitar explicitamente)


import argparse
import json
import os
import sys
from typing import List, Dict, Any, Tuple

# Optional: use jsonschema if available; otherwise, fallback to custom checks
try:
    import jsonschema
    from jsonschema import Draft202012Validator
    JSONSCHEMA_AVAILABLE = True
except Exception:
    JSONSCHEMA_AVAILABLE = False

GENERIC_STEP_PATTERNS = [
    "Navegar ate a pagina",
    "Observar comportamento",
    "Executar acao",
    "Resultado esperado: como no titulo",
]

TITLE_COMPONENT_HINTS = [
    "modal", "botao", "campo", "tela", "dialogo", "componente"
]

def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_schema(schema_path: str) -> Dict[str, Any]:
    return load_json(schema_path)

def validate_with_jsonschema(data: Any, schema: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    try:
        validator = Draft202012Validator(schema)
        for err in sorted(validator.iter_errors(data), key=lambda e: e.path):
            loc = "/".join([str(p) for p in err.path])
            errors.append(f"[schema] {loc or '<root>'}: {err.message}")
    except Exception as e:
        errors.append(f"[schema] Falha ao inicializar validador JSON Schema: {e}")
    return errors

def guardrails_checks(data: Dict[str, Any], allow_tags: bool = False, strict_component_ref: bool = False) -> Tuple[List[str], List[str]]:
    """
    Return (errors, warnings)
    """
    errors: List[str] = []
    warnings: List[str] = []

    suites = data.get("suites")
    if not isinstance(suites, list) or not suites:
        errors.append("[guard] Campo 'suites' ausente ou vazio")
        return errors, warnings

    for si, suite in enumerate(suites, start=1):
        if suite.get("id") != 1:
            errors.append(f"[guard] suites[{si}].id deve ser 1")
        if suite.get("title") != "Presente do Gub":
            errors.append(f"[guard] suites[{si}].title deve ser 'Presente do Gub'")

        cases = suite.get("cases", [])
        if not isinstance(cases, list) or not cases:
            errors.append(f"[guard] suites[{si}].cases ausente ou vazio")
            continue

        for ci, case in enumerate(cases, start=1):
            if case.get("id") != 1:
                errors.append(f"[guard] cases[{ci}].id deve ser 1")

            title = case.get("title", "")
            if not isinstance(title, str) or not title:
                errors.append(f"[guard] cases[{ci}].title ausente ou vazio")
            else:
                if not (title.startswith("Deve") or title.startswith("Não deve")):
                    errors.append(f"[guard] cases[{ci}].title deve iniciar com 'Deve' ou 'Não deve'")
                if strict_component_ref:
                    if not any(hint in title.lower() for hint in TITLE_COMPONENT_HINTS):
                        warnings.append(f"[guard] cases[{ci}].title nao parece referenciar componente/modal explicitamente (heuristica)")

            steps = case.get("steps")
            if not isinstance(steps, list):
                errors.append(f"[guard] cases[{ci}].steps nao eh uma lista")
                continue
            if not (4 <= len(steps) <= 8):
                errors.append(f"[guard] cases[{ci}].steps deve ter entre 4 e 8 passos (atual={len(steps)})")

            if steps:
                last_action = steps[-1].get("action", "")
                if "Resultado esperado:" not in last_action:
                    errors.append(f"[guard] cases[{ci}].steps[ultimo].action deve conter 'Resultado esperado:'")

            for pi, st in enumerate(steps, start=1):
                if st.get("expected_result", None) != "":
                    errors.append(f"[guard] cases[{ci}].steps[{pi}].expected_result deve ser string vazia")
                if st.get("data", None) != "":
                    errors.append(f"[guard] cases[{ci}].steps[{pi}].data deve ser string vazia")
                ssub = st.get("steps")
                if ssub != []:
                    errors.append(f"[guard] cases[{ci}].steps[{pi}].steps deve ser lista vazia []")
                action_text = st.get("action", "")
                for pat in GENERIC_STEP_PATTERNS:
                    if pat.lower() in action_text.lower():
                        warnings.append(f"[guard] cases[{ci}].steps[{pi}].action parece generico ('{pat}') - evite")

            tags = case.get("tags")
            if tags is None:
                errors.append(f"[guard] cases[{ci}].tags ausente")
            else:
                if not allow_tags and isinstance(tags, list) and len(tags) > 0:
                    warnings.append(f"[guard] cases[{ci}].tags nao vazio - por padrao deve ser [] (a menos que solicitado)")
                if isinstance(tags, list):
                    for ti, t in enumerate(tags, start=1):
                        if isinstance(t, str):
                            if t != t.strip():
                                warnings.append(f"[guard] cases[{ci}].tags[{ti}] contem espacos nas extremidades - aplique trim")

            if case.get("automation") != "is-not-automated":
                errors.append(f"[guard] cases[{ci}].automation deve ser 'is-not-automated' (padrao)")

    return errors, warnings

def main():
    parser = argparse.ArgumentParser(
        description="Validador de arquivos JSON do Qase (Gub v8): valida contra schema.json e aplica guardrails."
    )
    parser.add_argument("input", help="Caminho do arquivo JSON a validar")
    parser.add_argument("--schema", default="schema.json", help="Caminho para o JSON Schema (default: schema.json na mesma pasta)")
    parser.add_argument("--allow-tags", action="store_true", help="Permite tags nao vazias sem avisos")
    parser.add_argument("--strict-component-ref", action="store_true", help="Ativa heuristica que alerta titulos sem referencia explicita a modal/componente")
    args = parser.parse_args()

    try:
        data = load_json(args.input)
    except Exception as e:
        print(f"[erro] Nao foi possivel ler '{args.input}': {e}")
        return 2

    schema_path = args.schema
    if not os.path.isabs(schema_path):
        schema_path = os.path.join(os.path.dirname(os.path.abspath(args.input)), schema_path)

    schema = None
    if os.path.exists(schema_path):
        try:
            schema = load_schema(schema_path)
        except Exception as e:
            print(f"[aviso] Falha ao carregar schema '{schema_path}': {e}")
    else:
        print(f"[aviso] Schema '{schema_path}' nao encontrado - rodando apenas guardrails")

    errors: List[str] = []
    warnings: List[str] = []

    if schema is not None and JSONSCHEMA_AVAILABLE:
        errors.extend(validate_with_jsonschema(data, schema))
    elif schema is not None and not JSONSCHEMA_AVAILABLE:
        print('[aviso] Biblioteca jsonschema nao encontrada - instale para validacao completa. Prosseguindo com guardrails.')

    g_errors, g_warnings = guardrails_checks(data, allow_tags=args.allow_tags, strict_component_ref=args.strict_component_ref)
    errors.extend(g_errors)
    warnings.extend(g_warnings)


    print("\n==== Resultado da validacao ====\n")
    if errors:
        print(f"Erros ({len(errors)}):")
        for e in errors:
            print(f" - {e}")
    else:
        print("Erros: nenhum")


    if warnings:
        print(f"\nAvisos ({len(warnings)}):")
        for w in warnings:
            print(f" - {w}")

    else:
        print("\nAvisos: nenhum")

    print("\nResumo:")
    suites_count = len(data.get("suites", [])) if isinstance(data, dict) else 0
    cases_count = 0
    if suites_count:
        for s in data["suites"]:
            cases_count += len(s.get("cases", []))
    print(f" - suites: {suites_count}")
    print(f" - cases: {cases_count}")

    return 1 if errors else 0

if __name__ == "__main__":
    rc = main()
    sys.exit(rc)