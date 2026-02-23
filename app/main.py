from fastapi import FastAPI
from app.db.database import engine, Base
from app.models import user_model

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Backend Running 🚀"}