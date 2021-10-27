from flask import Blueprint, redirect, url_for, current_app, request, make_response, flash, render_template
from main.forms import  login_form, register_form
from flask_login import login_required, login_user, logout_user, current_user, LoginManager
import requests, json
from .auth import User

#Crear Blueprint
main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
    #Redireccionar a función de vista

    return render_template('principal.html')

@main.route('/login', methods= ['POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        #Enviar requests
        data = '{"email":"'+loginForm.email.data+'", "password":"'+loginForm.password.data+'"}'
        r = requests.post(
            current_app.config["API_URL"]+'/auth/login',
            headers={"content-type":"application/json"},
            data = data)
        #Si la request se realiza con éxito
        if r.status_code == 200:
            #Cargar valores del usuario de la respuesta
            user_data = json.loads(r.text)
            user = User(id = user_data.get("id"), email = user_data.get("email"),  role = user_data.get("role") )
            #Loguear objeto usuario
            login_user(user)
            # Crear una request de redirección
            if current_user.role == 'admin':
                req = make_response(redirect(url_for('admin.home')))
                #Setear cookie con el valor del token
            # elif current_user.role == 'proveedor':
                # req = make_response(redirect(url_for('proveedor.home')))
            req.set_cookie('access_token', user_data.get("access_token"), httponly = True)
                #Realizar la request
            return req
        else:
            #Mostrar error de autenticación
            flash('Usuario o contraseña incorrecta','danger')
    return redirect(url_for('main.index'))

@main.route('/logout')
def logout():
    #Crear una request de redirección
    req = make_response(redirect(url_for('main.index')))
    #Vaciar cookie
    req.set_cookie('access_token', '', httponly = True)
    #Deloguear usuario
    logout_user()
    #Realizar request
    return req
