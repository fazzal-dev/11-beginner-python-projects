import requests
from bs4 import BeautifulSoup

url = 'https://fazzal-dev.github.io/portfolio/'
req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')
title = soup.find_all('a', {'class': 'logo'})

gettitle = title[0].getText()


print(gettitle)
