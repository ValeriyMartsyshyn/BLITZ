from django.urls import path
from . import views

urlpatterns = [

    path('museums/filter/', views.museums),
    path('checkout/add', views.checkout_add),
    path('checkout/delete', views.checkout_delete),
]
