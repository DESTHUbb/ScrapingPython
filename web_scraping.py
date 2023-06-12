from bs4 import BeautifulSoup
import requests

# HTML From File
with open("index.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("p")[0]

print(tags.find_all("b"))

# HTML From Website
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Improvement:

from bs4 import BeautifulSoup
import requests

def read_local_html(file_path):
    with open(file_path, "r") as f:
	 content = f.read()
    return content

def get_html_from_url(url):
	result = requests.get(url)
    return result.text

def extract_bold_tags(html_content):
    doc = BeautifulSoup(html_content, "html.parser")
 tags = doc.find_all("p")[0]
    return tags.find_all("b")

def extract_newegg_product_price(html_content):
    doc = BeautifulSoup(html_content, "html.parser")
prices = doc.find_all(text="$")
    parent = prices[0].parent
 strong = parent.find("strong")
    return strong.string

local_html_content = read_local_html("index.html")
bold_tags = extract_bold_tags(local_html_content)
print(bold_tags)

url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

