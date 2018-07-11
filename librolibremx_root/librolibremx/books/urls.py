from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list', views.listBooks, name="list_books")
]
