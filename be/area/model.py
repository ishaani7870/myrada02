import uuid
from uuid import UUID
from typing import Optional, Dict
from pydantic import BaseModel, Field, Json

class areaCreate(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4, alias="_id")
    area_name: str = Field(...)
      
class areaUpdate(BaseModel):
    area_name: Optional[str]= None
