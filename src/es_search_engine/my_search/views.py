from django.http import HttpResponseRedirect
from django.shortcuts import render

from .utils import get_all_indices


def home(request):
    indices = get_all_indices()
    context = {
        'indices': indices
    }
    print(indices)
    return render(request, 'home.html', context=context)

def search(request, index_name):
    if request.method == "POST":
        print(request.POST)
        context = {
            'index_name': index_name
        }
        return render(request, 'search.html', context=context)
    else:
        context = {
            'index_name': index_name
        }
        return render(request, 'search.html', context=context)
