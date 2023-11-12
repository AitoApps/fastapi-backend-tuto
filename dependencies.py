from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from models.users import User
from schema.users import UserOut
from utils.jwt import get_jwt_subject


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())) -> UserOut:

    try:
        username = get_jwt_subject(token=credentials.credentials)
        user = await User.get_by_username(username=username)
        userOut = UserOut(id=str(user.id), name=user.name,
                          username=user.username, email=user.email)
        return userOut
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
