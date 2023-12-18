from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('Dashboard')  # Redirige a la página después del inicio de sesión
            else:
                messages.error(request, 'Credenciales incorrectas. Inténtalo de nuevo.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})
