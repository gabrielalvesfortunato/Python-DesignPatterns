from typing import List, Any
from abc import ABCMeta, abstractmethod


class Item:
    def __init__(self, nome: str, valor: float) -> None:
        self.__nome: str  = nome
        self.__valor: float = valor

    def __repr__(self) -> str:
        return f'{self.nome} - {self.valor}'

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def valor(self) -> float:
        return self.__valor


class Orcamento:
    def __init__(self) -> None:
        self.__itens: List[Item]  = []
        self.estado_atual = StateOrcamentoEmAnalise()
        self.__desconto_extra: float = 0.0

    def __len__(self) -> int:
        return len(self.__itens)

    def __repr__(self) -> str:
        return f'{self.itens}'

    @property
    def valor(self) -> float:
        total: float = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    @property
    def itens(self) -> List:
        return self.__itens    

    def aprova_orcamento(self) -> Any:
        self.estado_atual.aprova_orcamento(orcamento)

    def reprova_orcamento(self) -> Any:
        self.estado_atual.reprova_orcamento(orcamento)

    def finaliza_orcamento(self) -> Any:
        self.estado_atual.finaliza_orcamento(orcamento)

    def adicionar_item(self, item: Item) -> None:
        self.itens.append(item)

    def adiciona_desconto_extra(self, desconto: float) -> None:
        self.__desconto_extra += desconto

    def aplica_desconto_extra(self) -> None:
        self.estado_atual.aplica_desconto_extra(self)


## APLICANDO O PATTERN ººTemplate Methodºº PARA OS ESTADOS DE ORCAMENTO ##
class TemplateStateDeUmOrcamento(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.desconto_aplicado = False

    @abstractmethod
    def aplica_desconto_extra(self, orcamento: Orcamento) -> Any:
        ...

    @abstractmethod
    def aprova_orcamento(self, orcamento: Orcamento) -> Any:
        ...

    @abstractmethod
    def reprova_orcamento(self, orcamento: Orcamento) -> Any:
        ...

    @abstractmethod
    def finaliza_orcamento(self, orcamento: Orcamento) -> Any:
        ...


## APLICANDO O PATTERN ººSTATEºº PARA OS ESTADOS DE ORCAMENTO ##
class StateOrcamentoEmAnalise(TemplateStateDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento: Orcamento) -> Any:
        if not self.desconto_aplicado:
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)
            self.desconto_aplicado = True
        else:
            raise Exception("Desconto já aplicado")

    def aprova_orcamento(self, orcamento: Orcamento) -> Any:
        orcamento.estado_atual = StateOrcamentoAprovado()

    def reprova_orcamento(self, orcamento: Orcamento) -> Any:
        orcamento.estado_atual = StateOrcamentoReprovado()

    def finaliza_orcamento(self, orcamento: Orcamento) -> Any:
        raise Exception('''
            Orçamentos em aprovação não podem ser finalizados.
        ''')


class StateOrcamentoAprovado(TemplateStateDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento: Orcamento) -> Any:
        if not self.desconto_aplicado:
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
            self.desconto_aplicado = True
        else:
            raise Exception("Desconto já aplicado.")

    def aprova_orcamento(self, orcamento: Orcamento) -> Any:
        raise Exception("Orçamento já aprovado.")

    def reprova_orcamento(self, orcamento: Orcamento) -> Any:
        raise Exception("Orçamentos aprovados não podem ser reprovados.")

    def finaliza_orcamento(self, orcamento: Orcamento) -> Any:
        orcamento.estado_atual = StateOrcamentoFinalizado()


## Orçamentos reprovados NÃO recebem descontos ##
class StateOrcamentoReprovado(TemplateStateDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento: Orcamento) -> Any:
        if not self.desconto_aplicado:
            orcamento.adiciona_desconto_extra(orcamento.valor * 0)
            self.desconto_aplicado = True
        else:
            raise Exception("Desconto já aplicado.")

    def aprova_orcamento(self, orcamento: Orcamento) -> Any:
        raise Exception("Orçamentos reprovados não podem ser aprovados.")

    def reprova_orcamento(self, orcamento: Orcamento) -> Any:
        raise Exception('''
            Orcamentos reprovados não podem ser reprovados novamente.
        ''')

    def finaliza_orcamento(self, orcamento: Orcamento) -> Any:
        orcamento.estado_atual = StateOrcamentoFinalizado()


## Orcamentos finalizados NÃO recebem descontos ##
class StateOrcamentoFinalizado(TemplateStateDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento: Orcamento) -> Any:
        if not self.desconto_aplicado:
            orcamento.adiciona_desconto_extra(orcamento.valor * 0)
            self.desconto_aplicado = True
        else:
            raise Exception("Desconto já aplicado.")

    def aprova_orcamento(self, orcamento: Orcamento) -> Any:
        raise Exception('''
            Orçamentos finalizados não podem ser aprovados.
        ''')

    def reprova_orcamento(self, orcamento: Orcamento) -> Any:
        raise Exception("Orçamentos finalizados não podem ser reprovados.")

    def finaliza_orcamento(self, orcamento: Orcamento) -> Any:
        raise Exception('''
            Orçamentos finalizados não podem ser finalizados novamente.
        ''')





if __name__ == "__main__":
    item_orcamento1 = Item("Bola de Plástico", 10.00)
    item_orcamento2 = Item("Conjunto de Porcelana", 100.00)
    item_orcamento3 = Item("Conjunto de talheres de prata", 25.99)
    item_orcamento4 = Item("Notebook", 100.99)
    item_orcamento5 = Item("Cama de Casal", 50.99)
    item_orcamento6 = Item("Mesa de Escritório", 295.90)

    orcamento = Orcamento()
    orcamento.adicionar_item(item_orcamento1)
    orcamento.adicionar_item(item_orcamento2)
    orcamento.adicionar_item(item_orcamento3)
    orcamento.adicionar_item(item_orcamento4)
    orcamento.adicionar_item(item_orcamento5)
    orcamento.adicionar_item(item_orcamento6)

    print(f'Orçamento antes do desconto: {orcamento.valor}')
    orcamento.reprova_orcamento()
    orcamento.finaliza_orcamento()
    orcamento.aplica_desconto_extra()
    print(f'Orçamento depois do desconto (Finalizado): {orcamento.valor}')
