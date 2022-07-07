from django.views.generic import TemplateView

from .models import Recurso, Servico, Funcionario

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        lista_recursos = Recurso.objects.order_by('?').all()
        
        context['recursos1'] = lista_recursos[:int(len(lista_recursos)/2)]
        context['recursos2'] = lista_recursos[int(len(lista_recursos)/2):]
        
        
        
        
        return context