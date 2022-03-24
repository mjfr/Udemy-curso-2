from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# import datetime as dt

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
URL = "https://www.python.org/"

driver.get(URL)
driver.maximize_window()
upcoming_events_div = driver.find_element(By.CLASS_NAME, "event-widget")
# Pode parecer um pouquinho complicado, porém é fácil: List comprehension que busca as datas dos próximos eventos.
# As datas são obtidas como uma string de um datetime. Logo, convertemos a string para um objeto datetime, depois,
# Convertemos novamente o objeto datetime para uma string porém formatado para o formato de data dd/mm/YYYY
# upcoming_event_dates = [
#     dt.datetime.strftime(dt.datetime.strptime(date.get_attribute("datetime").split("T")[0], "%Y-%m-%d"), "%d/%m/%Y")
#     for date in upcoming_events_div.find_elements(By.TAG_NAME, "time")
# ]
# OU
# Uma maneira mais curta também utilizando list comprehension: primeiramente obtém-se os datetimes que estão na div
# de "Upcoming Events" e assim pegamos seu atributo datetime que nos retorna um datetime em forma de string.
# Fazemos o primeiro split para separar a data do tempo e depois outro split para destituir a data de seus - separadores
# por fim, invertemos a ordem da lista obtida após o segundo split para transformar a data no formato que estamos
# acostumados e realizamos um join com uma barra agindo como separador.
# * Só fui pensar nesse método após demoradamente desenvolver o primeiro ;(
upcoming_events_dates = [
    "/".join(date.get_attribute("datetime").split("T")[0].split("-")[::-1])
    for date in upcoming_events_div.find_elements(By.TAG_NAME, "time")
]

upcoming_events_titles = [
    title.text for title in upcoming_events_div.find_elements(By.TAG_NAME, "a")[1::]
]

upcoming_events = {}
for number in range(len(upcoming_events_dates)):
    upcoming_events[number] = {
        "time": upcoming_events_dates[number],
        "name": upcoming_events_titles[number]
    }

print(upcoming_events)

driver.close()
