
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, Float, ForeignKey, String, Integer
from WorkOutApi.contrib.models import BaseModel

class AtletaModel(BaseModel):
    __tablename__ = 'atletas'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    creat_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
    categoria: Mapped['CategoriaModel'] = relationship('CategoriaModel', back_populates='atletas', lazy="selectin")
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centros_treinamento.pk_id'))
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship('CentroTreinamentoModel', back_populates='atletas', lazy="selectin")
