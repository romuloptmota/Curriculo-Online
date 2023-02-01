from django.views.generic import TemplateView
from .models import Inicio, Formacao, Conhecimento, Cursos, Experiencias


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['inicio'] = Inicio.objects.all()
        context['formacao'] = Formacao.objects.all().order_by('id')
        context['conhecimento'] = Conhecimento.objects.all().order_by('id')
        context['cursos'] = Cursos.objects.all().order_by('id')
        context['experiencias'] = Experiencias.objects.all().order_by('id')

        return context
