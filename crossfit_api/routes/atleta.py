from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Atleta
from schemas import AtletaCreateSchema, AtletaSchema
from database import get_db

router = APIRouter()

@router.post("/", response_model=AtletaSchema)
async def criar_atleta(atleta: AtletaCreateSchema, db: AsyncSession = Depends(get_db)):
    novo_atleta = Atleta(**atleta.dict())
    db.add(novo_atleta)
    await db.commit()
    await db.refresh(novo_atleta)
    return novo_atleta

@router.get("/", response_model=list[AtletaSchema])
async def listar_atletas(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Atleta))
    atletas = result.scalars().all()
    return atletas
