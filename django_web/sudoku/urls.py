from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("index_2",views.index_2,name="index2"),
    path('<int:category_id>', views.getSudokuByCategoryId, name="sudoku_by_category_id"),
    path('<str:category>', views.getSudokuByCategory, name='sudoku_by_category'),
]