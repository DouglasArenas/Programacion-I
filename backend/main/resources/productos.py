from flask_restful import recursos
from flask import request

class Productos(recursos):

    def get(self, id):

        if int(id) in Productos:

            return Productos[int(id)]

        return '', 404
class Producto(recursos):

    def get(self, id):

        if int(id) in Producto:

            return Producto[int(id)]

        return '', 404