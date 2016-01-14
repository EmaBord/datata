from django.conf.urls import patterns, url
from nombres.views import NombresView

urlpatterns = patterns ('recruiting.derivada.views',
			 url(r'nombres$', NombresView.as_view(), name='nombres'),
			 
			 
			)