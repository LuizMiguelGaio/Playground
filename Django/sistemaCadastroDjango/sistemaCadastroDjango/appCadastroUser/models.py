from django.db import models

class Usuario(models.Model): #herença da classe model que ja vem pronta no django
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=200)
    email = models.TextField(max_length=100)
    password = models.TextField(max_length=20) #Estudar como validar isso
    passwordcheck = models.TextField(max_length=20) #if(password==passwordcheck? pass : error) ???


