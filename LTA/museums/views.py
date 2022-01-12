from django.shortcuts import render
from django.http import HttpResponse
from .models import Museums
from django.core.paginator import Paginator
from django.template.defaulttags import register


@register.filter
def get_stars(value):
    return range(int(value))


@register.filter
def get_stars_o(value):
    return range(5 - int(value))


@register.filter
def get_img(museum):
    return f'/static/museums/photos/{museum.id}.jpg'


def museums(request):
    all_museums = Museums.objects.all()
    page = request.GET.get('page', 1)

    if not page:
        page = 1

    p = Paginator(all_museums, 5)
    page_response = p.page(page)

    data = {
        'all_museums': page_response,
        'pages': p
    }
    return render(request, 'museums/category.html', data)


def museum_id(request, id_museum):

    museum = Museums.objects.get(id=id_museum)
    data = {
        'museum': museum
    }
    return render(request, 'museums/item.html', data)

