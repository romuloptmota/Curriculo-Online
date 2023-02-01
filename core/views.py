from django.views.generic import TemplateView
from.models import Inicio


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['inicio'] = Inicio.objects.all()

        return context
