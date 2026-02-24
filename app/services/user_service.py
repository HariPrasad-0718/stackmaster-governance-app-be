from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user_model import User
from app.core.security import verify_password, create_token, hash_password
import uuid
from datetime import datetime


# ---------------- LOGIN ---------------- #

def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    token = create_token({
        "user_id": str(user.user_id),
        "role": user.role
    })

    return {
        "access_token": token,
        "role": user.role,
        "user_id": str(user.user_id)
    }


# ---------------- CREATE USER ---------------- #

def create_user(db: Session, data):

    # ⭐ ROLE NORMALIZATION (UI → DB safe values)
    role_map = {
        "Admin": "admin",
        "POD Lead": "pod_lead",
        "POD Member": "pod_member",
        "admin": "admin",
        "pod_lead": "pod_lead",
        "pod_member": "pod_member"
    }

    normalized_role = role_map.get(data.role)

    if not normalized_role:
        raise HTTPException(status_code=400, detail="Invalid role value")

    # ⭐ Pod member must have reporting manager
    if normalized_role == "pod_member" and not data.reporting_manager_id:
        raise HTTPException(status_code=400, detail="Pod member must have reporting manager")

    user = User(
        user_id=uuid.uuid4(),
        name=data.name,
        email=data.email,
        password=hash_password(data.password),
        role=normalized_role,
        reporting_manager_id=data.reporting_manager_id,
        is_active=True,
        created_at=datetime.utcnow()
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user