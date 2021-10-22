from os import sep
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

url = "https://www2.assemblee-nationale.fr/documents/liste/(type)/ta"
get = requests.get(url)
soup = BeautifulSoup(get.text, 'html.parser')

# for item in soup.find_all(attrs={"data-id": True}):
# print(item['data-id'])
##omc = item['data-id']
# Retourne les codes des textes de loi en objet metier cartesian

omc = soup.findAll(class_="liens-liste")
ta = [li for ul in omc for li in ul.findAll('li')]
last_Ta = ta[0]

print(last_Ta.h3.text)
# print(last_Ta.span.text)
print(last_Ta.p.text)

new_Ta = []

for i in last_Ta:
    new_i = {}
    new_i['Texte'] = last_Ta.h3.text
    #new_i['Date'] = last_Ta.span.text
    new_i['Sujet'] = last_Ta.p.text
    new_Ta.append(new_i)

print(new_Ta[0])

df = pd.DataFrame(new_Ta, columns=['Texte', 'Sujet'])
print(df.head(1).to_csv(r'civic\parseCSV\lastOMC.csv', index=False, encoding='utf-8'))
