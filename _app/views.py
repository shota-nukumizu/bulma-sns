from .models import ArticleModel

from django.urls import reverse_lazy

from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth import authenticate, login, logout

from django.views.generic import CreateView, UpdateView

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
	object_list = ArticleModel.objects.all()
	return render(request, 'index.html', {'object_list': object_list})

def logoutfunc(request):
	logout(request)
	return redirect('login')

def detailfunc(request, pk):
    item = get_object_or_404(ArticleModel, pk=pk)
    return render(request, 'detail.html', {'item': item})

def deletefunc(request, pk):
    item = ArticleModel.objects.delete(pk=pk)
    return redirect('index')


class ArticleCreate(CreateView):
	template_name = 'create.html'
	model = ArticleModel
	fields = {'title', 'content', 'image', 'name', 'tag'}
	success_url = reverse_lazy('index')


class ArticleUpdate(UpdateView):
	template_name = 'update.html'
	model = ArticleModel
	fields = {'title', 'content', 'image', 'name', 'tag'}
	success_url = reverse_lazy('index')
