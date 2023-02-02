from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


PROFILE_TYPE = (
    (1, 'Admin'),
    (2, 'Médico'),
    (3, 'Paciente')
)

from .Profile import Profile
