from fastapi import FastAPI
import random

app = FastAPI()

# http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello Word"}

# http://127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"teste": "deu certo"}

# http://127.0.0.1:8000/teste2
@app.get("/teste2")
async def funcaoteste2():
    return {"teste": True, "num_aleatorio": random.randint(0,1000)}