from typing import Annotated, Optional
from pydantic import ConfigDict, Field, PositiveFloat

from WorkOutApi.categorias.schemas import CategoriaIn
from WorkOutApi.centro_treinamento.schemas import CentroTreinamentoIn
from WorkOutApi.contrib.schemas import BaseSchemas, OutMixin

class Atleta(BaseSchemas):
    nome: Annotated[str, Field(description='Nome do Atleta', example='Joao', max_length=50)]
    cpf:  Annotated[str, Field(description='CPF do Atleta', example='12345678900', max_length=11)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', example='60.5')]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta', example='1.78')]
    sexo: Annotated[str, Field(description='Sexo do Atleta', example='M', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[CentroTreinamentoIn, Field(description="Centro de Treinamento do atleta")]


class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchemas):
    nome: Annotated[Optional [str], Field(None, description='Nome do Atleta', example='Joao', max_length=50)]
    categoria: Annotated[Optional [CategoriaIn], Field(None, description="Categoria do atleta")]

    model_config = ConfigDict(from_attributes=True)