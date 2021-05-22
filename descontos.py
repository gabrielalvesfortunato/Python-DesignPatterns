from typing import Union

from orcamento import Orcamento

### PATTERN CHAIN OF RESPONSABILITY - UMA CLASSE EVOCA OUTRA SE NAO FOR USADA ###
class SemDesconto:

    def calcula(self, orcamento: Orcamento) -> float:
        return 0.0


class DescontoOrcamentoPorMaisDeQuinhentosReais:

    def __init__(self, proximo_desconto: SemDesconto) -> None:
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento: Orcamento) -> float:
        if orcamento.valor > 500:
            return round(orcamento.valor * 0.07)
        else:
            return self.__proximo_desconto.calcula(orcamento)


class DescontoPorCincoItens:

    def __init__(self, proximo_desconto: 
                       DescontoOrcamentoPorMaisDeQuinhentosReais) -> None:
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento: Orcamento) -> float:
        if len(orcamento) > 5:
            return round(orcamento.valor * 0.1)
        else:
            return self.__proximo_desconto.calcula(orcamento)
