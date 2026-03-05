from fastapi import FastAPI, Depends, Request
from typing import Annotated
from projectTypes import SearchParam
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Asadullah 🚀 FastAPI is working"}

@app.get("/sending")
def sending_data():
    return {"message": "sending data...."}


@app.get("/show/{id}")
def show(id:int):
    return {"message": "show Todo Object with {id}"}

@app.post("/todo")
def created(item:dict):
    return {"message": "Todo Created", "item":item}

@app.put("/todo/{id}")
def updated(id:int):
    return {"message": "Todo Updated", "item":id}

@app.delete("/todo/{id}")
def deleted(id:int):
    return {"message": "Todo deleted", "item":id}

# searching param ?name=Asad&limit=10&skip=0

@app.get("/search")
def search(request: Annotated [SearchParam, Depends()]):
    return {"message": "searching params", "request":request}


@app.get("/search2")
def search2(request: Request):
    params = request.query_params
    return {"message": "simple search without pydantic", "params":params}





