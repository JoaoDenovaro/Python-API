from dotenv import dotenv_values
from uuid import uuid1
from bcrypt import gensalt, hashpw

class Utilidades(object):

    @staticmethod
    def obter_connection_string():
        ambiente = dotenv_values()
        dialeto = ambiente.get('SQLA_DIALECT')
        driver = ambiente.get('SQLA_DRIVER')
        user = ambiente.get('DB_USER')
        senha = ambiente.get('DB_PASSWORD')
        host = ambiente.get('DB_HOST')
        porta = ambiente.get('DB_PORT')
        nome = ambiente.get('DB_NAME')
        return f'{dialeto}+{driver}://{user}:{senha}@{host}:{porta}/{nome}'
    
    @staticmethod
    def uuid36():
        return str(uuid1())
    
    @staticmethod
    def obter_salt():
        return gensalt()

    @staticmethod
    def hash_senha(senha: str, salt: str):
        return hashpw(senha, salt)
