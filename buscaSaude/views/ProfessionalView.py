from django.http import HttpResponse
from buscaSaude.models import Profile


def list_professional_view(request):
    nome = request.GET.get("username")
    especialidade = request.GET.get("bairro")
    bairro = request.GET.get("bairro")
    cidade = request.GET.get("cidade")
    estado = request.GET.get("uf")

    professionals = Profile.objects.all()
    # all() : Profile.objects.first()

    print(professionals)

    # sample data
    # http://localhost:8000/professional/?uf=1
    return HttpResponse("Lista de profissionais...")
