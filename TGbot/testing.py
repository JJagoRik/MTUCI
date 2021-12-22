import requests
from bs4 import BeautifulSoup


ssilka = requests.get('https://www.hltv.org/stats/players?startDate=2020-11-10&endDate=2021-11-10&rankingFilter=Top20')
HLTV = BeautifulSoup(ssilka.text, 'lxml')
names = HLTV.find_all('td', class_="playerCol")
stats = HLTV.find_all('td', class_='ratingCol')
for i in names:
    print(i.text)
print('---------------------------------------')
for i in stats:
    print(i.text)