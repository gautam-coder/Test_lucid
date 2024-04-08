from fastapi import APIRouter, Depends
from data_base import get_session,sessionmaker
from models import User
from schemas import UserCreate
from utils import verify_password, create_access_token

router = APIRouter()

@router.post("/signup")
async def signup(user_data: UserCreate,session: sessionmaker=Depends(get_session)):
    # Hash password before saving
    hashed_password = verify_password(user_data.password, None)

    # Create new user object
    new_user = User(email=user_data.email, password=hashed_password)

    session.add(new_user)
    session.commit()

    # Generate access token on successful signup
    access_token = create_access_token(data={"sub": new_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
