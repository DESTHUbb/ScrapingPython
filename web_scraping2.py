from bs4 import BeautifulSoup
import re

with open("index.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("input", type="text")
for tag in tags:
	tag['placeholder'] = "I changed you!"

with open("changed.html", "w") as file:
	file.write(str(doc))

	
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Improvement:

from bs4 import BeautifulSoup
	with open("index.html", "r") as f:
		    html = f.read()

soup = BeautifulSoup(html, "html.parser")
for tag in soup.find_all("input", type="text"):

