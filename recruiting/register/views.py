from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout as Logout
from django.conf import settings

HOME = 'asignacion'
HOME_LOGOUT = 'register'

class RegisterAndLoginView(TemplateView):
    template_get            = 'register/get.html'  
    template_login			= 'register/login.html' 

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(HOME)
        else:
            return render(request,self.template_get)       

    def post(self, request, *args, **kwargs):
    	if 'register' in request.POST:
    		return self.register(request)
    	elif 'login' in request.POST:
    		return self.login(request)
        elif 'login_captcha' in request.POST:
            correct = self.verify_captcha(request)
            if correct:
                return self.login(request)
            else:
                return render(request,self.template_login,{'error_captcha_msg':1})
    	else:
    		return render(request, self.template_get)

    def login(self,request):
    	
    		username = request.POST['user']
    		password = request.POST['pass']
    		user = authenticate(username=username, password=password)
    		if user is not None:
    			login(request, user)
    			return redirect(HOME)
    		else:
    			return render(request,self.template_login,{'error_login_msg':1})
    
    		

    def register(self,request):
    	correct = self.verify_captcha(request)
    	if correct:
    		password1 = request.POST['password1']
    		password2 = request.POST['password2']
    		if password1 == password2:
    			username = request.POST['username']
    			users = User.objects.filter(username=username)
    			if not users:
    				user = User.objects.create_user(username, '',password1)
    				user = authenticate(username=username, password=password1)
    				login(request,user)
    				return redirect(HOME)    			
    			else:
    				return render(request,self.template_get,{'error_register_msg':1})    			
    		else:
    			return render(request,self.template_get,{'error_password_msg':1})
    	else:
    		return render(request,self.template_get,{'error_captcha_msg':1})
 	
    def verify_captcha(self,request):
    	import requests
    	url = settings.URL_VERIFY_GOOGLE
    	client_response = str(request.POST.get('g-recaptcha-response'))
    	values = {'secret' : settings.SECRET_KEY_GOOGLE,
          		  'response' : client_response,
          		  'remoteip':''
          		 }
        response = requests.post(url, data = values)
        if "false" in response.text:
        	return False
        elif "true" in response.text:
        	return True


        

def logout(request):
	Logout(request)
	return redirect(HOME_LOGOUT)









