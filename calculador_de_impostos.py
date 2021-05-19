from typing import Union

from orcamento import Orcamento
from impostos import ICMS, ISS

Class = Union[ICMS, ISS]


class CalculadoraImpostos:

    @staticmethod
    def realiza_calculo(orcamento: Orcamento, imposto: Class) -> float:
        imposto_calculado: float = imposto.calcula(orcamento)
        return imposto_calculado
