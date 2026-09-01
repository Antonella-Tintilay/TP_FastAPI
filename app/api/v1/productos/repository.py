from typing import Optional

from app.core.db import bump_producto_id, categoria as categorias, productos
from app.models.categoria import Categoria
from app.models.producto import Producto
from app.api.v1.productos.schemas import ProductoCreate, ProductoUpdate


# --- Helpers privados -------------------------------------------------

def _find_categoria(categoria_id: int) -> Optional[Categoria]:
    for c in categorias:
        if c.id == categoria_id:
            return c
    return None


def _find_producto(producto_id: int) -> Optional[Producto]:
    for p in productos:
        if p.id == producto_id:
            return p
    return None


def _to_dict(p: Producto) -> dict:
    categoria = _find_categoria(p.categoria_id)
    return {
        "id": p.id,
        "nombre": p.nombre,
        "precio": p.precio,
        "stock": p.stock,
        "activo": p.activo,
        "categoria": {
            "id": categoria.id,
            "nombre": categoria.nombre,
        }
        if categoria is not None
        else None,
    }


# --- Lecturas -----------------------------------------------------------

def list_productos(
    query: Optional[str] = None, categoria_id: Optional[int] = None
) -> list[dict]:
    resultado = productos
    if query:
        resultado = [p for p in resultado if query.lower() in p.nombre.lower()]
    if categoria_id is not None:
        resultado = [p for p in resultado if p.categoria_id == categoria_id]
    return [_to_dict(p) for p in resultado]


def get_by_id(producto_id: int) -> Optional[dict]:
    p = _find_producto(producto_id)
    return _to_dict(p) if p is not None else None


def search_by_nombre(query: str) -> list[dict]:
    coincidencias = [p for p in productos if query.lower() in p.nombre.lower()]
    return [_to_dict(p) for p in coincidencias]


# --- Validaciones ---------------------------------------------------------

def ensure_categoria(categoria_id: int) -> tuple[bool, Optional[str]]:
    if _find_categoria(categoria_id) is None:
        return False, f"La categoria {categoria_id} no existe"
    return True, None


# --- Escrituras -------------------------------------------------------

def create(data: ProductoCreate) -> dict:
    nuevo = Producto(
        id=bump_producto_id(),
        nombre=data.nombre,
        precio=data.precio,
        stock=data.stock,
        categoria_id=data.categoria_id,
        activo=True,
    )
    productos.append(nuevo)
    return _to_dict(nuevo)


def update(producto_id: int, data: ProductoUpdate) -> Optional[dict]:
    producto = _find_producto(producto_id)
    if producto is None:
        return None

    cambios = data.model_dump(exclude_unset=True)
    for campo, valor in cambios.items():
        setattr(producto, campo, valor)

    return _to_dict(producto)


def delete(producto_id: int) -> bool:
    producto = _find_producto(producto_id)
    if producto is None:
        return False
    productos.remove(producto)
    return True