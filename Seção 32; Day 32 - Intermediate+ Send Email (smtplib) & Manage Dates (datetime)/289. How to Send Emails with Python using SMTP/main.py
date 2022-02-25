import smtplib
# IDENTIDADE DA CONTA DO EMAIL @ IDENTIDADE DO PROVEDOR DO EMAIL
TESTING_EMAIL = "*"
MADE_UP_PASSWORD = "*"
TEMPORARY_FAKE_EMAIL = "qucz@fls4.gleeze.com"
HOST = "smtp-mail.outlook.com"

# connection = smtplib.SMTP(host=HOST, port=587)
# connection.starttls()  # Transpor Layer Security
# connection.login(user=TESTING_EMAIL, password=MADE_UP_PASSWORD)
# connection.sendmail(TESTING_EMAIL, TEMPORARY_FAKE_EMAIL, "Subject:TESTE\n\nHello, trying to send an email from Python3")
# connection.close()

# Podemos fazer da mesma forma que quando vamos trabalhar com arquivos. Utilizamos a keyword with
with smtplib.SMTP(HOST) as connection:
    connection.starttls()  # --> Adiciona segurança a conexão com o servidor do e-mail. Dessa
# # forma, caso o e-mail seja interceptado, a mensagem estará criptografada.
    connection.login(user=TESTING_EMAIL, password=MADE_UP_PASSWORD)
    connection.sendmail(from_addr=TESTING_EMAIL, to_addrs=TEMPORARY_FAKE_EMAIL,
                        msg="Subject:TESTE\n\nHello, trying to send an email from Python3")
