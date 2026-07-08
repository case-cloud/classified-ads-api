from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CategoryBase(BaseModel):
    name: str
    slug: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: str
    phone: Optional[str] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class AdBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: Optional[int] = None
    location: Optional[str] = None
    category_id: int


class AdCreate(AdBase):
    pass


class AdUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    location: Optional[str] = None
    category_id: Optional[int] = None
    is_active: Optional[bool] = None


class Ad(AdBase):
    id: int
    author_id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    category: Category
    author: User

    class Config:
        from_attributes = True