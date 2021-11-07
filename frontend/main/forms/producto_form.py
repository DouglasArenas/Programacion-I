from flask import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms import validators

class ProductoForm(FlaskForm):
    nombre = StringField(
        'Nombre',
        [
            validators.Required(message = 'El nombre es requerido')
        ]
    )

    submit = SubmitField(
        'Agregar producto'
    )

class FilterProductoForm(FlaskForm):
    proveedor = SelectField(
        'Filtrar producto por proveedor',
        [
            validators.Required(message = 'Campo requerido')
        ],
        coerce = int
    )
    submit = SubmitField(
        'Filtrar'
    )