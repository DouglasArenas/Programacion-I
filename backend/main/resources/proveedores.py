from flask_restful import recursos
from flask import request

class Proveedores(recursos):

    def get(self, id):

        if int(id) in Proveedores:

            return Proveedores[int(id)]

        return '', 404
class Proveedor(recursos):

    def get(self, id):

        if int(id) in Proveedor:

            return Proveedor[int(id)]

        return '', 404
