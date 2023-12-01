from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) #O método authenticate verifica se há usuários
                                                                            # com as credencicais passadas de parâmetro, se n houver retorna NOne
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!!")
            return redirect('homepage')
        else:
            messages.error(request, 'Something gone wrong!!')
            return redirect('homepage')
    else:
        return render(request, 'home.html', {})

def login_user(rerquest):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!!')
    return redirect(home)

def register_user(request):
    return render(request, 'register.html', {})
