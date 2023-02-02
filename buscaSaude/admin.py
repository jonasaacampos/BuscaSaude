from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Especialidade)
admin.site.register(Endereco)
admin.site.register(Bairro)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Avalicao)

