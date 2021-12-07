from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.museums),
    path('get_by_id/<int:id>', views.museum_id)

]
