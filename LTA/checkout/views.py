from django.shortcuts import render
from museums.models import Museums
from django.http import HttpResponse


def checkout(request):

    if request.session.get('cart', None) and len(request.session.get('cart')) != 1:

        products = Museums.objects.filter(id__in=request.session['cart'][1:])

        data = {
            'products': products
        }

        return render(request, 'checkout/checkout.html', data)
    return HttpResponse("No museums chosen")
