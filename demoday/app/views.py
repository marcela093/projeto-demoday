from django.shortcuts import render, get_object_or_404
from .models import Depoimento
from .forms import DepoimentoForm
from django.utils import timezone
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def index(request):
    return render(request, 'index.html')
@never_cache
def cursos(request):
    return render(request, 'cursos.html')
@never_cache
def eventos(request):
    return render(request, 'eventos.html')
@never_cache
def depoimentos(request):
    depoimentos = Depoimento.objects.filter(data__lte=timezone.now()).order_by('data') 
    return render(request, 'depoimentos.html', {'depoimentos': depoimentos})
@never_cache
def depoimentos_empresas(request):
    depoimentos = Depoimento.objects.filter(data__lte=timezone.now()).order_by('data') 
    return render(request, 'depoimentos-empresa.html', {'depoimentos': depoimentos})
@never_cache
def avaliacao(request):
    if request.method == "POST":
        form = DepoimentoForm(request.POST)
        if form.is_valid():
            depoimento = form.save(commit=False)
            depoimento.data = timezone.now()
            depoimento.save()
            return redirect('depoimentos.html') 
            # , pk=post.pk
    else:
         form = DepoimentoForm()
    return render(request, 'avaliacao.html', {'form': form})
@never_cache    
def login(request):
    return render(request, 'login.html')
@never_cache    
def base(request):
    return render(request, 'base.html')