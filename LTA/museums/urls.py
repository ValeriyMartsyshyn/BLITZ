from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.museums, name='museums'),
    path('<int:id_museum>', views.museum_id)

]