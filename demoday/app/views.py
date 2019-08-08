from django.shortcuts import render

# Create your views here.

def app(request):
    return render(request, 'cursos.html')


#def app(request):
    #return render(request, 'eventos.html')

