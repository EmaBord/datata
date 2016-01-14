class Articulo():	
	def __init__(self,key,value):
		self.value = value
		self.key = key
	
	def __cmp__(self,other):
		if other.value > self.value:
			return 1
		elif other.value < self.value:
			return -1
		else:
			return 0
			
		
	def __repr__(self):
		return str(self.key)+":"+str(self.value)
		


		
from heapq import heappush, heappop
class MaxHeap():
	def __init__(self):
		self.elements = []
	
	def push(self,element):
		heappush(self.elements, element)
		
	def pop(self):
		return heappop(self.elements)
		
	def __repr__(self):
		return str(self.elements)

def  evaluar(persona,articulo):
        if persona==0:
            return "Art."+str(articulo) 
        else:
            return """<input name='#"""+str(persona)+"""-"""+str(articulo)+""" 'class='form-control sm-input' style='width: 3em;'' type='number' step='1' min='0' value='0'>"""

