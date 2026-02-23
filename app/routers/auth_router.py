from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user_schema import LoginRequest
from app.services.user_service import login_user

router = APIRouter(prefix="/api/auth", tags=["Auth"])

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    try:
        return login_user(db, data.email, data.password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))