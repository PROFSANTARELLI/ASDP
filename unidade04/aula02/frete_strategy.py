class FreteSedex:
    def calcular(self):
        return 30
class FretePAC:
    def calcular(self):
        return 20
class FreteTransportadora:
    def calcular(self):
        return 25

class FreteExpresso:
    def calcular(self):
        return 50


class CalculadoraFrete:
    def __init__(self, estrategia):
        self.estrategia = estrategia
    def calcular(self):
        return self.estrategia.calcular()

opcao = input(
    "Escolha: sedex, pac, transportadora ou expresso: "
)
if opcao == "sedex":
    estrategia = FreteSedex()
elif opcao == "pac":
    estrategia = FretePAC()
elif opcao == "transportadora":
    estrategia = FreteTransportadora()
elif opcao == "expresso":
    estrategia = FreteExpresso()
else:
    estrategia = FreteTransportadora()
frete = CalculadoraFrete(
    estrategia
)
print(
    f"Frete calculado: R$ {frete.calcular()}"
)
