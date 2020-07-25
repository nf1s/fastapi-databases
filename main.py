# -*- coding: utf-8 -*-
"""Sample main.py used for testing purposes

"""
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from models import db, User as ModelUser


class SchemaUser(BaseModel):
    first_name: str
    last_name: str
    age: int


app = FastAPI()

db.init_app(app)


@app.post("/user/")
async def create_user(user: SchemaUser):
    user_id = await ModelUser.create(**user.dict())
    return {"user_id": user_id}


@app.get("/user/{id}", response_model=SchemaUser)
async def get_user(id: int):
    user = await ModelUser.get(id)
    return SchemaUser(**user).dict()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
