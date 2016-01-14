from sympy import *	
from django.shortcuts import render

def derivada(func):
	def diferencial(self,funcion,value_x):
		func(self,funcion,value_x)		
		x = Symbol('x')
		y = eval(funcion)		
		pendiente = y.diff(x)
		from math import exp, expm1
		x = int(value_x)
		pendiente = eval(str(pendiente))
		
		y = eval(funcion)
		b = y - pendiente* x

		""" y = mx+b"""
		yprima = str(pendiente)+ "*x + "+str(b)


		resultado = []
		resultado.append(yprima)
		
		resultado.append(y) 
		return resultado
	return diferencial


expresiones = ("exp","EXP","sin","SIN","cos","COS")

def format(func):
	def parse(self,data):
		func(self,data)		
		for expresion in expresiones:
			data[0] = data[0].replace(expresion,"Math."+expresion)# para dibujar con javascript en el cliente
			data[1] = data[1].replace(expresion,"Math."+expresion)
			#print data		
		return data
	return parse