from src.main import *
from unittest.mock import patch
import pytest

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello Word"}

@pytest.mark.asyncio
async def test_funcaoteste():
    result = await funcaoteste() 
    assert result == {"teste": "deu certo", "num_aleatorio": result["num_aleatorio"]}  

@pytest.mark.asyncio
async def test_funcaoteste2():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()  
    assert result == {"teste": "deu certo", "num_aleatorio": 12345}

@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result

async def update_estudante(id_estudante):
    if id_estudante > 0:
        return True  
    return False  

async def delete_estudante(id_estudante):
    if id_estudante > 0:
        return True  
    return False  

@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(5)
    assert result
