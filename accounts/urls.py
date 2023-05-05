from django.urls import path
from . import views
urlpatterns=[
    path('singUp/',views.singUp, name='singup'),
    path('login/',views.logIn,name='login'),
    path('logout/',views.user_logout,name='logout')
]