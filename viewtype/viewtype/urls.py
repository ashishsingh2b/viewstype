"""viewtype URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/',views.func),
    path('cl/',views.Myview.as_view(),name='cl'),
    path('my/',views.My.as_view(),name='my'),
    path('third/',views.Mythird.as_view(name="Bittu"),name='third'),
    path('forth/',views.Myforth.as_view(),name='forth'),
    path('home/',views.home.as_view(),name='home'),
    path('homef/',views.homef,name='homef'),
    path('homev/',views.homev.as_view(),name='homev'),
    path('contact/',views.contact,name='contact'),
    path('con/',views.con.as_view(),name='con'),
    path('cont/',views.cont,name='cont'),
    path('conta/',views.conta,{'template_name':'contact.html'},name='cont'),

]


