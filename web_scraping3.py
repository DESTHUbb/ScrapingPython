from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents

prices = {}

for tr in trs[:10]:
	name, price = tr.contents[2:4]
	fixed_name = name.p.string
	fixed_price = price.a.string

	prices[fixed_name] = fixed_price

print(prices)

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////7

# Improvement:

from bs4 import BeautifulSoup
import requests

def get_crypto_prices(url: str):
	result = requests.get(url).text
        doc = BeautifulSoup(result, "html.parser")
	
	    tbody = doc.tbody
   	    trs = tbody.contents

    prices = {}

    for tr in trs[:10]:
        name, price = tr.contents[2:4]
        fixed_name = name.p.string
        fixed_price = price.a.string
        prices[fixed_name] = fixed_price
	
    return prices
def print_prices(prices: dict):
    for name, price in prices.items():
	        print(f'{name}: {price}')

if __name__ == "__main__":

