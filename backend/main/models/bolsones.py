from .. import db
from datetime import datetime

class Bolson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    approved = db.Column(db.Boolean, default = False, nullable = False)
    date = db.Column(db.DateTime, nullable = False)
    buys = db.relationship('Compra', back_populates='bolson')

    def _repr_(self):
        return '<Bolson: %r %r %r >' % (self.name, self.approved, self.date)

    def to_json(self):
        bolson_json = {
            'id': self.id,
            'name': str(self.name),
            'approved': self.approved,
            'date': self.date.strftime('%Y-%m-%d')
        }
        return bolson_json
    @staticmethod

    def from_json(bolson_json):
        id = bolson_json.get('id')
        name = bolson_json.get('name')
        date = datetime.strptime(bolson_json.get('date'), '%Y-%m-%d')
        approved = bolson_json.get('approved')
        return Bolson(id=id,
                    name=name,
                    approved=approved,
                    date=date
                    )