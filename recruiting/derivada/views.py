from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from helpers import derivada,format
from recruiting.helpers import TemplateMethod

class DerivadaView(TemplateView,TemplateMethod):
    template_get            = 'derivada/get.html'
   
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DerivadaView, self).dispatch(*args, **kwargs)


    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_get,self.buildContext(context))
    
      
    def post(self, request, *args, **kwargs):
        try:
            funcion = request.POST.get("funcion")
            x       = request.POST.get("x")
            resultado = self.derivar(funcion,x)
            yprima_pura = resultado[1]
            clean = self.evaluar([str(funcion),str(resultado[0])])
            resultado[0] = clean [0]
            funcion = clean[1]
            context = {'yprima':resultado[0],"x":x,"y":resultado[1],"funcion":funcion}
            return render(request, self.template_get,self.buildContext(context))
        except:
            context = {"error_msg":1}
            return render(request,self.template_get,self.buildContext(context))

    @derivada  	
    def derivar(self,funcion,value_x):
    	return funcion


    @format
    def evaluar(self,data):
    	return data