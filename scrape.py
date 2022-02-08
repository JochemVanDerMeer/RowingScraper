from bs4 import BeautifulSoup
import requests

from io import StringIO
from html.parser import HTMLParser

#relevant fields for Phocas
fields = ["HE", "DE", "LHE", "LDE", "HSB", "DSB", "LHSB", "LDSB", "HG", "DG", "LHG", "LDG", "HEj8", "DEj8", "LHEj8", "LDEj4", "HEj4", "DEj4", "LHEj4", "HCl8", "DCl8", "HEj 8", "DEj 8", "LHEj 8", "LDEj 4", "HEj 4", "DEj 4", "LHEj 4", "HCl 8", "DCl 8" ]

url = "https://regatta.time-team.nl/nkir/2021/results/r887e9218-413b-458d-b96b-11443b7617fb.php#19ea174d-de19-460f-9537-8ffcbf75a566"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

title = "Geen titel gevonden"
title = doc.find_all("h2")
title = title[0].get_text()
print(title)
matches = []
for i in fields:
    if i in title:
        matches.append(i)
print(max(matches, key=len))


results = []
for even in doc.find_all("tr", {"class": "even"}):
    team = even.td.next_sibling
    if team.get_text() == "PHO":
        counter = 0
        for x in even:
            doc.find_all("td", {"style": "text-align: right;"})
            if ':' in x.get_text() and ',' in x.get_text() and len(x.get_text()) == 7:
                counter += 1
                if counter == 4:
                    results.append([x.get_text()])    

for odd in doc.find_all("tr", {"class": "odd"}):
    team = odd.td.next_sibling
    if team.get_text() == "PHO":
        counter = 0
        for x in odd:
            doc.find_all("td", {"style": "text-align: right;"})
            if ':' in x.get_text() and ',' in x.get_text() and len(x.get_text()) == 7:
                counter += 1
                if counter == 4:
                    results.append([x.get_text()])            


for j in results:
    print(j)
    print()
    print()
