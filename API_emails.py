import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailAPI(object):

    def __init__(self) -> None:
        self.smtp_ssl_host = "smtp.gmail.com"
        self.smtp_ssl_port = 465
        self.user: str = "teste@teste.com"
        self.password: str = "teste123456"
        self.server = smtplib.SMTP_SSL(self.smtp_ssl_host, self.smtp_ssl_port)
        self.message: str = ""

    def escrever_email(self, mensagem: str) -> None:
        self.message = mensagem

    def enviar_email(self) -> None:
        email_msg = MIMEMultipart()
        email_msg["From"] = self.user
        email_msg["To"] = self.user
        email_msg["Subject"] = "Mensagem teste."
        email_msg.attach(MIMEText(self.message, 'plain'))
        self.server.login(self.user, self.password)
        self.server.sendmail(email_msg['From'], email_msg["To"], email_msg.as_string())

    def desativar_servidor(self)-> None:
        self.server.quit()
