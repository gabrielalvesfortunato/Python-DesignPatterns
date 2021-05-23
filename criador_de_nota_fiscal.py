from datetime import date


# Esse padrão para o python muitas vezes não faz muito sentido
# uma vez que dá pra solucionar o problema com os próprios
# recursos da linguagem de forma muito simples. O que acabou
# acontecendo NESSE CASO foi uma adição desnecessária de
# complexidade ao código.

## PATTERN BUILDER ##
class BuilderNotaFiscal(object):

    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__itens = None
        self.__detalhes = None

    def __repr__(self) -> str:
        return f'\nRazão Social: {self.__razao_social}\n' \
               f'CNPJ: {self.__cnpj}\n' \
               f'Data de emissão: {self.__data_de_emissao}\n' \
               f'Detalhes: {self.__detalhes}\n'

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self

    def constroi(self):
        if self.__razao_social is None:
            raise Exception("Razao social deve ser preenchida.")
        if self.__cnpj is None:
            raise Exception("CNPJ deve ser preenchido.")
        if self.__itens is None:
            raise Exception("Itens deve ser preenchido.")
        if self.__data_de_emissao is None:
            self.__data_de_emissao = date.today()
        else:
            return NotaFiscal( razao_social=self.__razao_social,
                               cnpj=self.__cnpj,
                               data_de_emissao=self.__data_de_emissao,
                               itens=self.__itens,
                               detalhes=self.__detalhes
            )
