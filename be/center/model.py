import uuid
from uuid import UUID
from typing import Optional, Dict
from pydantic import BaseModel, Field, Json

class centerCreate(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4, alias="_id")
    center_name: str = Field(...)
      
class centerUpdate(BaseModel):
    center_name: Optional[str]= None
