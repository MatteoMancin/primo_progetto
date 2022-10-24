from django.urls import URLPattern, path
from .views import index0, maxmin, media
app_name = "prova_pratica_0"

urlpatterns = [
    path("", index0, name="index0"),
    path("maxmin", maxmin, name="maxmin"),
    path("media", media, name="media"),
]