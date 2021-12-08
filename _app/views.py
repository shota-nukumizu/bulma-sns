from django.db import IntegrityError
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def signupfunc(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		try:
			user = User.objects.create_user(username, '', password)
			return render(request, 'login.html', {})
		except IntegrityError:
			return render(request, 'signup.html', {'error': 'このユーザはすでに登録されています'})
	return render(request, 'signup.html', {})


def loginfunc(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('index')
		
		else:
			return render(request, 'login.html', {})
	
	return render(request, 'login.html', {})


@login_required
def index_func(request):
	return render(request, 'index.html', {})

def logoutfunc(request):
	logout(request)
	return redirect('login')