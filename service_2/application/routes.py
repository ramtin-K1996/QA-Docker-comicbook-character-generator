from application import app
from random import choice

@app.route('/get_a1', methods=['GET'])
def a1():
    power=choice(["strength", "intelligence"])
    return power