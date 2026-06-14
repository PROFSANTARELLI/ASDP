from database_layer import pedidos

def salvar_pedido(pedido):
    pedidos.append(pedido)

def listar_pedidos():
    return pedidos