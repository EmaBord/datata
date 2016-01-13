from django.conf.urls import patterns, url
from asignacion.views import AsignacionView,asignacionesAjax

urlpatterns = patterns ('recruiting.asignacion.views',
			 url(r'asignacion$', AsignacionView.as_view(), name='asignacion'),
			 url(r'^$', AsignacionView.as_view(), name='asignacion_home'),
			 url(r'asignacion/(?P<size>[0-9]+)/$',asignacionesAjax, name='asignacion_ajax'),
			 
			)
