import requests
results = requests.get('https://www.rottentomatoes.com/browse/tv-list-2/')
from bs4 import BeautifulSoup
title = 'a'
notes = 'b'
year = 'c'
with open('rotten.csv', 'w') as s:
    s.write('SERIES;NOTAS\n')

def scrap ():
    soup = BeautifulSoup(results.text, 'html.parser')

    title = soup.findAll('div', class_='movie_info')
    title = BeautifulSoup(str(title), 'html.parser').findAll('h3')
    notes = soup.findAll('div', class_='movie_info')
    notes = BeautifulSoup(str(notes), 'html.parser').findAll('span',class_='tMeterScore')

    with open('rotten.csv', 'a') as s:
        i = 0
        for i in range(0, len(title)):
            s.write(title[i].text.replace(',', '').replace(';', '') + ';' + notes[i].text + ';' + '\n')
scrap()
print(title)