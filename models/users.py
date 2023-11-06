from beanie import Document, Indexed


class User(Document):
    # class DocumentMeta:
    #     collection_name = "users"

    name: str
    username: Indexed(str, unique=True)
    email: Indexed(str, unique=True)
    hashed_password: str
