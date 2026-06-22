from repositories.cliente_repository import (
   ClienteRepository
)
class ClienteRepositoryFake(
   ClienteRepository
):
   def listar(self):
       return [
           "Maria",
           "Carlos",
           "Fernanda"
       ]
