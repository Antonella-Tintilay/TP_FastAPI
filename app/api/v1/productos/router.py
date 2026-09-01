from fastapi import APIRouter, HTTPException, Query, status
from . import repository as repo
from .schemas import ProductoResponse,ProductoCreate,ProductoUpdate
router = APIRouter(prefix="/productos",tags=["Productos"])

@router.get("/",response_model=list[ProductoResponse])
def listar(
    query:str | None = Query(default=None,description="Buscar por nombre"),
    categoria_id: int | None = Query(default=None,ge=1,descritpion="Filtrar por categoria")
):
    """ Listar productos """
    resultado = repo.list_productos()
    if query:
        resultado = repo.search_by_nombre(query)
    if categoria_id is not None:
        resultado = [p for p in resultado if p["categoria"] and p["categoria"]["id"] == categoria_id]

    return resultado

@router.get("/{producto_id}",response_model=ProductoResponse)
def obtener(producto_id:int):
    producto = repo.get_by_id(producto_id)
    if producto is None:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/",response_model=ProductoResponse,status_code = status.HTTP_201_CREATED)
def crear(data:ProductoCreate):
    ok, error = repo.ensure_categoria(data.categoria_id)
    if not ok:
        raise HTTPException(status_code=400, detail=error)
    return repo.create(data)

@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar(producto_id: int, data: ProductoUpdate):
    # Si cambia la carrera o las materias, validamos que existan
    if data.categoria_id is not None:
        actual = repo.get_by_id(producto_id)
        if actual is None:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        cid = data.categoria_id if data.categoria_id is not None else actual["categoria"].id
        ok, error = repo.ensure_categoria(cid)
        if not ok:
            raise HTTPException(status_code=400, detail=error)

    updated = repo.update(producto_id, data)
    if updated is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated


@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(producto_id: int):
    if not repo.delete(producto_id):
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return None