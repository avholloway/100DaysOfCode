from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

chrome_driver_path = "/Users/anhollow/Programming/Utilities/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

money = driver.find_element_by_id("money")

cookie = driver.find_element_by_id("cookie")

item_ids = [
    "buyTime machine",
    "buyPortal",
    "buyAlchemy lab",
    "buyShipment",
    "buyMine",
    "buyFactory",
    "buyGrandma",
    "buyCursor",
]

while True:

    for i in range(10):
        cookie.click()

    for _, item_id in enumerate(item_ids):
        item = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.ID, item_id)))
        if item.get_attribute('class') != "grayed":
            print(f"\tbuying {item_id}!")
            item.click()
            break

driver.quit()