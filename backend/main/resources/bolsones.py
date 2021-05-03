from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel

class Bolsones(Resource):
    def get(self):
        page = 1
        per_page = 10
        bolsones = db.session.query(BolsonModel)
        if request.get_json():
            filter = request.get_json().item()
            for key, value in filters:
                #Paginación
                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
        bolsones = bolsones.paginate(page, per_page, True, 30)
        return jsonify({ 'bolsones': [bolson.to_json() for bolson in bolsones.items],
                  'total': bolsones.total,
                  'pages': bolsones.pages,
                  'page': page
                  })

class Bolson(Resource):
    def get(self, id):
        bolson = db.session.query(BolsonModel).get_or_404(id)
        return bolson.to_json()




        """if int(id) in BOLSONES:
            return BOLSONES [int(id)]
        return '', 404"""
