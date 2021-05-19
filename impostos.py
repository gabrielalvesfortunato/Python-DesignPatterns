from orcamento import Orcamento


class ISS:
    def __repr__(self) -> str:
        return f'{self.calcula}'    

    @staticmethod
    def calcula(orcamento: Orcamento) -> float:
        return orcamento.valor * 0.1


class ICMS:
    def __repr__(self) -> str:
        return f'{self.calcula}'      

    @staticmethod
    def calcula(orcamento: Orcamento) -> float:
        return orcamento.valor * 0.06 
