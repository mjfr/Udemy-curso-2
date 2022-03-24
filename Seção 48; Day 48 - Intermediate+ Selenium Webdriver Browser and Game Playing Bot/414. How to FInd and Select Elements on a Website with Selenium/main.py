from selenium import webdriver
# Usado para selecionar o tipo de elemento
from selenium.webdriver.common.by import By
# Instalei: pip install webdriver-manager segundo a documentação do Selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# chrome_driver_path = "D:\\Python aprendizado\\Angela Yu\\100 Days of Code - The Complete Python Pro Bootcamp" \
#                      " for 2022\\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Mostrando como a tarefa de ontem poderia ser finalizada de maneira mais rápida e eficiente:
PRODUCT_URL = "https://www.amazon.com.br/dp/B084DWCZY6/ref=pav_d_fromAsin_B07PDHSJ1H_toAsin_B084DWCZY6"
driver.get(PRODUCT_URL)
# .find_element() pode ser encadeado
price = driver.find_element(By.CLASS_NAME, "a-price")
print(price.text.replace(".", "").replace("\n", ","))

driver.close()
