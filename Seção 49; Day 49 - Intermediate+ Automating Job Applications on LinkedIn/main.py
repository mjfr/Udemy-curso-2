import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?currentJobId=2962289759&f_" \
               "AL=true&geoId=106057199&keywords=python&location=Brasil&sortBy=R"
LOGIN_INFO = {
    "email": os.environ["EMAIL"],
    "password": os.environ["PASSWORD"]
}
service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.get(url=LINKEDIN_URL)
time.sleep(3)

driver.find_element(By.LINK_TEXT, "Sign in").click()
forms = driver.find_element(By.XPATH, "//*[@id=\"organic-div\"]/form")
forms.find_element(By.ID, "username").send_keys(LOGIN_INFO["email"])
forms.find_element(By.ID, "password").send_keys(LOGIN_INFO["password"])
forms.submit()

time.sleep(3)
# Minimiza a janela das mensagens que atrapalha no click do botão +Seguir
driver.find_element(By.XPATH, "/html/body/div[6]/aside/div[1]/header/div[3]/button[2]").click()
job_list = driver.find_element(By.CSS_SELECTOR, "ul.jobs-search-results__list").find_elements(
    By.CSS_SELECTOR, "a.disabled, ember-view, job-card-container__link, job-card-list__title")
# Dessa forma a lista obtém apenas 8 links, pois é necessário rolar a página para baixo para pegar mais links
# Porém, o objetivo não é pegar todos os links, apenas alguns para ter ideia que funciona e como funciona.
job_links = [job.get_attribute("href") for job in job_list][::2]  # [::2] pois há dois a tags que retornam o mesmo link

for job in range(len(job_list)-1):
    time.sleep(3)
    # Itera sobre os links salvos, pois se iterar sob os elementos, quando a página recarregar suas referências serão
    # perdidas, consequentemente gerando um erro.
    driver.get(job_links[job])
    time.sleep(3)
    html = driver.find_element(By.TAG_NAME, "html")
    driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button").click()
    for _ in range(8):
        html.send_keys(Keys.ARROW_DOWN)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "button.follow").click()
    driver.back()

driver.get("https://www.linkedin.com/my-items/saved-jobs/")
