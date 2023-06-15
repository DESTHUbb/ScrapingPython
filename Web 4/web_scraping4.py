from bs4 import BeautifulSoup
import requests
import re

search_term = input("What product do you want to search for? ")

url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

items_found = {}

for page in range(1, pages + 1):
	url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={page}"
	page = requests.get(url).text
	doc = BeautifulSoup(page, "html.parser")

	div = doc.find(
		class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
	items = div.find_all(text=re.compile(search_term))

	for item in items:
		parent = item.parent
		if parent.name != "a":
			continue

		link = parent['href']
		next_parent = item.find_parent(class_="item-container")
		try:
			price = next_parent.find(class_="price-current").find("strong").string
			items_found[item] = {"price": int(price.replace(",", "")), "link": link}
		except:
			pass

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

for item in sorted_items:
	print(item[0])
	print(f"${item[1]['price']}")
	print(item[1]['link'])
	print("-------------------------------")

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////7

# Improvements:

import requests
from bs4 import BeautifulSoup
import re


def get_num_pages(url):
       """Get the total number of search pages"""
page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    page_text = soup.find(class_="list-tool-pagination-text").strong
    return int(str(page_text).split("/")[-2].split(">")[-1][:-1])

def get_items(url, search_term):
	"""Gets the products of a page"""
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    div = soup.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(text=re.compile(search_term))
    items_found = {}
    for item in items:
	    parent = item.parent
        if parent.name != "a":
		continue
        link = parent['href']
 next_parent = item.find_parent(class_="item-container")
        try:
	    price = next_parent.find(class_="price-current").find("strong").string
		            items_found[item] = {"price": int(price.replace(",", "")), "link": link}
 except:
            pass
    return items_found

def search_items(search_term):
	"""Performs the search for products and shows them ordered by price"""
    base_url = "https://www.newegg.ca/p/pl"
    params = {"d": search_term, "N": 4131}
url = f"{base_url}?{'&'.join([f'{k}={v}' for k,v in params.items()])}"
    pages = get_num_pages(url)
    items_found = {}
  for page in range(1, pages + 1):
        url = f"{base_url}?{'&'.join([f'{k}={v}' for k,v in params.items()])}&page={page}"
        items_found.update(get_items(url, search_term))
    sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])
    for item in sorted_items:
	print(item[0])
        print(f"${item[1]['price']}")
  	print(item[1]['link'])
        print("-------------------------------")

if __name__ == '__main__':








