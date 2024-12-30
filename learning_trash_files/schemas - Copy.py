from enum import Enum
from pydantic import BaseModel


class XFlag(Enum):
    green = "green"
    red = "red"


class MessageSchema(BaseModel):
    message: str
