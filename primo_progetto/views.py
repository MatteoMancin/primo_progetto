from django.shortcuts import render

def index_generale(request):
    return render(request, "index_generale.html")

def admin(request):
    return render(request, "/admin/")