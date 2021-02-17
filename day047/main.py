import sys
import requests
from bs4 import BeautifulSoup as soup

product_url = "https://www.trollandtoad.com/pokemon/pokemon-sealed-product/base-set-1st-edition-booster-box-pokemon-/1109926"

response = requests.get(product_url)
response.raise_for_status()

page = soup(response.text, "html.parser")

stock = int(page.select_one(".productDescOption div").string.strip().replace("(", "").split(" ")[0])
price = float(page.select_one(".buyBox span").string.replace("$", "").replace(",", ""))

print("Base Set 1st Edition Booster Box (Pokemon)")
print(f"In Stock: {stock}; Price: ${price}")

if stock > 0 and price < 100:
    print("BUY! BUY! BUY! BUY! BUY! BUY! BUY! BUY!")