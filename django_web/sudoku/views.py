from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hoofdmenu Sudoku \n1- sudoku spelen \n2- sudoku oplossen")

def sudoku_spelen(request):
    return HttpResponse("Hier ga je sudoku spelen")

def sudoku_oplossen(request):
    return HttpResponse("Hier ga je sudoku laten oplossen")
