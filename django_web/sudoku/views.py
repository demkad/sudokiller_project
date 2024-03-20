from django.shortcuts import render, redirect
from django.http.response import HttpResponse,HttpResponseNotFound
from django.urls import reverse

# Create your views here.
sudoku = {"sudoku_spelen":"Hier ga je sudoku spelen",
          "sudoku_oplossen":"Hier ga je sudoku laten oplossen"}

def index(request):
    return render(request,'sudoku/index.html')

def index_2(request):
    list_items = ""
    category_list = list(sudoku.keys())
    for category in category_list:
        redirect_path = reverse("sudoku_by_category", args= [category])
        list_items += f"<li><a href=\"{redirect_path}\">{category}</a></li>"
        html = f"<ul>{list_items}</ul>"
    return HttpResponse(html)

def getSudokuByCategory(request,category):
    try:
        category_text = sudoku[category]        
        return HttpResponse(f"<h1>{category_text}</h1>")
    except:
        return HttpResponseNotFound(f"<h1>Verkeerde category</h1>")

def getSudokuByCategoryId(request,category_id):
    category_list = list(sudoku.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound("Verkeerde category")
    category_name = category_list[category_id-1]
    redirect_path = reverse("sudoku_by_category", args= [category_name])
    return redirect(redirect_path)



"""def sudoku_spelen(request):
    return HttpResponse("Hier ga je sudoku spelen")

def sudoku_oplossen(request):
    return HttpResponse("Hier ga je sudoku laten oplossen")"""
