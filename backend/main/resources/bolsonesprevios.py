from flask_restful import Resource
from flask import request
"from main.models import BolsonModel

BOLSONESPREVIOS = {
    1: {'primer bolson previo': 'BolsonP1'},
    2: {'segundo bolson previo': 'BolsonP2'},
    3: {'tercer bolson previo': 'BolsonP3'},
}


class BolsonesPrevios(Resource):
    def get(self):
        return BOLSONESPREVIOS


class BolsonPrevio(Resource):
    def get(self, id):
        if int(id) in BOLSONESPREVIOS:
            return BOLSONESPREVIOS[int(id)]
        return "", 404
        