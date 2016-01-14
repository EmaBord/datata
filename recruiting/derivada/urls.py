from django.conf.urls import patterns, url
from derivada.views import DerivadaView

urlpatterns = patterns ('recruiting.derivada.views',
			 url(r'derivada$', DerivadaView.as_view(), name='derivada'),
			 
			 
			)