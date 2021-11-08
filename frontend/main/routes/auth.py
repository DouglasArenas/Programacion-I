from .. import login_manager
from flask import request, flash, redirect, url_for,current_app
from flask_login import UserMixin, LoginManager, current_user
import jwt
from functools import wraps

class User(UserMixin):
    def __init__(self ,id ,email ,role):
        self.id = id
        self.email = email
        self.role = role

@login_manager.request_loader
def load_user(request):
    #Verificar si la cookie ha sido cargada
    if 'access_token' in request.cookies:
        try:
            decoded = jwt.decode(request.cookies['access_token'], current_app.config["SECRET_KEY"], algorithms=["HS256"], verify=False)
            user = User(decoded["id"],decoded["email"],decoded["role"])
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

def proveerdor_required(fn):
    @wraps(fn)
    def wrapper(*args, **kws):
        if not current_user.role == "proveedor":
            flash('Acceso restringido a proveedor.','warning')
            return redirect(url_for('main.index'))
        return fn(*args, **kws)
    return wrapper

def cliente_required(fn):
    @wraps(fn)
    def wrapper(*args, **kws):
        if not current_user.role == "cliente":
            flash('Acceso restringido a cliente.','warning')
            return redirect(url_for('main.index'))
        return fn(*args, **kws)
    return wrapper

def admin_provider_required(fn):
    @wraps(fn)
    def wrapper(*args, **kws):
        if not current_user.role == "admin" and not current_user.role == "proveedor":
            flash('Acceso restringido a administradores y proveedores', 'warning')
            return redirect(url_for('main.index'))
        return fn(*args, **kws)
    return wrapper

def admin_client_required(fn):
    @wraps(fn)
    def wrapper(*args, **kws):
        if not current_user.role == "admin" and not current_user.role == "cliente":
            flash('Acceso restringido a administradores y clientes', 'warning')
            return redirect(url_for('main.index'))
        return fn(*args, **kws)
    return wrapper
