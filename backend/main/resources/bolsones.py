from flask_restful import Resource
from flask import request

BOLSONES = {
    1: {'Primer bolson': 'Bolson1'},
    2: {'Segundo bolson': 'Bolson2'},
    3: {'Tercer bolson': 'Bolson3'}
}

class Bolsones(Resource):

    def get(self, id):

        if int(id) in BOLSONES:

            return BOLSONES[int(id)]

        return '', 404


class Bolson(Resource):

    def get(self, id):

        if int(id) in BOLSONES:

            return BOLSONES[int(id)]

        return '', 404
