from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from helpers import Articulo, MaxHeap,evaluar
from recruiting.helpers import TemplateMethod

class AsignacionView(TemplateView,TemplateMethod):
    template_get            = 'asignacion/get_asignacion.html'
    template_table          = 'asignacion/table_asignacion.html'
    template_table_result   = 'asignacion/table_asignacion_result.html' 
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AsignacionView, self).dispatch(*args, **kwargs)


    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_get,self.buildContext(context))

    def post(self, request, *args, **kwargs):        
        if "size" in request.POST:
            return self.size(request, *args, **kwargs)
        elif "data" in self.request.POST:
            return self.data(request,*args,**kwargs)

    def size(self,request,*args,**kwargs):
        size =  request.POST.get("size")
        size = int(size)
        personas  = [p for p in xrange(1,size+1)]# esto podria ser la consulta en la db
        context = {'personas':personas,'size':size}
        return render(request, self.template_table,self.buildContext(context) )
    
    def data(self,request,*args,**kwargs):
        size =  request.POST.get("data")
        size = int(size)
        query_dyct = request.POST.dict()
        claves = request.POST.dict().keys()       
        personas = {}# creo una diccionario de personas
        for clave in claves:# T(n) = O(n) peor de los casos
            if clave != "csrfmiddlewaretoken" and clave != "data":
                felicidad = int(query_dyct[clave])
                if felicidad > 0:
                    id_persona = clave.split("#")[1].split('-')[0]
                    id_articulo = clave.split("#")[1].split('-')[1]
                    if id_persona not in personas.keys():
                        maxh = MaxHeap()
                        maxh.push(Articulo(id_articulo,felicidad))# T(n) =  O(log n) peor de los casos
                        personas[id_persona] = maxh
                    else:                    
                        personas[id_persona].push(Articulo(id_articulo,felicidad))# T(n) =  O(log n) peor de los casos
       
        maximas_felicidades = []
        felicidad_colectiva = 0      
        for id_persona in personas.keys(): #O(n) peor de los casos
            articulo_maxima_felicidad = personas[id_persona].pop()# O(1) siempre
            maxima_felicidad = articulo_maxima_felicidad.value
            articulo = articulo_maxima_felicidad.key                  
            if maxima_felicidad != 0:                        
                maximas_felicidades.append({'articulo':articulo,'maxima_felicidad':maxima_felicidad,'persona':id_persona})
                felicidad_colectiva +=  int(maxima_felicidad)                 
        context =  {'felicidad_colectiva': felicidad_colectiva,'maximas_felicidades':maximas_felicidades}
        return render(request, self.template_table_result,self.buildContext(context))



@csrf_exempt 
@login_required
def asignacionesAjax(request,size):
    import json
    size = int(size)           
    personas  = [[ evaluar(p,a) for p in xrange(0,size+1)] for a in xrange(1,size+1)]# esto podria ser la consulta en la db
    jSon = {'aaData':personas}
    data = json.dumps(jSon)
    return HttpResponse(data, content_type='application/json')