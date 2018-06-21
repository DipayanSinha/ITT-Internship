"""Learning URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name = "home"),
    path('login/',views.login_user,name = "login"),
    path('logout/',views.logout_user,name ="logout"),
    path('register/',views.register_user,name="register"),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('change_password/',views.change_password,name ='change_password'),
    path('run_java/',views.run_java,name='run_java'),
    path('display_java/',views.display_java,name='display_java'),
    path('run_ide/',views.run_ide,name='run_ide')
]
