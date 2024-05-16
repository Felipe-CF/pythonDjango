from django.contrib import admin # type: ignore
from .models import Produto
# Register your models here.

@admin.register(Produto) # decorator
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 
        'preco', 
        'estoque', 
        'slug', 
        'criado', 
        'modificado', 
        'ativo'
        ]