"""webtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from pages.views import sign_in, sign_up, log_out
from movies.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movie_list_view, name='home'),
    path('<int:id>', dynamic_movie_view, name='movie'),
    path('create/', movie_create_view, name='create'),
    path('login/', sign_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('register/', sign_up, name='register'),
    path('reserve/', reserve_view, name='reserve'),
    path('reserve/<int:id>', reserve_seat_view, name='reserve_seat'),
    path('ticket/', my_ticket_view, name='ticket'),
]
