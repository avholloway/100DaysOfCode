import requests
from bs4 import BeautifulSoup as soup

# read local HTML file
with open("website2.html") as f:
    contents = [line.strip() for line in f.readlines()]
contents = "".join(contents)

# convert to soup
page = soup(contents, "html.parser")

# print page pretty
# print(page.prettify())

options = page.select("option")
for option in options:
    if option.get("selected") is not None:
        print(option.get("value"))