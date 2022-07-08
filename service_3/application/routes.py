from application import app
from random import choice

@app.route('/get_a2', methods=['GET'])
def a2():
    publisher=choice(["DC", "Marvel"])
    return publisher