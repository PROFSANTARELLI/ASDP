class ClienteUseCase:
   def __init__(self, repository):
       self.repository = repository
   def listar_clientes(self):
       return self.repository.listar()
