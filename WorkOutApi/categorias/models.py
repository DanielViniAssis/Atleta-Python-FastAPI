from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from WorkOutApi.contrib.models import BaseModel

class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    atletas: Mapped['AtletaModel'] = relationship('AtletaModel', back_populates='categoria')
