from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user_schema import CreateUser
from app.services.user_service import create_user
from app.db.database import get_db

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.post("")
def add_user(data: CreateUser, db: Session = Depends(get_db)):
    user = create_user(db, data)
    return {"message": "User created", "user_id": str(user.user_id)}