from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8,default=0)
    qnt_estoque = models.IntegerField('Quantidade em Estoque', default=0)

    def __str__(self):
        return f"Cód:{self.id}  Produto:{self.nome}"

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email', max_length=100)

    def __str__(self):
        return f"idCliente:{self.id} {self.nome} {self.sobrenome}"