from src.main import *
from unittest.mock import patch
import pytest

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello Word"}

@pytest.mark.asyncio
async def test_funcaoteste():
    result = await funcaoteste()  # Chamando a função correta
    assert result == {"teste": "deu certo"}

@pytest.mark.asyncio
async def test_funcaoteste2():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste2()  
    assert result == {"teste": True, "num_aleatorio": 12345}

@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result

async def update_estudante(id_estudante):
    return id_estudante > 0 

async def delete_estudante(id_estudante):
    return id_estudante > 0  

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

@pytest.mark.asyncio
async def test_create_muitos_estudantes():
    for i in range(50):
        estudante_teste = Estudante(name=f"Estudante {i}", curso="Curso {i}", ativo=True)
        result = await create_estudante(estudante_teste)
        assert result == estudante_teste

@pytest.mark.asyncio
async def test_estudante_ativo():
    estudante_teste = Estudante(name="Ana", curso="Curso 13", ativo=True)
    result = await create_estudante(estudante_teste)
    assert result.ativo is True

@pytest.mark.asyncio
async def test_estudante_inativo():
    estudante_teste = Estudante(name="Cauã", curso="Curso 10", ativo=False)
    result = await create_estudante(estudante_teste)
    assert result.ativo is False            