from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/main.html')


def about(request):
    return HttpResponse('About us')


def cart(request):
    return HttpResponse('Client cart')


def result_page(request):
    return render(request, 'main/res.html')