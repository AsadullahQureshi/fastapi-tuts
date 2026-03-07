from fastapi import FastAPI, Depends, Request
from typing import Annotated
from projectTypes import SearchParam
from app.routing import todo_routing
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello Asadullah Qureshi 🚀 FastAPI is working"}


@app.get("/sending")
def sending_data():
    return {"message": "sending data...."}


@app.get("/show/{id}")
def show(id: int):
    return {"message": "show Todo Object with {id}"}


# searching param ?name=Asad&limit=10&skip=0


@app.get("/search")
def search(request: Annotated[SearchParam, Depends()]):
    return {"message": "searching params", "request": request}


@app.get("/search2")
def search2(request: Request):
    params = request.query_params
    return {"message": "simple search without pydantic", "params": params}


# include todo other router
app.include_router(todo_routing.router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    errors = {}
    for error in exc.errors():
        errors[error["loc"][-1]] = error["msg"]
    return JSONResponse(
        content={"message": "Validation Error", "errors": errors}, status_code=422
    )
