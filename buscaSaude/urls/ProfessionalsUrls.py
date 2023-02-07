from django.urls import path
from buscaSaude.views.ProfessionalView import list_professional_view, add_favorite_view


urlpatterns = [
    path("", list_professional_view, name="professionals"),
    path("favorito",add_favorite_view, name="professional-favorite"),
]