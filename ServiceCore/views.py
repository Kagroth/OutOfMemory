from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from ServiceCore.forms import LoginForm, RegisterForm


def index(request):
    return render(request, 'outofmemory/index.html') # strona glowna


# widok logowania
def loginuser(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            user = authenticate(username=request.POST.get('email').split('@')[0], password=request.POST.get('password'))

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'outofmemory/index.html',
                              {'message': 'Podano niepoprawne dane!'}) # sciezka
        else:
            return render(request, 'outofmemory/index.html',
                          {'message': 'Podano niepoprawne dane!'}) # sciezka
    else:
        return render(request, 'outofmemory/index.html',
                      {'message': 'Podaj wszystkie wymagane dane!'}) # sciezka


# widok logout
def logoutuser(request):
    logout(request)
    return redirect('index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            try:
                User.objects.create_user(username=email.split("@")[0], email=request.POST.get('email'), password=request.POST.get('password'), first_name=request.POST.get('firstName'), last_name=request.POST.get('lastName'))
            except:
                return render(request, 'outofmemory/index.html',
                              {'message': 'Nie udało się zarejestrować'}) #sciezka

            return render(request, 'outofmemory/index.html',
                          {'message': 'Rejestracja przebiegła pomyślnie!'}) #sciezka
        else:
            return render(request, 'outofmemory/index.html',
                          {'message': 'Podaj wszystie wymagane dane!'}) #sciezka

    return index(request) #sciezka