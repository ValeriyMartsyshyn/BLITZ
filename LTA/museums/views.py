from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return HttpResponse('Hello museums')


def museum_name(request, name):

    return HttpResponse('Get by name')


def filtered(request):

    return HttpResponse('filtered museums')