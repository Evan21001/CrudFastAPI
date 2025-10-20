 Descripción
API CRUD completa implementada con FastAPI que incluye todas las operaciones básicas:
- ✅ **CREATE** (POST) - Crear nuevos items
- ✅ **READ** (GET) - Leer items (todos y por ID)
- ✅ **UPDATE** (PUT) - Actualizar items existentes
- ✅ **DELETE** (DELETE) - Eliminar items

Crear un item (POST):
<img width="598" height="750" alt="image" src="https://github.com/user-attachments/assets/3a2e44cb-e856-43b8-bd43-63014643397e" />

Actualizar el item (PUT):
<img width="521" height="701" alt="image" src="https://github.com/user-attachments/assets/126ca8df-2cd2-4889-a4b9-00544e90939c" />

Eliminar el item (DELETE):
<img width="608" height="691" alt="image" src="https://github.com/user-attachments/assets/61aaa680-a8bb-4475-868d-5b952e3d4103" />

## 📁 Estructura del proyecto
```
CrudFastAPI/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── item.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── memory_db.py
│   └── api/
│       ├── __init__.py
│       └── routes/
│           ├── __init__.py
│           └── items.py
├── requirements.txt
└── README.md
```

## ✅ Funcionalidades implementadas

- [x] Modelo `ItemUpdate` para validación de datos PUT
- [x] Función `update_item_by_id()` en la base de datos
- [x] Función `delete_item_by_id()` en la base de datos
- [x] Endpoint PUT `/api/v1/items/{item_id}`
- [x] Endpoint DELETE `/api/v1/items/{item_id}`
- [x] Manejo de errores 404 para items no encontrados
- [x] Documentación automática con Swagger UI
- [x] Validación de datos con Pydantic
- [x] Base de datos en memoria para simulación

## 🎉 ¡Ejercicio completado!
La API CRUD está completamente funcional con todas las operaciones implementadas.
