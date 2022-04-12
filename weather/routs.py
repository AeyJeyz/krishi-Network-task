from sys import prefix
from flask import Blueprint

weather = Blueprint('weather',__name__, url_prefix='/weather')

@weather.route('/getweather')
def getdata():
    return {'key':'value'}