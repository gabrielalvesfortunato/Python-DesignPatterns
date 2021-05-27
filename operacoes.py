from abc import ABCMeta, abstractmethod
from impressao import Impressao


## PATTERN INTERPETRER ##
class Expressoes(object, metaclass=ABCMeta):

    @abstractmethod
    def realiza_operacao(self):
        ...

    @abstractmethod
    def aceita(self, visitor: Impressao):
        ...


class Numero(Expressoes):

    def __init__(self, numero: float):
        self._numero = numero

    def realiza_operacao(self):
        return self._numero

    def aceita(self, visitor: Impressao):
        visitor.visita_numero(self)


class Subtracao(Expressoes):

    def __init__(self, expressao_esquerda: Numero, expressao_direira: Numero):
        self._expressao_direita: Numero = expressao_direira
        self._expressao_esquerda: Numero = expressao_esquerda

    @property
    def expressao_direita(self):
        return self._expressao_direita

    @property
    def expressao_esquerda(self):
        return self._expressao_esquerda

    def realiza_operacao(self):
        return self._expressao_esquerda.realiza_operacao() - \
               self._expressao_direita.realiza_operacao()

    def aceita(self, visitor: Impressao):
        visitor.visita_subtracao(self)


class Soma(Expressoes):

    def __init__(self, expressao_esquerda: Numero, expressao_direira: Numero):
        self._expressao_direita: Numero = expressao_direira
        self._expressao_esquerda: Numero = expressao_esquerda

    @property
    def expressao_direita(self):
        return self._expressao_direita

    @property
    def expressao_esquerda(self):
        return self._expressao_esquerda

    def realiza_operacao(self):
        return self._expressao_esquerda.realiza_operacao() + \
               self._expressao_direita.realiza_operacao()

    def aceita(self, visitor: Impressao):
        visitor.visita_soma(self)





if __name__ == '__main__':

    impressao =  Impressao()

    expressao_direita = Subtracao(Numero(100), Numero(20))
    expressao_esquerda = Soma(Numero(5), Numero(2))
    calculo = Soma(expressao_esquerda, expressao_direita)

    calculo.aceita(impressao)
