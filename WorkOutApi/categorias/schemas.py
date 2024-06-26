from typing import Annotated
from pydantic import UUID4, Field
from WorkOutApi.contrib.schemas import BaseSchemas


class CategoriaIn(BaseSchemas):
    nome: Annotated[str, Field(description='Nome da Categoria', example='scale', max_length=10)]

class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description="Identificador da categoria")]