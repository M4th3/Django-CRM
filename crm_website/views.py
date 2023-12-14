from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecord
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

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})

    else:
        messages.error(request, 'You must be logged in to accesss this page!!!') 
        return redirect('homepage')  

def delete_record(request, pk):
    records = Record.objects.get(id=pk)
    records.delete()
    messages.success(request, 'The record has been deleted successfully')
    return redirect('homepage')

def add_record(request):
    form = AddRecord()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddRecord(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'The record has been add with success!!!')
                return redirect('homepage')  
    else:
        messages.error(request, 'You must been logged in!!')
        return redirect('homepage')         
    return render(request, 'add.html', {'form':form})

def update_record(request,pk):
    if request.user.is_authenticated:
        current_data = Record.objects.get(id=pk)
        form = AddRecord(instance=current_data)
        if request.method == 'POST':
            new_form = AddRecord(request.POST)
            if new_form.is_valid():
                new_form.save()
            messages.success(request, 'Your record has been updated successfully!!!')
            return redirect('homepage')
        
        return render(request, 'update.html', {'form': form, 'current_data':current_data})

    else:
        messages.error(request, 'You need to be logged in to update a record!!!')

            