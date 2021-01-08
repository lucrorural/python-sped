# -*- coding: utf-8 -*-

from ..blocos import Bloco
from .registros import (
    Registro0000,
    Registro0010,
    Registro0030,
    Registro0040,
    Registro0045,
    Registro0050,
    RegistroQ100,
    RegistroQ200,
    Registro9999
)


class Bloco0(Bloco):
    """
    Abre o arquivo, identifica a pessoa física,
    os imóveis rurais, as contas bancárias e
    referencia o período do LCDPR.
    """
    registro_abertura = None
    registro_encerramento = None


class BlocoQ(Bloco):
    """
    Apresenta o demonstrativo do resultado da atividade rural
    """
    registro_abertura = None
    registro_encerramento = None


class Bloco9(Bloco):
    """
    Identificação do Contador e Encerramento do Arquivo Digital
    """
    registro_abertura = None
    registro_encerramento = None
