from flask_restful import recursos
from flask import request

class BolsonesVenta(recursos):

    def get(self, id):

        if int(id) in BolsonesVenta:

            return BolsonesVenta[int(id)]

        return '', 404
class BolsonVenta(recursos):

    def get(self, id):

        if int(id) in BolsonVenta:

            return BolsonVenta[int(id)]

        return '', 404