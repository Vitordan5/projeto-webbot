import requests
from bs4 import BeautifulSoup

rotten = requests.get('https://www.rottentomatoes.com/browse/tv-list-2/')
soup = BeautifulSoup(rotten.text, 'html.parser')
data = soup.findAll('div', class_="movie_info")
print(data)