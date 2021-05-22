from orcamento import Orcamento
from impostos import *

## Pattern Strategy ##
class CalculadoraImpostos:

    @staticmethod
    def realiza_calculo(orcamento: Orcamento, imposto) -> float:
        imposto_calculado: float = imposto.calcula(orcamento)
        return round(imposto_calculado)
