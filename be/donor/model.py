import uuid
from uuid import UUID
from typing import Optional, Dict
from pydantic import BaseModel, Field, Json

class donorCreate(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4, alias="_id")
    donor_name: str = Field(...)
      
class donorUpdate(BaseModel):
    donor_name: Optional[str]= None
