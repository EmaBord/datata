from nombres.models import Menu 
def addMenuContext(func):
	def contexto(self,contexto):
		func(self,contexto)		
		menu = Menu.objects.filter(pk=1)
		if menu:
			menu = menu[0]
			contexto["asignacion"] 	= menu.asignacion
			contexto["derivada"]	= menu.derivada
			contexto["nombres"]		= menu.nombres
		return contexto
	return contexto


class TemplateMethod:
	
	@addMenuContext
	def buildContext(self,context):
		return context
    





