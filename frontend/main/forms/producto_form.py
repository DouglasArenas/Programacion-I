from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms.validators import InputRequired
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

class ProductoFilterForm(FlaskForm):
    proveedorid = SelectField('', [validators.optional()], coerce = int,)
    ordenamiento = SelectField('',
            choices = [('producto',"Producto"),('proveedor',"Proveedor")],
            validators=[InputRequired()], coerce=str, default='producto')
    envio = SubmitField("Filtrar")
