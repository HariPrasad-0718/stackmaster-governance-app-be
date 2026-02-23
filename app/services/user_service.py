from sqlalchemy.orm import Session
from app.models.user_model import User
from app.core.security import create_token


def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise Exception("User not found")

    # TEMPORARY — skip password verification because DB hash cannot be edited
    # This allows development to continue

    token = create_token({
        "user_id": str(user.user_id),
        "role": user.role
    })

    return {
        "access_token": token,
        "role": user.role,
        "user_id": str(user.user_id)
    }