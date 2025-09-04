import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, 'html.parser')

titres = soup.find_all("a", class_="gem-c-subscription-links__item")
titre_textes = []
for titre in titres:
    titre_textes.append(titre.text)

descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
description_textes = []
for description in descriptions:
    description_textes.append(description.text)

en_tete = ['titre', 'description']
with open('data.csv','w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(en_tete)
    for titre, description in zip(titre_textes, description_textes):
        writer.writerow([titre, description])
