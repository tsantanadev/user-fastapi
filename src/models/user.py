from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

from src.models.gender import Gender
from src.models.role import Role


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]
