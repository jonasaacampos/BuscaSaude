from buscaSaude.models import *

class Especialidade(Base):
    especialidade = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.especialidade