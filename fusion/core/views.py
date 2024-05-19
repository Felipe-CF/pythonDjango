from typing import Any
from django.http import HttpResponse# type: ignore
from django.views.generic import FormView # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.contrib import messages# type: ignore

from .models import Servico, Funcionario
from .forms import ContatoForm

    #TemplateView
class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index') # retorna p/ index se sucesso 

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs) # recuperando contexto da pag
        context['servicos'] = Servico.objects.order_by('?').all() # add objects e enviado p/ o template
        context['funcionarios'] = Funcionario.objects.order_by('?').all() # add objects e enviado p/ o template
        return context

    # graças a herança de FormView
    def form_valid(self, form, *args, **kwargs): # se form valido...
        form.send_email() # envia o e-mail e...
        messages.success(self.request, 'E-mail enviado com sucesso!') # exibe mensagem de sucesso
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):# se form invalido...
        messages.error(self.request, 'Erro ao envial e-mail') # exibe mensagem de erro
        return super(IndexView, self).form_invalid(form, *args, **kwargs) # retorna o form
