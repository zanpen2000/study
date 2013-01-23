from django.shortcuts import render_to_response, HttpResponse
from books.models import Book

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if request.GET['q']:
        # get query keyword
        q = request.GET['q']
        # get results
        books = Book.objects.filter(title__icontains=q)
        # output
        return render_to_response('search_results.html',
                                  {'books':books,'query':q})
    else:
        return search_form(request)
        #return render_to_response('search_form.html',{'error':True})
        #return render_to_response('search_form.html')
        #return HttpResponse('Please submit a search term.')