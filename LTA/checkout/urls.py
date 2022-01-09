from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.checkout, name='checkout'),
    path('update_pdf', views.update_pdf),
    path('pdf', views.pdf)
]