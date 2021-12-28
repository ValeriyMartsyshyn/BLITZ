from django.shortcuts import render, HttpResponse
from museums.models import Museums
from django.db.models import Q
from .filters import filter_museums


def museums(request):
    price_min = request.GET.get('price_min', 0)
    price_max = request.GET.get('price_max', 500)
    min_rating = request.GET.get('rating', 0)
    categories_ids = filter_museums(request)
    all_museums = Museums.objects.filter(
        Q(rating__gte=min_rating)
        & Q(price__gte=price_min)
        & Q(price__lte=price_max)
        & (Q(category__in=categories_ids) if categories_ids else Q())
    )
    data = {
        'all_museums': all_museums
    }

    return render(request, 'api/museums.html', data)
