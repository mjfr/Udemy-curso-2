from InternetSpeedTwitterBot import InternetSpeedTwitterBot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

TWITTER_URL = "https://twitter.com/i/flow/login"
SPEED_TEST_URL = "https://www.speedtest.net/"
PROMISED_DOWN = 240
PROMISED_UP = 20

speed_test_bot = InternetSpeedTwitterBot(SPEED_TEST_URL)
speed_test_bot.get_internet_speed()


def speed_comparison():
    if (PROMISED_DOWN / 100 * 80) > speed_test_bot.down or (PROMISED_UP / 100 * 80) > speed_test_bot.up:
        return f"Hey internet provider, why is my internet speed {speed_test_bot.down} down/{speed_test_bot.up} up" \
               f" when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up?\n*Automatically generated tweet for learning" \
               f" purposes only"
    return None


def twitter_log_in(bot):
    time.sleep(3)
    username = bot.driver.find_element(By.TAG_NAME, "input")
    username.send_keys(bot.TWITTER_USERNAME)
    username.send_keys(Keys.ENTER)
    time.sleep(2)
    if bot.driver.find_element(By.TAG_NAME, "input").get_attribute("name") == "text":
        confirming_username = bot.driver.find_element(By.TAG_NAME)
        confirming_username.send_keys(bot.TWITTER_USERNAME)
        confirming_username.send_keys(Keys.ENTER)
        time.sleep(2)
    password = bot.driver.find_element(By.NAME, "password")
    password.send_keys(bot.TWITTER_PASSWORD)
    password.send_keys(Keys.ENTER)
    time.sleep(2)


def start_bot():
    test_result = speed_comparison()
    if test_result is not None:
        twitter_bot = InternetSpeedTwitterBot(TWITTER_URL)
        twitter_log_in(twitter_bot)
        twitter_bot.tweet_at_provider(test_result)


start_bot()
