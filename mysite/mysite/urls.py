"""mysite URL Configuration

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

from mysite import views
from books import views as bkviews
from contact import views as ctviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.my_homepage_view),
    url(r'^hello/$', views.hello),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^meta/$', views.display_meta),
    # url(r'^search-form/$', bkviews.search_form),
    url(r'^search/$', bkviews.search),
    url(r'^contact/$', ctviews.contact),
    url(r'^contact/thanks/$', ctviews.thanks),
]
