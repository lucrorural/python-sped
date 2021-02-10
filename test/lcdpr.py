# -*- coding: utf-8 -*-

import unittest
import os
import sys

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

from sped.lcdpr.arquivos import ArquivoDigital


class TestLcdpr(unittest.TestCase):

    def test_read_registro(self):
        txt = u"""
|1001|1|
|1990|2|
|9001|1|
|9990|2|
|9999|21|
""".replace('\n', '\r\n')

        # Permite validacao de string grandes
        self.maxDiff = None
        arq = ArquivoDigital()

        arq._registro_abertura.NOME_ESC = 'LCDPR'
        arq._registro_abertura.COD_VER = '0014'

        self.assertEqual(txt, arq.getstring())

if __name__ == '__main__':
    unittest.main()
