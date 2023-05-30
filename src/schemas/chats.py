from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ChatBase(BaseModel):
    message: Optional[str] = None


class ChatIn(ChatBase):
    sender_id: int
    receiver_id: int


class ChatOut(ChatIn):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class ChatUpdate(ChatBase):
    pass
