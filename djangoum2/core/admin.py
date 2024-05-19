from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest # type: ignore
from .models import Post

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('titulo', 'autor')

# @admin.register(Post) usuário só enxerga seus posts
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('titulo', '_autor')
    
#     def _autor(self, instance): # instance = Post
#         return f'{instance.autor.get_full_name()}'
#     def get_queryset(self, request):
#         query = super(PostAdmin, self).get_queryset(request)
#         return query.filter(autor=request.user)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor')
    exclulde = ['autor']
    
    def _autor(self, instance): # usuario logado é quem cria o post
        return f'{instance.autor.get_full_name()}'
    def get_queryset(self, request):
        query = super(PostAdmin, self).get_queryset(request)
        return query.filter(autor=request.user)
    def save_model(self, request,obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)