# -*- coding: utf-8 -*-

from .. import arquivos
from . import blocos
from . import registros
from . blocos import Bloco0, BlocoQ, Bloco9
from . registros import (
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


class ArquivoDigital(arquivos.ArquivoDigital):
    registro_abertura = Registro0000
    registro_encerramento = Registro9999
    registros = registros
    blocos = blocos

    def __init__(self):
        super(ArquivoDigital, self).__init__()
        self._blocos['0'] = Bloco0()
        self._blocos['Q'] = BlocoQ()
        self._blocos['9'] = Bloco9()

    def prepare(self):
        # Registro9999 QTD_LIN -> Quantidade total de linha no arquivo
        reg_count = 1
        for bloco in self._blocos.values():
            reg_count += len(bloco.registros)

            if bloco == self._blocos['9']:
                bloco.registros[0].valores[7] = str(reg_count)
