from bs4 import BeautifulSoup
import requests
with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')
requests=requests.get('https://www.rottentomatoes.com/top-tv/')
print(requests.text)

#match = soup.find('div', class_='col col-left col-full-xs')
#print(match)

#titulo = match.h2.text
#print(titulo)

#article = soup.find('div', class_='article')
#print(article)

#headline = article.h2.a.text



