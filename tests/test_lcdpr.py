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
from sped.lcdpr.registros import (Registro0000, Registro0010, Registro0030,
                                  Registro0040, Registro0045, Registro0050,
                                  Registro9999, RegistroQ100, RegistroQ200)


class TestLcdpr():

    def test_read_registro(self):
        txt = u"""|0000|LCDPR|0014|00000000000|TESTE|0|0||01012020|31122020|
|0010|1|
|0030|ROD MT 570 KM 12 A ESQUERDA|S/N||Zona Rural|MT|5102637|78000000|000006599999999|teste@gmail.com|
|0040|1|BR|BRL|00000000|00000000000000|130000000|FAZENDA I|ESTRADA 1|SN||ZONA RURAL|MT|5102637|78000000|1|79,99|
|0045|1|3|99999999999|PROPRIETARIO TESTE|79,99|
|0050|0|BR|756|Banco Cooperativo do Brasil S.A.|1111|2222222|
|Q100|01012020|1|0|196107|6|HISTORICO TESTE POSITIVO|99999999000000|1|134,66|0|134,66|P|
|Q100|01022020|1|0|196108|6|HISTORICO TESTE NEGATIVO|99999999000000|2|0|266,35|-131,69|N|
|Q200|012020|134,66|0|134,66|P|
|Q200|022020|0|266,35|-131,69|N|
|9999|Contabilidade|00000000000|MT12345678|contato@lucrorural.com.br|6599999999|11|
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

        bloco_0 = arq._blocos['0']
        reg_0010 = Registro0010()
        reg_0010.FORMA_APUR = '1'
        bloco_0.add(reg_0010)

        reg_0030 = Registro0030()
        reg_0030.ENDERECO = 'ROD MT 570 KM 12 A ESQUERDA'
        reg_0030.NUM = 'S/N'
        reg_0030.COMPL = ''
        reg_0030.BAIRRO = 'Zona Rural'
        reg_0030.UF = 'MT'
        reg_0030.COD_MUN = '5102637'
        reg_0030.CEP = '78000000'
        reg_0030.NUM_TEL = '000006599999999'
        reg_0030.EMAIL = 'teste@gmail.com'
        bloco_0.add(reg_0030)

        reg_0040 = Registro0040()
        reg_0040.COD_IMOVEL = '1'
        reg_0040.PAIS = 'BR'
        reg_0040.MOEDA = 'BRL'
        reg_0040.CAD_ITR = '00000000'
        reg_0040.CAEPF = '00000000000000'
        reg_0040.INSCR_ESTADUAL = '130000000'
        reg_0040.NOME_IMOVEL = 'FAZENDA I'
        reg_0040.ENDERECO = 'ESTRADA 1'
        reg_0040.NUM = 'SN'
        reg_0040.COMPL = ''
        reg_0040.BAIRRO = 'ZONA RURAL'
        reg_0040.UF = 'MT'
        reg_0040.COD_MUN = '5102637'
        reg_0040.CEP = '78000000'
        reg_0040.TIPO_EXPLORACAO = '1'
        reg_0040.PARTICIPACAO = 79.99
        bloco_0.add(reg_0040)

        reg_0045 = Registro0045()
        reg_0045.COD_IMOVEL = '1'
        reg_0045.TIPO_CONTRAPARTE = '3'
        reg_0045.ID_CONTRAPARTE = '99999999999'
        reg_0045.NOME_CONTRAPARTE = 'PROPRIETARIO TESTE'
        reg_0045.PERC_CONTRAPARTE = 79.99
        bloco_0.add(reg_0045)

        reg_0050 = Registro0050()
        reg_0050.COD_CONTA = '0'
        reg_0050.PAIS_CTA = 'BR'
        reg_0050.BANCO = '756'
        reg_0050.NOME_BANCO = 'Banco Cooperativo do Brasil S.A.'
        reg_0050.AGENCIA = '1111'
        reg_0050.NUM_CONTA = '2222222'
        bloco_0.add(reg_0050)

        bloco_Q = arq._blocos['Q']

        reg_q100 = RegistroQ100()
        reg_q100.DATA = date(2020, 1, 1)
        reg_q100.COD_IMOVEL = '1'
        reg_q100.COD_CONTA = '0'
        reg_q100.NUM_DOC = '196107'
        reg_q100.TIPO_DOC = '6'
        reg_q100.HIST = 'HISTORICO TESTE POSITIVO'
        reg_q100.ID_PARTIC = '99999999000000'
        reg_q100.TIPO_LANC = '1'
        reg_q100.VL_ENTRADA = 134.66
        reg_q100.VL_SAIDA = 0
        reg_q100.SLD_FIN = 134.66
        reg_q100.NAT_SLD_FIN = 'P'
        bloco_Q.add(reg_q100)

        reg_q100 = RegistroQ100()
        reg_q100.DATA = date(2020, 2, 1)
        reg_q100.COD_IMOVEL = '1'
        reg_q100.COD_CONTA = '0'
        reg_q100.NUM_DOC = '196108'
        reg_q100.TIPO_DOC = '6'
        reg_q100.HIST = 'HISTORICO TESTE NEGATIVO'
        reg_q100.ID_PARTIC = '99999999000000'
        reg_q100.TIPO_LANC = '2'
        reg_q100.VL_ENTRADA = 0
        reg_q100.VL_SAIDA = 266.35
        reg_q100.SLD_FIN = -131.69
        reg_q100.NAT_SLD_FIN = 'N'
        bloco_Q.add(reg_q100)

        reg_q200 = RegistroQ200()
        reg_q200.MES = '012020'
        reg_q200.VL_ENTRADA = 134.66
        reg_q200.VL_SAIDA = 0
        reg_q200.SLD_FIN = 134.66
        reg_q200.NAT_SLD_FIN = 'P'
        bloco_Q.add(reg_q200)

        reg_q200 = RegistroQ200()
        reg_q200.MES = '022020'
        reg_q200.VL_ENTRADA = 0
        reg_q200.VL_SAIDA = 266.35
        reg_q200.SLD_FIN = -131.69
        reg_q200.NAT_SLD_FIN = 'N'
        bloco_Q.add(reg_q200)

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
