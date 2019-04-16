from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from ServiceCore.forms import LoginForm


def index(request):
    return render(request, 'outofmemory/index.html')


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