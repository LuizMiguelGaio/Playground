from django.shortcuts import render, redirect
from .models import Usuario
from django.http import HttpResponse

def home(request):
    return render(request, 'cadastro/home.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('username')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.password = request.POST.get('password')
        novo_usuario.passwordcheck = request.POST.get('passwordcheck')
        novo_usuario.save()
        # Redireciona o usuário para uma página de sucesso ou para a lista de usuários, por exemplo
        return redirect('usuarios')
    else:
        # Se não for um POST, pode ser útil renderizar um formulário vazio
        return render(request, 'cadastro/cadastrar_usuario.html', {})  # Certifique-se de passar o objeto request aqui

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'cadastro/usuarios.html', {'usuarios': usuarios})
