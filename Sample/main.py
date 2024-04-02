from fastapi import FastAPI, Response, HTTPException
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {'data':'json'}


@app.post("/post")
def post(payload: dict=Body(...)):
    return payload


class Person(BaseModel):
    name : str
    age : int
    address : str

class ShowPerson(Person):
    name: str

@app.post("/person")
def person(request: Person):
    return request

@app.get("/person/{id}")
def person(id):
    return id