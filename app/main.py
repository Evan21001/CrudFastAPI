from fastapi import FastAPI
from app.api.routes import items

app = FastAPI(
    title="CRUD FastAPI",
    description="API CRUD completa con operaciones CREATE, READ, UPDATE y DELETE",
    version="1.0.0"
)

# Include the items router
app.include_router(items.router, prefix="/api/v1", tags=["items"])


@app.get("/")
def read_root():
    """Endpoint raíz de la API"""
    return {
        "message": "¡Bienvenido a la API CRUD FastAPI!",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
def health_check():
    """Endpoint de verificación de salud"""
    return {"status": "healthy"}
