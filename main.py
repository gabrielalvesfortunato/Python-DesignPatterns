from orcamento import Orcamento, Item
from calculador_de_descontos import CalculadorDescontos
from calculador_de_impostos import CalculadoraImpostos
from impostos import *

    
if __name__ == "__main__":
    
    print("\n|-------------------------------------------|\n")

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
    desconto_orcamento = CalculadorDescontos()
    desconto = desconto_orcamento.calcula(orcamento)
    valor_com_desconto = orcamento.valor - desconto

    print(orcamento)
    print("Valor Total do orçamento: %.2f" % (orcamento.valor))
    print(f'Desconto no orçamento atual: {desconto}')
    print("Valor do orçamento com desconto: %.2f" % (valor_com_desconto))
    print(f'Quantidade de itens no orcamento: {(len(orcamento))}')
    
    print("\n|-------------------------------------------|\n")

    print('--- TESTANDO IMPOSTOS ---\n')

    print(f'ISS: {CalculadoraImpostos.realiza_calculo(orcamento, ISS())}')
    print(f'ICMS: {CalculadoraImpostos.realiza_calculo(orcamento, ICMS())}')
    print(f'ICPP: {CalculadoraImpostos.realiza_calculo(orcamento, ICPP())}')
    print(f'IKCV: {CalculadoraImpostos.realiza_calculo(orcamento, IKCV())}')
    print(f'ISS e ICMS: {CalculadoraImpostos.realiza_calculo(orcamento, ISS(ICMS()))}')
    print(f'ICPP e IKCV: {CalculadoraImpostos.realiza_calculo(orcamento, ICPP(IKCV()))}')
