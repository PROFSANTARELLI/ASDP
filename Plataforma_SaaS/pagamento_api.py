from fastapi import FastAPI
app = FastAPI()
@app.post("/pagamento")
def pagamento():
   return {
       "status": "Pagamento aprovado"
   }
