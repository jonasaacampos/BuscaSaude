from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from buscaSaude.models import Profile


def list_professional_view(request):
    nome = request.GET.get("username")
    especialidade = request.GET.get("especialidade")
    bairro = request.GET.get("bairro")
    cidade = request.GET.get("cidade")
    estado = request.GET.get("uf")

    professionals = Profile.objects.filter(perfil=2)
    # teste para paginação
    #professionals = Profile.objects.all()

    # all() : Profile.objects.first()

    if nome is not None and nome != "":
        professionals = professionals.filter(Q(user__fisrt_name__contains=nome) | Q(user__username__contains=nome))
    if especialidade is not None:
        professionals = professionals.filter(especialidades__id=especialidade)

    if bairro is not None:
        professionals = professionals.filter(enderecos__bairro=bairro)
    else:
        if cidade is not None:
            professionals = professionals.filter(enderecos__bairro_cidade=cidade)
        elif estado is not None:
            professionals = professionals.filter(enderecos__bairro_cidade_uf=estado)


    # paginação
    if len(professionals) > 0:
        paginator = Paginator(professionals, 8)
        page = request.GET.get('page')
        professionals = paginator.get_page(page)

    get_copy = request.GET.copy()
    parameters = get_copy.pop("page", True) and get_copy.urlencode()

    context = {
        "professionals": professionals,
        "parameters": parameters
    }

    return render(request, template_name="professional/professionals.html", context=context, status=200)


def add_favorite_view(request):
    page = request.POST.get("page")
    nome = request.POST.get("nome")
    especialidade = request.POST.get("especialidade")
    bairro = request.POST.get("bairro")
    cidade = request.POST.get("cidade")
    uf = request.POST.get("uf")
    id = request.POST.get("id")

    try:
        profile = Profile.objects.filter(user=request.user).fisrt()
        professional = Profile.objects.filter(user__id=id).first()
        profile.favoritos.add(professional.user)
        profile.save()
        mensagem = "Adicionado à seus profissionais favoritos"
        _type = "success"
    except Exception as e:
        print(f"Erro: {e} ")
        mensagem = "Não foi possível adiocionar aos favoritos, tente mais tarde"
        _type = "danger"

    if page:
        arguments = f"?page={page}"
    else:
        arguments = "?oage=1"
    if nome:
        arguments += f"&nome={nome}"
    if especialidade:
        arguments += f"&especialidade={especialidade}"
    if bairro:
        arguments += f"&bairro={bairro}"
    if cidade:
        arguments += f"&cidade={cidade}"
    if uf:
        arguments += f"&uf={uf}"

    arguments += f"&mensagem={mensagem, _type}"

    return redirect(to=f"/professional/{arguments}")