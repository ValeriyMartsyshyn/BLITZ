from django.shortcuts import render
from museums.models import Museums


def checkout(request):
    products = Museums.objects.filter(id__in=request.session['cart'][1:])

    data = {
        'products': products
    }

    return render(request, 'checkout/checkout.html', data)
