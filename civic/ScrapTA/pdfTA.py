import requests
import re
from bs4 import BeautifulSoup


url = "https://www2.assemblee-nationale.fr/documents/liste/(type)/ta"
get = requests.get(url)
soup = BeautifulSoup(get.text, 'html.parser')

cake = soup.findAll('a', href=re.compile(
    '^https://www.assemblee-nationale.fr/dyn/old/15/ta/ta0'))


for i in cake:
    print(i['href'])
