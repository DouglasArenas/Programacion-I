from flask_restful import recursos
from flask import request

class BolsonesPrevios(recursos):

    def get(self, id):

        if int(id) in BolsonesPrevios:

            return BolsonesPrevios[int(id)]

        return '', 404