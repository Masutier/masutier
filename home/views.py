from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .decorators import allowed_users, admin_only


def home (request):

    context={"title": "Home"}
    return render(request, 'home/masutier.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Algo no salio bien, Intentalo de nuevo!')

    context = {"title": "Login"}
    return render(request, "home/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect('home')

    return render(request, 'home/login.html')

