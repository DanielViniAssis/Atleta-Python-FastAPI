from uuid import uuid4
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class BaseModel(DeclarativeBase):
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False)
