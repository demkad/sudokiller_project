from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("sudoku_spelen", views.sudoku_spelen, name="sudoku_spelen"),
    path("sudoku_oplossen", views.sudoku_oplossen, name="sudoku_oplossen")
]