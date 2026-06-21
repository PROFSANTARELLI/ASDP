from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL",
               "postgresql://admin:admin@postgres:5432/deliveryhub")
engine = create_engine(DATABASE_URL)

@app.on_event("startup")
def criar_tabela():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS pedidos (
                id SERIAL PRIMARY KEY,
                cliente VARCHAR(100),
                status VARCHAR(50)
            )
        """))
        conn.execute(text("""
            INSERT INTO pedidos (cliente, status)
            SELECT 'Maria', 'Em preparo'
            WHERE NOT EXISTS (SELECT 1 FROM pedidos)
        """))
        conn.commit()

@app.get("/pedidos")
def listar_pedidos():
    with engine.connect() as conn:
        resultado = conn.execute(text("SELECT id, cliente, status FROM pedidos"))
        return [{"id": r[0], "cliente": r[1], "status": r[2]} for r in resultado]

@app.get("/arquivos")
def listar_arquivos():
   caminho = "/app/storage/imagens"
   arquivos = os.listdir(caminho)
   return {
       "arquivos": arquivos
   }
