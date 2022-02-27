from django.shortcuts import render
from django.http.response import JsonResponse
from lorem_text import lorem

from .models import SearchData
from .forms import SearchHistoryForm
# Create your views here.
#admin usename: mdrashidulhasan pass: Rashidul$123

def search(request):
    context = {}
    form = SearchHistoryForm()
    context['form'] = form
    
    if request.method == 'POST':
        search_query = request.POST.get('search')
        search_result = lorem.words(50)
        SearchData.objects.create(search_query=search_query, search_result=search_result)
        context['result'] = search_result
    return render(request, 'history/index.html', context)


def search_history(request):
    context = []
    search_data = SearchData.objects.all()
    print(len(search_data.filter(search_query='hello')))
    for search in search_data:
        context.append({'search_query': search.search_query, 'search_result': search.search_result, 'searched_at': search.searched_at})
    return JsonResponse(context, safe=False)