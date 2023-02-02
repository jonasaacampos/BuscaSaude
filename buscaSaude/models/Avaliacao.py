from buscaSaude.models import *


class Avalicao(Base):
    user_avaliador = models.ForeignKey(User, related_name="avaliou", on_delete=models.CASCADE)
    user_avaliado = models.ForeignKey(User, related_name="avaliado", on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    comentarios = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

    def __str__(self):
        return f"Avaliador: {self.user_avaliador.first_name} | Avaliado: {self.user_avaliado}"



