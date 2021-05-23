from datetime import datetime, date
from validate_docbr import CNPJ
from typing import List, Any

from criador_de_nota_fiscal import BuilderNotaFiscal


class Item(object):
    def __init__(self, descricao: str, valor: float) -> None:
        self.__descricao: str = descricao
        self.__valor: float = valor

    def __repr__(self) -> str:
        return f'{self.descricao}: R${self.valor}'

    @property
    def valor(self) -> float:
        return self.__valor

    @property
    def descricao(self) -> str:
        return self.__descricao


class NotaFiscal(object):

    def __init__(self, razao_social: str, cnpj: CNPJ, itens: Item,
                 data_de_emissao: date = datetime.today().strftime("%d/%m/%Y"),
                 detalhes: str = "Sem Detalhes", observers = []) -> None:
        if self._validar_entrada_de_dados(detalhes, cnpj):
            self.__razao_social = razao_social
            self.__cnpj = cnpj
            self.__data_de_emissao = data_de_emissao
            self.__detalhes = detalhes
            self.__itens = []

            ## Pattern Observer ##
            for observer in observers:
                observer(self)

    def __repr__(self) -> str:
        return f'\nRazão Social: {self.razao_social}\n' \
               f'CNPJ: {self.cnpj}\n' \
               f'Data de emissão: {self.data_de_emissao}\n' \
               f'Detalhes: {self.detalhes}\n'

    @property
    def razao_social(self) -> str:
        return self.__razao_social

    @property
    def cnpj(self) -> CNPJ:
        cnpj_format = CNPJ()
        return cnpj_format.mask(self.__cnpj)

    @property
    def data_de_emissao(self) -> date:
        return self.__data_de_emissao

    @property
    def detalhes(self) -> str:
        return self.__detalhes

    @property
    def itens(self):
        self.__itens

    def retorna_itens(self) -> List:
        for item in self.__itens:
            return item

    def adicionar_item(self, item: Item) -> None:
        self.__itens.append(item)

    @staticmethod
    def _validar_detalhes_na_nota_fiscal(detalhes: str) -> bool:
        if len(detalhes) > 30:
            raise ValueError('''
                Detalhes da nota não podem ter mais do que 30 caracteres!!
            ''')
            return False
        else:
            return True

    @staticmethod
    def _validar_cnpj(cnpj: str) -> Any:
        validador_cnpj = CNPJ()
        if validador_cnpj.validate(cnpj):
            return True
        else:
            raise ValueError("CNPJ Inválido!!!")

    def _validar_entrada_de_dados(self, detalhes: str, cnpj: str) -> bool:
        if self._validar_detalhes_na_nota_fiscal(detalhes) and (
            self._validar_cnpj(cnpj)
        ):
            return True
        else:
            return False





if __name__ == "__main__":

    from observers import *


    itens = [
        Item(
            "ITEM A",
            100.00
        ),
        Item(
            "ITEM B",
            250.00
        ),Item(
            "ITEM C",
            340.0
        )
    ]

    nota_fiscal = NotaFiscal(
        "FHSA Limitada",
        "71199181000175",
        itens,
        observers = [imprimir, enviar_nota_fiscal_por_email, salvar_no_banco_de_dados]
    )

    print(nota_fiscal)
    nota_fiscal.adicionar_item(itens)
    print(nota_fiscal.retorna_itens())
