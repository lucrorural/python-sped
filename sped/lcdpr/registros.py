# -*- coding: utf-8 -*-

from ..campos import Campo, CampoData, CampoFixo, CampoNumerico
from ..registros import Registro


class Registro0000(Registro):
    """
    ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DA PESSOA FÍSICA
    """
    campos = [
        CampoFixo(1, 'REG', '0000'),
        Campo(2, 'NOME_ESC', 'LCDPR'),
        Campo(3, 'COD_VER'),
        Campo(4, 'CPF'),
        Campo(5, 'NOME'),
        Campo(6, 'IND_SIT_INI_PER'),
        Campo(7, 'SIT_ESPECIAL'),
        CampoData(8, 'DT_SIT_ESP'),
        CampoData(9, 'DT_INI'),
        CampoData(10, 'DT_FIN'),
    ]


class Registro0010(Registro):
    """
    PARÂMETROS DE TRIBUTAÇÃO
    """
    campos = [
        CampoFixo(1, 'REG', '0010'),
        CampoNumerico(2, 'FORMA_APUR', precisao=0),
    ]


class Registro0030(Registro):
    """
    DADOS CADASTRAIS DO CONTRIBUINTE
    """
    campos = [
        CampoFixo(1, 'REG', '0030'),
        Campo(2, 'ENDERECO'),
        Campo(3, 'NUM'),
        Campo(4, 'COMPL'),
        Campo(5, 'BAIRRO'),
        Campo(6, 'UF'),
        Campo(7, 'COD_MUN'),
        Campo(8, 'CEP'),
        Campo(9, 'NUM_TEL'),
        Campo(10, 'EMAIL'),
    ]


class Registro0040(Registro):
    """
    DADOS CADASTRAIS DO CONTRIBUINTE
    """
    campos = [
        CampoFixo(1, 'REG', '0040'),
        Campo(2, 'COD_IMOVEL'),
        Campo(3, 'PAIS'),
        Campo(4, 'MOEDA'),
        Campo(5, 'CAD_ITR'),
        Campo(6, 'CAEPF'),
        Campo(7, 'INSCR_ESTADUAL'),
        Campo(8, 'NOME_IMOVEL'),
        Campo(9, 'ENDERECO'),
        Campo(10, 'NUM'),
        Campo(11, 'COMPL'),
        Campo(12, 'BAIRRO'),
        Campo(13, 'UF'),
        Campo(14, 'COD_MUN'),
        Campo(15, 'CEP'),
        Campo(16, 'TIPO_EXPLORACAO'),
        CampoNumerico(17, 'PARTICIPACAO'),
    ]


class Registro0045(Registro):
    """
    CADASTRO DE TERCEIROS
    """
    campos = [
        CampoFixo(1, 'REG', '0045'),
        Campo(2, 'COD_IMOVEL'),
        CampoNumerico(3, 'TIPO_CONTRAPARTE', precisao=0),
        Campo(4, 'ID_CONTRAPARTE'),
        Campo(5, 'NOME_CONTRAPARTE'),
        CampoNumerico(6, 'PERC_CONTRAPARTE', precisao=2),
    ]


class Registro0050(Registro):
    """
    CADASTRO DAS CONTAS BANCÁRIAS DO PRODUTOR RURAL
    """
    campos = [
        CampoFixo(1, 'REG', '0050'),
        CampoNumerico(2, 'COD_CONTA', precisao=0),
        Campo(3, 'PAIS_CTA'),
        Campo(4, 'BANCO'),
        Campo(5, 'NOME_BANCO'),
        Campo(6, 'AGENCIA'),
        Campo(7, 'NUM_CONTA'),
    ]


class RegistroQ100(Registro):
    """
    DEMONSTRATIVO DO RESULTADO DA ATIVIDADE RURAL
    """
    campos = [
        CampoFixo(1, 'REG', 'Q100'),
        CampoData(2, 'DATA'),
        Campo(3, 'COD_IMOVEL'),
        Campo(4, 'COD_CONTA'),
        Campo(5, 'NUM_DOC'),
        Campo(6, 'TIPO_DOC'),
        Campo(7, 'HIST'),
        Campo(8, 'ID_PARTIC'),
        Campo(9, 'TIPO_LANC'),
        CampoNumerico(10, 'VL_ENTRADA', precisao=2),
        CampoNumerico(11, 'VL_SAIDA', precisao=2),
        CampoNumerico(12, 'SLD_FIN', precisao=2),
        Campo(13, 'NAT_SLD_FIN'),
    ]


class RegistroQ200(Registro):
    """
    RESUMO MENSAL DO DEMONSTRATIVO DO RESULTADO DA ATIVIDADE RURAL
    """
    campos = [
        CampoFixo(1, 'REG', 'Q200'),
        Campo(2, 'MES'),
        CampoNumerico(3, 'VL_ENTRADA', precisao=2),
        CampoNumerico(4, 'VL_SAIDA', precisao=2),
        CampoNumerico(5, 'SLD_FIN', precisao=2),
        Campo(6, 'NAT_SLD_FIN'),
    ]


class Registro9999(Registro):
    """
    IDENTIFICAÇÃO DO CONTADOR E ENCERRAMENTO DO ARQUIVO DIGITAL
    """
    campos = [
        CampoFixo(1, 'REG', '9999'),
        Campo(2, 'IDENT_NOM'),
        Campo(3, 'IDENT_CPF_CNPJ'),
        Campo(4, 'IND_CRC'),
        Campo(5, 'EMAIL'),
        Campo(6, 'FONE'),
        CampoNumerico(7, 'QTD_LIN', precisao=0),
    ]
