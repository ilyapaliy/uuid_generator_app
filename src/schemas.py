from enum import Enum
from pydantic import BaseModel
from uuid import UUID


class XFlag(Enum):
    green = "green"
    red = "red"


class UUIDResponse(BaseModel):
    uuid: UUID


class AMQPMessage(BaseModel):
    uuid: UUID
    xflag: XFlag

    def to_log_message(self):
        return(f"UUID: {self.uuid} - X-Flag: {self.xflag}")
