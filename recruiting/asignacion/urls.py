from django.conf.urls import patterns, url
from asignacion.views import AsignacionView

urlpatterns = patterns ('recruiting.asignacion.views',
			 url(r'asignacion$', AsignacionView.as_view(), name='asignacion'),
			 url(r'^$', AsignacionView.as_view(), name='asignacion'),
			 url(r'asignacion/(?P<size>[0-9]+)/$',AsignacionView.as_view(), name='asignacion_ajax'),
			 
			)
