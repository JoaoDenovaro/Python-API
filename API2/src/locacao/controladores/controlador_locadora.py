from fastapi import HTTPException, status, Depends
from typing import List, Optional, Annotated
from locacao.viewmodels.vms_locadora import *
from locacao.repositorios.repositorio_locadora import RepositorioLocadora
from locacao.controladores.controlador_base import ControladorBase
from locacao.util.util import Utilidades
from locacao.dependencias.singletons import obter_repositorio_locadora  

class ControladorLocadora(ControladorBase):
    
    def __init__(self) -> None:
        self.endpoints = [self.listar_locadoras]
    
    async def listar_locadoras(self, 
        repo : Annotated[RepositorioLocadora, Depends(obter_repositorio_locadora)],
        nome: Optional[str] = None,
        horario_abertura: Optional[str] = None,
        horario_fechamento: Optional[str] = None,
        endereco: Optional[str] = None) -> List[VMLocadora]:

        encontrados = repo.filtrar(nome=nome, horario_abertura=horario_abertura,
                                horario_fechamento=horario_fechamento,
                                endereco=endereco)
        return list(map(VMLocadora.converter_modelo, encontrados))
    listar_locadoras.rota = {'path': '/locadora/', 'methods': ['GET']}
        