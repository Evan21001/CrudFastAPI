from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    """Base model for Item with common fields"""
    name: str
    price: float


class ItemCreate(ItemBase):
    """Model for creating a new item"""
    pass


class ItemUpdate(BaseModel):
    """Model for updating an item"""
    name: str
    price: float


class Item(ItemBase):
    """Complete Item model with ID"""
    id: int

    class Config:
        from_attributes = True
