from fastapi import FastAPI
from pydantic import BaseModel

from db import MONGODB_CLIENT
from gen import ai

app = FastAPI()


@app.get("/")
async def test():
    return {"message": "test"}


class Chat(BaseModel):
    content: str
    # roomName: str
    # isGroupChat: bool
    # isOpenChat: bool
    # authorName: str
    # authorHash: str
    # hasMention: str


@app.post("/insert")
async def chat_insert(data: Chat):
    db = MONGODB_CLIENT.get_database("shallot_bot")
    col = db.get_collection("test")

    col.insert_one(document=data.model_dump())


class Msg(BaseModel):
    msg: str


@app.post("/generate")
async def gemini(msg: Msg):
    print(msg)
    result = ai(msg.msg)
    return {"response": result}
