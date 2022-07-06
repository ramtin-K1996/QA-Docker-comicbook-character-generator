from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    power = requests.get('http://service_2:5000/get_a1').text
    publisher = requests.get('http://service_3:5000/get_a2').text
    superhero = requests.post('http://service_4:5000/character', json=dict(power=power, publisher=publisher))

    return render_template('home.html', power=power, publisher=publisher, superhero =superhero.text)