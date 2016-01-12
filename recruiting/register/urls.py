from django.conf.urls import patterns, url
from register.views import RegisterAndLoginView,logout
urlpatterns = patterns ('recruiting.asignacion.views',
			 url(r'register$', RegisterAndLoginView.as_view(), name='register'),
			 url(r'login$',RegisterAndLoginView.as_view(), name='login'),
			 url(r'logout$',logout, name='logout'),
			 url(r'accounts/login/$', RegisterAndLoginView.as_view(), name='register'),
			 
			 
			)