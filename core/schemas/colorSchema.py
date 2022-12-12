from pydantic import BaseModel


class ColorCreate(BaseModel):
    name: str
    recipe: str

class Color(BaseModel):
    id: int
    name: str
    recipe: str
    
    class Config:
        orm_mode = True
        

  
    