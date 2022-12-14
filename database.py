# --- Imports: ---
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- Create a Postgres engine instance ---
engine = create_engine("postgresql+psycopg2://ink-silk-print:123456@localhost:5432/postgres") 

# --- Create a declarativeMeta instance ---
Base = declarative_base()

# Create a SessionLocal class from sessionmaker factory
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
 
