from django.urls import path
from .views import view_a, view_b, view_c
app_name = "prova_pratica_1"
urlpatterns = [
    path("", view_a, name="lista_materie"),
    path("lista_voti_assenze", view_b, name="lista_voti_assenze"),
    path("media_voti", view_c, name="media_voti"),
]