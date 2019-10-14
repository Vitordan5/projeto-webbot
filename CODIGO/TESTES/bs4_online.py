import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.rottentomatoes.com/top-tv/')
soup = BeautifulSoup(page.text,'html.parser')
base2 = soup.find(class_='col col-left col-full-xs')
print(base2.text)