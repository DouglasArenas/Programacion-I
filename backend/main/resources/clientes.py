
from flask_restful import Resource
from flask import request, jsonify
from .. import db
#from main.models import UsuarioModel
#from flask_jwt_extended import jwt_required, get_jwt_identity
#from main.auth.decoradores import admin_required

class Clientes(Resource):
    # @jwt_required()
    def get(self):
        page = 1
        per_page = 10
        clientes = db.session.query(UsuarioModel).filter(UsuarioModel.rol == 'cliente')
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key =="page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
        clientes = clientes.paginate(page, per_page, True, 30)
        return jsonify({ 'clientes': [cliente.to_json() for cliente in clientes.items],
                  'total': clientes.total,
                  'pages': clientes.pages,
                  'page': page
                  })
#    @jwt_required()
    def post(self):
        cliente = UsuarioModel.from_json(request.get_json())
        db.session.add(cliente)
        db.session.commit()
        return cliente.to_json(), 201

class Cliente(Resource):
    #@jwt_required()
    def get(self, id):
        cliente = db.session.query(UsuarioModel).get_or_404(id)
        return cliente.to_json()
    # @admin_required
    def delete(self, id):
        cliente = db.session.query(UsuarioModel).get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return '', 204
    # @jwt_required()
    def put(self, id):
        cliente = db.session.query(UsuarioModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(cliente, key, value)
        db.session.add(cliente)
        db.session.commit()
        return cliente.to_json(), 201