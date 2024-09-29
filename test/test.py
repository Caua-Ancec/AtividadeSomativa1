from src.main import *
from unittest.mock import patch

def test_root():
    assert root() == {"message": "Hello Word"}

def test_funcaoteste():
    assert root() == {"teste": "deu certo"}

def test_funcaoteste2():
    with patch('random.randint', return_value=12345):
        result = funcaoteste()  # Certifique-se de que isso chama a função
    assert result == {"teste": True, "num_aleatorio": 12345}  # Não precisa de parênteses aqui

def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    result = create_estudante(estudante_teste)
    assert estudante_teste == result  # Verifica se o estudante foi criado corretamente

def update_estudante(id_estudante):
    if id_estudante > 0:
        return True  
    return False  

def delete_estudante(id_estudante):
    if id_estudante > 0:
        return True  
    return False  

def test_update_estudante_negativo():
    assert not update_estudante(-5)  

def test_update_estudante_positivo():
    assert update_estudante(10)  

def test_delete_estudante_negativo():
    assert not delete_estudante(-5)  

def test_delete_estudante_positivo():
    assert delete_estudante(5)