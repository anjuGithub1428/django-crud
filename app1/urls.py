"""
URL configuration for django_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
   path('',views.home_page,name='home page'),
   path('login',views.login_fn,name='login page'),
   path('signup',views.sign_fn,name='Sign page'), 
   path('productadd',views.pdtadd_fn,name='Add product page'),
   path('studadd',views.studadd_fn,name='Add student page'),
   path('studview',views.studview_fn,name='View student page'),
   path('updatestud/<int:id>',views.updstd_fn,name='Update student page'),
   path('updatestud_again',views.updstdagain_fn,name='Update Student page'),
   path('deletestud/<int:id>',views.delstd_fn,name='Delete Student page'),
   path('searchstud',views.studview_fn,name='Search'),
   path('login',views.login_fn_tchr,name='login page'),
   path('logout1',views.logout1,name='logout page'),
]
