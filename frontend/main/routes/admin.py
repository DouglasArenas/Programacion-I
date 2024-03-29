from logging import log, logMultiprocessing
from flask import redirect, render_template, url_for, Blueprint, current_app, request
import requests, json 
from flask_login import current_user, login_required, LoginManager
from .auth import admin_required
from main.forms import PerfilForm, BolsonForm

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/principal')
@login_required
def principal():
    return render_template('principaladmin.html', title='Admin', bg_color="bg-success")


@admin.route('/crear-proveedor')
@login_required
def crear_proveedor():

    page = {
        "page": 1
    }
    r = requests.get(f'{current_app.config["API_URL"]}/usuarios', headers={"content-type": "application/json"}, json=page, auth=BearerAuth(str(request.cookies['access_token'])))

    usuarios = json.loads(r.text)["usuarios"]
    page = json.loads(r.text)["page"]
    pages = json.loads(r.text)["pages"]


    return render_template('crear_proveedor.html', title='Admin', bg_color="bg-dark", usuarios = usuarios, page = page, pages = pages)


# @admin.route('/add-proveedor/<int:id>')
# @login_required
# def add_proveedor(id):

#     json = {
#         'role': 'proveedor'
#     }

#     r = requests.put(f'{current_app.config["API_URL"]}/usuario/{id}', headers={"content-type": "application/json"}, json = json, auth=BearerAuth(str(request.cookies['access_token'])))
#     return redirect(url_for('admin.agregar_proveedor'))

@admin.route('/remove-proveedor/<int:id>')
@login_required
def remove_proveedor(id):
    json = {
        'role': 'cliente'
    }
    r = requests.put(f'{current_app.config["API_URL"]}/usuario/{id}', headers={"content-type": "application/json"}, json = json, auth=BearerAuth(str(request.cookies['access_token'])))
    return redirect(url_for('admin.agregar_proveedor'))

    

# class BearerAuth(requests.auth.AuthBase):
#     def __init__(self, token):
#         self.token = token
#     def __call__(self, r):
#         r.headers["authorization"] = "Bearer " + self.token
#         return r 


# @admin.route('/perfil/<int:id>', methods=['POST', 'GET'])
# @login_required
# def editar_perfil(id):
#     form = cargar_un_perfil(id)
#     return render_template('editarperfiladmin.html', title='Admin', bg_color='bg-secondary', form = form)    

# @admin.route('/bolsones-venta')
# def bolsones_venta():

#     page = {
#         "page": 1
#     }
#     r = requests.get(f'{current_app.config["API_URL"]}/bolsones-venta', headers={"content-type": "application/json"}, json=page)
#     bolsones = json.loads(r.text)["bolsonesventa"]
#     page = json.loads(r.text)["page"]
#     pages = json.loads(r.text)["pages"]


#     return render_template('ver_bolsones.html', bg_color = 'bg-dark', bolsones = bolsones, page = page, pages = pages)


@admin.route('/agregar-bolson', methods=['POST', 'GET'])
@login_required
def crear_bolson():

    data = {
        'per_page': 10
    }

    r = requests.get(f'{current_app.config["API_URL"]}/productos', headers={"content-type": "application/json"}, json = data)
    productos = json.loads(r.text)["productos"]


    productos = [(producto['id'], producto['nombre'])  for producto in productos]
    productos.insert(0, (0, '--Seleccionar producto'))

    form = BolsonForm()
    form.producto.choices = productos
    # form.producto2.choices = productos
    # form.producto3.choices = productos
    # form.producto4.choices = productos
    # form.producto5.choices = productos

    if form.validate_on_submit():


        bolson = {
            'nombre': form.nombre.data,
            'aprobado': form.venta.data,
            'imagen': form.imagen.data,
            'descripcion': form.descripcion.data
        }
        r = requests.post(f'{current_app.config["API_URL"]}/bolsones-pendientes', headers={"content-type": "application/json"}, json = bolson, auth=BearerAuth(str(request.cookies['access_token'])))

        bolsonId = json.loads(r.text)['id']

        productos = [form.producto.data]#, form.producto2.data, form.producto3.data, form.producto4.data, form.producto5.data]
        for producto in productos:
            if producto != 0:
                print('it works')
                data = {
                    'productoId': producto,
                    'bolsonId': int(bolsonId),
                    'cantidad': 10
                }
                try:
                    r = requests.post(f'{current_app.config["API_URL"]}/productos-bolsones', headers={"content-type": "application/json"}, json=data, auth=BearerAuth(str(request.cookies['access_token'])))
                except:
                    pass
            else:
                print('it doesnt work')

    return render_template('crear_bolson.html', title='Admin', bg_color='success', form = form)

# @admin.route('/ver-productos')
# def productos():

#     data = {
#         'per_page': 15
#     }

#     r = requests.get(f'{current_app.config["API_URL"]}/productos', headers={"content-type": "application/json"}, json = data, auth=BearerAuth(str(request.cookies['access_token'])))



#     productos = json.loads(r.text)['productos']
#     page = json.loads(r.text)['page']
#     pages = json.loads(r.text)['pages']

#     return render_template('ver_productos_admin.html', bg_color = 'bg-dark', title = 'Admin', productos = productos, page = page, pages= pages)

# @admin.route('/producto-eliminar/<int:id>')
# def eliminar_producto(id):

#     r = requests.delete(f'{current_app.config["API_URL"]}/producto/{id}', headers={"content-type": "application/json"}, auth=BearerAuth(str(request.cookies['access_token'])))

#     return redirect(url_for('admin.productos'))

@admin.route('/compras')
def compras():

    data = {

    }

    r = requests.get(f'{current_app.config["API_URL"]}/compras', headers={"content-type": "application/json"}, json = data, auth=BearerAuth(str(request.cookies['access_token'])))

    compras = json.loads(r.text)['compras']
    page = json.loads(r.text)['page']
    pages = json.loads(r.text)['pages']

    return render_template('compras_admin.html', bg_color = 'bg-dark', title = 'Panel Admin', compras = compras)

@admin.route('/compra/<int:id>')
def ver_compra(id):

    r = requests.get(f'{current_app.config["API_URL"]}/compra/{id}', headers={"content-type": "application/json"}, auth=BearerAuth(str(request.cookies['access_token'])))

    compra = json.loads(r.text)

    return render_template('admin_ver_compra.html', bg_color = 'bg-dark', title = 'Ver compra', compra = compra)
