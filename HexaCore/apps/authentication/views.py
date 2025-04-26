from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'authentication/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'authentication/login.html')


@login_required
def dashboard(request):
    rol = request.user.groups.first().name if request.user.groups.exists() else 'Sin Rol'
    return render(request, 'authentication/dashboard.html', {'rol': rol})


def logout_view(request):
    logout(request)
    return redirect('login')
