from enum import Enum
from typing import Literal


user.role = "admin"

class Role(Enum):
    ADMIN = "admin"
    USER = "user"
    
------------------------
def priceing(currecy: Literal["USD", "EUR"]):
    pass

------------------------
def process(obj: SomeClass):
    assert isinstance(obj, SomeClass)