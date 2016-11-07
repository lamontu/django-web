
from django.http import HttpResponse
import datetime
from django.http import Http404

# from django.template import Template, Context
# from django.template.loader import get_template

# from django.shortcuts import render_to_response
from django.shortcuts import render


def my_homepage_view(request):
    return HttpResponse("My Homepage")


def hello(request):
    return HttpResponse("Hello world")


'''
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body</html>" % now
    return HttpResponse(html)
'''

'''
def current_datetime(request):
    now = datetime.datetime.now()
    t = Template(("<html><body>It is now {{ current_date }}.</body></html>"))
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
'''

'''
def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
'''

def current_datetime(request):
    now = datetime.datetime.now()
    # return render_to_response('current_datetime.html', {'current_date': now})
    return render(request,'current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        timeoffset = int(offset)
    except ValueError:
        raise Http404()
    nexttime = datetime.datetime.now() + datetime.timedelta(hours=timeoffset)
    return render(request, 'hours_ahead.html', {'hour_offset': timeoffset, 'next_time': nexttime})


def display_meta(request):
    meta_values = request.META.items()
    meta_values = sorted(meta_values, key = lambda d: d[0], reverse=True)
    return render_to_response('display_meta.html', {'values': meta_values})











