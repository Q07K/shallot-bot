from fastapi import FastAPI
from pydantic import BaseModel

from gen import ai

app = FastAPI()

@app.get("/")
async def test():
    return {"message": "test"}


class Msg(BaseModel):
    msg: str


@app.post("/generate")
async def gemini(msg: Msg):
    print(msg)
    result = ai(msg.msg)
    return {'response': result}