import requests
from bs4 import BeautifulSoup

with open("https://www.gov.uk/search/news-and-communications","r") as file:
    soup = BeautifulSoup(file.read(), 'html.parser')

