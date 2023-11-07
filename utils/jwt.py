from fastapi import HTTPException
from jose import jwt, JWTError
from pydantic import SecretStr
from config.settings import settings
from datetime import datetime, timedelta


def _get_secret_value(secret: SecretStr) -> str:
    if isinstance(secret, SecretStr):
        return secret.get_secret_value()
    return secret


def generate_jwt(data: dict, secret: str | SecretStr = settings.SECRET_KEY, lifetime_minutes: int = settings.JWT_EXPIRE_MINUTES, algorithm: str = settings.JWT_ALGORITHM) -> str:
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=lifetime_minutes)
    payload["exp"] = expire
    return jwt.encode(payload, _get_secret_value(secret), algorithm=algorithm)


def decode_jwt(encoded_jwt: str, secret: str | SecretStr = settings.SECRET_KEY, algorithm: str = settings.JWT_ALGORITHM) -> dict[str, any]:
    return jwt.decode(encoded_jwt, _get_secret_value(secret), algorithms=algorithm)


def get_jwt_subject(token: str) -> str:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        print("token", token)
        payload: dict[str, any] = decode_jwt(encoded_jwt=token)
        subject: str = payload.get("sub")
        if subject is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return subject
