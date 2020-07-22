from django.http import HttpResponseRedirect
from django.shortcuts import render

from .utils import get_all_indices, query_index


def home(request):
    indices = get_all_indices()
    context = {
        'indices': indices
    }
    return render(request, 'home.html', context=context)

def search(request, index_name):
    if request.method == "POST":
        context = {
            'index_name': index_name
        }

        query_results = query_index(request.POST.get("index_name"), request.POST.get("request"))

        context = {
            'query_results': query_results
        }

        return render(request, 'search.html', context=context)
    else:
        context = {
            'index_name': index_name
        }
        return render(request, 'search.html', context=context)
