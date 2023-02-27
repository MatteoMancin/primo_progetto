from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articolo, Giornalista
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import JsonResponse

# def home(request):
#     a = ""
#     g = ""

#     for art in Articolo.objects.all():
#         a += (art.titolo + "<br>")dxc
    
#     for gio in Giornalista.objects.all():
#         g += (gio.nome + "<br>")
#     response = "Articoli:<br>" + a + "<br>Giornalisti:<br>" + g

#     return HttpResponse("<h1>"+response+"</h1>")


# def home(reqeust):
#     a = []              #rispetto alla versione precedente commentata, in questa funzione aggiungiamo tutte
#     g = []              #le occorrenze a delle lista che successivamente visualizziamo
#     for art in Articolo.objects.all():
#         a.append(art.titolo)
    
#     for gio in Giornalista.objects.all():
#         g.append(gio.nome)

#     response  = str(a) + "<br>" + str(g)
#     print(response)

#     return HttpResponse("<h1>"+response+"</h1>")

def home(request):
    articoli = Articolo.objects.all()           #ora gli articoli e i giornalisti sono immagazzinati in un
    giornalisti = Giornalista.objects.all()     #dizionario context.
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepageNews.html", context)

def articoloDetailView (request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)

class ArticoloDetailViewCB (DetailView):
    model = Articolo
    template_name = "articolo_detail.html"

class GiornalistaDetailViewCB (DetailView):
    model = Giornalista
    template_name = "giornalista_detail.html"

class ArticoloListView (ListView):
    model = Articolo
    template_name = "lista_articoli.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articoli"] = Articolo.objects.all()
        return context
    
class GiornalistaListView (ListView):
    model = Giornalista
    template_name = "lista_giornalisti.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["giornalisti"] = Giornalista.objects.all()
        return context

def giornalisti_list_api(request):
    giornalisti = Giornalista.objects.all()
    data = {"giornalisti":list(giornalisti.values("pk","nome","cognome"))}
    response = JsonResponse(data)
    return response

def giornalista_api(request, pk):
    try:
        giornalista = Giornalista.objects.get(pk=pk)
        data = {'giornalista':{
            "nome":giornalista.nome,
            "cognome":giornalista.cognome,
            }   
        }
        response = JsonResponse(data)
    except Giornalista.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code":404,
                "message":"Giornalista non trovato"
            }},
           status = 404)
    return response


def articoli_list_api(request):
    articoli = Articolo.objects.all()
    data = {"articoli":list(articoli.values("pk","titolo","contenuto"))}
    response = JsonResponse(data)
    return response

def articolo_api(request, pk):
    try:
        articolo = Articolo.objects.get(pk=pk)
        data = {'articolo':{
            "titolo":articolo.titolo,
            "cognome":articolo.contenuto,
            }   
        }
        response = JsonResponse(data)
    except Articolo.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code":404,
                "message":"Articolo non trovato"
            }},
           status = 404)
    return response

def tabella_giornalisti(request):
    return render(request, "tabella_giornalisti.html")

def tabella_articoli(request):
    return render(request, "tabella_articoli.html")

