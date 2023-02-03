from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ("user", "perfil", "data_nascimento", "updated_at", "status", "especialidadesList")
    list_display_links = ("user", "perfil", "data_nascimento")

    list_filter = ("user__is_active",)

    def especialidadesList(self, obj):
        return [i.especialidade for i in obj.especialidades.all()]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Especialidade)
admin.site.register(Endereco)
admin.site.register(Bairro)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Avalicao)

