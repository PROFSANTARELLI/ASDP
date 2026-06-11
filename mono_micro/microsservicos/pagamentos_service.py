# rapidoeats/microsservicos/pagamentos_service.py
# ============================================================
# MICROSSERVIÇO DE PAGAMENTOS — porta 8002
# Responsabilidade única: processar e rastrear pagamentos
# Nota: Em produção, este serviço se comunicaria com o serviço
# de pedidos via HTTP ou mensageria (ex: RabbitMQ, Kafka)
# ============================================================

from fastapi import FastAPI, HTTPException
from datetime import datetime
import random

app = FastAPI(
    title="RapidoEats — Serviço de Pagamentos",
    description="Microsserviço responsável pelo processamento de pagamentos",
    version="1.0.0"
)

# Base de dados própria e isolada
pagamentos_db = {}

METODOS_ACEITOS = ["pix", "credito", "debito", "voucher"]

@app.post("/pagamentos", status_code=201)
def processar_pagamento(pedido_id: int, valor: float, metodo: str):
    """
    Processa o pagamento de um pedido.
    Em arquitetura real, após aprovar, publicaria um evento
    'pagamento.aprovado' para que o serviço de pedidos
    e o de notificações reajam de forma assíncrona.
    """
    if metodo not in METODOS_ACEITOS:
        raise HTTPException(
            status_code=400,
            detail=f"Método inválido. Aceitos: {METODOS_ACEITOS}"
        )
    
    # Simulação de aprovação (90% de aprovação)
    aprovado = random.random() > 0.1
    
    pagamento = {
        "id": len(pagamentos_db) + 1,
        "pedido_id": pedido_id,
        "valor": valor,
        "metodo": metodo,
        "status": "aprovado" if aprovado else "recusado",
        "codigo_autorizacao": f"AUTH-{random.randint(10000, 99999)}" if aprovado else None,
        "processado_em": datetime.now().isoformat()
    }
    pagamentos_db[pagamento["id"]] = pagamento
    return pagamento

@app.get("/pagamentos/pedido/{pedido_id}")
def buscar_pagamento_por_pedido(pedido_id: int):
    """Retorna os pagamentos associados a um pedido."""
    resultado = [p for p in pagamentos_db.values() if p["pedido_id"] == pedido_id]
    if not resultado:
        raise HTTPException(status_code=404, detail="Nenhum pagamento encontrado para este pedido")
    return resultado

@app.get("/health")
def health():
    return {"servico": "pagamentos", "status": "online", "porta": 8002}