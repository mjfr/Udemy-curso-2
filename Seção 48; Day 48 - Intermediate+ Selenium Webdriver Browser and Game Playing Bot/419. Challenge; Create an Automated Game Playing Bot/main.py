from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "https://orteil.dashnet.org/experiments/cookie/"
service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get(url=URL)

cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")


def click(clickable):
    clickable.click()


def cookie_amount():
    return int(driver.find_element(By.CSS_SELECTOR, "#money").text)


def get_formatted(element):
    return int(element.find_element(By.TAG_NAME, "b").text.replace(",", "").split("-")[-1::][0].strip())


def items_from_store():
    store = driver.find_element(By.CSS_SELECTOR, "#store")
    id_list = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal",
               "buyTime machine"]#, "buyElder Pledge"]
    to_be_formatted_list = []
    for item in id_list:
        to_be_formatted_list.append(get_formatted(store.find_element(By.ID, item)))
    return to_be_formatted_list


def bot():
    condition = True
    time_start = time.time()
    while condition:
        if time.time() == time_start + 300:
            print("5 minutos passaram")
            condition = False
        click(cookie)


bot()

# No momento o bot apenas clica, devo encontrar um método para fazer com que o bot compare valores e por fim compre os
# upgrades necessários
