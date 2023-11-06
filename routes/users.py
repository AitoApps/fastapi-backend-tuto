from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from models.users import User

from schema.users import UserCreate, UserOut
from utils.security import Password

router = APIRouter(prefix="/users", tags=["user"])


@router.post("/signup")
async def signup(user_data: UserCreate):
    exist = await User.find_one(User.email == user_data.email)
    if exist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="user with that email already exist")
    hashed_password = Password.hash_password(password=user_data.password)
    user: User = await User(email=user_data.email, hashed_password=hashed_password,
                            name=user_data.name, username=user_data.username).insert()
    content = UserOut(email=user.email, name=user.name, username=user.username)

    return content

    # return JSONResponse(
    #     content=UserOut(email=user.email, name=user.name, username=user.username), status_code=status.HTTP_201_CREATED
    # )
