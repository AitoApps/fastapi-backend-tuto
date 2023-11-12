from enum import Enum
from typing import Optional
from beanie import Document, PydanticObjectId


class PostType(str, Enum):
    post: str = "post"
    repost: str = "repost"
    reply: str = "reply"


class Post(Document):
    text: str
    user_id: PydanticObjectId
    type: PostType
    originalPostId: Optional[PydanticObjectId]

    class Settings:
        name = "posts"
