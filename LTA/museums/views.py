from django.shortcuts import render
from django.http import HttpResponse
from .models import Museums


def museums(request):

    return HttpResponse('Hello museums')


def museum_id(request, id_museums):
    return HttpResponse(f'{id_museums=}')
