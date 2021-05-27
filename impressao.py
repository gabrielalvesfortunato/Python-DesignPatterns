### PATTERN VISITOR ###


class Impressao(object):

    def visita_soma(self, soma):
        print (f'+ ({soma.expressao_esquerda.aceita(self)})'
               f'({soma.expressao_direita.aceita(self)})')

    def visita_subtracao(self, subtracao):
        print (f'- ({subtracao.expressao_esquerda.aceita(self)})'
               f'({subtracao.expressao_direita.aceita(self)})')

    def visita_numero(self, numero):
        print (numero.realiza_operacao())
