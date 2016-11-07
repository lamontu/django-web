# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from users import views


urlpatterns = [
    url(r'^$', views.first_page),
    url(r'^login/', views.user_login),
    url(r'^logout/', views.user_logout),
    url(r'^register/', views.register),
]


