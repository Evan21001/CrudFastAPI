from typing import List, Optional
from app.models.item import Item, ItemCreate, ItemUpdate

# In-memory database simulation
items_db: List[Item] = []
next_id = 1


def get_items_db() -> List[Item]:
    """Obtener todos los items"""
    return items_db


def add_item(item: ItemCreate) -> Item:
    """Agregar un nuevo item"""
    global next_id
    new_item = Item(id=next_id, name=item.name, price=item.price)
    items_db.append(new_item)
    next_id += 1
    return new_item


def get_item_by_id(item_id: int) -> Optional[Item]:
    """Obtener un item por ID"""
    for item in items_db:
        if item.id == item_id:
            return item
    return None


def update_item_by_id(item_id: int, item_update: ItemUpdate) -> Optional[Item]:
    """Actualizar un item por ID"""
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            updated_item = Item(id=item_id, name=item_update.name, price=item_update.price)
            items_db[idx] = updated_item
            return updated_item
    return None


def delete_item_by_id(item_id: int) -> bool:
    """Eliminar un item por ID"""
    global items_db
    original_length = len(items_db)
    items_db = [item for item in items_db if item.id != item_id]
    return len(items_db) < original_length
