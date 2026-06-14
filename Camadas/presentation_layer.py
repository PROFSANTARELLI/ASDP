from business_layer import processar_pedido

resultado = processar_pedido("Ana", "Pizza", 12)
print(f"Pedido recebido: {resultado}")
print(f"Total: R$ {resultado['total']}")