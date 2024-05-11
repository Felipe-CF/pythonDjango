from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'curso': 'programação web com Django framework',
        'outro': 'django'
    }
    return render(request, 'index.html', context)
    # retorna um template renderizado
def contato(request):
    return render(request, 'contato.html')
