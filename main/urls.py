from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('menu/', views.menu, name='menu'),
    path('menu/burgers/', views.burgers, name='burgers'),
    path('menu/biryanis/', views.biryanis, name='biryanis'),
    path('menu/curries/', views.curries, name='curries'),
    path('menu/tiffins/', views.tiffins, name='tiffins'),
    path('menu/softdrinks/', views.softdrinks, name='softdrinks'),
    path('cart/', views.cart, name='cart'),
    path('pay/', views.pay, name='pay'),
    path('myorders/', views.myorders, name='myorders'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-home/', views.admin_home, name='admin_home'),
    path('admin-items/', views.admin_manage_items, name='admin_manage_items'),
]