import requests
from bs4 import BeautifulSoup
import re


url = "https://www2.assemblee-nationale.fr/documents/liste/(type)/ta"
get = requests.get(url)
soup = BeautifulSoup(get.text, 'html.parser')

descTA = soup.findAll(string=re.compile("loi"))

fi = descTA[3]

print(fi)

## no_parsed = soup.find_all('ul', class_="liens-liste")
# print(descTA)
