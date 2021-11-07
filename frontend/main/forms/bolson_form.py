from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField
from wtforms.fields.html5 import DateField, DateTimeField
from wtforms import validators

class BolsonForm(FlaskForm):

    nombre = StringField(
        'Nombre del bolson',
        [
            validators.Required(message = 'El nombre es requerido')
        ]
    )
    fecha = DateField("Fecha",
        [
            validators.Required()
        ],  format='%Y-%m-%d'
        )

    venta = IntegerField(
        'Listo para la venta',
        [
            validators.Required(message = 'Este campo es requerido')
        ]
    )

    productoId = SelectField(
        'Seleccionar producto',
        [
            validators.Required(message = 'Este campo es requiredo')
        ],
        choices = [('Seleccionar producto'), ('Naranja'), ('Mandarina')]
    )

    submit = SubmitField(
        'Agregar bolson'
    )
class FormFilterBolsones(FlaskForm):
    desde = DateTimeField('',[validators.optional()], format='%Y-%m-%d')
    hasta = DateTimeField('',[validators.optional()], format='%Y-%m-%d')
    envio = SubmitField('Filtrar')
