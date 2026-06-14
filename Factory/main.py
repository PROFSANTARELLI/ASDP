from fastapi import FastAPI

app = FastAPI()


# Classes de pagamento

class Pix:

    def processar(self):
        return "Pagamento realizado via PIX"


class Cartao:

    def processar(self):
        return "Pagamento realizado via Cartão"


class Boleto:

    def processar(self):
        return "Pagamento realizado via Boleto"
    
class Paypal:

    def processar(self):
        return "Pagamento realizado via PayPal"
    


# Factory

class PagamentoFactory:

    @staticmethod
    def criar_pagamento(tipo):

        if tipo == "pix":
            return Pix()

        elif tipo == "cartao":
            return Cartao()

        elif tipo == "boleto":
            return Boleto()
        
        elif tipo == "paypal":
            return Paypal()

        else:
            raise ValueError("Método inválido")


# Endpoint

@app.get("/pagamento/{tipo}")
def pagamento(tipo: str):

    metodo = PagamentoFactory.criar_pagamento(tipo)

    return {
        "tipo": tipo,
        "resultado": metodo.processar()
    }
