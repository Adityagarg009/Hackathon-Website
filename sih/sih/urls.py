"""sih URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Homepage,name='home'),
    path('login/', views.LoginPage,name='login'),
    path('home/', views.Homepage,name='home'),
    path('index/',views.Index,name='index'),
    path('logout/',views.Logout,name='logout'),
    path('about/',views.Aboutpage,name='about'),
    path('signup/',views.SignupPage,name='signup'),
    path('book1/',views.Book1,name='book1'),
    path('index/book1',views.Book1,name='book1'),
]
