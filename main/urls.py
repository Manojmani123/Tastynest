from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
]