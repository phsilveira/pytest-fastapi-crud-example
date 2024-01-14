from datetime import datetime
from typing import List
from pydantic import BaseModel
from typing import Optional


class UserBaseSchema(BaseModel):
    id: Optional[str] = None
    first_name: str
    last_name: str
    address: Optional[str] = None
    activated: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListUserResponse(BaseModel):
    status: str
    results: int
    users: List[UserBaseSchema]
