from bs4 import BeautifulSoup
import requests
from urls import urls
from fields import fields

open('output.txt', 'w').close()

def scrape(inp):
    results = []
    for i in inp:
        team = i.td.next_sibling
        if team.get_text() == "PHO":
            counter = 0
            for x in i:
                doc.find_all("td", {"style": "text-align: right;"})
                if ':' in x.get_text() and ',' in x.get_text() and len(x.get_text()) == 7 or x.get_text() == "--":
                    counter += 1
                    if counter == nrOfCheckpoints:
                        results.append([x.get_text()])
    return results

scrapeResults = []
for url in urls:
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    year = url[34:38]
    temp = []
    title = "Geen veld gevonden"
    nrOfCheckpoints = 4

    title = doc.find_all("h2")
    if len(title) > 0:
        title = title[0].get_text()
    else:
        title = "Veld onbekend"
    matches = []
    for i in fields:
        if i in title:
            matches.append(i)
    if len(matches) > 0:
        temp.append(max(matches, key=len))
    else:
        temp.append(title)
    temp.append(year)

    results = []
    results.append(scrape(doc.find_all("tr", {"class": "even"})))
    results.append(scrape(doc.find_all("tr", {"class": "odd"})))

    for j in results:
        temp.append(j)

    scrapeResults.append(temp)
    for fst in scrapeResults:
        for idx, val in enumerate(fst):
            if val == []:
                del fst[idx]

for i in scrapeResults:
    with open("output.txt", "a") as f:
        f.write(str(i))
        f.write("\n")
    
