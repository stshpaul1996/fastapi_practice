from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProductIn(BaseModel):
    name : str
    cost : int
    manufacture : str
    created_at : datetime
    brand : Optional[bool] = False

class ProductOut(BaseModel):
    id: int
    name : str
    cost : int


    class Config:
        orm_mode = True
  