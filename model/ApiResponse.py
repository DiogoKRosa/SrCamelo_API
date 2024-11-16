from pydantic import BaseModel 
from typing import List, Dict, Union

class APIResponse(BaseModel):
    status: int
    message: str
    data: Union[List[dict], dict] | None = None