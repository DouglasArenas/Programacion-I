from flask import request, jsonify, Blueprint
from .. import db
from main.models import UsuarioModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from .. import jwt


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['POST'])
def login():
    usuario = db.session.query(UsuarioModel).filter(UsuarioModel.mail == request.get_json().get("mail")).first_or_404()
    if usuario.validate_pass(request.get_json().get("password")):
        print(usuario)
        access_token = create_access_token(identity=usuario)
        data = {
            'id': str(usuario.id),
            'mail': usuario.mail,
            'access_token': access_token,
            'role': str(usuario.rol)
        }

        return data, 200
    else:
        return 'Incorrect password', 401


@jwt.user_identity_loader
def user_identity_lookup(usuario):
    print("identity")
    return usuario.id

@jwt.additional_claims_loader
def add_claims_to_access_token(usuario):
    print("claims")
    claims = {
        'role': usuario.rol,
        'id': usuario.id,
        'email': usuario.mail
    }
    return claims

@auth.route('/register', methods=['POST'])
def register():
    usuario = UsuarioModel.from_json(request.get_json())
    exists = db.session.query(UsuarioModel).filter(UsuarioModel.mail == usuario.mail).scalar() is not None
    if exists:
        return 'Duplucated mail', 409
    else:
        try:
            db.session.add(usuario)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return usuario.to_json(), 201