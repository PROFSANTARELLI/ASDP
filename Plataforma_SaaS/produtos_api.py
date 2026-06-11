from fastapi import FastAPI
app = FastAPI()
@app.get("/produtos/1")
def produto():
   return {
       "id": 1,
       "produto": "Notebook",
       "valor": 3500
   }
@app.get("/produtos/2")
def produto():
    return {
         "id": 2,
         "produto": "Smartphone",
         "valor": 2500
    }
@app.get("/produtos/3")
def produto():
    return {
         "id": 3,
         "produto": "Tablet",
         "valor": 1500
    }
