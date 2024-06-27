from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Categoria
from schemas import CategoriaCreateSchema, CategoriaSchema
from database import get_db

router = APIRouter()

@router.post("/", response_model=CategoriaSchema)
async def criar_categoria(categoria: CategoriaCreateSchema, db: AsyncSession = Depends(get_db)):
    nova_categoria = Categoria(**categoria.dict())
    db.add(nova_categoria)
    await db.commit()
    await db.refresh(nova_categoria)
    return nova_categoria

@router.get("/", response_model=list[CategoriaSchema])
async def listar_categorias(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Categoria))
    categorias = result.scalars().all()
    return categorias
