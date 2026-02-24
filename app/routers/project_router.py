from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.project_schema import CreateProject
from app.services.project_service import create_project

router = APIRouter(prefix="/api/projects", tags=["Projects"])


@router.post("/")
def add_project(data: CreateProject, db: Session = Depends(get_db)):
    return create_project(db, data)