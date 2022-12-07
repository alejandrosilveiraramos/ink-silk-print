# --- Imports: ---
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from fastapi import HTTPException

from sqlalchemy.orm import validates


# --- Create a Postgres engine instance ---
engine = create_engine("postgresql+psycopg2://ink-silk-print:123456@localhost:5432/postgres") 

# --- Create a declarativeMeta instance ---
Base = declarative_base()
 
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
  
    
"""
    # Validates to not insert empty Values
    
    @validates('name')
    def validate_name(self, key, value):
        if value == '':
            raise HTTPException(status_code=404, detail="Item not found")
        return value
    
    @validates('recipe')
    def validate_recipe(self, key, value):
        if value == '':
            raise ValueError('Recipe cannot be empty')
        return value
"""    
    
    
"""
    --- CheckConstraint way ---
    from sqlalchemy.schema import CheckConstraint
    
    I need to study the Constraint 
         
      __table_args__ = (
        CheckConstraint('name =! None'),
    )
    
   """
""" 
    --- Validator using @validates ---
    from sqlalchemy.orm import validates
    

    
       @validates("recipe")
    def validate_recipe(self, key, colors):
        if "@" not in colors:
            raise ValueError("Error: Failed recipe None validation")
        return colors
        
    Not null not working?
    
        @validates("name")
    def validates_name(self, id, colors):
        if "@" not in colors:
            raise ValueError("Not exist @ in the Name")
        return colors
"""