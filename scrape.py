from bs4 import BeautifulSoup
import requests

from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

url = "https://regatta.time-team.nl/nkir/2021/results/r887e9218-413b-458d-b96b-11443b7617fb.php#19ea174d-de19-460f-9537-8ffcbf75a566"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

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
