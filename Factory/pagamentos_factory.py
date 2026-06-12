class Pix:
   def processar(self):
       return "Pagamento realizado via PIX"

class Cartao:
   def processar(self):
       return "Pagamento realizado via Cartão"

class Boleto:
   def processar(self):
       return "Pagamento realizado via Boleto"
   class PagamentoFactory:
   @staticmethod
   def criar_pagamento(tipo):
       if tipo == "pix":
           return Pix()
       elif tipo == "cartao":
           return Cartao()
       elif tipo == "boleto":
           return Boleto()
       else:
           raise ValueError("Método de pagamento inválido")
