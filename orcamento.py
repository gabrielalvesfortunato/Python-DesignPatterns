from typing import List


class Item:
    def __init__(self, nome: str, valor: float) -> None:
        self.__nome  = nome
        self.__valor = valor

    def __repr__(self) -> str:
        return f'{self.nome} - {self.valor}'

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, novo_valor: float) -> None:
        self.__valor = novo_valor


class Orcamento:
    def __init__(self) -> None:
        self.__itens: List[Item]  = []

    def __len__(self) -> int:
        return len(self.__itens)

    def __repr__(self) -> str:
        return f'{self.itens}'

    @property
    def valor(self) -> float:
        total: float = 0.0
        for item in self.__itens:
            total += item.valor
        return total

    @property
    def itens(self) -> List:
        return self.__itens    

    def adiciona_item(self, item: Item) -> None:
        self.itens.append(item)
