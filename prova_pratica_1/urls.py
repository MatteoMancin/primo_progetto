from django.urls import path
from .views import view_a, view_b, view_c, home, StudenteDetailViewCB, VerificaListViewCB, VerificaDetailViewCB
app_name = "prova_pratica_1"
urlpatterns = [
    path("", home, name="homepage"),
    path("lista_materie", view_a, name="lista_materie"),
    path("lista_voti_assenze", view_b, name="lista_voti_assenze"),
    path("media_voti", view_c, name="media_voti"),
    path("studenti/<int:pk>", StudenteDetailViewCB.as_view(), name="studente_detail"),
    path("lista_verifiche", VerificaListViewCB.as_view(), name="lista_verifiche"),
    #path("verifica/<int:pk>", VerificaDetailViewCB.as_view(), name="verifica_detail"),
]