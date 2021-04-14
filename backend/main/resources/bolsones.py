from flask_restful import Resource
from flask import request

BOLSONES = {
    1: {'bolson uno': 'Combo_one'},
    2: {'bolson dos': 'Combo_two'},
    3: {'bolson tres': 'Combo_three'},
}


class Bolsones(Resource):
    def get(self):
        return BOLSONES


class Bolson(Resource):
    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return "", 404
