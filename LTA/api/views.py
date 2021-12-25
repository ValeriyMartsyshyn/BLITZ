from django.shortcuts import render, HttpResponse
from museums.models import Museums
from django.db.models import Q



def museums(request):
    price_min = request.GET.get('price_min', 0)
    price_max = request.GET.get('price_max', 500)
    min_rating = request.GET.get('rating', 0)

    all_museums = Museums.objects.filter(
        Q(rating__gte=min_rating) & Q(price__gt=price_min) & Q(price__lt=price_max)
    )
    data = {
        'all_museums': all_museums
    }

    return render(request, 'api/museums.html', data)
