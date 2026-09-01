# API de Gestión de Productos (`tp-productos-api`)

## Descripción
Esta API RESTful desarrollada con **FastAPI** permite la gestión e interacción con productos y categorías. Utiliza `@dataclass` para los modelos del dominio y **Pydantic** para la validación y esquematización de las peticiones y respuestas HTTP.

---

## Integrantes del Grupo

| Nombre y Apellido | Usuario de GitHub |
| :---------------- | :---------------- |
| Integrante 1      | [@usuario1](https://github.com/usuario1) |
| Integrante 2      | [@usuario2](https://github.com/usuario2) |

---

## Estructura del Proyecto

```text
tp-productos-api/
├── app/
│   ├── main.py                   # Inicialización de FastAPI e inclusión de routers
│   ├── core/
│   │   └── db.py                 # Simulación de BD (listas de categorías y productos)
│   ├── models/
│   │   ├── categoria.py          # @dataclass Categoria
│   │   └── producto.py           # @dataclass Producto
│   └── api/
│       └── v1/
│           └── productos/
│               ├── router.py     # Endpoints HTTP para /productos (APIRouter)
│               ├── schemas.py    # Esquemas de Pydantic (Base, Create, Update, Response)
│               └── repository.py # Capa de acceso a datos y validaciones de negocio
├── .gitignore                    # Reglas de exclusión para Git (venv, __pycache__)
├── README.md                     # Documentación del proyecto
└── requirements.txt              # Dependencias del proyecto