
from sqlalchemy import Integer, String, Column
from database import Base

from sqlalchemy.orm import validates 
from fastapi import HTTPException


# --- Create a Color class inheriting from Base ---
class Color(Base):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    recipe = Column(String(256))
    
    @validates('name')
    def validate_name(self, key, value):
        if value == '':
            raise HTTPException(status_code=204, detail="Item: name, cannot be Empty")
        return value
    
    @validates('recipe')
    def validate_recipe(self, key, value):
        if value == '':
            raise HTTPException(status_code=204, detail="Item: recipe, cannot be Empty")
  
