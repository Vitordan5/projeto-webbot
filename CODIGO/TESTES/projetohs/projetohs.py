from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def ola():
    return render_template("projetoo.html")


app.run()
