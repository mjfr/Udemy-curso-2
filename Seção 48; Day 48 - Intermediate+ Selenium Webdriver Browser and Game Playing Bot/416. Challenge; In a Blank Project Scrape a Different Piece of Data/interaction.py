from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# Classe que contém constantes das teclas que podemos usar
from selenium.webdriver.common.keys import Keys
# Importado para deixar o chrome aberto
from selenium.webdriver.chrome.options import Options

WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Main_Page"
CHALLENGE_URL = "http://secure-retreat-92358.herokuapp.com/"
service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)


# driver.get(WIKIPEDIA_URL)
# articles_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(articles_count.text)
# # articles_count.click()
#
# # Encontra um elemento (link) através de seu texto
# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# # all_portals.click()
#
# # Busca pelo atributo name="search" no DOM
# search = driver.find_element(By.NAME, "search")
# # Envia a string para o campo de texto
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get(CHALLENGE_URL)
form = driver.find_element(By.CSS_SELECTOR, ".form-signin")
first_name = form.find_element(By.NAME, "fName")
last_name = form.find_element(By.NAME, "lName")
email_address = form.find_element(By.NAME, "email")
first_name.send_keys("Matheus")
last_name.send_keys("José")
email_address.send_keys("email@email.com")
form.submit()
