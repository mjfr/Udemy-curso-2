import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
weekday = now.weekday()  # Retorna um número (começando do 0 que é segunda)

if year == 2022:
    print("It is happening!!")
print(year)
print(month)
print(day)
print(weekday)

# Podemos criar objetos datetime próprios, definindo datas específicas.
date_of_birth = dt.datetime(year=1999, month=5, day=1)  # Ao não especificar a hora, o padrão é 00:00:00
print(date_of_birth)
