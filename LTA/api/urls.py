from django.urls import path
from . import views

urlpatterns = [

    path('museums/', views.museums),
]
