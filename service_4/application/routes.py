from application import app
from random import choice
from flask import request

@app.route('/character',methods=['POST'])
def character():
    data_sent = request.get_json()
    superhero=""
    #different chances for superhero depending on 'power level' 

    if data_sent['power'] == "intelligence" and data_sent['publisher'] == "Marvel":
        superhero= choice(["IRONMAN","mr fantastic","mr fantastic","mr fantastic"])

    elif data_sent['power'] == "strength" and data_sent['publisher'] == "Marvel":
        superhero= choice(["HULK","Spider-man","Spider-man","Spider-man","Spider-man"])
    
    elif data_sent['power'] == "strength" and data_sent['publisher'] == "DC":
        superhero= choice(["SUPERMAN","green lantern","green lantern","green lantern","green lantern"])

    
    elif data_sent['power'] == "intelligence" and data_sent['publisher'] == "DC":
        superhero= choice(["BATMAN","Martian Manhunter","Martian Manhunter"])

    else:
        superhero="nothing"
    

    

    return superhero
