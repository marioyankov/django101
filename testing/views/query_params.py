from django.shortcuts import render


def query_params_views(request):
    q = request.GET.get('q')
    context = {
        'q': q,
    }
    return render(request, 'testing/query_params.html', context)
