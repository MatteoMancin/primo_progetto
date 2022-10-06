from django.urls import path
from .views import homepage, welcome, lista, chiSiamo, variabili

app_name = "prima_app"
urlpatterns = [
    path('', homepage, name="homepage"),
    path('welcome', welcome, name="welcome"),  
    path('lista/', lista, name="lista"),
    path('chi_siamo/', chiSiamo, name="chiSiamo"),
    path('variabili/',variabili,  name="variabili" )
]
#ciao