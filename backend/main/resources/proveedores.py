from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProveedorModel


class Proveedor(Resource):
    def get(self, id):
        proveedor = db.session.query(ProveedorModel).get_or_404(id)
        try:
            return proveedor.to_json()
        except:
            return '', 404

    def delete(self, id):
        proveedor = db.session.query(ProveedorModel).get_or_404(id)
        try:
            db.session.delete(proveedor)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        proveedor = db.session.query(ProveedorModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(proveedor, key, value)
        try:
            db.session.add(proveedor)
            db.session.commit()
            return proveedor.to_json(), 201
        except:
            return '', 404

class Proveedores(Resource):
    def get(self):
        page = 1
        per_page = 10
        proveedores = db.session.query(ProveedorModel)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)
        proveedores = proveedores.paginate(page, per_page, True, 30)

        return jsonify({
            'proveedores': [proveedor.to_json() for proveedor in proveedores.items],
            'total': proveedores.total,
            'pages': proveedores.pages,
            'page': page
        })

    def post(self):
        proveedor = ProveedorModel.from_json(request.get_json())
        try:
            db.session.add(proveedor)
            db.session.commit()
        except:
            return '', 404
        return proveedor.to_json(), 201