import requests
results = requests.get('https://www.imdb.com/search/title/?num_votes=100000,&sort=user_rating,desc&title_type=tv_series&')
from bs4 import BeautifulSoup
title = 'a'
notes = 'b'
year = 'c'
with open('listadeseries.csv', 'w') as s:
    s.write('SERIES;NOTAS;ANO DE LANÇAMENTO\n')

def scrap ():
    soup = BeautifulSoup(results.text, 'html.parser')

    title = soup.findAll('h3', class_='lister-item-header')
    title = BeautifulSoup(str(title), 'html.parser').findAll('a')
    notes = soup.findAll('div', class_='inline-block ratings-imdb-rating')
    notes = BeautifulSoup(str(notes), 'html.parser').findAll('strong')
    year = soup.findAll('h3', class_='lister-item-header')
    year = BeautifulSoup(str(year), 'html.parser').findAll('span', class_='lister-item-year text-muted unbold')

    with open('listadeseries.csv', 'a') as s:
        i = 0
        for i in range(0, len(title)):
            s.write(title[i].text.replace(',', '').replace(';', '') + ';' + notes[i].text + ';' + year[i].text[0:5].replace('(', '').replace(')', '')+'\n')
scrap()

results = requests.get('https://www.imdb.com/search/title/?title_type=tv_series&num_votes=100000,&sort=user_rating,desc&start=51&ref_=adv_nxt')
scrap()

results = requests.get('https://www.imdb.com/search/title/?title_type=tv_series&num_votes=100000,&sort=user_rating,desc&start=101&ref_=adv_nxt')
scrap()

