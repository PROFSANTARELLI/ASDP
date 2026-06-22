# adapter_pagamento.py — arquivo completo e funcional

# ── Sistema Legado (não pode ser alterado) ───────────────────
class GatewayLegado:
    def realizar_pagamento(self):
        return "Pagamento realizado pelo sistema legado"

# ── Sistema Atual (espera processar_pagamento) ───────────────
class SistemaAtual:
    def finalizar_compra(self, gateway):
        print(gateway.processar_pagamento())

# ── Adapter: traduz um padrão para o outro ───────────────────
class PagamentoAdapter:
    def __init__(self, gateway_legado):
        self.gateway_legado = gateway_legado

    def processar_pagamento(self):          # ← nome que o SistemaAtual espera
        return self.gateway_legado.realizar_pagamento()  # ← chama o legado

# ── Teste SEM adapter (vai gerar erro — isso é esperado) ─────
print("=== TESTE SEM ADAPTER ===")
try:
    gateway = GatewayLegado()
    sistema = SistemaAtual()
    sistema.finalizar_compra(gateway)
except AttributeError as e:
    print(f"Erro esperado: {e}")

# ── Teste COM adapter (deve funcionar) ───────────────────────
print("\n=== TESTE COM ADAPTER ===")
gateway_legado  = GatewayLegado()
gateway_adapter = PagamentoAdapter(gateway_legado)
sistema         = SistemaAtual()
sistema.finalizar_compra(gateway_adapter)
