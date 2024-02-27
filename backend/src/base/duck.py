import datetime
from dataclasses import dataclass


@dataclass
class Duck:
    name: str
    age: int
    address: str
    favorite_pond: str
    duck_created: datetime.datetime
    duck_updated: datetime.datetime

