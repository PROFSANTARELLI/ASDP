from fastapi import FastAPI
app = FastAPI()
@app.get("/usuarios/1")
def usuario():
    return {
        "id": 1,
        "nome": "Ana"
    }
@app.get("/usuarios/2")
def usuario():
    return {
        "id": 2,
        "nome": "Bruno"
    }
@app.get("/usuarios/3")
def usuario():
    return {
        "id": 3,
        "nome": "Carla"
    }

