from fastapi import FastAPI
from app.db.database import engine, Base
from app.models import user_model
from app.routers.auth_router import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Backend Running 🚀"}