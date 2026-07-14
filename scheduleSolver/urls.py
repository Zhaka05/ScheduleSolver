from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("classmate_info/", views.Anketa.as_view(), name='info')
]
