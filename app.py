from flask import Flask, render_template, request, redirect
import random
import string
import base64
import os

from flask.typing import StatusCode
from twiliosend import send


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    res = str(''.join(random.choices(string.ascii_lowercase + string.digits, k = 15)))
    return render_template('index.html', code=res)

@app.route('/create/<code>')
def create(code):
    # lol = str(base64.b64decode(name))[2:-1]
    # lol = lol[0:int(len(lol)/2)]
    # print(lol)
    return render_template('create.html', code=code)

@app.route('/create/<code>,<email>')
def createe(code, email):
    send(email)
    return redirect('/create/'+code)
    # return render_template('create.html', code=code)


@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/results/<sim>,<wpm>')
def results(sim, wpm):
    return render_template('results.html', sim=round(float(sim)*100, 3), wpm=round(float(wpm), 3))

if __name__ == "__main__":
    app.run(debug=True)