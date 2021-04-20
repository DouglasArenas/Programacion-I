from .. import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    idproveedor = db.Column(db.Integer, db.ForeignKey("proveedor.id"), nullable=False)
    proveedor = db.relationship("Proveedor", back_populates="productos", uselist=False, single_parent=True)

    def __repr__(self):
        return '<Productos: %r %r >' % (self.name, self.idproveedor)

    def to_json(self):
        producto_json = {
            "id": self.id,
            "name": str(self.name),
            "proveedor": self.proveedor.name

        }
        return producto_json
    @staticmethod

    def from_json(producto_json):
        id = prodcuto_json.get('id')
        name = producto_json.get('name')
        idproveedor = producto_json.get('idproveedor')
        return Producto(id=id,
                    name=name,
                    idproveedor=idproveedor,
                    )
