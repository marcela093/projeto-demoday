from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def cursos(request):
    return render(request, 'cursos.html')

def eventos(request):
    return render(request, 'eventos.html')

def depoimentos(request):
    return render(request, 'depoimentos.html')

def depoimentos_empresas(request):
    return render(request, 'depoimentos-empresa.html')

def avaliacao(request):
    return render(request, 'avaliacao.html')
    
def login(request):
    return render(request, 'login.html')
    
def base(request):
    return render(request, 'base.html')