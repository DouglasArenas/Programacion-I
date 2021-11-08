from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import InputRequired
from wtforms import validators


class ProveedorFilterForm(FlaskForm):
    ordenamiento = SelectField(
        '',
        choices=[('nombre', "nombre"), ('apellido', "apellido")],
        validators=[InputRequired()], coerce=str, default='nombre'
        )
    envio = SubmitField("filtrar")
