from pydantic import BaseModel


class Attachment(BaseModel):
    user_id: str
    post_id: str
    mime_type: str
