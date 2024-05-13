from django.urls import path # type: ignore
from .views import index, contato, produto

urlpatterns=[
    # 'url', 'view', 'name'
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto')
]