from flask_restful import Resource
from flask import request

BOLSONESPENDIENTES = {
    1: {'Primer bolson': 'Bolson1'},
    2: {'Segundo bolson': 'Bolson2'},
    3: {'Tercer bolson': 'Bolson3'}
}

class BolsonPendiente(Resource):
    def get(self, id):
        if int(id) in BOLSONESPENDIENTES:
            return BOLSONESPENDIENTES[int(id)]
        return "", 404

    def delete(self, id):
        if int(id) in BOLSONESPENDIENTES:
            del BOLSONESPENDIENTES[id]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in BOLSONESPENDIENTES:
            bolsonprevio = BOLSONESPENDIENTES[int(id)]
            date = request.get_json()
            bolsonprevio.update(date)
            return bolsonprevio, 201
        return '', 404