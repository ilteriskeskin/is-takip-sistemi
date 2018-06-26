from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.apps import apps
Coin = apps.get_model('coin', 'Coin')
# Create your views here.

def index(request):
    articles = Article.objects.all()

    return render(request, "index.html", {"articles":articles})

def about(request):
    return render(request, "about.html")

@login_required(login_url='/user/login')
def articles(request):
    articles = Article.objects.all()

    return render(request, "articles.html", {"articles":articles})

@login_required(login_url='/user/login/')
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }

    return render(request, "dashboard.html", context)

@login_required(login_url='/user/login/')
def addarticle(request):
    form = ArticleForm(request.POST or None)

    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()

        messages.success(request, "Görev Kaydı Başarılı Bir Şekilde Alındı.")

        return redirect("index")

    return render(request, "addarticle.html", {"form":form})
@login_required(login_url='/user/login/')
def detail(request, id):
    article = get_object_or_404(Article, id = id)
    return render(request, "detail.html", {"article":article})

@login_required(login_url='/user/login/')
def updateArticle(request, id):
    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None, instance = article)
    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()

        messages.success(request, "Görev Başarılı Bir Şekilde Güncellendi.")

        return redirect("index")

    return render(request, "update.html", {"form":form})

@login_required(login_url='/user/login/')
def deleteArticle(request, id):
    article = get_object_or_404(Article, id = id)
    article.delete()

    messages.success(request, "Görev Başarılı Bir Şekilde Silindi.")

    return redirect("index")

@login_required(login_url='/user/login/')
def userList(request):
    
    coins = Coin.objects.all()

    return render(request, "userlist.html", {'coins' : coins})