import requests

results = requests.get(
    'https://www.imdb.com/search/title/?num_votes=100000,&sort=user_rating,desc&title_type=tv_series&')
results1 = requests.get(
    'https://www.imdb.com/search/title/?title_type=tv_series&num_votes=100000,&sort=user_rating,desc&start=51&ref_=adv_prv')
results2 = requests.get(
    'https://www.imdb.com/search/title/?title_type=tv_series&num_votes=100000,&sort=user_rating,desc&start=101&ref_=adv_nxt')

from bs4 import BeautifulSoup

soup = BeautifulSoup(results.text, 'html.parser')
title = soup.findAll('h3', class_='lister-item-header')
title = BeautifulSoup(str(title), 'html.parser').findAll('a')
notes = soup.findAll('div', class_='inline-block ratings-imdb-rating')
notes = BeautifulSoup(str(notes), 'html.parser').findAll('strong')
year = soup.findAll('h3', class_='lister-item-header')
year = BeautifulSoup(str(year), 'html.parser').findAll('span', class_='lister-item-year text-muted unbold')
soup = BeautifulSoup(results.text, 'html.parser')

soup1 = BeautifulSoup(results1.text, 'html.parser')
title1 = soup1.findAll('h3', class_='lister-item-header')
title1 = BeautifulSoup(str(title1), 'html.parser').findAll('a')
notes1 = soup1.findAll('div', class_='inline-block ratings-imdb-rating')
notes1 = BeautifulSoup(str(notes1), 'html.parser').findAll('strong')
year1 = soup1.findAll('h3', class_='lister-item-header')
year1 = BeautifulSoup(str(year1), 'html.parser').findAll('span', class_='lister-item-year text-muted unbold')

soup2 = BeautifulSoup(results2.text, 'html.parser')
title2 = soup2.findAll('h3', class_='lister-item-header')
title2 = BeautifulSoup(str(title2), 'html.parser').findAll('a')
notes2 = soup2.findAll('div', class_='inline-block ratings-imdb-rating')
notes2 = BeautifulSoup(str(notes2), 'html.parser').findAll('strong')
year2 = soup2.findAll('h3', class_='lister-item-header')
year2 = BeautifulSoup(str(year2), 'html.parser').findAll('span', class_='lister-item-year text-muted unbold')

with open('listadeseries.csv', 'w') as s:
    s.write('SERIES;NOTAS;ANO DE LANÇAMENTO\n')
    i = 0
    for i in range(0, len(title)):
        s.write(title[i].text.replace(',', '').replace(';', '') + ';' + notes[i].text + ';' + year[i].text[1:5] + '\n')
    for i in range(0, len(title1)):
        s.write(title1[i].text.replace(',', '').replace(';', '') + ';' + notes1[i].text + ';' + year1[i].text[1:5] + '\n')
    for i in range(0, len(title2)):
        s.write(title2[i].text.replace(',', '').replace(';', '') + ';' + notes2[i].text + ';' + year2[i].text[1:5] + '\n')
