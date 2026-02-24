from fastapi import FastAPI
from app.db.database import engine, Base
from app.models import user_model
from app.routers.auth_router import router as auth_router
from app.routers.user_router import router as user_router

app = FastAPI()   # ⭐ FIRST create app

Base.metadata.create_all(bind=engine)

# ⭐ THEN include routers
app.include_router(auth_router)
app.include_router(user_router)


@app.get("/")
def root():
    return {"message": "Backend Running 🚀"}