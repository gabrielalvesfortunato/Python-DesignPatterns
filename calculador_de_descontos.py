from orcamento import *
from descontos import * 


class CalculadorDescontos:
    
    @staticmethod
    def calcula(orcamento: Orcamento) -> float:
        desconto: float = DescontoPorCincoItens(
            DescontoOrcamentoPorMaisDeQuinhentosReais(SemDesconto())
            ).calcula(orcamento)
        return desconto
