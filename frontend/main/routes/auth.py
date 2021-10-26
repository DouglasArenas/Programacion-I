from .. import login_manager
<<<<<<< HEAD
from flask import request, flash, redirect, url_for,current_app
from flask_login import UserMixin, LoginManager, current_user
import jwt
from functools import wraps

#Clase que contendrá los datos del usuario logueado
class User(UserMixin):
    def __init__(self ,id ,email ,role):
=======
from flask import request, flash, redirect, url_for
from flask_login import UserMixin, LoginManager, current_user
import jwt
import requests

class User(UserMixin):
    def __init__(self, id, email, role):
>>>>>>> eda5d572befd683eb2f143b17dee4b071842d2e7
        self.id = id
        self.email = email
        self.role = role

<<<<<<< HEAD
#Método que le indica a LoginManager como obtener los datos del usuario logueado
#En nuestro caso al trabajar con JWT los datos se obtendran de los claims del Token
#que ha sido guardado en una cookie en el browser
@login_manager.request_loader
def load_user(request):
    #Verificar si la cookie ha sido cargada
    if 'access_token' in request.cookies:
        try:
            #Decodificar el token
            decoded = jwt.decode(request.cookies['access_token'], current_app.config["SECRET_KEY"], algorithms=["HS256"], verify=False)
            #Cargar datos del usuario
            user = User(decoded["id"],decoded["email"],decoded["role"])
            #Devolver usuario logueado con los datos cargados
            return user
        except jwt.exceptions.InvalidTokenError:
            print('Invalid Token.')
        except jwt.exceptions.DecodeError:
            print('DecodeError.')
    return None

#Función que sobreescribe el método al intentar ingresar a una ruta no autorizada
@login_manager.unauthorized_handler
def unauthorized_callback():
    flash('Debe iniciar sesión para continuar.','warning')
    #Redireccionar a la página que contiene el formulario de login
    return redirect(url_for('main.index'))

#Define la función de verificación de admin para las rutas
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kws):
        if not current_user.role == "admin":
            flash('Acceso restringido a administradores.','warning')
            return redirect(url_for('main.index'))
        return fn(*args, **kws)
    return wrapper
=======
@login_manager.request_loader
def load_user(request):
    if 'accsess_token' in request.cookies:
        try:
            jwt_options = {
                'verify_signature': False,
                'verify_exp': True,
                'verify_nbf': False,
                'verify_iat': True,
                'verify_aud': False
            }
            token = request.cookies['access_token']
            data = jwt.decode(token, options=jwt_options, algorithms=["HS256"])
            user = User(data["id"], data["mail"], data["role"])
            return user
        except jwt.exceptions.InvalidTokenError:
            print('Token invalido')
        except jwt.exceptions.DecodeError:
            print('Decode Error')
    return None
@login_manager.unauthorized_handler
def unauthorized_callback():
    flash('Inicie sesion para continuar', 'warning')
    return redirect(url_for('main.login'))

def admin_required(fn):
    def wrapper(*args, **kwargs):
        if not current_user.role == 'admin':
            return redirect(url_for('bolsones.venta', page=1))
        else:
            return fn(*args, **kwargs)
    return wrapper

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call___(self, r):
        r.headers["authorization"] = "Bearer" + self.token
        return r
>>>>>>> eda5d572befd683eb2f143b17dee4b071842d2e7
