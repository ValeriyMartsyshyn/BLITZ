from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index),
    path('/get_by_name/<name>', views.museum_name),
    path('/filtered', views.filtered)

]