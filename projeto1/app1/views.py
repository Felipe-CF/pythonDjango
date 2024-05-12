from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from .models import Produto, Cliente

# Create your views here.
def index(request):
    context = {
        'curso': 'programação web com Django framework',
        'outro': 'django',
        'produtos': Produto.objects.all(),
        'clientes': Cliente.objects.all()
    }
    return render(request, 'index.html', context)
    # retorna um template renderizado
def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    p = get_object_or_404(Produto, id=pk)

    context = {
        'produto': p
    }
    return render(request, 'produto.html', context)

# tentando acessar um elemento que não existe
def error404(request, exception):
    template = loader.get_template('404.html')
    
    return HttpResponse(
        content=template.render(), 
        content_type='text/html; charset=utf8',
        status=404
        )

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(
        content=template.render(), 
        content_type='text/html; charset=utf8',
        status=500
        )