from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupfunc, name='signup'),
]