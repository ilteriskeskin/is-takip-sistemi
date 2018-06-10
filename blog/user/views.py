from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from article.models import Article

# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)

        messages.success(request, "Kayıt başarılı, giriş sayfasına yönlendirildiniz.")
        
        return redirect("index")

    context = {
        "form" : form
    }

    return render(request, "register.html", context)

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Kullanıcı Adı veya Parola Hatalı !")
            return render(request, "login.html", context)

        messages.success(request, "Başarıyla Giriş Yaptınız.")
        login(request, user)

        return redirect("index")

    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yapıldı.")
    
    return redirect("index")

@login_required(login_url='/user/login/')
def userJob(request, id): 
    return render(request, "userjob.html")