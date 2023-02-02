from buscaSaude.models import *


class Estado(Base):
    uf = models.CharField(null=False, max_length=20)

    def __str__(self):
        return self.uf


class Cidade(Base):
    uf = models.ForeignKey(Estado, null=True, related_name='uf+', on_delete=models.SET_NULL)
    cidade = models.CharField(null=False, max_length=40)

    def __str__(self):
        return f"{self.cidade}, {self.uf}"


class Bairro(Base):
    cidade = models.ForeignKey(Cidade, null=True, related_name="cidade+", on_delete=models.SET_NULL)
    bairro = models.CharField(null=False, max_length=40)

    def __str__(self):
        return f"{self.bairro} - {self.cidade}"


class Endereco(Base):
    nome_do_local = models.CharField(null=False, max_length=100)
    bairro = models.ForeignKey(Bairro, null=True, related_name="bairro+", on_delete=models.SET_NULL)
    endereco = models.CharField(null=False, max_length=150)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    funcionamento_horario_inicio = models.TimeField()
    funcionamento_horario_fim = models.TimeField()
    funcionamento_dias = models.IntegerField(choices=DIAS_DE_ATENDIMENTO)

    telefone = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return self.nome_do_local

