from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "This is an test", 'random': random.randint(1, 100)}

@app.get("/random/{limit}")
async def read_item(limit: int):
    return {'random with limit': random.randint(1, limit), "limit": limit}
