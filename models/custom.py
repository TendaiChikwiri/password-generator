from pydantic import BaseModel


class CustomPassword(BaseModel):
    length: int
    symbols: bool
    numbers: bool
    letters: bool
