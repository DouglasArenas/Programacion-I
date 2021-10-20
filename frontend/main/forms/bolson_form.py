from flask import Flask
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField, IntegerField, SelectField, BooleanField
from wtforms.fields.html5 import EmailField, DateField
from wtforms import validators

class BolsonForm(FlaskForm):

    nombre = StringField(
        'Nombre del bolson',
        [
            validators.Required(message = 'El nombre es requerido')
        ]
    )

    descripcion = StringField(
        'Descripcion',
        [
            validators.Required(message = 'La descripcion es requrida')
        ]
    )

    venta = IntegerField(
        'Listo para la venta',
        [
            validators.Required(message = 'Este campo es requerido')
        ]
    )

    producto = SelectField(
        'Seleccionar producto',
        [
            validators.Required(message = 'Este campo es requiredo')
        ],
        choices = [('Seleccionar producto'), ('Naranja'), ('Mandarina')]
    )

    imagen = StringField(
        'Imagen del bolson',
        [
            validators.Required(message = 'Este campo es requerido')
        ]
    )

    submit = SubmitField(
        'Agregar bolson'
    )

    