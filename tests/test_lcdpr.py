# -*- coding: utf-8 -*-

import pytest
import os
import sys
from datetime import date

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

from sped.lcdpr.arquivos import ArquivoDigital
from sped.lcdpr.registros import Registro9999


class TestLcdpr():

    def test_read_registro(self):
        txt = u"""|0000|LCDPR|0014|00000000000|TESTE|0|0||01012020|31122020|
|9999|Contabilidade|00000000000|MT12345678|contato@lucrorural.com.br|6599999999|2|
""".replace('\n', '\r\n')

        arq = ArquivoDigital()
        arq._registro_abertura.NOME_ESC = 'LCDPR'
        arq._registro_abertura.COD_VER = '0014'
        arq._registro_abertura.CPF = '00000000000'
        arq._registro_abertura.NOME = 'TESTE'
        arq._registro_abertura.IND_SIT_INI_PER = '0'
        arq._registro_abertura.SIT_ESPECIAL = '0'
        arq._registro_abertura.DT_SIT_ESP = ''
        arq._registro_abertura.DT_INI = date(2020, 1, 1)
        arq._registro_abertura.DT_FIN = date(2020, 12, 31)

        bloco_9 = arq._blocos['9']
        reg_9999 = Registro9999()
        reg_9999.IDENT_NOM = "Contabilidade"
        reg_9999.IDENT_CPF_CNPJ = "00000000000"
        reg_9999.IND_CRC = "MT12345678"
        reg_9999.EMAIL = "contato@lucrorural.com.br"
        reg_9999.FONE = "6599999999"
        bloco_9.add(reg_9999)

        arq.prepare()

        assert txt == arq.getstring()
