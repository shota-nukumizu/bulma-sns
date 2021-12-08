from django.shortcuts import render
from django.contrib.auth.models import User

def signupfunc(request):
	if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
	return render(request, 'signup.html', {'some': 100})