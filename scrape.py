from bs4 import BeautifulSoup
import requests

#relevant fields for Phocas
fields = ["HE", "DE", "LHE", "LDE", "HSB", "DSB", "LHSB", "LDSB", "HG", "DG", "LHG", "LDG", "HEj8", "DEj8", "LHEj8", "LDEj4", "HEj4", "DEj4", "LHEj4", "HCl8", "DCl8", "HEj 8", "DEj 8", "LHEj 8", "LDEj 4", "HEj 4", "DEj 4", "LHEj 4", "HCl 8", "DCl 8" ]

urls = ["https://regatta.time-team.nl/nkir/2021/results/e5b29ee9c-7fc9-492e-b0e1-a6512a26f0d8.php",
"https://regatta.time-team.nl/nkir/2021/results/e6d4a42e6-ca26-43d4-b618-63a1801360b0.php",
"https://regatta.time-team.nl/nkir/2021/results/e680cd704-9ba9-48c0-8728-a4cfb2b36cc9.php", 
"https://regatta.time-team.nl/nkir/2021/results/r21f8743c-08db-408f-bf14-10234043df99.php#912c48e3-97e1-45b0-aed5-93c333639188",
"https://regatta.time-team.nl/nkir/2021/results/r1023ba23-2a41-475f-b925-c1c045b235d8.php#88bc2057-59e5-4138-b36f-b17456b1778f"]

def scrape(inp):
    results = []
    for i in inp:
        team = i.td.next_sibling
        if team.get_text() == "PHO":
            counter = 0
            for x in i:
                doc.find_all("td", {"style": "text-align: right;"})
                if ':' in x.get_text() and ',' in x.get_text() and len(x.get_text()) == 7:
                    counter += 1
                    if counter == nrOfCheckpoints:
                        results.append([x.get_text()])
    return results

scrapeResults = []
for url in urls:
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    temp = []
    title = "Geen veld gevonden"
    nrOfCheckpoints = 4

    title = doc.find_all("h2")
    title = title[0].get_text()
    matches = []
    for i in fields:
        if i in title:
            matches.append(i)
    temp.append(max(matches, key=len))

    results = []
    results.append(scrape(doc.find_all("tr", {"class": "even"})))
    results.append(scrape(doc.find_all("tr", {"class": "odd"})))

    for j in results:
        temp.append(j)

    scrapeResults.append(temp)
    for fst in  scrapeResults:
        for idx,val in enumerate(fst):
            if val == []:
                del fst[idx]


print(scrapeResults)