from django.shortcuts import render

from django.http import HttpResponse

from books.models import Book


# Create your views here.
'''
def search_form(request):
    return render(request, 'search_form.html')
'''

'''
def search(request):
    if 'q' in request.GET:
        message = 'Yor searched for: %r' % request.GET['q']
    else:
        message = 'Your submitted an empty form.'
    return HttpResponse(message)
'''

'''
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        searchbooks = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html', 
                      books': searchbooks, 'query':q})
    else:
        return HttpResponse('Please submit a search term.')
'''

'''
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        searchbooks = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html',
                      {'books': searchbooks, 'query': q})
    else:
        return render(request, 'search_form.html', {'error': True})
'''

'''
def search(request):
    error_flag = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error_flag = True
        elif len(q) > 20:
            error_flag = True
        else:
            searchbooks = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',
                          {'books': searchbooks, 'query': q})
    return render(request, 'search_form.html', {'error': error_flag})
'''

def search(request):
    error_types = [] 
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error_types.append('Enter a search term.')
        elif len(q) > 20:
            error_types.append('Please enter at most 20 characters.')
        else:
            searchbooks = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',
                          {'books': searchbooks, 'query': q})
    return render(request, 'search_form.html', {'errors': error_types})
