from .. import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    surname = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.String(100), nullable = False)
    mail = db.Column(db.String(100), nullable = False)

    def _repr_(self):
        return '<Cliente: %r %r %r %r >' % (self.name, self.surname, self.phone, self.mail)

    def to_json(self):
        cliente_json = {
            'id': self.id,
            'name': str(self.name),
            'surname': str(self.surname),
            'phone': str(self.phone),
            'mail': str(self.mail)
        }
        return cliente_json
    @staticmethod

    def from_json(cliente_json):
        id = cliente_json.get('id')
        name = cliente_json.get('name')
        surname = cliente_json.get('surname')
        phone = cliente_json.get('phone')
        mail = cliente_json.get('mail')
        return Cliente(id=id,
                    name=name,
                    surname=surname,
                    phone=phone,
                    mail=mail
                    )
