from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Main page')


def about(request):
    return HttpResponse('About us')


def cart(request):
    return HttpResponse('Client cart')