from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse

def user_Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=['password'])
            if user is not None:
                login(request, user)
                return HttpResponse("Login successful!")
            else:
                return HttpResponse("Invalid credentials.")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
