from flask import Blueprint, url_for, render_template, redirect, current_app
from main.forms import register_form, login_form
import requests, json

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
    return render_template('bolsones.html', title='Venta de bolsones')

@main.route('/register', methods=['POST', 'GET'])
def register():

    return render_template('registro.html', title='Register')

@main.route('/login', methods=['POST', 'GET'])
def login():
    #form = LoginForm()
    return render_template('inicio_sesion.html', title='Login') #form = form)

@main.route('/logout')
def logout():
    return redirect(url_for('main.index'))
