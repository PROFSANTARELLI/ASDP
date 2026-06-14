from data_access_layer import salvar_pedido

PRECO_UNITARIO = 50.0

def calcular_total(quantidade):
    desconto = 0.10 if quantidade > 10 else 0
    return quantidade * PRECO_UNITARIO * (1 - desconto)

def processar_pedido(cliente, produto, quantidade):
    if quantidade <= 0:
        return "Quantidade inválida"
    total = calcular_total(quantidade)
    pedido = {"cliente": cliente, "produto": produto,
              "quantidade": quantidade, "total": total}
    salvar_pedido(pedido)
    return pedido