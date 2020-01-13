from bs4 import BeautifulSoup as BS
import requests as r
r = r.get('http://anekdotov.net/')
r.encoding= 'windows-1251'

soup = BS(r.text, 'lxml')
i = 0
for item in soup.find_all('div'):
    if i<=5 :
        print(item.text)
        i = i-1