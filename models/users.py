from typing import List, Optional
from beanie import BackLink, Document, Indexed, Link
from pydantic import Field
from utils.security import Password
from utils.jwt import generate_jwt


class User(Document):
    name: str
    username: Indexed(str, unique=True)
    email: Indexed(str, unique=True)
    hashed_password: str

    class Settings:
        name = "users"

    @classmethod
    async def get_by_email(self, *, email: str):
        return await self.find_one(self.email == email)

    @classmethod
    async def get_by_username(self, *, username: str):
        return await self.find_one(self.username == username)

   # This is a class method for user authentication.
    # It is used to verify user credentials based on their email and password.

    @classmethod
    async def authenticate(cls, *, email: str, password: str):
        """
            This is a class method for user authentication.
            It verifies user credentials based on their email and password.
        """
        # Retrieve a user by their email address from the database.
        user: User = await cls.get_by_email(email=email)

        # Check if the user was found or if the provided password matches the stored hashed password.
        if not user or not Password.verify_password(password=password, hashed_password=user.hashed_password):
            # If either condition is not met, return None to indicate authentication failure.
            return None

        # If both conditions are met, return the authenticated user.
        return user

    def generate_token(self):
        payload = {
            "sub": str(self.username),
        }

        return generate_jwt(data=payload)
