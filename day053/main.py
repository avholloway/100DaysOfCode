import os
import re
import requests
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup as soup

chrome_driver_path = "/Users/anhollow/Programming/Utilities/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
form_address = "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(1) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input"
form_cost = "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(2) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input"
form_url = "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(3) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input"
form_submit = "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div"

GOOGLE_FORM = os.getenv("GOOGLE_FORM")
ZILLOW_URL = os.getenv("ZILLOW_URL")

headers = {
    "Accept-Language": "en-us",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
}

response = requests.get(ZILLOW_URL, headers=headers)
response.raise_for_status()

page = soup(response.text, "html.parser")

# print(page.prettify())

listings = page.select("div#grid-search-results ul li")

for listing in listings:
    try:
        url = listing.select_one("a.list-card-link")['href'].strip()
    except:
        continue
    url = f"https://www.zillow.com{url}" if "zillow.com" not in url else url
    try:
        address = listing.select_one("address").text.strip()
    except:
        continue
    try:
        cost = listing.select_one("div.list-card-price").text.strip()
    except:
        continue
    try:
        cost = re.match("\$[\d,.]+", cost).group()
    except:
        continue

    driver.get(GOOGLE_FORM)

    sleep(2)

    print(f"{cost} - {address} \n{url} \n\n")

    address_field = driver.find_element_by_css_selector(form_address)
    address_field.send_keys(address)

    cost_field = driver.find_element_by_css_selector(form_cost)
    cost_field.send_keys(cost)

    url_field = driver.find_element_by_css_selector(form_url)
    url_field.send_keys(url)

    submit_button = driver.find_element_by_css_selector(form_submit)
    submit_button.click()

    sleep(2)