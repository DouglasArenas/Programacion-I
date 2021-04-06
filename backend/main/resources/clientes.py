from flask_restful import recursos
from flask import request

class Clientes(recursos):

    def get(self, id):

        if int(id) in Clientes:

            return Clientes[int(id)]

        return '', 404
class Cliente(recursos):

    def get(self, id):

        if int(id) in Cliente:

            return Cliente[int(id)]

        return '', 404