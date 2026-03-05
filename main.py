from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Asadullah 🚀 FastAPI is working"}

@app.get("/sending")
def sending_data():
    return {"message": "sending data...."}

