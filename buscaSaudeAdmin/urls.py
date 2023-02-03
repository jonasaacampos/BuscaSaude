from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("buscaSaude.urls.HomeUrls")),
    path("profile/", include("buscaSaude.urls.ProfileUrls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
