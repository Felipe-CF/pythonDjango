import uuid
from django.test import TestCase # type: ignore
from model_mommy import mommy # type: ignore

from core.models import get_arquivo_path

class GetFilepathTest(TestCase):
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png' # len = 40 char
    def test_get_file_path(self):
        arquivo = get_arquivo_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))

class ServicoTestCase(TestCase):
    def setUp(self):
        self.servico = mommy.make('Servico') 
    def test_str(self):
        self.assertEqual(str(self.servico), self.servico.servico)
        # return do str tem que ser igual ao atributo 

class CargoTestCase(TestCase):
    def setUp(self):
        self.cargo = mommy.make('Cargo') 
    def test_str(self):
        self.assertEqual(str(self.cargo), self.cargo.cargo)
        # return do str tem que ser igual ao atributo 

class FuncionarioTestCase(TestCase):
    def setUp(self):
        self.funcionario = mommy.make('Funcionario') 
    def test_str(self):
        self.assertEqual(str(self.funcionario), self.funcionario.nome)
        # return do str tem que ser igual ao atributo
