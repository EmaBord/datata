from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from helpers import derivada,format

class DerivadaView(TemplateView):
    template_get            = 'derivada/get.html'
   
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DerivadaView, self).dispatch(*args, **kwargs)


    def get(self, request, *args, **kwargs):
        return render(request, self.template_get)
    
      
    def post(self, request, *args, **kwargs):
    	
    	try:
    		funcion = request.POST.get("funcion")
    		x       = request.POST.get("x")
    		resultado = self.derivar(funcion,x)
    		yprima_pura = resultado[1]
    		clean = self.evaluar([str(funcion),str(resultado[0])])
    		resultado[0] = clean [0]
    		funcion = clean[1]
       		if int(x) >= int(resultado[1]):
    		 	mayor=x
    		else:
    		 	mayor=resultado[1]
    		print mayor
    		return render(request, self.template_get,{'yprima':resultado[0],"x":x,"y":resultado[1],"funcion":funcion,"mayor":mayor
    			})
    	except:
    		return render(request,self.template_get,{"error_msg":1})

    @derivada  	
    def derivar(self,funcion,value_x):
    	return funcion


    @format
    def evaluar(self,data):
    	return data