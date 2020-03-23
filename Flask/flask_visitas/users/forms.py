from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flask_visitas.users.models import User

# key - value
ACCESS = [
    ('0', 'Profesor'),
    ('1', 'Jefe de Departamento'),
    ('2', 'Subdirector'),
    ('3', 'Gestión Tecnológica'),
    ('4', 'Admin')
]


class RegistrationForm(FlaskForm):
    name = StringField('Nombre Completo',
                       validators=[DataRequired(),
                                   Length(min=10, max=100)])
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=5, max=20)])
    email = StringField('Correo', validators=[DataRequired(), Email()])
    access = SelectField('Tipo de Usuario', validators=[DataRequired()], choices=ACCESS)
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Registrar')

    @staticmethod
    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('That username already exist. Please choose another one')

    @staticmethod
    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('That email already exist. Please choose another one')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class UpdateAccountForm(FlaskForm):
    name = StringField('Nombre Completo',
                       validators=[DataRequired(),
                                   Length(min=10, max=100)])
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=5, max=20)])
    email = StringField('Correo', validators=[DataRequired(), Email()])
    access = SelectField('Tipo de Usuario', validators=[DataRequired()], choices=ACCESS)
    picture = FileField('Actualizar foto de perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Actualizar')
    delete = SubmitField('Eliminar')
    data_user_prev = None

    @staticmethod
    def validate_username(self, username):

        if username.data != current_user.username and current_user.access != 4:
            self.user_exist(username)

        if self.data_user_prev.username != username.data:
            self.user_exist(username)

    @staticmethod
    def user_exist(username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('That username already exist. Please choose another one')

    @staticmethod
    def validate_email(self, email):

        if email.data != current_user.email and current_user.access != 4:
            self.mail_exist(email)

        if self.data_user_prev.email != email.data:
            self.mail_exist(email)

    @staticmethod
    def mail_exist(email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('That email already exist. Please choose another one')



