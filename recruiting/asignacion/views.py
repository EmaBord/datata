from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

class AsignacionView(TemplateView):
    template_get            = 'asignacion/get_asignacion.html'
    template_table          = 'asignacion/table_asignacion.html'
    template_table_result   = 'asignacion/table_asignacion_result.html' 

    def get(self, request, *args, **kwargs):
        return render(request, self.template_get)

    def post(self, request, *args, **kwargs):        
        if "size" in request.POST:
            return self.size(request, *args, **kwargs)
        elif "data" in self.request.POST:
            return self.data(request,*args,**kwargs)

    def size(self,request,*args,**kwargs):
        size =  request.POST.get("size")
        size = int(size)
        articulos = [a for a in xrange(1,size+1)]
        personas  = [p for p in xrange(1,size+1)]
        return render(request, self.template_table, {'articulos': articulos,'personas':personas,'size':size})
    
    def data(self,request,*args,**kwargs):
        size =  request.POST.get("data")
        size = int(size)
        query_dyct = request.POST.dict()
        claves = request.POST.dict().keys()
        personas = {}# creo una diccionario de personas
        for persona in xrange(1,size+1):
            personas[str(persona)] = {} 
        ''' el diccionario personas esta formado de la siguient manera:'''
        ''' {id_persona:{felicidad:articulo}}'''       
        for clave in claves:
            try:
                id_persona = clave.split("#")[1].split('-')[0]
                id_articulo = clave.split("#")[1].split('-')[1]
                felicidad = query_dyct[clave]
                personas[id_persona][int(felicidad)] = id_articulo # para obtener el maximo mas facil,
                ''' en caso de haya mas de uno con el mismo valor se queda con el primero en procesar,'''
                ''' si quisieramos quedarnos con todos los articulos tendria una lista de los mismos '''               
            except:
                pass                    
        maximas_felicidades = []
        felicidad_colectiva = 0            
        for id_persona in personas.keys():            
            maxima_felicidad = max(personas[id_persona].keys())
            maximas_felicidades.append({'articulo':personas[id_persona][maxima_felicidad],'maxima_felicidad':maxima_felicidad,'persona':id_persona})
            felicidad_colectiva +=  int(maxima_felicidad)
        return render(request, self.template_table_result, {'felicidad_colectiva': felicidad_colectiva,'maximas_felicidades':maximas_felicidades})
