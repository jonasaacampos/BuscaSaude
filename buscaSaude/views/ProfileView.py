from django.http import HttpResponse

def list_profile_view(request, id=None):
    return HttpResponse(f"<h1>Usuário de id {id} </h1>")