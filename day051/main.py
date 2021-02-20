import os
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException,
                                        StaleElementReferenceException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class InternetSpeedBot():
    def __init__(self):
        self.chrome_driver_path = "/Users/anhollow/Programming/Utilities/chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        self.download_speed = 0
        self.download_unit = ""
        self.upload_speed = 0
        self.upload_unit = ""
        self.down = ""
        self.up = ""

        self.TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
        self.TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

    def run(self):
        self.get_internet_speed()
        self.tweet_it()
        self.shutdown()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        start = self.driver.find_element_by_css_selector("a.js-start-test")
        start.click()

        sleep(60)

        self.download_speed = float(self.driver.find_element_by_css_selector("div.result-item-download div.result-data span.result-data-value").text)
        self.download_unit = self.driver.find_element_by_css_selector("div.result-item-download div.result-label span.result-data-unit").text
        self.down = f"{self.download_speed}{self.download_unit}"

        self.upload_speed = float(self.driver.find_element_by_css_selector("div.result-item-upload div.result-data span.result-data-value").text)
        self.upload_unit = self.driver.find_element_by_css_selector("div.result-item-upload div.result-label span.result-data-unit").text
        self.up = f"{self.upload_speed}{self.upload_unit}"

        print(self.down, self.up)

    def tweet_it(self):
        self.driver.get("https://twitter.com/login")

        sleep(5)

        element = self.driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(6) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-19h5ruw.r-1udh08x.r-1inuy60.r-ou255f.r-m611by > div > input")
        element.send_keys(self.TWITTER_EMAIL)
        element = self.driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(7) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-19h5ruw.r-1udh08x.r-1inuy60.r-ou255f.r-m611by > div > input")
        element.send_keys(self.TWITTER_PASSWORD)
        element.send_keys(Keys.RETURN)

        sleep(30)

        element = self.driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-atwnbb > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-glunga.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div > div > div > div > div.css-901oao.r-18jsvk2.r-6koalj.r-16y2uox.r-1qd0xha.r-1b6yd1w.r-16dba41.r-ad9z0x.r-bcqeeo.r-qvutc0 > div > div > div > div > div > div > div > div")
        element.send_keys(f"[Automated Tweet] Download: {self.down} / Upload: {self.up}")
        element = self.driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-atwnbb > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-glunga.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(4) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-1n0xq6e.r-1vuscfd.r-1dhvaqw.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span")
        element.click()

    def shutdown(self):
        self.driver.quit()

bot = InternetSpeedBot()
bot.run()