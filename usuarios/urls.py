from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='login'),
    path('logout/', views.logout, name='logout')
]
