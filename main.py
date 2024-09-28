from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/helloword")
async def root():
    return {"message": "Hello Word"}

@app.get("/funcaoteste1")
async def funcaoteste():
    return {"teste": "deu certo"}

@app.get("/funcaoteste2")
async def funcaoteste2():
    return {"teste": True, "num_aleatorio": random.randint(0,1000)}