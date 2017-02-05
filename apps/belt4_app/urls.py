"""belt4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$',views.register),
    url(r'^dashboard$',views.dashboard),
    url(r'^login$',views.login),
    url(r'^logout$', views.logout),
    url(r'^additem$', views.additem),
    url(r'^addingitem/(?P<id>\d+)$', views.addingitem),
    url(r'^addtomy/(?P<id>\d+)/(?P<aid>\d+)$', views.addtomy),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^show/(?P<id>\d+)$', views.show)

]
