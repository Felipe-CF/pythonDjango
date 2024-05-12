from django.contrib import admin

from .models import Produto, Cliente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'qnt_estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
