from bs4 import BeautifulSoup as BS
import requests as r
r = r.get('http://anekdotov.net/')
r.encoding = 'windows-1251'

soup = BS(r.text, 'lxml')
i = 0
for item in soup.find_all('div', {"class": 'anekdot'}):
    if i <= 5:
        print(item.text, end='\n')
        i = i-1
# mydivs = soup.find_all("div", {"class": "stylelistrow"})