from application import app
from random import choice

@app.route('/get_a2', methods=['GET'])
def a1():
    publisher=choice(["DC", "Marvel"])
    return publisher