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


def get_formatted(element: str):
    try:
        return int(element.replace(",", "").split("-")[-1::][0].strip())
    except ValueError:
        pass


def cookie_amount():
    return int(driver.find_element(By.CSS_SELECTOR, "#money").text.replace(",", ""))


def get_prices():
    return [get_formatted(price.text) for price in driver.find_elements(By.CSS_SELECTOR, "#store b")
            if get_formatted(price.text) is not None]


def bot():
    cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
    store_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
    ids_from_store = [item.get_attribute(By.ID) for item in store_items]
    upgrade_time = time.time() + 2
    ending_time = time.time() + 300
    while True:
        cookie.click()
        if time.time() > upgrade_time:
            upgrades_price = {price1: id1 for price1, id1 in zip(get_prices(), ids_from_store)}
            available_upgrades = {price2: id2 for price2, id2 in upgrades_price.items() if cookie_amount() >= price2}
            try:
                driver.find_element(By.ID, available_upgrades[max(available_upgrades)]).click()
            except ValueError:
                continue
            upgrade_time += 5
        if time.time() > ending_time:
            break


bot()
cookie_per_sec = driver.find_element(By.ID, "cps").text
print(cookie_per_sec)
