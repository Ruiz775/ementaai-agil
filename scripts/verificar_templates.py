"""Verifica se os templates de issue seguem o padrão do time.

Toda história precisa pedir objetivo, contexto e critérios de aceitação.
Todo defeito precisa pedir comportamento, esperado, passos e impacto.
"""
import pathlib
import sys

import yaml

RAIZ = pathlib.Path(__file__).resolve().parent.parent
PASTA = RAIZ / ".github" / "ISSUE_TEMPLATE"

OBRIGATORIOS = {
    "historia.yml": {"objetivo", "contexto", "criterios"},
    "defeito.yml": {"comportamento", "esperado", "passos", "impacto"},
}


def campos_obrigatorios(template: dict) -> set:
    return {
        bloco["id"]
        for bloco in template.get("body", [])
        if bloco.get("id") and bloco.get("validations", {}).get("required")
    }


def verificar() -> list:
    erros = []
    for nome, esperados in OBRIGATORIOS.items():
        arquivo = PASTA / nome
        if not arquivo.exists():
            erros.append(f"{nome}: arquivo não encontrado")
            continue
        template = yaml.safe_load(arquivo.read_text(encoding="utf-8"))
        faltando = esperados - campos_obrigatorios(template)
        if faltando:
            erros.append(f"{nome}: campos obrigatórios ausentes: {sorted(faltando)}")
    return erros


if __name__ == "__main__":
    problemas = verificar()
    for p in problemas:
        print("ERRO:", p)
    if problemas:
        sys.exit(1)
    print("Templates OK")
