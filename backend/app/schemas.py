from pydantic import BaseModel
from typing import Optional


class ApplicationBase(BaseModel):
    company: str
    position: str
    status: str = "Pendiente"
    notes: Optional[str] = None


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationUpdate(BaseModel):
    company: Optional[str] = None
    position: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None


class ApplicationResponse(ApplicationBase):
    id: str
    created_at: str
