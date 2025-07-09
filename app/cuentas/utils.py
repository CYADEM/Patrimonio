from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginar_queryset(request, queryset, items_por_pagina=10):
    paginator = Paginator(queryset, items_por_pagina)
    page = request.GET.get('page')
    try:
        objetos = paginator.page(page)
    except PageNotAnInteger:
        objetos = paginator.page(1)
    except EmptyPage:
        objetos = paginator.page(paginator.num_pages)
    return objetos
