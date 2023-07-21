"""
Una demo hecha con FastAPI para el módulo de productivización
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_world(message: str='Hello World') -> object:
    """
    Devuelve el valor del mensaje recibido. Si no recibe mensaje, devuelve 'Hello World'

    :param str message: El mensaje a devolver
    """
    return {"message": message}
