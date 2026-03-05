from pydantic import BaseModel
from typing import Optional

class SearchParam(BaseModel):
    name:str
    limit:int
    skip: Optional[int] = None
    