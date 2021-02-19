from time import sleep

from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException,
                                        StaleElementReferenceException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

chrome_driver_path = "/Users/anhollow/Programming/Utilities/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)


def click_cookie():
    try:
        cookie.click()
    except:
        pass


def buy_item(id):
    if (item := get_element(id)):
        try:
            item.click()
        except:
            pass


def get_style(id):
    style = None
    if (item := get_element(id)):
        try:
            style = item.get_attribute("style")
        except:
            pass
    return style if style else ""


def get_class(id):
    class_ = None
    if (item := get_element(id)):
        try:
            class_ = item.get_attribute('class')
        except:
            pass
    return class_ if class_ else ""


def get_element(id):
    element = None
    try:
        element = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(
            expected_conditions.presence_of_element_located((By.ID, id))
        )
    except:
        pass
    return element if element else None


driver.get("http://orteil.dashnet.org/experiments/cookie/")

money = get_element("money")
things_to_buy = [
    "buyElder Pledge",
    "buyTime machine",
    "buyPortal",
    "buyAlchemy lab",
    "buyShipment",
    "buyMine",
    "buyFactory",
    "buyGrandma",
    "buyCursor",
]

cookie = get_element("cookie")
while cookie:

    for i in range(20):
        click_cookie()

    for _, id in enumerate(things_to_buy):
        if id == "buyElder Pledge":
            if "block" in get_style(id):
                buy_item(id)
        else:
            if "grayed" not in get_class(id):
                buy_item(id)