from django.shortcuts import render
import random
def index0(request):
    return render(request, "index0.html")

def maxmin(request):
    x = random.randint(0,10)
    y = random.randint(0, 10)
    context = {
        'num1': x,
        'num2': y,
        'somma': x + y,
    }
    return render(request, "maxmin.html", context)

def media(request):
    lista = []
    for i in range(30):
        lista.append(random.randint(0,10))
    context = {
        "lista": lista,
        "media": sum(lista)/len(lista),
    }
    return render(request, "media.html", context)
