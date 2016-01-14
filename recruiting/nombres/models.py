from django.db import models

class Menu(models.Model):
	asignacion = models.CharField(max_length =100)
	derivada   = models.CharField(max_length =100)
	nombres	   = models.CharField(max_length =100)
