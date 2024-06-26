from datetime import datetime
from typing import Annotated
from pydantic import UUID4, BaseModel, Field


class BaseSchemas(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True

class OutMixin(BaseSchemas):
    id: Annotated[UUID4, Field(description="Identificador")]
    creat_at: Annotated[datetime, Field(description="Data da Criação")] 