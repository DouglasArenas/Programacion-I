from flask_restful import recursos
from flask import request

class Compras(recursos):

    def get(self, id):

        if int(id) in Compras:

            return Compras[int(id)]

        return '', 404
class Compra(recursos):

    def get(self, id):

        if int(id) in Compra:

            return Compra[int(id)]

        return '', 404