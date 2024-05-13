from django.shortcuts import render # type: ignore
from django.contrib import messages # type: ignore
from .forms import ContatoForm

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None) # form pode conter dados(quando o usuario submeter), ou não
    
    if request.method == 'POST': # envio de dados
        if form.is_valid(): # valida o form
            nome = form.cleaned_data['nome'] # cleamed_data['name']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            messages.success(request, 'E-mail enviado com sucesso')
            form = ContatoForm() # limpando o form
            # {%bootstrap_messages%} 
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    
    context = {
        'form': form
    }
    return render(request, 'contato.html', context=context)


def produto(request):
    return render(request, 'produto.html')