##################
### User Model ###
##################

from pydantic import BaseModel
from typing import Optional

# User Entity
class User(BaseModel):
    id: Optional[str]
    username: str
    email: str