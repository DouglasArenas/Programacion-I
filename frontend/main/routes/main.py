from os import access
from flask import Blueprint, redirect, url_for, current_app, request, make_response, flash, render_template
from main.forms import LoginForm, RegisterForm
from flask_login import login_required, login_user, logout_user, current_user, LoginManager
import requests, json
from .auth import User

#Crear Blueprint
main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
    #Redireccionar a función de vista
    return render_template('principal.html')


@main.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = {
            "nombre": form.nombre.data,
            "apellido": form.apellido.data,
            "telefono": form.telefono.data,
            "email": form.email.data,
            "password": form.password.data
        }
        r = requests.post(
            f'{current_app.config["API_URL"]}/auth/register', json=user
        )
        if r.status_code == 201:
            return redirect(url_for('main.login'))

    return render_template('registro.html', title='Register',bg_color="bg-secondary", form=form)

@main.route('/login', methods= ['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        data = {
            'email': form.email.data,
            'password': form.password.data
        }
        r = requests.post(
            f'{current_app.config["API_URL"]}/auth/login',
            headers={"content-type": "application/json"},
            json=data
        )
        if r.status_code == 200:
            user_data = json.loads(r.text)
            user = User(id=user_data.get('id'), email=user_data.get('mail'), role=user_data.get('role'))
            login_user(user)
            req = make_response(redirect(url_for('main.register')))

            req.set_cookie('access_token', user_data.get('access_token'), httponly=True)
            if current_user.is_authenticated:
                print(current_user.email, 'email del current user')
            return req
        else:
            flash("Usuario o contraseña incorrecta")

    return render_template('inicio_sesion.html', title='Iniciar sesion', form = form)

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
