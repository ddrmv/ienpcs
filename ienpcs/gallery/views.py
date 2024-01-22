from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("index, to include bg1, bg2, bgt, bgtutu")
