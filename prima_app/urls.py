from django.urls import path
from .views import homepage, welcome, lista, chiSiamo, variabili, index
app_name = "prima_app"
urlpatterns = [
    path("", index, name="index"),
    path('homepage/', homepage, name="homepage"),
    path('welcome', welcome, name="welcome"),  
    path('lista/', lista, name="lista"),
    path('chi_siamo/', chiSiamo, name="chiSiamo"),
    path('variabili/',variabili,  name="variabili" ),
]
#ciao