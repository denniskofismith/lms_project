
from django.urls import path
from .views import login,register,logOut


urlpatterns = [
    path('login/',login),
    path('register/',register),
    path('logout/',logOut,name='logout')
]