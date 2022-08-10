from pydantic import BaseModel
from typing import Optional


class ScriptInputData(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None
