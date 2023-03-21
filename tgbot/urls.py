#from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
        path('', views.home,name='home'),
        path('features/',views.features,name='tgbot'),
        path('userdetails/',views.userdetails,name='userdetails')
]
urlpatterns += staticfiles_urlpatterns()