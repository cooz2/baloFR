import requests
from bs4 import BeautifulSoup
import re


url = "https://www2.assemblee-nationale.fr/documents/liste/(type)/ta"
get = requests.get(url)
soup = BeautifulSoup(get.text, 'html.parser')

## nota = soup.findAll("h3")

no_ta = soup.findAll(string=re.compile("adopté"))

ta_no = no_ta[1]

print(ta_no)
