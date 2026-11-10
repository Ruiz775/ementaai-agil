import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

import verificar_templates as vt  # noqa: E402


class TestTemplates(unittest.TestCase):
    def test_templates_do_repositorio_estao_validos(self):
        self.assertEqual(vt.verificar(), [])

    def test_detecta_campo_obrigatorio_ausente(self):
        template = {"body": [{"id": "objetivo", "validations": {"required": True}},
                             {"id": "contexto"}]}
        self.assertEqual(vt.campos_obrigatorios(template), {"objetivo"})


if __name__ == "__main__":
    unittest.main()
