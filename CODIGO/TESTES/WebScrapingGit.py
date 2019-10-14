import requests
results = requests.get('https://www.revistabula.com/9153-lista-das-100-melhores-series-de-tv-de-todos-os-tempos-segundo-hollywood/')
from bs4 import BeautifulSoup
soup = BeautifulSoup(results.text, 'html.parser')
link_series = soup.find_all('div', class_='shortcode-featured-content')
for link in link_series:
    print(link.text)


