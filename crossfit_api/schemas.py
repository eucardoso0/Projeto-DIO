from pydantic import BaseModel

class CategoriaBaseSchema(BaseModel):
    nome: str

class CategoriaCreateSchema(CategoriaBaseSchema):
    pass

class CategoriaSchema(CategoriaBaseSchema):
    id: int

    class Config:
        orm_mode = True

class AtletaBaseSchema(BaseModel):
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str
    centro_treinamento: str
    categoria_id: int

class AtletaCreateSchema(AtletaBaseSchema):
    pass

class AtletaSchema(AtletaBaseSchema):
    id: int

    class Config:
        orm_mode = True

class CategoriaBaseBaseSchema(BaseModel):
    nome: str
    endereco: str
    proprietario: str

class CategoriaBaseCreateSchema(CategoriaBaseBaseSchema):
    pass

class CategoriaBaseSchema(CategoriaBaseBaseSchema):
    id: int

    class Config:
        orm_mode = True
