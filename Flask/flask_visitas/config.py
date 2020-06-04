import os


class Config:
    SECRET_KEY = 'e7e4b44cfa377d362eae765337be7361872b62bb7fc0bf2fea25f4d88222291f'
    SQLALCHEMY_DATABASE_URI = f'mysql://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASS")}' \
                                f'@localhost/proyecto_visitas'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")



