from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    created_at: str
