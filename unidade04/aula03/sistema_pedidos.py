class PedidoService:
   def salvar_pedido(self):
       print("Pedido salvo")

class EmailService:
   def enviar_email(self):
       print("E-mail enviado")

class PagamentoService:
   def processar_pagamento(self):
       print("Pagamento processado")

class RelatorioService:
   def gerar_relatorio(self):
       print("Relatório gerado")

pedido = PedidoService()
email = EmailService()
pagamento = PagamentoService()
relatorio = RelatorioService()
pedido.salvar_pedido()
email.enviar_email()
pagamento.processar_pagamento()
relatorio.gerar_relatorio()
