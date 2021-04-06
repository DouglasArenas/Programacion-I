from flask_restful import recursos
from flask import request

class Bolsones(recursos):

    def get(self, id):

        if int(id) in Bolsones:

            return Bolsones[int(id)]

        return '', 404
class Bolson(recursos):

    def get(self, id):

        if int(id) in Bolson:

            return Bolson[int(id)]

        return '', 404




