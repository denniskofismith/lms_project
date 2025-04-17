
from django.urls import path
from .views import login,register,logOut


urlpatterns = [
    path('login/',login,name='signIn'),
    path('register/',register,name='signUp'),
    path('logout/',logOut,name='logout')
]