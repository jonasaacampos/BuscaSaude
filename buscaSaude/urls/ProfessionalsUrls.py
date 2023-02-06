from django.urls import path
from buscaSaude.views.ProfessionalView import list_professional_view


urlpatterns = [
    path("", list_professional_view, name="professionals"),
]