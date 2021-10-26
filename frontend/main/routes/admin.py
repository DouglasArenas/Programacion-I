<<<<<<< HEAD
from flask import Blueprint, render_template, redirect, url_for, current_app, request
# Importar objeto Form
from main.forms import login_form, register_form
from flask_login import login_required, LoginManager,current_user
# Importar librería request para realizar consulta y json para manejar la estructura de datos
import requests, json
from .auth import admin_required

#Crear Blueprint
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def index():
    loginForm = LoginForm()
    data = {}
    #Página por defecto
    data['page'] = 1
    #Cantidad de elementos por página para esta tabla
    data['per_page'] = 4
     #Número de página
    if 'page' in request.args:
        #Si se han usado los botones de paginación cargar nueva página
        data["page"] = request.args.get('page','')
    #Crear headers
    headers = {
    'content-type': "application/json"
    }

    # Generar consulta GET al endpoint
    r = requests.get(
        current_app.config["API_URL"]+'/usuarios',
        headers=headers,
        data = json.dumps(data))
    #Convertir respuesta de JSON a  diccionario
    usuarios = json.loads(r.text)["usuarios"]
    #Cargar datos de paginación de API
    pagination = {}
    # Obtener cantidad de páginas
    pagination["pages"] = json.loads(r.text)["pages"]
    # Obtener página actual
    pagination["current_page"] = json.loads(r.text)["page"]
    #Mostrar template
    return render_template('ver_usuarios.html', usuarios=usuarios, loginForm = loginForm, pagination= pagination )

@admin.route('/view/<int:id>')
@login_required
def view(id):
    # Generar consulta GET al endpoint
    #Obtener token
    auth = request.cookies['access_token']
    #Crear headers
    headers = {
    'content-type': "application/json",
    'authorization': "Bearer "+auth
    }
    r = requests.get(
        current_app.config["API_URL"]+'/professor/'+str(id),
        headers=headers)
    # Verificar código de respuesta
    if(r.status_code==404):
        # Si el recurso no existe redireccionar
        return redirect(url_for('professor.index'))
    #Convertir respuesta de JSON a  diccionario
    professor = json.loads(r.text)
    #Mostrar template
    return render_template('professor_view.html',professor=professor  )
=======
from flask import redirect, render_template, url_for, Blueprint, current_app, request
import requests, json 
from flask_login import login_required, LoginManager, current_user
from .auth import admin_required

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
>>>>>>> eda5d572befd683eb2f143b17dee4b071842d2e7
