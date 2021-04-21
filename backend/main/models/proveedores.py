from .. import db

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.String(100), nullable = False)
    productos = db.relationship('Producto', back_populates='proveedor')

    def _repr_(self):
        return '<Proveedor: %r %r >' % (self.name, self.phone)
    def to_json(self):
        proveedor_json = {
            'id': self.id,
            'name': str(self.name),
            'phone': str(self.phone)
        }
        return proveedor_json
    @staticmethod

    def from_json(proveedor_json):
        id = proveedor_json.get('id')
        name = proveedor_json.get('name')
        phone = proveedor_json.get('phone')
        return Proveedor(id=id,
                    name=name,
                    phone=phone
                    )