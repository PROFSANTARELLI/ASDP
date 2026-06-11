# monolito/main.py
# ============================================================
# MONOLITO: Toda a lógica em um único processo.
# Pedidos, Pagamentos e Notificações rodam juntos na porta 8000.
# ============================================================

from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="RapidoEats — Monolito",
    description="Sistema de delivery com arquitetura monolítica",
    version="1.0.0"
)

# Banco de dados em memória (simulação)
pedidos_db = []

# -----------------------------------------------------------
# MÓDULO DE PEDIDOS
# -----------------------------------------------------------
@app.post("/pedidos")
def criar_pedido(item: str, quantidade: int):
    """Cria um novo pedido na plataforma."""
    pedido = {
        "id": len(pedidos_db) + 1,
        "item": item,
        "quantidade": quantidade,
        "status": "recebido",
        "criado_em": datetime.now().isoformat()
    }
    pedidos_db.append(pedido)
    return {"mensagem": "Pedido criado com sucesso", "pedido": pedido}

@app.get("/pedidos")
def listar_pedidos():
    """Lista todos os pedidos registrados."""
    return {"total": len(pedidos_db), "pedidos": pedidos_db}

# -----------------------------------------------------------
# MÓDULO DE PAGAMENTOS
# -----------------------------------------------------------
@app.post("/pagamentos")
def processar_pagamento(pedido_id: int, metodo: str):
    """Processa o pagamento de um pedido."""
    # Em um monolito real, aqui acessaríamos diretamente
    # a mesma base de dados dos pedidos — acoplamento direto!
    return {
        "pedido_id": pedido_id,
        "metodo": metodo,
        "status": "aprovado",
        "processado_em": datetime.now().isoformat()
    }

# -----------------------------------------------------------
# MÓDULO DE NOTIFICAÇÕES
# -----------------------------------------------------------
@app.post("/notificacoes")
def enviar_notificacao(pedido_id: int, mensagem: str):
    """Envia uma notificação ao cliente."""
    return {
        "pedido_id": pedido_id,
        "mensagem": mensagem,
        "canal": "email",
        "enviado_em": datetime.now().isoformat()
    }

# -----------------------------------------------------------
# ENDPOINT DE SAÚDE (Health Check)
# -----------------------------------------------------------
@app.get("/health")
def health_check():
    """Verifica se o sistema está operacional."""
    return {
        "status": "online",
        "servico": "RapidoEats Monolito",
        "total_pedidos": len(pedidos_db)
    }