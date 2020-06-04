from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flask_visitas.usuarios.models import User
from flask_visitas.usuarios.choices import access, department


class RegistrationForm(FlaskForm):
    name = StringField('Nombre Completo',
                        validators=[DataRequired(),
                                    Length(min=10, max=100)])
    email = StringField('Correo', validators=[DataRequired(), Email()])
    access = SelectField('Tipo de Usuario', validators=[DataRequired()], choices=access)
    department = SelectField('Departamento', validators=[DataRequired()], choices=department)
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña',
                                        validators=[DataRequired(),
                                                    EqualTo('password')])
    submit = SubmitField('Registrar')

    # @staticmethod
    # def validate_username(self, username):
    #
    #     user = User.query.filter_by(username=username.data).first()
    #
    #     if user:
    #         raise ValidationError('Ese usuario ya existe. Por favor escoja algún otro')

    @staticmethod
    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Ya existe una cuenta con ese Email. Escoja otro por favor')


class LoginForm(FlaskForm):
    email = StringField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Ingresar')


class UpdateAccountForm(FlaskForm):
    name = StringField('Nombre Completo',
                        validators=[DataRequired(),
                                    Length(min=10, max=100)])
    email = StringField('Correo', validators=[DataRequired(), Email()])
    access = SelectField('Tipo de Usuario', validators=[DataRequired()], choices=access)
    department = SelectField('Departamento', validators=[DataRequired()], choices=department)
    picture = FileField('Actualizar foto de perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Actualizar')
    data_user_prev = None

    # @staticmethod
    # def validate_username(self, username):
    #
    #     if username.data != current_user.username and current_user.access != 4:
    #         self.user_exist(username)
    #
    #     if self.data_user_prev.username != username.data:
    #         self.user_exist(username)
    #
    # @staticmethod
    # def user_exist(username):
    #     user = User.query.filter_by(username=username.data).first()
    #
    #     if user:
    #         raise ValidationError('Ese usuario ya existe. Por favor escoja algún otro')

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
            raise ValidationError('Ya existe una cuenta con ese Email. Escoja otro por favor')


class RequestResetForm(FlaskForm):
    email = StringField('Correo', validators=[DataRequired(), Email()])
    submit = SubmitField('Recuperar Contraseña')

    @staticmethod
    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()

        if user is None:
            raise ValidationError('No existe una cuenta registrada con ese Email.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña',
                                        validators=[DataRequired(),
                                                    EqualTo('password')])
    submit = SubmitField('Restablecer Contraseña')


