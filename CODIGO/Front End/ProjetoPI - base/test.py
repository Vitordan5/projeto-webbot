from flask import Flask, render_template, jsonify
import requests
import json
from bs4 import BeautifulSoup


def scrapping():
    rotten = requests.get("https://www.rottentomatoes.com/browse/tv-list-2/")
    soup = BeautifulSoup(rotten.text, 'html.parser')
    data = soup.findAll('td', class_="middle_col")
    response = [item.get_text() for item in data]

    return response


app = Flask(__name__)


@app.route('/')
def index():

    data = scrapping()
    return render_template('index.html', data=data)

app.run(debug=True)