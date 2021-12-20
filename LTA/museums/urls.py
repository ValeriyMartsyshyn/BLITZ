from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.museums),
    path('get_by_id/<int:id_museum>', views.museum_id)

]
