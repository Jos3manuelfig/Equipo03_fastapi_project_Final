# schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class TransaccionBase(BaseModel):
    t_fecha: datetime
    t_monte: Decimal
    t_montr: Decimal
    t_descrip: str
    t_estado: str
    id_user: int
    id_tasa: int
    id_emisor: int
    id_receptor: int
    id_pais: int

class TransaccionCreate(TransaccionBase):
    pass

class TransaccionUpdate(BaseModel):
    t_fecha: Optional[datetime] = None
    t_monte: Optional[Decimal] = None
    t_montr: Optional[Decimal] = None
    t_descrip: Optional[str] = None
    t_estado: Optional[str] = None
    id_user: Optional[int] = None
    id_tasa: Optional[int] = None
    id_emisor: Optional[int] = None
    id_receptor: Optional[int] = None
    id_pais: Optional[int] = None

