from pydantic import BaseModel
from typing import List
from datetime import datetime


class Event(BaseModel):
    id: int
    type: str
    detail: str
    timestamp: datetime
    

class Player(BaseModel):
    id: int
    name: str
    events: List[Event] = []

class PlayerCreate(BaseModel):
    name: str      