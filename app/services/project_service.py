from sqlalchemy.orm import Session
from app.models.project_model import Project


def create_project(db: Session, data):
    project = Project(**data.dict())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project