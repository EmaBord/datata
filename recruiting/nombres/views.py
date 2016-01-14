from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class NombresView(TemplateView):
    template_get            = 'nombres/get.html'
   
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NombresView, self).dispatch(*args, **kwargs)


    def get(self, request, *args, **kwargs):
        return render(request, self.template_get)
    
      
    def post(self, request, *args, **kwargs):
    	
    		return render(request, self.template_get)

  