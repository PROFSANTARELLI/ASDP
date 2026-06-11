# microsservicos/pedidos_service.py
# ============================================================
# MICROSSERVIÇO DE PEDIDOS — porta 8001
# Responsabilidade única: gerenciar o ciclo de vida dos pedidos
# ============================================================

from fastapi import FastAPI, HTTPException
from datetime import datetime

app = FastAPI(
    title="RapidoEats — Serviço de Pedidos",
    description="Microsserviço responsável pelo ciclo de vida dos pedidos",
    version="1.0.0"
)

# Base de dados própria deste serviço (isolamento de dados)
pedidos_db = {}
contador_id = 0

@app.post("/pedidos", status_code=201)
def criar_pedido(item: str, quantidade: int, cliente_id: str):
    """Cria um novo pedido e retorna seu identificador único."""
    global contador_id
    contador_id += 1
    pedido = {
        "id": contador_id,
        "item": item,
        "quantidade": quantidade,
        "cliente_id": cliente_id,
        "status": "aguardando_pagamento",
        "criado_em": datetime.now().isoformat()
    }
    pedidos_db[contador_id] = pedido
    return pedido

@app.get("/pedidos/{pedido_id}")
def buscar_pedido(pedido_id: int):
    """Retorna os detalhes de um pedido específico."""
    if pedido_id not in pedidos_db:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedidos_db[pedido_id]

@app.patch("/pedidos/{pedido_id}/status")
def atualizar_status(pedido_id: int, novo_status: str):
    """Atualiza o status de um pedido (chamado por outros serviços via API)."""
    if pedido_id not in pedidos_db:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    pedidos_db[pedido_id]["status"] = novo_status
    pedidos_db[pedido_id]["atualizado_em"] = datetime.now().isoformat()
    return {"mensagem": "Status atualizado", "pedido": pedidos_db[pedido_id]}

@app.get("/health")
def health():
    return {"servico": "pedidos", "status": "online", "porta": 8001}