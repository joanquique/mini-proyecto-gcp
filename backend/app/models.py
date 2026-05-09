from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    position = Column(String, nullable=False)
    status = Column(String, default="Pendiente")
    notes = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)