from django.shortcuts import render
from museums.models import Museums
from django.http import HttpResponse, FileResponse
from django.template.loader import render_to_string


def checkout(request):
    if request.session.get('cart', None) and len(request.session.get('cart')) != 0:

        products = Museums.objects.filter(id__in=request.session['cart'])
        budget = get_budget(products, balance=200)
        data = {
            'products': products,
            'budget': budget,
        }

        return render(request, 'checkout/checkout.html', data)
    return HttpResponse("No museums chosen")


def update_pdf(request):
    id_museum = request.session['cart']
    museums = Museums.objects.filter(id__in=id_museum)
    data = {
        'museums': museums
    }

    with open('checkout/pdf_files/plan.html', 'w', encoding='utf-8') as file:
        file.write(render_to_string('checkout/pdf.html', request=request, context=data))

    return HttpResponse('OK')


def pdf(request):
    return FileResponse(open('checkout/pdf_files/plan.html', 'rb'), as_attachment=True)


def get_budget(products, balance):
    cost = 0
    for i in products:
        cost += i.price

    return balance - cost
