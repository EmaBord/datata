from django.conf.urls import include, url
urlpatterns = [

    url(r'^', include('asignacion.urls')),
    url(r'^', include('register.urls')),	
    
]
