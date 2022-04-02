from distutils.command.config import config
from distutils.debug import DEBUG
from msilib.schema import Class



class DevelopmentConfig():
   DEBUG = True
   MYSQL_HOST = 'localhost'
   MYSQL_USER = 'luistdea'
   MYSQL_PASSWORD = 'luis123'
   MYSQL_DB = 'cursos'

config = {

    'development' : DevelopmentConfig
}
    

 