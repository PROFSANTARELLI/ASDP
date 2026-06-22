def calcular_frete(tipo):
    if tipo == "sedex":
        return 30
    elif tipo == "pac":
        return 20
    elif tipo == "transportadora":
        return 25
    else:
        return 0
print(
    calcular_frete("sedex")
)
