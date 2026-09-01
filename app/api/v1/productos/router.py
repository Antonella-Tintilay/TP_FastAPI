from typing import Optional
from fastapi import APIRouter, HTTPException
import repository
from schemas import UsuarioCreate, UsuarioLogin, UsuarioResponse

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/registro", response_model=UsuarioResponse, status_code=201)
def registrar_usuario(data: UsuarioCreate):
    if not repository.email_disponible(data.email):
        raise HTTPException(status_code=400, detail="Ya existe una cuenta con este email")
    return repository.create(data)
