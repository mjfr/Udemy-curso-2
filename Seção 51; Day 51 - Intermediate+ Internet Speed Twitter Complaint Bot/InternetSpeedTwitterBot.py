import os
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InternetSpeedTwitterBot:
    def __init__(self, url: str):
        self.up = 0
        self.down = 0
        self.TWITTER_USERNAME = "LearningPython_"
        self.TWITTER_PASSWORD = os.environ["PASSWORD"]
        self.url = url
        self.service = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.maximize_window()
        self.driver.get(url=url)

    def get_internet_speed(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.js-start-test, test-mode-multi").click()
        print("Even if the test ends, be patient, it takes 120 seconds to go to the next stage")
        time.sleep(120)
        self.driver.find_element(By.TAG_NAME, "html").send_keys(Keys.ESCAPE)
        time.sleep(2)
        self.up = float(self.driver.find_element(By.XPATH, "//*[@id=\"container\"]/div/div[3]/div/div/div/div[2]/"
                                                           "div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]"
                                                           "/div/div[2]/span").text)
        self.down = float(self.driver.find_element(By.XPATH, "//*[@id=\"container\"]/div/div[3]/div/div/div/div[2]/"
                                                             "div[3]/div[3]/div/div[3]/div/div/"
                                                             "div[2]/div[1]/div[2]/div/div[2]/span").text)
        self.driver.close()
        time.sleep(3)

    def tweet_at_provider(self, message):
        if message is not None:
            self.driver.find_element(By.LINK_TEXT, "Tweet").click()
            message_box = self.driver.find_element(By.CSS_SELECTOR, "div.public-DraftStyleDefault-block, "
                                                                    "public-DraftStyleDefault-ltr")
            message_box.send_keys(message, Keys.CONTROL + Keys.ENTER)
