from django.urls import path
from .views import home, ArticoloDetailViewCB, ArticoloListView, GiornalistaDetailViewCB, GiornalistaListView, articoli_list_api, articolo_api, giornalisti_list_api, giornalista_api #articoloDetailView


app_name = "news"

urlpatterns = [
    path("", home, name="homepageNews"),
    #path("articoli/<int:pk>", articoloDetailView, name="articolo_detail")
    path("articoli/<int:pk>", ArticoloDetailViewCB.as_view(), name="articolo_detail"),
    path("lista_articoli/", ArticoloListView.as_view(), name="lista_articoli"),
    path("giornalisti/<int:pk>", GiornalistaDetailViewCB.as_view(), name="giornalista_detail"),
    path("lista_giornalisti/", GiornalistaListView.as_view(), name="lista_giornalisti"),
    path("giornalisti_list_api/", giornalisti_list_api, name="giornalista_list_api"),
    path("articoli_list_api/", articoli_list_api, name="articoli_list_api"),
    path("giornalista_api/<int:pk>", giornalista_api, name="giornalista_api"),
    path("articolo_api/<int:pk>", articolo_api, name="articolo_api"),

]