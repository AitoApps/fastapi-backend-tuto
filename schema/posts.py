from enum import Enum
from pydantic import BaseModel


class PostType(str, Enum):
    post: str = "post"
    repost: str = "repost"
    reply: str = "reply"


class PostCreate(BaseModel):
    text: str
    type: PostType
    originalPostId: str
