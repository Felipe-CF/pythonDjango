from django.views.generic import TemplateView # type: ignore


class IndexView(TemplateView):
    template_name = 'index.html'

