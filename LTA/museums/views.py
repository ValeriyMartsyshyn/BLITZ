from django.shortcuts import render
from django.http import HttpResponse
from .models import Museums


def museums(request):
    all_museums = Museums.objects.all()
    data = {
        'all_museums': all_museums
    }
    return render(request, 'museums/category.html', data)


def museum_id(request, id_museum):

    museum = Museums.objects.get(id=id_museum)
    data = {
        'museum': museum
    }
    return render(request, 'museums/item.html', data)
