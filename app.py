from flask import Flask, render_template, request, redirect
import random
import string
import base64
import os
import firebase_admin   
from firebase_admin import credentials, firestore


cred = credentials.Certificate("notmytypeeee-firebase-adminsdk-crsss-c15772aedc.json")
firebase_admin.initialize_app(cred)

# from flask.typing import StatusCode

from twiliosend import send


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    res = str(''.join(random.choices(string.ascii_lowercase + string.digits, k = 15)))
    return render_template('index.html', code=res)

@app.route('/create-room/<code>,<email>')
def create(code,email):
    # lol = str(base64.b64decode(name))[2:-1]
    # lol = lol[0:int(len(lol)/2)]
    # print(lol)
    db = firestore.client()
    # email = "xyz@lol.com"
    data = {
        "members" : [
            {
                'email' : email,
                'accuracy' : 0,
                'wpm':0
            }
        ]
    }

    db.collection(u'rooms').document(code).set(data)
    return render_template('create.html', code=code, email = email)

@app.route('/join/<code>,<email>')
def join(code,email):
    
    return render_template('join.html', code=code, email=email)

@app.route('/joinn/<code>,<email>')
def joinn(code,email):
    db = firestore.client()

    data = [{
        'email' : email,
                'accuracy' : 0,
                'wpm':0
    }]

    db.collection(u'rooms').document(code).update({u'members': firestore.ArrayUnion(data)})

    return render_template('join.html', code=code)

@app.route('/create/<code>,<email>')
def createe(code, email):
    send(email)
    return redirect('/create/'+code)
    # return render_template('create.html', code=code)


@app.route('/play/<code>,<email>')
def play(code, email):
    return render_template('play.html', code=code, email=email)

@app.route('/results/<sim>,<wpm>')
def results(sim, wpm):
    return render_template('results.html', sim=round(float(sim)*100, 3), wpm=round(float(wpm), 3))

if __name__ == "__main__":
    app.run(debug=True)