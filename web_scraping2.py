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
    tag["placeholder"] = "I changed you!"

with open("changed.html", "w") as file:
    file.write(str(soup))

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Improvements and updates made:
1: # Reading the HTML file: In the original version, the open method was used to read the HTML file and then passed to the BeautifulSoup constructor. 
   # In the improved version, open is used to read the entire contents of the file in a single text string, and this string is passed to the BeautifulSoup constructor.



	
