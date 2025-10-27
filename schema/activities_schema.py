from pydantic import BaseModel
from typing import List

class NumbersIn(BaseModel):
    numbers:List[int]