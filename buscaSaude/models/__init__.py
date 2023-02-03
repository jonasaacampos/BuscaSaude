from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Base(models.Model):
    status = models.BooleanField("Ativo?", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


PROFILE_TYPE = (
    (1, 'Admin'),
    (2, 'Médico'),
    (3, 'Paciente')
)

DIAS_DE_ATENDIMENTO = (
    (1, "2ª a 6ª"),
    (2, "2ª a sábado"),
    (3, "Somente com agendamento"),
    (4, "Teleconsulta e Agendamento Presencial"),
    (5, "Teleconsulta somente"),
    (6, "Urgência e Emergência - 24hs"),
)

from .Profile import Profile
from .Especialidade import Especialidade
from .Endereco import Estado, Cidade, Bairro, Endereco
from .Avaliacao import Avalicao
