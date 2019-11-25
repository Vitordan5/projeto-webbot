from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin
from Model.Series import Series
import requests
import json
from bs4 import BeautifulSoup


def scrapping():
    rotten = requests.get("https://www.rottentomatoes.com/browse/tv-list-2/")
    soup = BeautifulSoup(rotten.text, 'html.parser')
    data = soup.findAll('td', class_="middle_col")
    response = [item.get_text() for item in data]

    return response

def findAllSeries():
    auth = ("couchdb", "couchdb")
    j = {
       "selector": {
          "_id": {
             "$gt": None
          }
       }
    }
    r = requests.post("http://localhost:5984/series/_find", json=json.loads(str(j).replace("None", "null").replace("'", "\"")), auth=auth)
    j2 = json.loads(r.text)
    response = list()
    return j2["docs"]

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
cors = CORS(app)

@app.route('/')
def index():
    data = findAllSeries()
    return render_template('index.html', data=data)

@app.route('/search/title/<title>')
@cross_origin()
def searchTitle(title):
    auth = ("couchdb", "couchdb")
    j = {
        "selector": {
            "title_s": {
                "$regex": title.upper()
            }
        }
    }
    r = requests.post("http://localhost:5984/series/_find",
                      json=json.loads(str(j).replace("'", "\"")), auth=auth)
    j2 = json.loads(r.text)
    series = list()
    for j in j2['docs']:
        series.append(json.loads(json.dumps(Series(j['title'], j['genre'], j['year'], j['notes']).__dict__)))
    print(r.status_code)
    return jsonify(series)

@app.route('/search/genre/<genre>')
def searchGenre(genre):
    auth = ("couchdb", "couchdb")
    j = {
        "selector": {
            "genre_s": {
                "$regex": genre.upper()
            }
        }
    }
    r = requests.post("http://localhost:5984/series/_find",
                      json=json.loads(str(j).replace("'", "\"")), auth=auth)
    j2 = json.loads(r.text)
    print(r.status_code)
    return jsonify(j2)

@app.route('/search/year/<ano>')
def searchYear(ano):
    auth = ("couchdb", "couchdb")
    j = {
        "selector": {
            "year": {
                "$gte": int(ano)
            }
        }
    }
    r = requests.post("http://localhost:5984/series/_find",
                      json=json.loads(str(j).replace("'", "\"")), auth=auth)
    j2 = json.loads(r.text)
    print(r.status_code)
    return jsonify(j2)

app.run(debug=True)
