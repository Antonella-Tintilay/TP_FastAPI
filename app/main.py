from fastapi import FastAPI
from app.api.v1.productos.router import router as productos_router

app = FastAPI(title="IES Connect API")

@app.get("/")
def home():
    return {"mensaje": "Bienvenidos a la API de IES Connect"}

app.include_router(productos_router)
