# #################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
# actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas
import smtplib
import datetime as dt
from random import randint

TESTING_EMAIL = "*"
MADE_UP_PASSWORD = "*"
TEMPORARY_FAKE_EMAIL = "qucz@fls4.gleeze.com"
HOST = "smtp-mail.outlook.com"
now = dt.datetime.now()
month = now.month
day = now.day
try:
    csv_data = pandas.read_csv('./birthdays.csv')
except FileNotFoundError:
    with open('./birthdays.csv', 'w') as file_fix:
        file_fix.write("name,email,year,month,day\n")
        csv_data = pandas.read_csv('./birthdays.csv')
finally:
    dict_data = csv_data.to_dict(orient="records")


def get_all_birthdays(birthdays=dict_data):
    to_congratulate_list = [registry for registry in birthdays if month == registry["month"]
                            and day == registry["day"]]
    return to_congratulate_list


def assign_letter():
    birthday_list = get_all_birthdays()
    if len(birthday_list) > 0:
        for birthday_person in birthday_list:
            with open(file=f"./letter_templates/letter_{randint(1, 3)}.txt") as letter:
                random_letter = letter.read().replace("[NAME]", birthday_person["name"])
                send_letter(random_letter, birthday_person["email"])


def send_letter(birthday_letter, email):
    with smtplib.SMTP(host=HOST) as connection:
        connection.starttls()
        connection.login(user=TESTING_EMAIL, password=MADE_UP_PASSWORD)
        connection.sendmail(from_addr=TESTING_EMAIL, to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{birthday_letter}")


assign_letter()
