from sqlalchemy import create_engine
from locacao.util.util import Utilidades
from locacao.repositorios.repositorio_locadora import RepositorioLocadora
from locacao.repositorios.repositorio_pessoa import RepositorioPessoa
from locacao.repositorios.repositorio_veiculo import RepositorioVeiculo
from locacao.repositorios.repositorio_usuario import RepositorioUsuario
from locacao.autenticacao.autenticacao import Autenticador
from fastapi.security import OAuth2PasswordBearer

_autenticador = Autenticador(**Utilidades.obter_chaves()) 

esquema_oauth2 = OAuth2PasswordBearer(token_URL='v1/autenticacao/login')

sqlalchemy_engine = create_engine(Utilidades.obter_connection_string(), echo=True)

repositorio_locadora = RepositorioLocadora(sqlalchemy_engine)
repositorio_pessoa = RepositorioPessoa(sqlalchemy_engine)
repositorio_veiculo = RepositorioVeiculo(sqlalchemy_engine)
repositorio_usuario = RepositorioUsuario(sqlalchemy_engine)

obter_repositorio_locadora = lambda: repositorio_locadora
obter_repositorio_pessoa = lambda: repositorio_pessoa
obter_repositorio_veiculo = lambda: repositorio_veiculo
obter_repositorio_usuario = lambda: repositorio_usuario

autenticador = lambda: _autenticador
