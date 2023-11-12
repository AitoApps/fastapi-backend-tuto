from typing import Optional
from beanie import Document, PydanticObjectId


class Attachment(Document):
    user_id: PydanticObjectId
    post_id: PydanticObjectId
    mime_type: str

    class Settings:
        name = "attachments"
