import requests
import json
from enum import Enum


class TvBrowsingCategory(Enum):
    new_tv_tonight = "tv-list-1"
    most_popular = "tv-list-2"
    certified_fresh = "tv-list-3"

class RottenTomatoesClient:
    BASE_URL = "https://www.rottentomatoes.com/api/private"
    BASE_V1_URL = "{base_url}/v1.0".format(base_url=BASE_URL)
    BASE_V2_URL = "{base_url}/v2.0".format(base_url=BASE_URL)
    MOVIE_DETAILS_URL = "{base_url}/movies".format(base_url=BASE_V1_URL)
    SEARCH_URL = "{base_url}/search".format(base_url=BASE_V2_URL)
    BROWSE_URL = "{base_url}/browse".format(base_url=BASE_V2_URL)

    def __init__(self):
        pass

    def browse_tv_shows(category=TvBrowsingCategory.most_popular):
        r = requests.get(url=RottenTomatoesClient.BROWSE_URL, params={"type": category.value})

        r.raise_for_status()

        return r.json()


with open('popular.csv', 'a') as s:
    s.write('SERIES;NOTAS\n')
result = RottenTomatoesClient.browse_tv_shows()
data = json.dumps(result, indent=2)
for x in result["results"]:
    titulo = str(x['title'])
    nota = str(x['tomatoScore'])
    linha = titulo + ';' + nota + '\n'
    with open('popular.csv', 'a') as s:
        s.write(linha)

results = requests.get(
    'https://www.imdb.com/search/title/?num_votes=100000,&sort=user_rating,desc&title_type=tv_series&')
from bs4 import BeautifulSoup

title = 'a'
notes = 'b'
year = 'c'
with open('listadeseries.csv', 'w') as s:
    s.write('SERIES;NOTAS;ANO DE LANÇAMENTO\n')


def scrap():
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
            s.write(
                title[i].text.replace(',', '').replace(';', '') + ';' + notes[i].text + ';' + year[i].text[0:5].replace(
                    '(', '').replace(')', '') + '\n')


scrap()

results = requests.get(
    'https://www.imdb.com/search/title/?title_type=tv_series&num_votes=100000,&sort=user_rating,desc&start=51&ref_=adv_nxt')
scrap()

results = requests.get(
    'https://www.imdb.com/search/title/?title_type=tv_series&num_votes=100000,&sort=user_rating,desc&start=101&ref_=adv_nxt')
scrap()
