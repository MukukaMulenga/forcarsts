"""
URL configuration for forcast project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from weather_application.views import get_wether,get_default_weather

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_wether/',get_wether,name='get_wether'),
    path('',get_default_weather,name='get_default_weather')
    # path('show_data/',show_data,name="show_data")
]
