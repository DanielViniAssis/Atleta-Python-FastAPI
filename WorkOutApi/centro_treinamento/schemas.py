from typing import Annotated
from pydantic import UUID4, Field
from WorkOutApi.contrib.schemas import BaseSchemas


class CentroTreinamentoIn(BaseSchemas):
    nome: Annotated[str, Field(description='Nome do CT', example='Campo Do Brasil', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do CT', example='Rua x, Q02', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do CT', example='Maeco', max_length=30)]

class CentroTreinamento(BaseSchemas):
    nome: Annotated[str, Field(description='Nome do CT', example='Campo Do Brasil', max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador do Centro de Treinamento")]