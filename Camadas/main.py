# main.py — CÓDIGO DESORGANIZADO (antes da arquitetura em camadas)

pedidos = []

def fazer_pedido(cliente, produto, quantidade):
    if quantidade <= 0:
        return "Quantidade inválida"
    if quantidade > 10:
        desconto = 0.10
    else:
        desconto = 0
    preco_unitario = 50.0
    total = quantidade * preco_unitario * (1 - desconto)
    pedido = {"cliente": cliente, "produto": produto,
              "quantidade": quantidade, "total": total}
    pedidos.append(pedido)
    print(f"Pedido recebido: {pedido}")
    return pedido

resultado = fazer_pedido("Ana", "Pizza", 12)
print(f"Total: R$ {resultado['total']}")
