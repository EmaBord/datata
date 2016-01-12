from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class AsignacionView(TemplateView):
    template_get            = 'asignacion/get_asignacion.html'
    template_table          = 'asignacion/table_asignacion.html'
    template_table_result   = 'asignacion/table_asignacion_result.html' 
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AsignacionView, self).dispatch(*args, **kwargs)


    def  evaluar(self,persona,articulo):
        if persona==0:
            return "Art."+str(articulo) 
        else:
            return """<input name='#"""+str(persona)+"""-"""+str(articulo)+""" 'class='form-control sm-input' style='width: 3em;'' type='number' step='1' min='0' value='0'>"""
    
      
    def get(self, request, *args, **kwargs):
      
        if "size" in kwargs:
            import json
            size = int(kwargs.get("size"))
           
            personas  = [[ self.evaluar(p,a) for p in xrange(0,size+1)] for a in xrange(1,size+1)]
            jSon = {'aaData':personas}
            data = json.dumps(jSon)
            return HttpResponse(data, content_type='application/json')


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
        # grabar en archivo
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
        hay_datos = False
        for clave in claves:
            try:
                felicidad = query_dyct[clave]
                if felicidad > 0:
                    id_persona = clave.split("#")[1].split('-')[0]
                    id_articulo = clave.split("#")[1].split('-')[1]
                    
                    personas[id_persona][int(felicidad)] = id_articulo # para obtener el maximo mas facil,
                    ''' en caso de haya mas de uno con el mismo valor se queda con el primero en procesar,'''
                    ''' si quisieramos quedarnos con todos los articulos tendria una lista de los mismos '''               
                    hay_datos = True
            except:
                pass                    
        
        maximas_felicidades = []
        felicidad_colectiva = 0 
         
        if hay_datos:
            for id_persona in personas.keys():          
                try:
                    maxima_felicidad = max(personas[id_persona].keys())
                    articulo = personas[id_persona][maxima_felicidad]
                    
                    if maxima_felicidad != 0:                
                        
                        maximas_felicidades.append({'articulo':articulo,'maxima_felicidad':maxima_felicidad,'persona':id_persona})
                        felicidad_colectiva +=  int(maxima_felicidad)
                except:
                    pass
        return render(request, self.template_table_result, {'felicidad_colectiva': felicidad_colectiva,'maximas_felicidades':maximas_felicidades})
