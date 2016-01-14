from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from recruiting.helpers import TemplateMethod
from models import Menu

class NombresView(TemplateView,TemplateMethod):
    template_get            = 'nombres/get.html'
   
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NombresView, self).dispatch(*args, **kwargs)

    

    def get(self, request, *args, **kwargs):
        context = {}        
        return render(request, self.template_get,self.buildContext(context))
    
      
    def post(self, request, *args, **kwargs):
    	asignacion = request.POST.get("asignacion")
    	derivada = request.POST.get("derivada")
    	nombres = request.POST.get("nombres")    	
    	menu = Menu.objects.filter(pk=1)
    	if menu:
    		menu.update(asignacion=asignacion,derivada=derivada,nombres=nombres)
    	else:
    		Menu.objects.create(asignacion=asignacion,derivada=derivada,nombres=nombres)	
    	return render(request, self.template_get,{'asignacion':asignacion,'derivada':derivada,'nombres':nombres})

  