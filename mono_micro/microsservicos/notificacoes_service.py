# rapidoeats/microsservicos/notificacoes_service.py
# ============================================================
# MICROSSERVIÇO DE NOTIFICAÇÕES — porta 8003
# Responsabilidade única: enviar e registrar notificações
# aos clientes por diferentes canais
# ============================================================

from fastapi import FastAPI
from datetime import datetime
from enum import Enum

app = FastAPI(
    title="RapidoEats — Serviço de Notificações",
    description="Microsserviço responsável pelo envio de notificações aos clientes",
    version="1.0.0"
)

class Canal(str, Enum):
    email = "email"
    sms = "sms"
    push = "push"

# Histórico de notificações enviadas
historico = []

@app.post("/notificacoes", status_code=201)
def enviar_notificacao(
    cliente_id: str,
    pedido_id: int,
    mensagem: str,
    canal: Canal = Canal.email
):
    """
    Envia uma notificação ao cliente.
    Em arquitetura orientada a eventos, este serviço
    consumiria eventos como 'pedido.criado' e 'pagamento.aprovado'
    de uma fila (Kafka/RabbitMQ) sem precisar ser chamado diretamente.
    """
    notificacao = {
        "id": len(historico) + 1,
        "cliente_id": cliente_id,
        "pedido_id": pedido_id,
        "mensagem": mensagem,
        "canal": canal,
        "status": "entregue",
        "enviado_em": datetime.now().isoformat()
    }
    historico.append(notificacao)
    return {"mensagem": "Notificação enviada", "detalhe": notificacao}

@app.get("/notificacoes/cliente/{cliente_id}")
def historico_cliente(cliente_id: str):
    """Retorna o histórico de notificações de um cliente."""
    resultado = [n for n in historico if n["cliente_id"] == cliente_id]
    return {"cliente_id": cliente_id, "total": len(resultado), "notificacoes": resultado}

@app.get("/health")
def health():
    return {"servico": "notificacoes", "status": "online", "porta": 8003}