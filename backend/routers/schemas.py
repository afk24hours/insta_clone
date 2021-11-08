from pydantic import BaseModel
from datetime import datetime
from typing import List

# USER BASE
class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    class Config():
        orm_mode = True


# INSTAGRAM POSTS
class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int

class User(BaseModel): # USER FOR INSTA POST
    username: str
    class Config():
        orm_mode = True

class Comment(BaseModel): # COMMENT FOR POST DISPLAY
    text: str
    username: str
    timestamp: datetime
    class Config():
        orm_mode = True

class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comments: List[Comment]
    class Config():
        orm_mode = True


# USER AUTH
class UserAuth(BaseModel):
    id: int
    username: str
    email: str

# COMMENT BASE
class CommentBase(BaseModel):
    username: str
    text: str
    post_id: int