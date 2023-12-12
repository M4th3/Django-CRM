from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()
    

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
        return render(request, 'home.html', {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!!')
    return redirect(home)

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been succesfully registered, Wellcome !!!')
            return redirect('homepage')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
 
        
    return render(request, 'register.html', {'form':form})
 