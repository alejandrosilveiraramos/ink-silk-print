# --- Imports: ---
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session, validates

from core.models.database import engine, Base, Color

class ColorRequest(BaseModel):
    name: str
    recipe: str
    

# --- Create the database ---
Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def root():
    return {'Massage: ROOT - Color System On'}

# --- Create Color ---
@app.post("/colors", status_code=status.HTTP_201_CREATED)
def create_color(color: ColorRequest):
    
    #Create a new database Session
    session = Session(bind=engine, expire_on_commit=False)
    
    #Create an instance of the Color database model
    colordb = Color(name = color.name, recipe = color.recipe)
    

    
    #Add it to session and commit it
    session.add(colordb)
    session.commit()
    
    #Grab the id given to the object from the database
    id = colordb.id 
    
    #Close the session
    session.close()
    
    #Return the id, name and recipe
    return f"Create Color | ID: {id} | NAME: {colordb.name} | RECIPE: {colordb.recipe}"

# --- Read Color ---
@app.get("/colors/{id}")
def read_color(id: int):
    return "Read Color"
    
# --- Update Color ---
@app.put("/colors/{id}")
def update_color(id: int):
    return "Update Color"

# --- Delete Color ---
@app.delete("/colors/{id}")
def delete_color(id: int):
    return "Delete Color"


# --- Raed All Colors ---
@app.get("/read-all-colors")
def read_all_colors():
    return "All Colors"
