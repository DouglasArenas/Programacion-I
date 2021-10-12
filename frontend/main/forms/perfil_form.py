from flask_wtf import FlaskForm #Importa funciones de formulario
from wtforms import PasswordField, SubmitField, StringField #Importa campos
from wtforms.fields.html5 import EmailField #Importa campos HTML
from wtforms import validators #Importa validaciones

class UserForm(FlaskForm):

    #Definición de campo String
    firstname = StringField('Nombre',
    [
        #Definición de validaciones
        validators.Required(message = "El nombre es requerido"),
        validators.Length(min=5)
    ])

    lastname = StringField('Apellido',
    [
        validators.Required(message = "El apellido es requerido"),
        validators.Length(min=5)
    ])

    #Definición de campo de mail
    email = EmailField('Correo electronico',
    [
        validators.Required(message = "El correo electronico es requerido"),
        validators.Email( message ='Formato invalido'),
    ])

    #Definición de campo de contraseña
    password = PasswordField('Contrasenia', [
        validators.Required(),
         #El campo de contraseña debe coincidir con el de confirmuar
        validators.EqualTo('Confirmar', message='Passwords dont match')
    ])

    confirm = PasswordField('Repetir contrasenia')

    #Definición de campo submit
    submit = SubmitField("Enviar")
