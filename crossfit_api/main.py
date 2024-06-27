from fastapi import FastAPI
from routes import categoria, atleta, categoria_base
from database import engine, Base

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(categoria.router, prefix="/categorias", tags=["Categorias"])
app.include_router(atleta.router, prefix="/atletas", tags=["Atletas"])
app.include_router(categoria_base.router, prefix="/categorias_base", tags=["Categorias Base"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
