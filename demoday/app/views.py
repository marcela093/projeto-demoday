from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def depoimentos(request):
    return render(request, 'depoimentos.html')

def cursos(request):
    return render(request, 'cursos.html')

def eventos(request):
    return render(request, 'eventos.html')

