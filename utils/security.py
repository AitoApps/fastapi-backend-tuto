from passlib.context import CryptContext


class Password:
    pwd_context = CryptContext(schemes=["bcrypt"])

    @classmethod
    def hash_password(self, *, password: str):
        return self.pwd_context.hash(password)
