# 🎯 API CRUD FastAPI - Ejercicio Completado

## 📋 Descripción
API CRUD completa implementada con FastAPI que incluye todas las operaciones básicas:
- ✅ **CREATE** (POST) - Crear nuevos items
- ✅ **READ** (GET) - Leer items (todos y por ID)
- ✅ **UPDATE** (PUT) - Actualizar items existentes
- ✅ **DELETE** (DELETE) - Eliminar items

## 🚀 Cómo ejecutar

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar la aplicación
```bash
uvicorn app.main:app --reload
```

### 3. Acceder a la documentación
Abrir en el navegador: `http://localhost:8000/docs`

## 📚 Endpoints disponibles

### Items
- `GET /api/v1/items/` - Obtener todos los items
- `GET /api/v1/items/{item_id}` - Obtener un item por ID
- `POST /api/v1/items/` - Crear un nuevo item
- `PUT /api/v1/items/{item_id}` - Actualizar un item por ID
- `DELETE /api/v1/items/{item_id}` - Eliminar un item por ID

### Otros endpoints
- `GET /` - Endpoint raíz
- `GET /health` - Verificación de salud

## 🧪 Ejemplos de uso

### Crear un item
```bash
curl -X POST "http://localhost:8000/api/v1/items/" \
     -H "Content-Type: application/json" \
     -d '{"name": "Laptop", "price": 999.99}'
```

### Actualizar un item
```bash
curl -X PUT "http://localhost:8000/api/v1/items/1" \
     -H "Content-Type: application/json" \
     -d '{"name": "Laptop Gaming", "price": 1299.99}'
```

### Eliminar un item
```bash
curl -X DELETE "http://localhost:8000/api/v1/items/1"
```

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
