import requests
from bs4 import BeautifulSoup
import pandas as pd
page1 = requests.get('http://www.adorocinema.com/series-tv/melhores/')
soup = BeautifulSoup(page1.text, 'html.parser')

page2 = requests.get('http://www.adorocinema.com/series-tv/melhores/?page=2')
soup = BeautifulSoup(page2.text, 'html.parser')

page3 = requests.get('http://www.adorocinema.com/series-tv/melhores/?page=3')
soup = BeautifulSoup(page3.text, 'html.parser')

page4 = requests.get('http://www.adorocinema.com/series-tv/melhores/?page=4')
soup = BeautifulSoup(page4.text, 'html.parser')

title = soup.findAll('a', class_='no_underline')
year = soup.findAll('div', class_='oflow_a')
note = soup.findAll('span', class_='note')

titles = []
for name in title :
    titles.append(name.text.strip())
#print(titles)
dates =[]
for date in year :
    dates.append(date.text.strip())
#print(dates)
notes = []
for num in note:
    notes.append(num.text.strip())
print(notes)

