# --- Imports: ---
from fastapi import FastAPI, status, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal

from core.models import colorModelDB
from core.schemas import colorSchema

# --- Create the database ---
Base.metadata.create_all(engine)

app = FastAPI()

# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/")
def root():
    return {'Massage: ROOT - Color System On'}

# --- Create Color ---
@app.post("/colors", response_model=colorSchema.Color,status_code=status.HTTP_201_CREATED)
def create_color(color: colorSchema.ColorCreate, session: Session = Depends(get_session)):
    
    #Create an instance of the Color database model
    colordb = colorModelDB.Color(name = color.name, recipe = color.recipe)
    
    #Add it to session and commit it
    session.add(colordb)    
    session.commit()
    session.refresh(colordb)
    
    #Return the id, name and recipe
    return colordb

# --- Read Color ---

@app.get("/colors/{id}", response_model = colorSchema.Color)
def read_color(id: int, session: Session = Depends(get_session)):
    
    #Get the Color item by the given ID
    color = session.query(colorModelDB.Color).get(id)
    
    #HTTP code Status to check if ID does'nt exist
    if not color:
        raise HTTPException(status_code=404, detail="Color ID doesn't exist")
    #Returning (Color): ID, Name and Recipe 
    return color

    
# --- Update Color ---
@app.put("/colors/{id}")
def update_color(id: int, name: str, session: Session = Depends(get_session)):
    
    # Get the Color item with the given id
    color = session.query(colorModelDB.Color).get(id)

    # Update Color item with the given Name (if an item with the given id was found)
    if color:
        color.name = name
        session.commit()


    # Check if Color item with given id exists. If not, raise exception and return 404 not found response
    if not color:
        raise HTTPException(status_code=404, detail="The ID Color do not exist")
    

    return color
 

# --- Delete Color ---
@app.delete("/colors/{id}")
def delete_color(id: int, session: Session = Depends(get_session)):
    
    #Get the color by given ID
    color = session.query(colorModelDB.Color).get(id)
    
    # If color match Delete the Color by the given ID // Raise 404 Erro not exist
    if color:
        session.delete(color)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail="The ID Color do not exist")
    
    return None


# --- Raed All Colors ---
@app.get("/read-all-colors", response_model = List[colorSchema.Color])
def read_all_colors(session: Session = Depends(get_session)):
    
    #Get all Color Items
    color_list = session.query(colorModelDB.Color).all()
    
    #Close the session
    session.close()
    
    return color_list
