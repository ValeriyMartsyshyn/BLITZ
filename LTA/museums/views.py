from django.shortcuts import render
from django.http import HttpResponse
from .models import Museums


def museums(request):
    all_museums = Museums.objects.all()
    data = {
        'all_museums': all_museums
    }
    return render(request, 'museums/test.html', data)


def museum_id(request, id_museums):
    return HttpResponse(f'{id_museums=}')
