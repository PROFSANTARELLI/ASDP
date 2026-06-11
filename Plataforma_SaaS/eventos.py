def atualizar_estoque(produto):
    print(f"Estoque atualizado para {produto}")

def enviar_email(produto):
    print(f"E-mail enviado sobre a compra de {produto}")

def registrar_analytics(produto):
    print(f"Métrica registrada para {produto}")

def gerar_cashback(produto):
    print(f"Cashback gerado para compra de {produto}")

def publicar_evento(produto):
    atualizar_estoque(produto)
    enviar_email(produto)
    registrar_analytics(produto)
    gerar_cashback(produto)

# Simulação da geração do evento
publicar_evento("Notebook")