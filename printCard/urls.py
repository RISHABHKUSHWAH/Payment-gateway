from django.urls import path
from . import views
urlpatterns=[
    path('idcard/',views.id_card),
    path('adharcard/',views.adharcard),
    path('pancard/',views.pancard),
]