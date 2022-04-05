from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

GOOGLE_FORMS_URL = "https://docs.google.com/forms/d/e/1FAIpQLScVvlGSA7QjTZheDRKCa5kxQB0O1ywbq5MtEbgRUJ-gTZjXtw/" \
                   "viewform?usp=sf_link"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22users" \
             "SearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.303896" \
             "32177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3" \
             "Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afals" \
             "e%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B" \
             "%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D" \
             "%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%" \
             "22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isList" \
             "Visible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

# Selenium set-up
service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_for_soup = webdriver.Chrome(service=service, options=options)
driver_for_forms = webdriver.Chrome(service=service, options=options)


# BeautifulSoup set-up
def generate_soup():
    """
    Workaround for the lack of interactivity from Beautiful Soup. As the web page loads contents dynamically, it is not
    possible to get all elements from the page. This functions opens the page using selenium, scrolls down the page to
    load the content and only then it will get the markup for Beautiful Soup to use.
    :return: a full instance of BeautifulSoup
    """
    driver_for_soup.get(url=ZILLOW_URL)
    for _ in range(8):
        scrollable_html = driver_for_soup.find_element(By.TAG_NAME, "html")
        time.sleep(0.5)
        scrollable_html.send_keys(Keys.PAGE_DOWN)
    html = driver_for_soup.page_source
    driver_for_soup.close()
    return BeautifulSoup(markup=html, parser="lxml", features="lxml")


soup = generate_soup()

addresses, prices, links = [], [], []
for rental in soup.select(selector="div ul li article div", class_="list-card-info"):
    # Try block to avoid 240 'NoneType' object has no attribute 'getText' // 'get'
    try:
        address_text = rental.find(name="a")
        price_text = rental.find(name="div", class_="list-card-price").getText()
        link_text = address_text.get("href")
        if link_text[1] == "b":
            join_link = "https://zillow.com" + link_text
            link_text = join_link
    except AttributeError as message_error:
        continue
    addresses.append(address_text.getText())
    prices.append(price_text)
    links.append(link_text)

# Using Selenium to fill up the forms
driver_for_forms.get(url=GOOGLE_FORMS_URL)
for index in range(len(addresses)):
    inputs = driver_for_forms.find_elements(By.CSS_SELECTOR, "input.whsOnd, zHQkBf")
    address = addresses[index]
    price = prices[index]
    link = links[index]
    # List in reverse order from form just to use .pop() so it pops the last item from the list
    data = [link, price, address]
    for data_to_submit in inputs:
        data_to_submit.click()
        data_to_submit.send_keys(data.pop())
    driver_for_forms.find_element(By.CSS_SELECTOR, "span.NPEfkd, RveJvd, snByac").click()
    time.sleep(2)
    driver_for_forms.find_element(By.TAG_NAME, "a").click()
