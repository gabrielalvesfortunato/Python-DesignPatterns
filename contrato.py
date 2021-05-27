from  datetime import date
from typing import List

## PATTERN MEMENTO ##
class Contrato(object):

    def __init__(self, data: date, cliente: str, tipo: str) -> None:
        self._data: date = data
        self._cliente: str = cliente
        self._tipo: str = tipo.upper()

    def __repr__(self) -> str:
        return f'\nData: {self.data}\n' \
               f'Cliente: {self._cliente}\n' \
               f'Tipo do Contrato: {self._tipo}'

    @property
    def data(self) -> date:
        return self._data.strftime("%d/%m/%Y")

    @data.setter
    def data(self, data: str) -> None:
        self.data = data

    @property
    def cliente(self) -> str:
        return self._cliente

    @cliente.setter
    def cliente(self, cliente: str) -> None:
        self._cliente = cliente

    @property
    def tipo(self) -> str:
        return self._tipo

    @tipo.setter
    def tipo(self, tipo) -> None:
        self._tipo = tipo

    def avanca(self) -> None:
        if self._tipo == 'NOVO':
            self._tipo = 'EM ANDAMENTO'
        elif self._tipo == 'EM ANDAMENTO':
            self._tipo = 'ACERTADO'
        elif self._tipo == 'ACERTADO':
            self._tipo = 'CONCLUIDO'

    def salva_estado(self):
        return Estado(Contrato(data=self._data,
                               cliente=self._cliente,
                               tipo=self._tipo))

    def restaura_estado(self, estado):
        self._cliente = estado.contrato.cliente
        self._data = estado.contrato.data
        self._tipo = estado.contrato.tipo


class Estado(object):

    def __init__(self, contrato : Contrato) -> None:
        self._contrato: Contrato = contrato

    @property
    def contrato(self) -> Contrato:
        return self._contrato


class Historico(object):

    def __init__(self) -> None:
        self._estados_salvos: List = []

    def __repr__(self) -> str:
        return f'{self._estados_salvos}'

    def obtem_estado(self, index: int) -> Estado:
        return self._estados_salvos[index]

    def adiciona_estado(self, estado) -> None:
        self._estados_salvos.append(estado)


if __name__ == "__main__":

    historico = Historico()

    contrato = Contrato(data=date.today(),
                        cliente="Nome Sobrenome",
                        tipo="NOVO")

    print(contrato)
    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    print(contrato)
    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    print(contrato)
    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())
    print(contrato)

    contrato.restaura_estado(historico.obtem_estado(1))

    print(f'\n{contrato.tipo}')

