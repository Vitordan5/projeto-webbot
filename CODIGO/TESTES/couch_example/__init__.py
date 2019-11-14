from Model.Series import Series
import requests
import json
from bs4 import BeautifulSoup

results = requests.get(
    'https://www.imdb.com/search/title/?num_votes=100000,&sort=user_rating,desc&title_type=tv_series&')
results1 = requests.get(
    'https://www.imdb.com/search/title/?title_type=tv_series&num_votes=100000,&sort=user_rating,desc&start=51&ref_=adv_prv')
results2 = requests.get(
    'https://www.imdb.com/search/title/?title_type=tv_series&num_votes=100000,&sort=user_rating,desc&start=101&ref_=adv_nxt')

soup = BeautifulSoup(results.text, 'html.parser')
title = soup.findAll('h3', class_='lister-item-header')
title = BeautifulSoup(str(title), 'html.parser').findAll('a')
notes = soup.findAll('div', class_='inline-block ratings-imdb-rating')
notes = BeautifulSoup(str(notes), 'html.parser').findAll('strong')
year = soup.findAll('h3', class_='lister-item-header')
year = BeautifulSoup(str(year), 'html.parser').findAll('span', class_='lister-item-year text-muted unbold')
genre = soup.findAll('span', class_= 'genre')

auth = ('couchdb', 'couchdb')

counter = 0
for t in title:
    s = Series(t.text.replace("'", ""), genre[counter].text.replace("\n", "").strip(), int(year[counter].text[1:5]), float(notes[counter].text))
    print(s.__dict__)
    r = requests.post('http://localhost:5984/series', json=json.loads(str(s.__dict__).replace("'", "\"")), auth=auth)
    print(str(r.text))

soup1 = BeautifulSoup(results1.text, 'html.parser')
title1 = soup1.findAll('h3', class_='lister-item-header')
title1 = BeautifulSoup(str(title1), 'html.parser').findAll('a')
notes1 = soup1.findAll('div', class_='inline-block ratings-imdb-rating')
notes1 = BeautifulSoup(str(notes1), 'html.parser').findAll('strong')
year1 = soup1.findAll('h3', class_='lister-item-header')
year1 = BeautifulSoup(str(year1), 'html.parser').findAll('span', class_='lister-item-year text-muted unbold')
genre1 = soup.findAll('span', class_= 'genre')

counter = 0
for t in title1:
    s = Series(t.text.replace("'", ""), genre1[counter].text.replace("\n", "").strip(), int(year1[counter].text[1:5]), float(notes1[counter].text))
    r = requests.post('http://localhost:5984/series', json=json.loads(str(s.__dict__).replace("'", "\"")), auth=auth)
    print(str(r.text))

soup2 = BeautifulSoup(results2.text, 'html.parser')
title2 = soup2.findAll('h3', class_='lister-item-header')
title2 = BeautifulSoup(str(title2), 'html.parser').findAll('a')
notes2 = soup2.findAll('div', class_='inline-block ratings-imdb-rating')
notes2 = BeautifulSoup(str(notes2), 'html.parser').findAll('strong')
year2 = soup2.findAll('h3', class_='lister-item-header')
year2 = BeautifulSoup(str(year2), 'html.parser').findAll('span', class_='lister-item-year text-muted unbold')
genre2 = soup.findAll('span', class_= 'genre')

counter = 0
for t in title2:
    s = Series(t.text.replace("'", ""), genre2[counter].text.replace("\n", "").strip(), int(year2[counter].text[1:5]), float(notes2[counter].text))
    r = requests.post('http://localhost:5984/series', json=json.loads(str(s.__dict__).replace("'", "\"")), auth=auth)
    print(str(r.text))