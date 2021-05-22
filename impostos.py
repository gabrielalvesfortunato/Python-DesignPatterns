from abc import ABCMeta, abstractmethod

from orcamento import Orcamento

### PATTERN TEMPLATE METHOD ###
class TemplateImposto(metaclass=ABCMeta):
    ### PATTERN DECORATE UMA CLASSE É 'DECORADA' COM UMA OUTRA CLASSE/COMPORTAMENTO
    def __init__(self, outro_imposto = None) -> None:
        self.__outro_imposto = outro_imposto

    def __repr__(self) -> str:
        return f'{self.calcula(orcamento)}'

    def calculo_do_outro_imposto(self, orcamento: Orcamento) -> float:
        if self.__outro_imposto is not None:
            return self.__outro_imposto.calcula(orcamento)
        else:
            return 0

    @abstractmethod
    def calcula(self, orcamento: Orcamento) -> float:
        ...


### PATTERN TEMPLATE METHOD ###
class TemplateImpostoComCondicional(TemplateImposto, metaclass=ABCMeta):
    def __repr__(self) -> str:
        return super().__repr__()

    @abstractmethod
    def _deve_usar_maxima_taxacao(self, orcamento: Orcamento) -> bool:
        ...

    @abstractmethod
    def _maxima_taxacao(self, orcamento: Orcamento) -> float:
        ...

    @abstractmethod
    def _minima_taxacao(self, orcamento: Orcamento) -> float:
        ...

    def calcula(self, orcamento: Orcamento) -> float:
        if self._deve_usar_maxima_taxacao(orcamento):
            return self._maxima_taxacao(orcamento) + \
                   self.calculo_do_outro_imposto(orcamento)
        else:
            return self._minima_taxacao(orcamento) + \
                   self.calculo_do_outro_imposto(orcamento)


class ISS(TemplateImposto):
    def __repr__(self) -> str:
        return super().__repr__()

    def calcula(self, orcamento: Orcamento) -> float:
         return orcamento.valor * 0.1 + \
                self.calculo_do_outro_imposto(orcamento)


class ICMS(TemplateImposto):
    def __repr__(self) -> str:
        return super().__repr__()

    def calcula(self, orcamento: Orcamento) -> float:
        return orcamento.valor * 0.06 + \
               self.calculo_do_outro_imposto(orcamento)


class ICPP(TemplateImpostoComCondicional):
    def __repr__(self) -> str:
        return super().__repr__()

    def _maxima_taxacao(self, orcamento: Orcamento) -> float:
        return orcamento.valor * 0.07

    def _minima_taxacao(self, orcamento: Orcamento) -> float:
        return orcamento.valor * 0.05

    def _deve_usar_maxima_taxacao(self, orcamento: Orcamento) -> bool:
        if orcamento.valor > 500:
            return True
        return False


class IKCV(TemplateImpostoComCondicional):
    def __repr__(self) -> str:
        return super().__repr__()

    def _tem_item_maior_que_100_reais(self, orcamento: Orcamento) -> bool:
        for item in orcamento.itens:
            if item.valor > 100:
                return True
        return False

    def _maxima_taxacao(self, orcamento: Orcamento) -> float:
        return orcamento.valor * 0.1

    def _minima_taxacao(self, orcamento: Orcamento) -> float:
        return orcamento.valor * 0.03

    def _deve_usar_maxima_taxacao(self, orcamento: Orcamento) -> bool:
        if orcamento.valor > 500 and (
            self._tem_item_maior_que_100_reais(orcamento)
        ):
            return True
        else:
            return False
