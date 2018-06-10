from django.contrib import admin
from django.urls import path
from . import views

app_name = "job"

urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('addarticle/', views.addarticle, name = "addarticle"),
    path('article/<int:id>', views.detail, name = "detail"),
    path('update/<int:id>', views.updateArticle, name = "update"),
    path('delete/<int:id>', views.deleteArticle, name = "delete"),
    path('userlist/', views.userList, name = "userlist"),
    path('', views.articles, name = "articles"),
]