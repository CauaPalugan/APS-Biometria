from django.contrib import admin
from django.urls import include, path
from biometria import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
]