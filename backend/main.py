from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.usuarios import router as usuarios_router

app = FastAPI(title="API AquiEstoy")

# Orígenes desde los que se sirve el frontend en desarrollo (Live Server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios_router)


@app.get("/")
def inicio():
    return {"mensaje": "API AquiEstoy funcionando correctamente."}