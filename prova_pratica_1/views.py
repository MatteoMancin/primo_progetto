from django.shortcuts import get_object_or_404, render
from .models import Studenti, Verifica
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

def view_a(request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
    context = {
        "lista": materie
    }
    return render(request, "lista_materie.html", context)

def view_b(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    chiavi = voti.keys()
    context = {
        "voti": voti,
        "chiavi": chiavi
    }
    return render(request, "lista_voti_assenze.html", context)

def view_c(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    medie = []
    for x in voti.values():
        somma = 0
        for i in range(len(x)):
            somma += x[i][1]
        medie.append(somma/len(x))

    nomi = list(voti.keys())

    dict_medie = {}
    for i in range(len(medie)):
        dict_medie[nomi[i]] = medie[i]

    context = {
        'medie': dict_medie
    }

    return render(request, "media_voti.html", context)

def home(request):
    studenti = Studenti.objects.all()           #ora gli articoli e i giornalisti sono immagazzinati in un
    verifiche = Verifica.objects.all()     #dizionario context.
    context = {"studenti": studenti, "verifiche": verifiche}
    print(context)
    return render(request, "hompageStudenti.html", context)

def studenteDetailView (request, pk):
    studenti = get_object_or_404(Studenti, pk=pk)
    context = {"studenti": studenti}
    return render(request, "studente_detail.html", context)

class StudenteDetailViewCB (DetailView):
    model = Studenti
    template_name = "studente_detail.html"

class VerificaDetailViewCB (DetailView):
    model = Verifica
    template_name = "verifica_detail.html"

class StudentiListView (ListView):
    model = Studenti
    template_name = "lista_studenti.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["studenti"] = Studenti.objects.all()
        return context
    
class VerificaListViewCB (ListView):
    model = Verifica
    template_name = "lista_verifiche.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["verifiche"] = Verifica.objects.all()
        return context
