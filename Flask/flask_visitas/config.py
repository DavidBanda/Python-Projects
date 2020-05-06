import os


class Config:
    SECRET_KEY = 'e7e4b44cfa377d362eae765337be7361872b62bb7fc0bf2fea25f4d88222291f'
    # SQLALCHEMY_DATABASE_URI = f'mysql://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASS")}' \
    #                           f'@localhost/proyecto_visitas'
    SQLALCHEMY_DATABASE_URI = f'mysql://root:DAVIDAAROn15.@localhost/proyecto_visitas'
