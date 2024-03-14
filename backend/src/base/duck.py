import datetime
from typing import Optional
from pydantic import BaseModel


class Duck(BaseModel):
    name: str
    age: int
    address: str
    favorite_pond: str
    duck_created: Optional[datetime.datetime] = None
    duck_updated: Optional[datetime.datetime] = None
