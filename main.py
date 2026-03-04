from fastapi import FastAPI
from sqlalchemy import text
from database import engine

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI Backend Running", "developer": "Harish Jangam"}

@app.get("/db")
def check_database():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        db_version = result.fetchone()

    return {"database": str(db_version)}
