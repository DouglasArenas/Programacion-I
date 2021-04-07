from flask_restful import Resource
from flask import request

COMPRAS = {
    1: {'Primer compra': 'Papas y camotes'},
    2: {'Segunda compra': 'Zapallos y zanahorias'}
}

class Compras(Resource):

    def get(self, id):

        if int(id) in Compras:

            return Compras[int(id)]

        return '', 404
class Compra(Resource):

    def get(self, id):

        if int(id) in Compra:

            return Compra[int(id)]

        return '', 404