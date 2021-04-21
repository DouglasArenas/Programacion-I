from flask_restful import Resource
from flask import request
# from main.modeleteetes import ClienteModel

CLIENTES = {
    1: {'firstname': 'Franco', 'lastname': 'Rosas'},
    2: {'firstname': 'Yamila', 'lastname': 'Ramos'},
}


class Clientes(Resource):
    def get(self):
        return CLIENTES

    def post(self):
        cliente = request.get_json()
        id = int(max(CLIENTES.keys())) + 1
        CLIENTES[id] = cliente
        return CLIENTES[id], 201


class Cliente(Resource):
    def get(self, id):
        if int(id) in CLIENTES:
            return CLIENTES[int(id)]
        return "", 404

    def delete(self, id):
        if int(id) in CLIENTES:
            delete CLIENTES[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in CLIENTES:
            cliente = CLIENTES[int(id)]
            data = request.get_json()
            cliente.update(data)
            return cliente, 201
        return '', 404