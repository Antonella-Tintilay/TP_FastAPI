from app.models.categoria import Categoria
from app.models.producto import Producto
#tabla categorias

categoria : list[Categoria] = [
    Categoria(id=1,nombre="Electrónica"),
    Categoria(id=2,nombre="Hogar"),
    Categoria(id=3,nombre="Libreria")
]

#tabla productos

productos: list[Producto] = [
    Producto(id=1,nombre="Computadora",precio=800500.25,stock=20,categoria_id=1,activo=True),
    Producto(id=2,nombre="Tablet",precio=329500.25,stock=10,categoria_id=1,activo=True),
    Producto(id=3,nombre="Camara Web",precio=59500.25,stock=12,categoria_id=1,activo=True),
    Producto(id=4,nombre="Cama 2 1/2",precio=259500.99,stock=10,categoria_id=2,activo=True),
    Producto(id=5,nombre="Ropero de Cedro",precio=500500.98,stock=8,categoria_id=2,activo=True),
    Producto(id=6,nombre="Resma A4 70gr.",precio=6500.49,stock=50,categoria_id=3,activo=True)
]

_next_id: int = 7

def bump_producto_id() -> int:
    global _next_id
    nid = _next_id
    _next_id += 1
    return nid