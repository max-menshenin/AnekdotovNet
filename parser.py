from bs4 import BeautifulSoup as BS
import requests as req

req = req.get('http://anekdotov.net/')
req.encoding = 'windows-1251'


soup = BS(req.text, 'lxml')
jokes = []

i = 0
for item in soup.find_all('div', {"class": 'anekdot'}):
    if i <= 5:
        i = i-1
    jokes.append(item.text)
