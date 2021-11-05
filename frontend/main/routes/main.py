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


@main.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('registro.html', title='Register')

@main.route('/login', methods= ['POST'])
def login():
    return render_template('inicio_sesion.html', title='Iniciar sesion')

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
