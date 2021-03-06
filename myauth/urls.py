"""myauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
    url(r'^$', views.index, name='index'),
    url(r'^twitter/$', views.twitter_view, name='twitter_view'),
    url(r'^twitter/callback/$', views.twitter_callback, name='twitter_callback'),
    url(r'^google/callback/$', views.google_callback, name='google_callback'), 
    url(r'^facebook/callback/$', views.facebook_callback, name='facebook_callback'),
    url(r'^instagram/callback/$', views.instagram_callback, name='instagram_callback'),
    url(r'^linkedin/callback/$', views.linkedin_callback, name='linkedin_callback'),
    url(r'^live/callback/$', views.live_callback, name='live_callback'),
    url(r'^admin/', admin.site.urls),
]
