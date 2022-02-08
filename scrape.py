from bs4 import BeautifulSoup
import requests

# relevant fields for Phocas
fields = ["HE", "DE", "LHE", "LDE", "HSB", "DSB", "LHSB", "LDSB", "HG", "DG", "LHG", "LDG", "HVA", "HEj8", "DEj8", "LHEj8", "LDEj4",
          "HEj4", "DEj4", "LHEj4", "HCl8", "DCl8", "HEj 8", "DEj 8", "LHEj 8", "LDEj 4", "HEj 4", "DEj 4", "LHEj 4", "HCl 8", "DCl 8"]

urls = ["https://regatta.time-team.nl/nkir/2021/results/e1db283aa-e117-4a97-84a0-5b8c6e3b9fdb.php",
        "https://regatta.time-team.nl/nkir/2021/results/ec28a21b0-6afe-41b9-a6ec-690ec281f0ea.php",
        "https://regatta.time-team.nl/nkir/2021/results/e9f15a00b-6dce-4a76-a766-e9b0471ffe49.php",
        "https://regatta.time-team.nl/nkir/2021/results/e082fbfa9-ec66-496a-a9bf-31bdf7b860d3.php",
        "https://regatta.time-team.nl/nkir/2021/results/e4ecf8215-d90b-4fb3-aba6-2fe082581ea5.php",
        "https://regatta.time-team.nl/nkir/2021/results/eea7656c9-ce8f-4d45-8097-cc17d194e3a5.php",
        "https://regatta.time-team.nl/nkir/2021/results/e33e762f8-03b0-4b98-a132-8f6ac458726e.php",
        "https://regatta.time-team.nl/nkir/2021/results/e6d4a42e6-ca26-43d4-b618-63a1801360b0.php",
        "https://regatta.time-team.nl/nkir/2021/results/e680cd704-9ba9-48c0-8728-a4cfb2b36cc9.php",
        "https://regatta.time-team.nl/nkir/2021/results/efc7a0b71-f006-4f43-8231-2cb4f8d1ad4e.php",
        "https://regatta.time-team.nl/nkir/2021/results/e5b29ee9c-7fc9-492e-b0e1-a6512a26f0d8.php",
        "https://regatta.time-team.nl/nkir/2021/results/ead3520ad-4657-46e5-ae93-d03f138e33f4.php",
        "https://regatta.time-team.nl/nkir/2021/results/ef044e6f8-eba3-4a53-b005-3b901fe85543.php"]

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

    year = url[34:38]
    temp = []
    title = "Geen veld gevonden"
    nrOfCheckpoints = 4

    title = doc.find_all("h2")
    title = title[0].get_text()
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
    print(i)
    print()
