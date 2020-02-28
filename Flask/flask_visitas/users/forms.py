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
    ('3', 'Gestion Tecnologica'),
    ('4', 'Admin')
]


class RegistrationForm(FlaskForm):
    username = StringField('Usuario',
                           validators=[DataRequired(),
                                       Length(min=2, max=20)])
    email = StringField('Correo', validators=[DataRequired(), Email()])
    access = SelectField('Tipo de Usuario', validators=[DataRequired()], choices=ACCESS)
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña',
                                     validators=[DataRequired(), EqualTo('password')])
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
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class UpdateAccountForm(FlaskForm):
    username = StringField('Usuario',
                           validators=[DataRequired(),
                                       Length(min=2, max=20)])
    email = StringField('Correo', validators=[DataRequired(), Email()])
    access = SelectField('Tipo de Usuario', validators=[DataRequired()], choices=ACCESS)
    picture = FileField('Actualizar foto de perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Actualizar')

    @staticmethod
    def validate_username(self, username):

        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()

            if user:
                raise ValidationError('That username already exist. Please choose another one')

    @staticmethod
    def validate_email(self, email):

        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()

            if user:
                raise ValidationError('That email already exist. Please choose another one')