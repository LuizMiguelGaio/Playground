"""aqui nesse diretorio eu ponho as rotas pras URLs
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #criand rota, view resposável, nome de referência
    #é oque a pessoa digita na url
    #facebook.com
    path('', views.home, name='home'),
    #facebook.com/login
    #path('login/') exemplos
    path('usuario/', views.cadastrar_usuario, name="listagem_usuarios"), #virgula!!!!

    path('cadastro/', views.cadastrar_usuario, name="Cadastro")
]
