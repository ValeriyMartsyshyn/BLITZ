def filter_museums(request):
    sub = {'nature': 1,
           'memorial': 2,
           'art': 3,
           'gallery': 4,
           'history': 5}

    categories = [sub[i] for i in sub if request.GET.get(i) != 'false']

    return categories
