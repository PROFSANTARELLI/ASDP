from usecases.cliente_usecase import (
   ClienteUseCase
)
from repositories.cliente_repository_fake import (
   ClienteRepositoryFake
)
repository = ClienteRepositoryFake()

usecase = ClienteUseCase(
   repository
)
print(
   usecase.listar_clientes()
)
