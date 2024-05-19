# criar req http
# recuperar repostas
from django.test import TestCase # type: ignore
from django.test import Client # type: ignore
from django.urls import reverse_lazy # type: ignore


class IndexViewtestCase(TestCase):
    def setUp(self):
        self.dados = { 
                'nome': "Felipe",
                'email': "Felipe@gmail.com",
                'assunto': 'Felipe se formou',
                'mensagem': "Felipe se formou em pouco tempo"
            }
        self.cliente = Client() 

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)
        # redirect == 302
        # após o email ser enviado, é redirecionado para o index

    def test_form_invalid(self):
        dados = {
            'nome': "Felipe",
            'email': "Felipe@gmail.com",
        }

        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)

