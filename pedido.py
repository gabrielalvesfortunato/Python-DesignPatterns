from datetime import date
from abc import ABCMeta, abstractmethod


class Cliente(object):

    def __init__(self, nome: str, cpf: str, sexo: str, idade: int) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__sexo = sexo
        self.__idade = idade

    def __repr__(self) -> str:
        return f'\nNome: {self.nome}\n' \
               f'Idade: {self.idade}\n' \
               f'Sexo: {self.sexo}\n' \
               f'CPF: {self.cpf}\n'

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def sexo(self) -> str:
        return self.__sexo

    @property
    def idade(self) -> int:
        return self.__idade


class Pedido(object):

    def __init__(self, cliente: Cliente, valor: float) -> None:
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = "Pedido não Finalizado"

    def __repr__(self) -> str:
        return f'Cliente: {self.cliente.nome}\n' \
               f'Valor: {self.valor}\n' \
               f'Status: {self.status}\n' \
               f'Data de entrega: {self.__data_finalizacao}\n'

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def valor(self) -> float:
        return self.__valor

    @property
    def status(self) -> str:
        return self.__status

    @property
    def data_finalizacao(self) -> date:
        return self.__data_finalizacao

    def pagar(self) -> None:
        self.__status = "PAGO"
        self.__data_finalizacao = "Produto despachado."

    def finalizar(self) -> None:
        self.__data_finalizacao = date.today().strftime("%d/%m/%Y")
        self.__status = "ENTREGUE"


## PATTERN COMMAND ##
class Comando(metaclass=ABCMeta):

    @abstractmethod
    def executa(self) -> None:
        ...


class PagaPedido(Comando):

    def __init__(self, pedido: Pedido) -> None:
        self.__pedido = pedido

    def executa(self) -> None:
        self.__pedido.finalizar()


class ConcluiPedido(Comando):

    def __init__(self, pedido: Pedido) -> None:
        self.__pedido = pedido

    def executa(self) -> None:
        self.__pedido.pagar()


class FilaDeTrabalho(object):

    def __init__(self) -> None:
        self.__fila_de_comandos = []

    def __len__(self) -> int:
        return len(self.__fila_de_pedidos)

    def __getitem__(self, item):
        return self.__fila_de_comandos[item]

    def adicionar_comando(self, comando: Comando) -> None:
        self.__fila_de_comandos.append(comando)

    def processar_comandos(self) -> None:
        for comando in self.__fila_de_comandos:
            comando.executa()


if __name__ == "__main__":

    cliente1 = Cliente("Nome", "000.000.000-00",
                              "Masculino", 24)

    cliente2 = Cliente("Nome", "000.000.000-00",
                            "Feminino", 51)

    cliente3 = Cliente("Nome", "000.000.000-00",
                              "Masculino", 53)

    pedido1 = Pedido(cliente1, 999.00)
    pedido2 = Pedido(cliente2, 1999.00)
    pedido3 = Pedido(cliente3, 799.00)

    fila_de_trabalho = FilaDeTrabalho()
    fila_de_trabalho.adicionar_comando(PagaPedido(pedido1))
    fila_de_trabalho.adicionar_comando(PagaPedido(pedido2))
    fila_de_trabalho.adicionar_comando(ConcluiPedido(pedido3))

    fila_de_trabalho.processar_comandos()

    for comando in fila_de_trabalho:
        comando.executa()
