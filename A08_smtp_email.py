import os
import getpass
import re
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
SMTP_SERVIDOR = 'smtp.gmail.com'
SMTP_PORTA = 587
def enviar_email(origem, destino):
    mensagem = MIMEMultipart()
    mensagem['Subject'] = 'Assunto: imagens de paz'
    mensagem['To'] = destino
    mensagem['From'] = origem
    corpo_mensagem = 'Imagens em anexo.'
    # anexando arquivos
    arquivos = os.listdir(os.getcwd())
    exp_regular_jpg = re.compile(".jpg", re.IGNORECASE)
    arquivos = filter(exp_regular_jpg.search, arquivos)
    for nome_arquivo in arquivos:
        path = os.path.join(os.getcwd(), nome_arquivo)
        if not os.path.isfile(path):
            continue
        imagem = MIMEImage(open(path, 'rb').read(), _subtype="jpg")
        imagem.add_header('Content-Disposition', 'attachment',
                       filename=nome_arquivo)
        mensagem.attach(imagem)
    parte_textual = MIMEText('text', "plain")
    parte_textual.set_payload(corpo_mensagem)
    mensagem.attach(parte_textual)
    # criando sessão SMTP: simple mail transfer protocol
    sessao = smtplib.SMTP(SMTP_SERVIDOR, SMTP_PORTA)
    sessao.ehlo()
    sessao.starttls()
    sessao.ehlo
    password = getpass.getpass(prompt="Informe sua senha de e-mail: ")
    sessao.login(origem, password)
    sessao.sendmail(origem, destino, mensagem.as_string())
    print("Email enviado.")
    sessao.quit()

enviar_email('education.always.wins@gmail.com',
             'ivo.jorge.portugal@gmail.com')