from .. import db
from datetime import datetime

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purchasedate = db.Column(db.DateTime, nullable = False)
    retired = db.Column(db.Boolean, nullable = False)
    bolsonid= db.Column(db.Integer, db.ForeignKey('bolson.id'), nullable=False)
    bolson = db.relationship('Bolson', back_populates='compras', uselist=False, single_parent=True)

    def _repr_(self):
        return '<Compra: %r %r >' % (self.purchasedate, self.retired, self.bolsonid)

    def to_json(self):
        compra_json = {
            'id': self.id,
            'purchasedate': self.purchasedate.strftime('%Y-%m-%d'),
            'retired': str(self.retired),
            'bolson': self.bolson.name
        }
        return compra_json
    @staticmethod

    def from_json(compra_json):
        id = compra_json.get('id')
        purchasedate = datetime.strptime(compra_json.get('purchasedate'), '%Y-%m-%d')
        retired = compra_json.get('retired')
        bolsonid= compra_json.get('bolsonid')
        return Compra(id=id,
                    purchasedate=purchasedate,
                    retired=retired,
                    bolsonid=bolsonid
                    )