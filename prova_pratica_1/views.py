from django.shortcuts import render

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
