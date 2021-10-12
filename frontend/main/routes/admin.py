from flask import redirect, render_template, url_for, Blueprint, current_app, request
import requests, json 

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/home')
@login_required
def home():
    return render_template('principaladmin.html', title='Admin', bg_color="bg-success")

@admin.route('/agregar-proveedor')
def crear_proveedor():
    return render_template('crear_proveedor.html', title='Admin', bg_color="bg-success")
    #return render_template('pruebas.html', title='Admin', bg_color='bg-dark')


@admin.route('/agregar-bolson')
def agregar_bolson():

    r = requests.get(f'{current_app.config["API_URL"]}/productos', headers={"content-type": "application/json"}, json = data)
    productos = json.loads(r.text)["productos"]

    productos = [producto['nombre'] for producto in productos]

    return render_template('agregarbolson.html', title='Admin', bg_color='bg-secondary', form = form)