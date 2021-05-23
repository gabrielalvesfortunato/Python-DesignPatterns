from API_emails import EmailAPI

## PATTERN OBSERVER ##
def imprimir(nota_fiscal):
    print("Conectando à impressora..")
    print("Imprimindo documento...")
    print("Impressão finalizada!")


def enviar_nota_fiscal_por_email(nota_fiscal):
    print("Enviando nota fiscal para o email...")
    email = EmailAPI()
    email.escrever_email(nota_fiscal.__repr__())
    email.enviar_email()
    email.desativar_servidor()
    print("Nota fiscal enviada para o email!")


def salvar_no_banco_de_dados(nota_fiscal):
    print("Se conectando ao banco de dados...")
    print("Salvando dados no banco de dados...")
    print("Dados salvos!")
