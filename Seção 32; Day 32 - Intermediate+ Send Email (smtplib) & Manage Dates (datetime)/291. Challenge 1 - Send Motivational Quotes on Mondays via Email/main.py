import datetime as dt
import smtplib
from random import choice

TESTING_EMAIL = "*"
MADE_UP_PASSWORD = "*"
TEMPORARY_FAKE_EMAIL = "qucz@fls4.gleeze.com"
HOST = "smtp-mail.outlook.com"


def get_random_quote():
    with open(file="quotes.txt") as data:
        quotes_list = data.readlines()
    return choice(quotes_list)


def send_email():
    if dt.datetime.now().weekday() == 4:
        with smtplib.SMTP(host=HOST) as connection:
            connection.starttls()
            connection.login(user=TESTING_EMAIL, password=MADE_UP_PASSWORD)
            connection.sendmail(from_addr=TESTING_EMAIL, to_addrs=TEMPORARY_FAKE_EMAIL,
                                msg=f"Subject:Your weekly motivational quote!! Yay \\o/\n\n{get_random_quote()}")


send_email()
