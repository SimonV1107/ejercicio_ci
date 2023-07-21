"""
Algunos tests para el API de prueba
"""
import pytest
from api import hello_world


@pytest.mark.asyncio
async def test_hello_world_function_returns_a_dict_with_the_given_message():
    """
    Comprueba que la funcion hello_world devuelve correctamente el mensaje enviado
    """
    message = "other message"
    expected_result = {
        "message": message
    }
    result = await hello_world(message)

    assert result == expected_result


@pytest.mark.asyncio
async def test_hello_world_function_returns_hello_world_by_default():
    """
    Un test que falla de manera deliverada para probar GitHub Actions
    """
    result = await hello_world()
    expected_result = {
        "message": "Hello World"
    }

    assert result == expected_result
