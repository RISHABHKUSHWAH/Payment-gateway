from django.urls import path
from . import views
urlpatterns = [
    path('amountOfOrder/',views.amountOfOrder),
    path('orderComfirm/',views.orderConfirm)
]
