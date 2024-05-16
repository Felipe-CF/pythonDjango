from django.shortcuts import render # type: ignore
from django.contrib import messages # type: ignore
from django.shortcuts import redirect # type: ignore

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

def index(request):
    context={
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None) # form pode conter dados(quando o usuario submeter), ou não
    
    if request.method == 'POST': # envio de dados
        if form.is_valid(): # valida o form
            form.send_mail()

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
    # se for usuário anonimo 
    if str(request.user) != "AnonymousUser":
        if str(request.method) == 'POST': # quando o formulario tiver sido submetido
            
            form = ProdutoModelForm(request.POST, request.FILES) #upload d imagem
            if form.is_valid():
                form.save() # salva
                messages.success(request, 'Produto salvo com sucesso')
                form = ProdutoModelForm() # limpo o formulário
            else:
                messages.error(request, 'Erro ao salvar produto.')

        else:# quando o formulario não tiver sido submetido
            form = ProdutoModelForm()

        context={
            "form": form
        }

        return render(request, 'produto.html', context)
    else:
        return redirect('index')

