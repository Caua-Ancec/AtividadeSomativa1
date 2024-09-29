import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool

@app.get("/helloword")
async def root():
    return {"message": "Hello Word"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": "deu certo"}

@app.get("/funcaoteste2")
async def funcaoteste2():
    return {"teste": True, "num_aleatorio": random.randint(0,2000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_item(id_estudante: int):
    return id_estudante > 0

@app.delete("estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0