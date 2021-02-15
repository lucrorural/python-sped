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

from sped.efd.icms_ipi.arquivos import ArquivoDigital
from sped.efd.icms_ipi.registros import Registro0100


class TestSpedPisCofins():

    def test_read_registro(self):
        txt = u"""|0000|014|0|01012020|31122020|EMPRESA TESTE|53939351000129|33333333333|SP|222222222222|1234567|5999|0123|A|1|
|0001|0|
|0100|CONTABILIDADE|99999999999|MT00000000||78000000|AV. UM|1||CENTRO|6599999999||contato@lucrorural.com.br|5102637|
|0990|4|
|B001|1|
|B990|2|
|C001|1|
|C990|2|
|D001|1|
|D990|2|
|E001|1|
|E990|2|
|G001|1|
|G990|2|
|H001|1|
|H990|2|
|K001|1|
|K990|2|
|1001|1|
|1990|2|
|9001|0|
|9900|0001|1|
|9900|0100|1|
|9900|0990|1|
|9900|0000|1|
|9900|B001|1|
|9900|B990|1|
|9900|C001|1|
|9900|C990|1|
|9900|D001|1|
|9900|D990|1|
|9900|E001|1|
|9900|E990|1|
|9900|G001|1|
|9900|G990|1|
|9900|H001|1|
|9900|H990|1|
|9900|K001|1|
|9900|K990|1|
|9900|1001|1|
|9900|1990|1|
|9900|9001|1|
|9900|9900|24|
|9900|9990|1|
|9900|9999|1|
|9990|27|
|9999|47|
""".replace('\n', '\r\n')

        # Permite validacao de string grandes
        self.maxDiff = None
        arq = ArquivoDigital()

        arq._registro_abertura.COD_VER = '014'
        arq._registro_abertura.COD_FIN = '0'
        arq._registro_abertura.DT_INI = date(2020, 1, 1)
        arq._registro_abertura.DT_FIN = date(2020, 12, 31)
        arq._registro_abertura.NOME = 'EMPRESA TESTE'
        arq._registro_abertura.CNPJ = '53939351000129'
        arq._registro_abertura.CPF = '33333333333'
        arq._registro_abertura.UF = 'SP'
        arq._registro_abertura.IE = '222222222222'
        arq._registro_abertura.COD_MUN = '1234567'
        arq._registro_abertura.IM = '5999'
        arq._registro_abertura.SUFRAMA = '0123'
        arq._registro_abertura.IND_PERFIL = 'A'
        arq._registro_abertura.IND_ATIV = '1'

        contabilista = Registro0100()
        contabilista.NOME = 'CONTABILIDADE'
        contabilista.CPF = '99999999999'
        contabilista.CRC = 'MT00000000'
        contabilista.CEP = '78000000'
        contabilista.END = 'AV. UM'
        contabilista.NUM = '1'
        contabilista.COMPL = ''
        contabilista.BAIRRO = 'CENTRO'
        contabilista.FONE = '6599999999'
        contabilista.FAX = ''
        contabilista.EMAIL = 'contato@lucrorural.com.br'
        contabilista.COD_MUN = '5102637'
        arq._blocos['0'].add(contabilista)

        arq.prepare()

        assert txt == arq.getstring()
